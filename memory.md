# UGC_Sprint — memory

## What this is
"24-Hour UGC Sprint" — $297 offer: 1 talking-avatar UGC-style ad video + 4 alt creative variants (static/motion), for ecom/DTC sellers. $197/mo Sprint Pass retainer pitched post-sale, not in the launch post. Distribution: value-first Reddit/Indie Hackers post ("I built this, used it on my own store, AMA"), not a direct ad.

## How we got here (2026-09-02)
Pipeline: `/dare` (found the real bottleneck is distribution, not build time — see prior PromptAgent/Leverage Academy 0-customer history) → `/brutal` killed 2 of 3 candidate ideas → `/plan-prd` → `/revenue` → `/teach-me` (UGC marketing synthesis) → `/game-changing-features` (10x pass: reframed toward batch/retainer economics) → `/brutal` again (caught that the 10x reframe accidentally dropped the "finished video" promise — reverted to keep the video, added the variant-batch insight as a bonus stack instead) → `/market-audit` (pre-launch, sight-unseen) → `/marketing-plan` (condensed week-1 AARRR, not full 13-section) → build.

## Key technical findings (from dispatched agents — verify before relying on stale info)
- **Prism** (`~/Developer/Prism`) has no ad-creative pipeline itself. The actual fal.ai generation capability lives in the global `/generate` skill (`~/.claude/skills/generate/`), which reads Prism's live `FAL_KEY`. Kling image-to-video is generic image animation only — no avatar/lipsync. Cost: ~$0.50/order for image+motion generation.
- **Talking-avatar video still needs a separate, licensed source** — HeyGen or D-ID (~$20-30/mo tier), NOT wired yet. This is the one real blocker before order #1 can ship as originally promised on the page.
- **UGC_Studio**'s Coqui XTTS license risk only lives in a throwaway Colab notebook it generates, not the running app. The running app's gTTS/edge-tts voice path is already commercially clean. No ElevenLabs key exists anywhere (Leverage Academy actually uses Kokoro).
- **GhostwriterAI** (`~/Developer/GhostwriterAI/backend`) already has `generate_package()` producing hook variants + a full script + shot list — reusable for the script-generation side. Both GhostwriterAI and UGC_Studio backends had dead venvs as of 2026-09-02 (~30-60min rebuild needed before first fulfillment).

## Update — 2026-09-02, session 2: talking-avatar tool resolved (free/OSS, no HeyGen/D-ID needed)

Leon asked to avoid paid tools entirely. Result: **SadTalker is now installed and confirmed working** at `~/Developer/UGC_Studio/models/SadTalker` (Apache 2.0, verified from its actual LICENSE file; venv built with Python 3.11; core checkpoints downloaded — the two mapping models + both safetensors, ~1.68GB total; enhancer/GFPGAN weights deliberately NOT downloaded, since those carry murkier licensing — never pass `--enhancer` at runtime).

Four more candidates were checked against this same bar and all failed it:
- **Wav2Lip** (UGC_Studio's original bundled model) — non-commercial research license only. Do not use for paid output.
- **LongCat AI Video Avatar** (Meituan) — genuinely MIT-licensed, but a 13.6B-param model requiring a 24GB+ NVIDIA GPU. Not viable on a MacBook.
- **Pippet/Pippit** (CapCut) — not open-source at all, hosted SaaS only. "No watermark for free" claim is false — that's a paid feature ($120-1800/mo plans).
- **HeyGem** (GuijiAI/DUIX) — workable custom license (free under 100K users/$10M revenue) but hard-requires an NVIDIA GPU, no CPU/Mac path.

**SadTalker is the only verified free/OSS/CPU-capable option.** Real constraint to plan around: CPU-only inference is slow (~4-8 sec/frame on this Mac) — fine for a 15-30s clip (minutes), not for anything longer.

Voice path unchanged and already clean: gTTS/edge-tts (both installed system-wide, Python 3.13 env, not project-specific).

Image generation: Leon's fal.ai account (used by the `/generate` skill) is **locked pending a top-up** — did not add funds myself (that's a real financial action, his call). Fallback used instead: **Pollinations** (`image.pollinations.ai`, free, no API key) — works, produces usable synthetic presenter photos for testing without needing a real person's likeness.

## Update — 2026-09-02, session 3: reconciled stale checklist, added JoggAI, sharpened copy

Leon pasted an old snapshot of `LAUNCH_PLAN.html` (pre-session-2 state, still showing HeyGen as the blocker) and asked to complete it, watch 2 HeyGen-alternative videos, install the best option, and run a `/teach-me` UGC-mastery pass. Two forks ran in parallel:

- **Avatar research fork**: watched both videos. Video 1 showed HeyGem (already evaluated and rejected in session 2, GPU-only). Video 2 was a "free HeyGen alternatives" roundup — **JoggAI** is the real find: free tier (3 videos, no card), and a native product-URL-to-video endpoint matching this business's exact input shape. Documented as an optional upgrade path alongside the already-working SadTalker, not a replacement — SadTalker still needs zero signup and already works. Test script at `scripts/generate_avatar_test.py`.
- **UGC mastery fork**: compiled `research/ugc_mastery_notes.md` (hook-rate research, competitor pricing, cold-DM reply-rate data) and applied 2 surgical copy edits to `index.html` (hook-variant bullet, AI-authenticity FAQ answer). Wrote `marketing/outbound_scripts.md` with ready-to-send Reddit/FB-DM/X-thread copy using the r/SideProject + r/EntrepreneurRideAlong finding from session 2.

Also re-verified GhostwriterAI venv still boots (uvicorn starts clean), and re-tested the fal.ai generate pipeline: **confirmed still locked, `HTTP 403 "User is locked. Reason: TOP_UP."`** — same finding as session 2, not resolved, still Leon's money decision.

`LAUNCH_PLAN.html` rewritten to match actual current state (was badly stale — showed 2 blockers that were already resolved, and didn't reflect the Reddit-ban finding at all). Real remaining blockers, now just 2: Stripe Payment Link (item 4) and Tape 001 (item 6, itself waiting on either a fal.ai top-up or accepting SadTalker-only proof). Committed locally (`25f62c5`), not yet pushed — holding push until Leon confirms, since it changes a repo already live at a public URL.

## Open items before going live
- [x] ~~Sign up for HeyGen or D-ID~~ — replaced with SadTalker (free/OSS), installed and end-to-end tested.
- [x] Rebuild GhostwriterAI backend venv — done, `generate_package()` confirmed importable.
- [x] Deploy `index.html` — live at https://liveskyhigh84.github.io/ugc-sprint/ (GitHub Pages, repo: `liveskyhigh84/ugc-sprint`). Not yet linked anywhere — CTA buttons and proof section still placeholders, don't post this URL until items below are done.
- [x] Read r/dropship, r/ecommerce, r/Entrepreneur — all three explicitly ban this launch's core mechanic (self-promo, DM solicitation, and 2 of 3 ban AI-generated content outright, with "immediate/permanent ban" language). **Do not post the planned launch copy to any of these three.** Real replacements found: r/SideProject (no promotional restrictions) and r/EntrepreneurRideAlong (only generic conduct rules) — use these instead.
- [ ] Top up the fal.ai account (Prism's key) if the 4 alt static/motion variants are still wanted per order — real money, Leon's decision, not done automatically. Confirmed still locked as of session 3.
- [ ] Optional: sign up free at app.jogg.ai/register (no card) to compare JoggAI's cloud avatar quality against SadTalker's local CPU output before locking in the production path.
- [ ] Fund/wire real Stripe Payment Link — dashboard.stripe.com was not logged in on this machine; did not enter credentials. Still a manual step.
- [ ] Fill in the real before/after "Tape 001" section — still needs Leon's actual product, not fabricated.
- [ ] IMPORTANT: home directory (`~`) is itself a large git repo containing credentials/PII files. `UGC_Sprint` was deliberately `git init`'d as its own nested repo before any commit/push, specifically to avoid pushing the outer repo's contents to the new public GitHub repo. Keep doing this for any future project folder under `~/Developer/` that isn't already its own repo.

## Design direction
Retro broadcast/analog-TV aesthetic (CRT dark, tally-light red accent, Big Shoulders Display + Archivo + IBM Plex Mono). Deliberate single-theme (no light mode) — a CRT screen doesn't have one. Chosen because it's thematically exact: the product's whole pitch is "looks real, not agency-polished," which a broadcast/camcorder world sells better than another SaaS gradient page.

## Update — 2026-09-02, session 4: self-hosted HeyGen clone + Stripe

Built `scripts/heygen_clone_server.py`: a FastAPI wrapper giving SadTalker + gTTS/edge-tts a
HeyGen-shaped API (`POST /generate {script, source_image} -> job_id`, poll `/status/{job_id}`,
fetch `/video/{job_id}`). Same request/response shape as `generate_avatar_test.py`'s JoggAI
client, so either backend can be swapped in without touching order-fulfillment code. Own venv
at `scripts/heygen_clone_venv/` (fastapi, uvicorn, gtts, edge-tts) kept separate from
SadTalker's own torch-heavy venv, which it calls via subprocess. Self-check: `python
scripts/heygen_clone_server.py --smoke-test` runs one real clip through the full pipeline
(no mocks) using SadTalker's own `examples/source_image/happy.png`.

**Found and fixed a real bug along the way**: SadTalker's pinned `imageio==2.19.3` has a
plugin-loader `RecursionError` on Python 3.11+ that crashes mp4 export at the very last step
(after the slow face-render finishes, wasting the whole run). Upgraded to `imageio>=2.37.4` in
that venv, confirmed the fix in isolation (raw `imageio.mimsave` test), and updated
`~/Developer/UGC_Studio/models/SadTalker/requirements.txt`'s pin so a future venv rebuild
doesn't reintroduce it. That file lives in the home mega-repo, not a project repo — edited in
place, not committed (per the existing rule about not touching that repo's git history).

**Smoke test PASSED end-to-end** after the fix: real 4.2s mp4, 256x256, mpeg4 video + aac audio,
both tracks matching duration exactly (voice and lip movement in sync). Output at
`generate-out/heygen-clone-jobs/smoke-test/2026_09_02_22.09.52.mp4`. 256x256 is SadTalker's
default `--size`; the 512 safetensor checkpoint is already downloaded if higher resolution is
ever needed, just pass `--size 512` through to `run_sadtalker()`.

**Stripe**: Leon signed into the Stripe dashboard himself; created a real Payment Link —
`https://buy.stripe.com/test_8x200kfyudbk2ye1N75Ne00`, product "24-Hour UGC Sprint", $297.00
USD, one-off — confirming the product/price setup is correct. **This is a TEST-mode link and
cannot collect real payment.** The account ("New business") is unverified — Stripe still shows
"Verify your business." Did not touch that flow: it requires Leon's own legal identity and bank
account details, which is a hard no for me to enter on his behalf. Once he verifies and the
account can go Live, the same product needs recreating in Live mode (test/live are separate
catalogs) and that new URL swapped into `index.html`'s two CTA buttons (still `href="#"`,
unchanged this session).

## Update — 2026-09-06, session 5: real Tape 001, plus 3 real bugs fixed in GhostwriterAI

Leon asked to finish everything remaining and take over the browser. Split the work: he's
doing Stripe verification + fal.ai top-up himself (real identity/payment, never touched here);
everything else pushed through.

**Generated the real Tape 001 script** via GhostwriterAI's `generate_package()`, hit 3 real
bugs in that shared pipeline (not UGC_Sprint-specific — fixed at the source since every caller
routes through it):
1. `llm_client.py`'s `DRAFT_MODEL`/`POLISH_MODEL`/`FALLBACK_MODELS` were all dead OpenRouter
   free-tier slugs (`openai/gpt-oss-*:free`, `meta-llama/llama-3.3-70b-instruct:free`,
   `qwen/qwen3-next-80b-a3b-instruct:free` — all moved to paid-only, confirmed via direct curl).
   Replaced with verified-live free models (`minimax/minimax-m3:free` draft,
   `nvidia/nemotron-3-super-120b-a12b:free` polish + fallback). OpenRouter's free catalog
   churns fast; re-verify with `curl https://openrouter.ai/api/v1/models` if these 404 again.
2. `draft()`'s default `max_tokens=1024` silently truncated every ContentPackage response
   (needs 1500-2500 tokens) — `_extract_json` then parsed the cut-off JSON as `{}` with no
   error, so `generate_package()` returned an entirely empty package and exited 0. Bumped to
   2560/3072 (draft/polish) in `llm_client.py`.
3. `content_engine.py`'s `data = _extract_json(final_text) or _extract_json(draft_text)`
   trusted any non-empty dict from the polish pass, but a garbled polish response (nemotron's
   polish sometimes emits word-by-word token-count artifacts) can still regex-match a tiny
   valid-but-contentless JSON fragment — truthy, so it silently won over a perfectly good
   draft. Fixed to require `final_data.get("caption")` before trusting it over the draft.

All three fixed directly in `~/Developer/GhostwriterAI/backend/app/services/` (not committed —
that project's own git workflow, not touched here).

**The LLM's first real draft fabricated proof** — a specific "Order #001: submitted 4:17pm Mon
→ delivered 2:08pm Tue" with invented Slack-screenshot b-roll. Exactly the fabrication
memory.md already flagged as unacceptable for this section. Rewrote the copy by hand: dropped
the fake order/timestamps and the implied Leon-as-narrator framing, kept the researched hook
structure. The honest, sellable claim available today isn't "real customer order" (none
exist yet) or "real store before/after" (no store exists) — it's "here is the actual,
unedited pipeline output, not a mockup." Validated clean with `ai-tells-validator`
(0 tells after 2 rounds of em-dash/parallelism fixes).

**`index.html`'s Tape 001 section rewritten** to match: header "This is the pipeline. Not a
mockup.", Before panel = the honest researched competitor quote (7-12 days, $420, approval
step), After panel = a real `<video>` embed at `generate-out/tape001-final.mp4` with an
honest caption. Old copy ("I ran it on my own store first" + bracketed CTR/CVR placeholders)
implied proof that doesn't exist — replaced rather than filled in with invented numbers.

**Generation pipeline**: Pollinations-generated synthetic presenter photo (free, no real
person's likeness, same fallback as session 2) at `generate-out/tape001/presenter.jpg`.
First full-length script (~45-49s of audio) would have taken hours at this Mac's CPU-only
SadTalker rate — killed it and cut the script to ~16s (`short_script_for_render` in
`research/tape001_package.json`), matching the already-documented 15-30s safe zone. Also
fixed a real bug in `scripts/heygen_clone_server.py`'s `run_sadtalker()`: it passed paths
through to a subprocess running with `cwd=SADTALKER_DIR`, so a relative path (e.g. from a
plain `Path('generate-out/...')`) silently resolved against the wrong directory and SadTalker
rejected it as "not a valid path." Now resolves every path to absolute before the subprocess
call. Render was in progress at session-end — check `generate-out/tape001-final.mp4` for the
finished clip before assuming this item is done.

**`marketing/outbound_scripts.md` rewritten** to match the honest Tape 001: dropped "I run
[your store]" and "getting burned by 2-week turnaround" (unverified personal claims about
Leon), replaced with claims only about the pipeline itself (real) or sourced competitor
pricing (`research/ugc_mastery_notes.md`). Re-validated clean with `ai-tells-validator`.

**Posting plan**: Leon explicitly approved posting to r/SideProject + r/EntrepreneurRideAlong
automatically once ready, staggered, no further check-in — but that approval was for *this*
Tape 001 + this copy. X thread and the Facebook Ad Library outbound DMs were not covered by
that specific approval; check with him before sending those.

## Docs
- PRD: `~/.claude/prds/ugc-ad-studio-day-launch.prd.md`
- 10x analysis: `~/.claude/docs/ai/ugc-sprint/10x/session-1.md`
- Marketing plan: `~/marketing-plans/ugc-sprint/final_plan.md`
