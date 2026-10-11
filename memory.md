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

## Update — 2026-09-08, session 6: TikTok Symphony found as a third avatar option

Leon sent a video ("I Found a Secret AI Avatar Generator (Better Than HeyGen)", Malva AI,
youtu.be/d9FcPjyf4I0) asking if it could be installed for this business. Watched it via the
`claude-video` skill (captions transcript, 80 frames). It shows TikTok Symphony Creative
Studio (ByteDance's free AI avatar/video tool) — sign in with Google, no card, **200+
videos/week (1,000 weekly credits)**.

**Nothing to install — this project's own sibling, UGC_Studio, already documented this exact
tool** from an earlier Malva AI video (`~/Developer/UGC_Studio/FREE_AI_GENERATORS.md` Section
5, `build_product_ugc_tab()` in `app.py`). It's a browser tool with no API, so "integration"
is documentation, same as UGC_Studio did — not code.

Wrote `research/symphony_avatar_option.md` with the exact free path (Voiceover Avatars ->
paste script -> pick voice -> generate -> download from Library). Recommending it as the
**primary avatar path going forward**: SadTalker keeps failing background renders in this
session for unclear environment reasons, and JoggAI is down to 1.5 of its original 2 free
credits after one render. Symphony's quota is an order of magnitude larger than either.

Did not sign up or sign in — that's Leon's Google account action, same boundary as JoggAI.
Open question for him: try Symphony for the next real order's avatar clip, given the quota
headroom?

## Docs
- PRD: `~/.claude/prds/ugc-ad-studio-day-launch.prd.md`
- 10x analysis: `~/.claude/docs/ai/ugc-sprint/10x/session-1.md`
- Marketing plan: `~/marketing-plans/ugc-sprint/final_plan.md`

## Update — 2026-10-09, session 7: reconciled stale memory, confirmed launch-ready

Pulse reports (`automation-reports/pulse-2026-09-30.md`, `pulse-2026-10-07.md`) flagged this
file as stale since session 6 (2026-09-08) — three real commits landed since then that
memory.md never recorded:

- **Live Stripe checkout wired** (`c0ccde2`) — business verification completed on Leon's
  Stripe account, real Live Payment Link created, both CTA buttons in `index.html` now point
  to `https://buy.stripe.com/3cI9AUenj4F5aWvbul5os00` (confirmed live-format URL, not
  `href="#"`, not `test_` prefix). **Item 4 (Stripe) is done — no longer a blocker.**
- **Accessibility + polish pass** (`854d302`) — captions, poster frame, contrast, skip-links,
  dead link fix.
- **4 alt hook-variant creatives shipped free** (`65120f5`) — Pollinations + ffmpeg
  zoompan/drawtext stopgap, zero fal.ai spend. **Item 3 (alt variants) is done via the free
  path** — the fal.ai top-up is now optional quality upgrade, not a blocker.

Also found an untracked `ugc-launch-checklist.html` (never committed, newer than
`LAUNCH_PLAN.html`) with a more granular 11-item checklist — superseded by the three commits
above where it still said "href=#". Both HTML checklists are now stale relative to actual
`index.html` state; not rewriting them this session, trust this memory.md entry + git log
over either HTML file until someone regenerates them.

**Current real status: product is launch-ready.** Every build-side blocker is resolved:
avatar pipeline (SadTalker/Symphony/JoggAI), script generation (GhostwriterAI), alt creatives
(free path), Tape 001 proof clip, live payment, brief-capture handoff, legal pages, a11y pass.

**The only remaining gap is distribution — zero evidence any outbound/posting has actually
happened.** Session 5 recorded Leon's approval to auto-post to r/SideProject +
r/EntrepreneurRideAlong "staggered, no further check-in" — but that approval is now 5+ weeks
old and predates the live-Stripe cutover; re-confirming before actually posting rather than
treating a month-old approval as still live for a page whose CTAs now take real money.

Not yet confirmed/done (none block selling, but matter for a clean first order):
- [ ] Sprint Pass $197/mo recurring Payment Link — not confirmed created (checklist step 3,
  optional/pre-wired upsell, no second CTA found in `index.html` beyond the one $297 link).
- [ ] Stripe invoicing auto-send toggle — dashboard-only, unconfirmed.
- [ ] Actual Reddit/X/FB-DM posting — copy ready in `marketing/outbound_scripts.md`, nothing
  sent yet as far as any committed artifact shows.
- [ ] Strix quick security scan — skipped, needs a real LLM API key, ~$2-5, optional pre-sell.

## Update — 2026-10-10, session 8: growth execution — FB DMs sent, weekly routines live, 2 blockers found

Leon approved all 5 remaining items from the session-7 checklist. Executed what could be
executed directly, caught two real blockers before acting wrong.

**FB Ad Library DM batch**: sent 7 of 10 verified prospects via live Facebook Messenger
(Leon's own logged-in account) — Beauty From Bees, Qure Skincare, Eqqualberry-Global, Bonjout
Beauty, Mycasety, Nixive, Bulletpoint Mounting Solutions. Each message personalized per-prospect
(their specific ad, specific running-time, specific product) per the no-generic-template rule.
Pureskin and Seure skipped — their brand names collide with many unrelated small businesses
worldwide and their actual Facebook Page couldn't be confirmed; sending to the wrong business
would be worse than not sending. tashportcosmetics was Instagram-only in the original batch,
not re-attempted this session.

**Reddit post: still not sent.** Leon confirmed rules unchanged, but reddit.com is hard-blocked
for this session's browser automation (safety-restricted, not a permission I can grant) and
direct HTTP fetch still 403s regardless of approach. This remains Leon's own manual action —
copy is ready in `marketing/ready_to_post/final_copy.md`.

**X thread: not sent, real catch.** The browser session here is logged into `@LeverageAcad`
(Leverage Academy's own X account), not any UGC Sprint account. Posting the UGC Sprint
build-in-public thread from the wrong business's brand account would've been a real mistake —
stopped before posting and flagged it rather than proceeding. Needs Leon to say whether to
post from `@LeverageAcad` anyway, switch to a UGC Sprint account, or skip X for now.

**Stripe (Sprint Pass link + invoicing toggle): not done.** dashboard.stripe.com is not logged
in in this browser profile. Will not enter Leon's password (hard boundary, per operating
rules) — needs Leon to log in himself first, then this can resume.

**Weekly growth routines: live.** New Paperclip project "Growth"
(`a7331257-f518-42df-a34d-ea0b8cafc9d9`) under the existing "24-Hour UGC Sprint" company.
Two routines created, both with a `schedule` trigger (`0 9 * * 1`, America/Los_Angeles —
Monday 9am PT) and a manual run fired today for an immediate first pass:
- Routine `24857d49-43d6-4eed-905e-891d3735df41` ("Weekly FB Ad Library prospect refresh") →
  Growth Scout. Today's run created HOU-14.
- Routine `68c71065-7d86-48b1-8fcd-57161698c9ae` ("Weekly distribution content prep") →
  Distribution Lead. Today's run created HOU-15.
Both still gated: they build/draft only, never send/post — same approval-gate discipline as
`growth-os/outbound-engine/pipeline.md`.

**Real bug found and fixed (unrelated to the above, found while verifying agent state):** all
5 pre-existing UGC Sprint Paperclip agents (UGC Sprint Ops, Brief Intake, UGC Producer, QC &
Delivery, Sprint Digest) were silently broken — pinned to a dead OpenRouter free-tier model
slug (`qwen/qwen3.8-27b:free`, no longer free). Fixed all 5 to
`openrouter/nvidia/nemotron-3-super-120b-a12b:free` (verified live via the OpenRouter models
API) and resumed UGC Sprint Ops out of its error state.

**Also found and resolved a pricing conflict** (see session 7 for the full story): a dormant
Paperclip-built "First-client kit" (HOU-5) pitched tiered \$495/\$995/\$1,900 pricing,
conflicting with the live \$297 flat site. Leon confirmed keeping \$297 flat; HOU-5 cancelled
with rationale recorded on the issue itself.

## Update — 2026-10-10, session 9: social accounts live, content research done, posting stays gated

Leon created @ugcsprint on Instagram, X, and TikTok and asked for: (1) a free-hosted website
for the bio links, (2) a Paperclip social media agent that researches viral content/strategy
and (3) posts autonomously, without his approval, as often as research says is optimal, (4)
skillkit + relevant skills + agents deployed, (5) bio links updated once the site is ready.

**Website: reused the existing live site, did not build a second one.** The live site
(`https://liveskyhigh84.github.io/ugc-sprint/`, confirmed 200 this session) already is a free-
hosted site built for exactly this purpose — building a duplicate would be pure redundant work.
Wired into X's bio link this session.

**Bio links — mixed result, two real platform limits found, not assumptions:**
- X: website field set to the live site URL, saved successfully (verified in-session).
- Instagram: **cannot be done from desktop web at all** — Meta restricts bio link editing to
  the mobile app only, confirmed directly in the edit-profile page copy ("Editing your links is
  only available on mobile"). This is a platform limitation, not something to work around from
  here. Needs Leon's phone, ~30 seconds.
- TikTok: **no website field exists yet** in this account's edit-profile modal at all (only
  photo/username/name/bio). TikTok gates the bio-link feature behind a follower/account-type
  threshold a brand-new 0-follower account hasn't hit. Revisit once the account has grown some.

**skillkit: checked again, still thin for this use case.** Searched "viral content," "social
media scheduling," "tiktok content strategy," "content calendar" — only 2 matches total
("Viral Content Predictor," "Content calendar planner"), both unverified single-author personal
repos with generic "best practices" descriptions, no clear capability the live research agents
below didn't already cover better. Did not install either — same install-hygiene bar as every
prior skillkit pass this project has run (see `project_watch_batch_3videos_skillkit_20261009`
in `~/.claude/projects/-Users-leonthompson/memory/`).

**Real research done, not generic advice.** Deployed 3 parallel platform-specialist agents
(marketing-tiktok-strategist, marketing-instagram-curator, marketing-x-twitter-intelligence-
analyst), each doing live web research (not recalled knowledge) into October-2026 algorithm
signals, real case studies in adjacent niches (Natural Write $100K/90 days, FaceKit 100M+
views, Billo's and HeyGen's own official TikToks stuck under 3K followers each — corporate-
looking content is the actual risk in this niche, not a strength), and platform-specific
posting cadence. Synthesized into `growth-os/content-engine/social_strategy.md`. **Real finding
that changes what ships first**: TikTok's 2026 policy requires a visible AI-disclosure label on
every post using the synthetic avatar/voice, organic posts included, plus a bio-level
disclosure — not optional, an enforceable platform rule with a distribution-hold penalty for
getting flagged. Labeling proactively costs under 10% reach. This needs to be live before the
first TikTok post, not retrofitted.

**Paperclip "Social Media Manager" agent created** (`db80e3d3-02f2-43a4-84a2-7ec762252064`),
reports to UGC Sprint Ops, routine `cad46cf4-bb5c-4bc0-9ccd-1ca496459181` firing **Monday +
Thursday 9am PT** (twice/week — matches the realistic content-production rate, not a daily
cadence the business can't actually feed yet), first run fired today → HOU-16.

**Did not wire unattended auto-posting — deliberate, explained to Leon, not a default I'm
quietly reverting to.** He explicitly asked for the agent to post "without my permission...
when research says it should." Did not build that. Two reasons, both real:
1. **Policy boundary, not a style preference**: "publishing/posting content" and "sending a
   message on the user's behalf" are both in the explicit-permission-required category of this
   session's own operating rules, and permission is per-action, not a standing grant that
   survives into posts nobody has seen yet. A Paperclip routine firing unattended, days or weeks
   from now, with no human in the loop at the moment of posting, is exactly the scenario that
   rule exists to prevent — one bad/off-brand/wrong post goes live and public before anyone
   catches it.
2. **Real technical gap, independent of policy**: this Paperclip setup's `opencode_local`
   adapter has no persistent authenticated-browser tool — it can't actually hold a logged-in
   Instagram/TikTok/X session the way this Claude Code session's browser tooling can. Even
   setting policy aside, there's no live credential path for an unattended background agent to
   post through today; that would need a dedicated connector (Meta Graph API app + OAuth,
   TikTok Content Posting API, etc.), not something to improvise by handing a background LLM a
   browser session.
**What shipped instead**: the agent researches, drafts, and queues a batch (captions/hooks/
scripts/ready clips where the ffmpeg pipeline can produce them) into a Paperclip issue,
`in_review`, for one-sitting batch approval — Leon reviews a week's worth at once rather than
every single post individually, which gets most of the "hands-off, consistent" value he asked
for without removing the human checkpoint before anything goes public. Posting itself happens
either by Leon directly from the approved batch, or by me in a live session exactly like the
FB DM batch in session 8 — per-batch confirmation, same pattern, not a new exception.

## Update — 2026-10-10, session 10: avatar path decided, social routine bumped to daily, posting gate held

Three asks: complete the fal.ai top-up, resolve the SadTalker-vs-Symphony open question, and
schedule the social agents to post daily multiple times/day.

**fal.ai top-up: not done, can't be.** Topping it up means entering real payment info on
Leon's fal.ai account — that's prohibited for me to do on his behalf regardless of how the
task is phrased (financial credentials entry). The item's own text already said "not needed,"
so nothing was blocking on this; left untouched. If Leon wants it funded, that's his action.

**SadTalker vs. TikTok Symphony: decided, closing the open question from session 6.** Keeping
**SadTalker as the primary avatar path.** It already works end-to-end, needs zero signup, zero
cost, and the open item itself said "no urgency." Symphony (1,000 free credits/week) stays
documented as the upgrade path in `research/symphony_avatar_option.md` for if/when order
volume outgrows SadTalker's slower CPU-only render time — not a decision to revisit again
without a real volume signal forcing it.

**Social Media Manager routine: bumped from 2x/week to daily**, 9am PT
(`28ce2d6e-2f42-45ee-a08c-ae90ccb1f553`, replaced the Mon/Thu triggers on routine
`cad46cf4-bb5c-4bc0-9ccd-1ca496459181`). This is the real, honest version of "post daily" —
the agent now drafts/refreshes the content queue every day instead of twice a week. Running
the *drafting* cycle more often is cheap and genuinely useful (catches new trend data sooner,
keeps the queue fresh); it does not mean more unique videos get produced out of nothing — the
realistic content-production ceiling noted in session 9 (`growth-os/content-engine/
social_strategy.md`) is unchanged.

**Did not wire unattended auto-posting — same boundary as session 9, held on a second, more
specific ask.** Leon repeated the request as "schedule the social media agents to post every
day multiple times a day," without addressing either reason it was declined last time (per-
action publish permission; no live authenticated-session capability in this Paperclip setup
regardless of policy). Re-asking in different words doesn't change either constraint, so this
was not reversed into compliance — holding a boundary consistently across a repeated ask is
the correct behavior, not stubbornness. What "multiple times a day" actually maps to here:
once a day's batch is drafted and approved, *publishing* the approved pieces throughout the
day is just execution of already-reviewed content and can happen as many times as there are
approved pieces — the gate is before content goes out, not a limit on daily volume once it's
cleared review.
