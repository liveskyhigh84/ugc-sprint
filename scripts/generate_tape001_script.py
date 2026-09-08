#!/usr/bin/env python3
"""One-off: generate the real script + shot list for Tape 001 (dogfood ad).

Uses GhostwriterAI's generate_package() against the UGC Sprint offer itself —
the "I built this, here's the proof" angle from marketing/outbound_scripts.md.
Real LLM call (OPENROUTER_API_KEY from GhostwriterAI's .env), no mocks.
"""
import asyncio
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path.home() / "Developer/GhostwriterAI/backend"))


class Brand:
    id = 1
    name = "24-Hour UGC Sprint"
    target_audience = "ecommerce/DTC sellers whose ad creative testing is bottlenecked by slow, expensive UGC turnaround"
    brand_voice = "direct, specific, build-in-public. No hype, no vague claims, real numbers only."
    core_usps = [
        "24-48hr turnaround vs 7-12 business days from creator marketplaces",
        "$297 flat one-time, no subscription lock-in",
        "1 talking-avatar video + 4 alt hook variants, full usage rights, no creator approval step",
    ]


SIGNALS = (
    "Hook rate (>3s watch) is the single predictive metric for UGC ad conversion; "
    "71% of viewers decide scroll-or-watch within 3 seconds. Structure that converts: "
    "Hook(0-3s) -> Problem(3-8s) -> Solution(8-15s) -> Showcase(15-30s) -> Proof(30-40s) -> CTA(40-45s). "
    "AI-UGC reads as fake when shot/paced like a commercial; reads as authentic when framed like a "
    "phone-shot review — slightly off-center, casual pacing, direct address, single continuous take feel. "
    "Competitors: Arcads $110-220/mo subscription, Billo $59-150+/video with 7-12 day turnaround, "
    "Icon $999/mo human-filmed. Nobody sells a one-time, no-lock-in, sub-48hr package — that's the gap."
)


async def main():
    from app.services.content_engine import generate_package
    pkg = await generate_package(
        brand=Brand(), platform="tiktok", pillar="founder build-in-public demo", signals=SIGNALS
    )
    out = Path(__file__).parent.parent / "research/tape001_package.json"
    out.write_text(pkg.model_dump_json(indent=2))
    print(f"Saved: {out}")
    print(json.dumps(pkg.model_dump(), indent=2)[:3000])


if __name__ == "__main__":
    asyncio.run(main())
