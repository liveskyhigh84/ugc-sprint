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

## Open items before going live
- [x] ~~Sign up for HeyGen or D-ID~~ — replaced with SadTalker (free/OSS), installed and end-to-end tested.
- [x] Rebuild GhostwriterAI backend venv — done, `generate_package()` confirmed importable.
- [x] Deploy `index.html` — live at https://liveskyhigh84.github.io/ugc-sprint/ (GitHub Pages, repo: `liveskyhigh84/ugc-sprint`). Not yet linked anywhere — CTA buttons and proof section still placeholders, don't post this URL until items below are done.
- [x] Read r/dropship, r/ecommerce, r/Entrepreneur — all three explicitly ban this launch's core mechanic (self-promo, DM solicitation, and 2 of 3 ban AI-generated content outright, with "immediate/permanent ban" language). **Do not post the planned launch copy to any of these three.** Real replacements found: r/SideProject (no promotional restrictions) and r/EntrepreneurRideAlong (only generic conduct rules) — use these instead.
- [ ] Top up the fal.ai account (Prism's key) if the 4 alt static/motion variants are still wanted per order — real money, Leon's decision, not done automatically.
- [ ] Fund/wire real Stripe Payment Link — dashboard.stripe.com was not logged in on this machine; did not enter credentials. Still a manual step.
- [ ] Fill in the real before/after "Tape 001" section — still needs Leon's actual product, not fabricated.
- [ ] IMPORTANT: home directory (`~`) is itself a large git repo containing credentials/PII files. `UGC_Sprint` was deliberately `git init`'d as its own nested repo before any commit/push, specifically to avoid pushing the outer repo's contents to the new public GitHub repo. Keep doing this for any future project folder under `~/Developer/` that isn't already its own repo.

## Design direction
Retro broadcast/analog-TV aesthetic (CRT dark, tally-light red accent, Big Shoulders Display + Archivo + IBM Plex Mono). Deliberate single-theme (no light mode) — a CRT screen doesn't have one. Chosen because it's thematically exact: the product's whole pitch is "looks real, not agency-polished," which a broadcast/camcorder world sells better than another SaaS gradient page.

## Docs
- PRD: `~/.claude/prds/ugc-ad-studio-day-launch.prd.md`
- 10x analysis: `~/.claude/docs/ai/ugc-sprint/10x/session-1.md`
- Marketing plan: `~/marketing-plans/ugc-sprint/final_plan.md`
