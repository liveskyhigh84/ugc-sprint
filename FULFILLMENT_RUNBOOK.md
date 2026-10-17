# UGC Sprint — Fulfillment Runbook ($297 order)

Grounded in code as of 2026-10-17. Deliverable: 1 talking-avatar ad (15–30s) + 4 hook variants, 24–48h, one revision.

**Licence rule (hard):** paid output never uses Wav2Lip (non-commercial research) or Coqui XTTS-v2 (CPML).
Avatar = SadTalker (Apache-2.0), never `--enhancer`. `studio/server.py` enforces this with
`assert_commercial_safe()`; UGC_Studio enforces it with `UGC_COMMERCIAL_MODE=1`.

## 0. Pre-flight (once per session)
```bash
cd ~/Developer/UGC_Sprint
scripts/heygen_clone_venv/bin/python studio/server.py --self-check   # expect 3x PASS incl. "licence guard"
scripts/heygen_clone_venv/bin/python studio/server.py --port 8480 &  # Leverage Studio, local only
```

## 1. Order intake
- Customer pays the live Stripe Payment Link (`BUSINESS_PROCESS.html`), then submits `brief.html`
  (product URL, audience, first-3-seconds hook, claims to avoid) → mailto `jskywalker72@proton.me`.
- Match brief to the Stripe payment email / order ref. **Clock starts at brief receipt.**
- Save the brief to `orders/<YYYY-MM-DD>-<slug>/brief.txt` (create the folder; gitignored work area).

## 2. Script — GhostwriterAI `generate_package()`
`~/Developer/GhostwriterAI/backend/app/services/content_engine.py:538` —
`generate_package(brand, platform, pillar, signals=None) -> ContentPackage`.
Copy `scripts/generate_tape001_script.py`, edit the `Brand` class (name, target_audience, brand_voice,
core_usps from the brief) and `SIGNALS`, change the output path, then:
```bash
~/Developer/GhostwriterAI/backend/venv/bin/python scripts/generate_<order>_script.py
```
Use from the JSON: `talking_head.script` (spoken script, keep ≤30s ≈ 75 words — SadTalker CPU cost scales
with length), `copy.hook_variants` (4 hooks for step 5), `copy.caption`, `image_prompt`.
Strip any claim on the brief's "claims to avoid" list by hand.

## 3. Avatar — SadTalker (default)
Optional presenter image first (Pollinations, $0):
```bash
curl -s -X POST localhost:8480/api/generate/soul -H 'content-type: application/json' \
  -d '{"prompt":"<image_prompt from step 2>"}'            # -> {job_id}
```
Then the avatar video (voice + SadTalker in one job):
```bash
curl -s -X POST localhost:8480/api/generate/avatar -H 'content-type: application/json' \
  -d '{"script":"<talking_head.script>","voice":"edge","source_api_path":"/api/media/<soul job_id>"}'
curl -s localhost:8480/api/jobs/<job_id>                  # poll; completed -> media_url
```
- Runs `run_sadtalker()` (`--still --preprocess crop --cpu`, 256px, ~4–8 s/frame → minutes; timeout 55 min).
- Omit `source_api_path` to auto-generate a presenter.
- **Google Flow (optional, NOT cleared):** `research/google_flow_avatar_option.md`. Do not use for a paid
  order until Leon confirms free-tier commercial-use terms + watermark status.

## 4. Voice — edge-tts / gTTS
Handled inside step 3 by `synthesize_voice()`: `voice` = `edge` | `gtts` | `voicestudio[:<profile>]`.
edge falls back to gTTS on failure. Clone a voice only with written consent. Never XTTS.

## 5. Four variants — `/api/generate/variants`
```bash
# static cards, $0
curl -s -X POST localhost:8480/api/generate/variants -H 'content-type: application/json' \
  -d '{"product_prompt":"<product>","script_hook":"<hook>","count":4,"tier":"paid"}'
# 4s motion variants (paid chain kling-3,wan-3,free, max $0.75/clip; falls to free if fal/Higgsfield unfunded)
  -d '{"product_prompt":"<product>","script_hook":"<hook>","count":4,"motion":true,"tier":"paid"}'
# Higgsfield Ads Studio images (needs HF_API_KEY_ID/SECRET; falls back to local card)
  -d '{"product_prompt":"<product>","count":4,"tier":"paid","engine":"ads","niche":"..","audience":"..","product_image":"<path>"}'
```
`tier:"paid"` only for customer orders. One request uses one `script_hook`; to get 4 different hooks,
send 4 requests with `count:1`, one per `copy.hook_variants` entry. Poll each `job_id` as in step 3.

## 6. AI disclosure (required)
- Tell the customer in the delivery note: avatar and voice are AI-generated (synthetic presenter).
- TikTok 2026 policy: AIGC label on every post with a synthetic avatar/voice + bio disclosure
  (`growth-os/content-engine/social_strategy.md`). Meta: enable AI label. Customer is responsible for
  labelling when they post; we tell them so in writing.

## 7. QC + delivery
- Watch every file end-to-end: lip sync, audio clipped, hook text inside frame, no banned claims.
- `@marketing-short-video-editing-coach` / Paperclip "QC & Delivery" agent for pacing review.
- Deliver via email to the Stripe email: avatar mp4 + 4 variants + caption/hooks + disclosure note.
  Media files: `studio/media/<job_id>/`. Offer the one included revision.
- After delivery: pitch $197/mo Sprint Pass (link still unconfirmed).
