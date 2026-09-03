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

## Open items before going live
- [ ] Sign up for HeyGen or D-ID, compare cost/quality, wire the API key — this is the actual missing piece for order #1.
- [ ] Rebuild GhostwriterAI backend venv (Python 3.11 at `~/.local/bin/python3.11`), confirm `generate_package()` still runs.
- [ ] Read r/dropship and r/ecommerce directly for 10 minutes (self-promo policy + live demand signal) before posting — the research agent couldn't fetch Reddit directly.
- [ ] Fill in the real before/after "Tape 001" section on the landing page with an actual dogfooded example — currently a placeholder callout, deliberately not fabricated.
- [ ] Deploy `index.html` somewhere real (Cloudflare Pages / GitHub Pages / Vercel, all free) and wire the actual Stripe Payment Link into the CTA buttons (currently `href="#"` placeholders — did not create live Stripe products without explicit go-ahead).

## Design direction
Retro broadcast/analog-TV aesthetic (CRT dark, tally-light red accent, Big Shoulders Display + Archivo + IBM Plex Mono). Deliberate single-theme (no light mode) — a CRT screen doesn't have one. Chosen because it's thematically exact: the product's whole pitch is "looks real, not agency-polished," which a broadcast/camcorder world sells better than another SaaS gradient page.

## Docs
- PRD: `~/.claude/prds/ugc-ad-studio-day-launch.prd.md`
- 10x analysis: `~/.claude/docs/ai/ugc-sprint/10x/session-1.md`
- Marketing plan: `~/marketing-plans/ugc-sprint/final_plan.md`
