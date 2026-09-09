# TikTok Symphony — third avatar-generation option

From video "I Found a Secret AI Avatar Generator (Better Than HeyGen)" (Malva AI,
youtu.be/d9FcPjyf4I0, 2026-09). Same tool this project's sibling, UGC_Studio, already
documented from an earlier Malva AI video — see `~/Developer/UGC_Studio/FREE_AI_GENERATORS.md`
Section 5 and `build_product_ugc_tab()` in `app.py`. Nothing to install: it's a browser tool,
not an API or local model, so "integration" here means documenting the free path, same as
UGC_Studio did.

## What it is

TikTok Symphony Creative Studio, made by ByteDance (CapCut/TikTok's parent). Free tier:
**200+ videos/week (1,000 weekly credits, reset weekly)**. Sign in with Google, no card.

## Why it matters for this project right now

Both other avatar paths have real limits: SadTalker (local, free, CPU-only) keeps failing to
finish background renders in this session for unclear environment reasons (see memory.md
session 5); JoggAI (cloud, free tier) is down to 1.5 of its original 2 credits after one
Tape 001 render. Symphony's quota is an order of magnitude larger and needs no local compute.

## How to use it (Voiceover Avatars — talking head from script, the exact UGC Sprint shape)

1. Go to ads.tiktok.com/creative/creativestudio/home (verified working 2026-09-08; the earlier
   ads.tiktok.com/creativeai/symphony/home URL 404s), sign in with Google.
2. Left sidebar -> Tools -> Voiceover Avatars.
3. Browse the avatar catalog, pick one, preview auto-plays.
4. Continue -> paste the script into the Script field.
5. Pick a voice (filter by language/accent/age/gender).
6. Generate -> it renders the voiceover first, regenerate if it's off before committing to video.
7. Library tab -> download the finished video once ready.

There's also a Product Avatar feature (upload one product photo, avatar holds it, animates
into a UGC ad) — closer to the "hold the product" ad style than a straight talking-head, worth
trying for order fulfillment variety but not needed for Tape 001 specifically.

## Not done here

No account created, no sign-in attempted. This needs Leon's own Google sign-in the same way
JoggAI did — his call whether to use it for the next real render. Free/no-card either way.

## Recommendation

Use Symphony as the primary avatar path going forward given its quota, keep JoggAI as backup
until its credits refresh (if they do on a free tier) or Leon upgrades, keep SadTalker as the
zero-signup fallback if both cloud options are ever unavailable.
