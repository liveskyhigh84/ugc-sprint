# Talking-avatar API — alternatives to HeyGen

Researched from 2 videos Leon sent (2026-09-02) + doc lookups. Goal: unblock checklist item 1
without necessarily paying HeyGen's per-second rate.

## Comparison

| Tool | Type | Cost | Commercial rights | Fit for launch today |
|---|---|---|---|---|
| **HeyGen** (documented baseline) | Paid API | ~$0.033-0.10/sec (~$2-6/min) | Yes | Works now, no free tier |
| **D-ID** (documented baseline) | Paid API | ~$5.90/min API, or $4.70/mo Studio Lite | Yes | More expensive per-clip than HeyGen |
| **HeyGem** (video 1) | Open-source, self-hosted (GuijiAI/HeyGem.ai) | $0 marginal cost | Yes — Apache-2.0-style OSS, fully offline | **Not viable today**: requires an NVIDIA GPU with 8GB+ VRAM on Windows/Linux. Leon's machine is an 8GB M1 Mac — no CUDA, confirmed below viable tier (see `reference_local_ai_care_package.md`). Would need a rented cloud GPU box (RunPod/Vast.ai), same pattern already used for the LongCat avatar pipeline. Worth building later once order volume justifies renting GPU time — turns the $2-6/min HeyGen cost into near-zero marginal cost per video. |
| **Synthesia** (video 2) | Paid API | $18/mo cheapest plan | Yes | No recurring free tier (one-off free video only) — skip |
| **JoggAI** (video 2) | Freemium, real API | **Free tier: 3 videos, custom avatar, up to 30s, no payment method required.** Paid: $24-29/mo starter, $69/mo creator. API credits: 1 credit / 2 min video generation, 0.05 credit / photo avatar image — exact $/credit needs the dashboard (logged-in only, see docs.jogg.ai/api-reference/v2/QuickStart/Pricing) | Yes | **Recommended path for today.** Free, no card, has a real developer API, and — this is the actual find — a native **"Create Video from URL/Product info"** endpoint that takes a product URL and generates a video directly. That's not just an avatar API, it's the same input shape as this business's whole funnel (product URL → ad). |

## Recommendation

**Use JoggAI to get a working test clip today, keep HeyGen as the paid fallback if JoggAI's free
tier proves too limited, and treat HeyGem as a Phase 2 margin play once volume justifies a rented
GPU box** (not today — do not spend setup time on it before order #1).

Exact next step for Leon (not done here — needs his own signup, no payment involved):
1. Go to https://app.jogg.ai/register, sign up with Google (2 minutes, free).
2. Avatar menu → API settings → copy the API key.
3. Drop it into `~/Developer/UGC_Sprint/.env` as `JOGGAI_API_KEY=...`.
4. Run `python3 scripts/generate_avatar_test.py --product-url "https://your-test-product-url"`.

If JoggAI's free-tier output quality or the URL-to-video endpoint doesn't hold up, HeyGen's
pay-as-you-go ($5 min top-up) from the original checklist is still the fallback — nothing about
this changes that path, it's just no longer the only option to try first.

## Sources
- HeyGem repo: https://github.com/GuijiAI/HeyGem.ai (Windows/Linux, RTX 4070 recommended, 8GB VRAM minimum)
- JoggAI API docs: https://docs.jogg.ai/api-reference/v2/QuickStart/GettingStarted, .../Pricing
- Video 1: https://youtube.com/shorts/KbT5T8FXXGw (HeyGem demo)
- Video 2: https://youtu.be/vFlpaMT3z5I ("Best free alternatives for HeyGen AI Avatar" — Synthesia, JoggAI, Humantic AI)
