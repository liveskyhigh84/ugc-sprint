#!/usr/bin/env python3
"""Self-hosted HeyGen-shaped API: script + photo in, talking-avatar video out.

Free, local, no signup. Wraps two already-installed OSS tools:
  - TTS: gTTS (default) or edge-tts, both free
  - Avatar: SadTalker (CPU inference, ~4-8 sec/frame on this Mac)

API shape matches generate_avatar_test.py's JoggAI client so either
backend can be swapped in without touching the order-fulfillment code:

  POST /generate {script, source_image, voice?} -> {job_id}
  GET  /status/{job_id}                          -> {status, video_url?}
  GET  /video/{job_id}                            -> the mp4 file

Run: source scripts/heygen_clone_venv/bin/activate && python scripts/heygen_clone_server.py
Smoke test (no server needed): python scripts/heygen_clone_server.py --smoke-test
"""
import argparse
import asyncio
import subprocess
import sys
import uuid
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel

ROOT = Path(__file__).parent.parent
SADTALKER_DIR = Path.home() / "Developer/UGC_Studio/models/SadTalker"
SADTALKER_PYTHON = SADTALKER_DIR / "venv/bin/python"
JOBS_DIR = ROOT / "generate-out/heygen-clone-jobs"

app = FastAPI(title="HeyGen Clone (SadTalker + gTTS, self-hosted)")
JOBS: dict[str, dict] = {}


class GenerateRequest(BaseModel):
    script: str
    source_image: str  # path to a local portrait image
    voice: str = "gtts"  # "gtts" or "edge"


async def synthesize_voice(script: str, out_wav: Path, voice: str) -> None:
    if voice == "edge":
        import edge_tts
        communicate = edge_tts.Communicate(script, "en-US-GuyNeural")
        await communicate.save(str(out_wav))
    else:
        from gtts import gTTS
        mp3_path = out_wav.with_suffix(".mp3")
        gTTS(script).save(str(mp3_path))
        # SadTalker wants wav; ffmpeg is already a system dependency of this pipeline.
        subprocess.run(
            ["ffmpeg", "-y", "-i", str(mp3_path), str(out_wav)],
            check=True, capture_output=True,
        )


def run_sadtalker(audio_path: Path, source_image: Path, result_dir: Path) -> Path:
    if not SADTALKER_PYTHON.exists():
        raise RuntimeError(f"SadTalker venv not found at {SADTALKER_PYTHON}")
    # subprocess runs with cwd=SADTALKER_DIR — a relative path here would resolve
    # against the wrong directory, so every path must be absolute before the call.
    result_dir.mkdir(parents=True, exist_ok=True)
    cmd = [
        str(SADTALKER_PYTHON), "inference.py",
        "--driven_audio", str(audio_path.resolve()),
        "--source_image", str(source_image.resolve()),
        "--result_dir", str(result_dir.resolve()),
        "--still", "--preprocess", "full", "--cpu",
    ]
    proc = subprocess.run(cmd, cwd=SADTALKER_DIR, capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError(f"SadTalker failed: {proc.stderr[-2000:]}")
    videos = sorted(result_dir.glob("*.mp4"), key=lambda p: p.stat().st_mtime)
    if not videos:
        raise RuntimeError(f"SadTalker produced no video in {result_dir}. stderr: {proc.stderr[-500:]}")
    return videos[-1]


async def run_job(job_id: str, req: GenerateRequest) -> None:
    job_dir = JOBS_DIR / job_id
    job_dir.mkdir(parents=True, exist_ok=True)
    try:
        audio_path = job_dir / "voice.wav"
        await synthesize_voice(req.script, audio_path, req.voice)
        video_path = await asyncio.to_thread(
            run_sadtalker, audio_path, Path(req.source_image), job_dir
        )
        JOBS[job_id] = {"status": "completed", "video_path": str(video_path)}
    except Exception as e:  # ponytail: one wrapper, no per-stage error hierarchy needed at this scale
        JOBS[job_id] = {"status": "failed", "error": str(e)}


@app.post("/generate")
async def generate(req: GenerateRequest):
    if not Path(req.source_image).exists():
        raise HTTPException(400, f"source_image not found: {req.source_image}")
    job_id = uuid.uuid4().hex[:12]
    JOBS[job_id] = {"status": "processing"}
    asyncio.create_task(run_job(job_id, req))
    return {"job_id": job_id, "status": "processing"}


@app.get("/status/{job_id}")
def status(job_id: str):
    job = JOBS.get(job_id)
    if not job:
        raise HTTPException(404, "unknown job_id")
    out = {"status": job["status"]}
    if job["status"] == "completed":
        out["video_url"] = f"/video/{job_id}"
    if job["status"] == "failed":
        out["error"] = job["error"]
    return out


@app.get("/video/{job_id}")
def video(job_id: str):
    job = JOBS.get(job_id)
    if not job or job.get("status") != "completed":
        raise HTTPException(404, "video not ready")
    return FileResponse(job["video_path"], media_type="video/mp4")


def smoke_test() -> None:
    """ponytail: one runnable check for the real pipeline, not a mock. Takes
    a few minutes on CPU — that's SadTalker's actual inference cost, not a bug."""
    sample_image = SADTALKER_DIR / "examples/source_image/happy.png"
    assert sample_image.exists(), f"missing SadTalker sample image: {sample_image}"
    assert SADTALKER_PYTHON.exists(), f"missing SadTalker venv: {SADTALKER_PYTHON}"

    job_dir = JOBS_DIR / "smoke-test"
    job_dir.mkdir(parents=True, exist_ok=True)
    audio_path = job_dir / "voice.wav"
    asyncio.run(synthesize_voice(
        "This is a smoke test of the self-hosted avatar pipeline.", audio_path, "gtts"
    ))
    assert audio_path.exists() and audio_path.stat().st_size > 0, "TTS produced no audio"
    print(f"[smoke-test] voice ok: {audio_path} ({audio_path.stat().st_size} bytes)")

    video_path = run_sadtalker(audio_path, sample_image, job_dir)
    assert video_path.exists() and video_path.stat().st_size > 0, "SadTalker produced no video"
    print(f"[smoke-test] PASS: {video_path} ({video_path.stat().st_size} bytes)")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--smoke-test", action="store_true")
    parser.add_argument("--port", type=int, default=8420)
    args = parser.parse_args()

    if args.smoke_test:
        smoke_test()
        sys.exit(0)

    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=args.port)
