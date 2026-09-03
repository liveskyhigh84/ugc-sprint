# UGC Sprint — mastery notes (teach-me pass, 2026-09-02)

Structured for retrieval, not lecture: each section ends with the one thing to actually change or remember.

## 1. What makes a UGC ad convert

**The hook is the whole game.** 71% of TikTok/Reels viewers decide scroll-or-watch inside 3 seconds; average decision is 1.7s. A hook rate above 30% is considered strong in 2026; crossing 40% roughly doubles downstream conversion. The hook has to be about the viewer's situation or pain — not the brand — before the product ever appears. "Cleared my acne in six weeks" beats "great for your skin" because specificity reads as evidence, vagueness reads as ad copy.

**Structure that holds up**: Hook (0-3s, stop the scroll) → Problem (3-8s, name the pain) → Solution (8-15s, product as the fix) → Showcase (15-30s, product in use) → Proof (30-40s, a result) → CTA (40-45s). This is already implicit in the "5 hooks, one product" offer — worth stating on the page as *why* 5 variants matter, not just that they exist. Done: reworded the hook-variant bullet on index.html to name this directly.

**Fake vs authentic**: AI-UGC reads as fake when it's shot/paced like a commercial — too clean, too centered, too polished a voiceover. It reads as authentic when it's framed like a phone-shot review: slightly off-center, casual pacing, single continuous take feel. This is a production instruction for whatever avatar tool ends up wired (SadTalker per memory.md), not just copy — worth flagging to whoever builds the actual generation prompt/shotlist templates in GhostwriterAI: bias toward "phone camera, direct address, casual" framing in the shot list, away from "cinematic, wide shot, professional lighting."
**Remember**: hook rate is the single number that predicts everything downstream; the offer's core value is testing 5 hooks instead of 1.

## 2. Competitive landscape (confirmed 2026 pricing)

| Tool | Model | Price | Notes |
|---|---|---|---|
| Arcads | AI-generated | $110/mo (10 vids) / $220/mo (20 vids) | ~$11-22/clip, subscription-locked, no one-time option |
| Billo | Human creator marketplace | $59-150+/video, packages $500-2,500 | 7-12 business day turnaround, creator approval required |
| Icon | Human-filmed, positioned as "AI Admaker" | $999/mo for ~6 ads | ~$166/video — premium/human, not a real AI-price competitor |
| **UGC Sprint** | AI, one-time | **$297 flat, 24-48hr** | Only fixed-price fast-turnaround option in this set |

Nobody in this set sells a one-time, no-subscription, sub-48hr package. That's the actual gap, not "AI vs human" — the compare table on the page already leads with turnaround + rights, which is correct; no rewrite needed there.
**Remember**: don't compete on "AI-generated" as the pitch (Arcads owns that framing) — compete on flat price + no lock-in + fast, which nobody else offers.

## 3. Marketing execution, sharpened

**Facebook Ad Library outbound DM**: reply rates split hard by personalization — under 1% generic, ~8% lightly personalized, 12-28% deeply personalized. Tight lists under 50 recipients average 5.8% replies vs 2.1% for 500+ blasts. The move: pull 15-20 stores actually running visibly weak ads (static product photo only, no UGC, running 2+ weeks per Ad Library's "days running" field — long runtime with no UGC variant means they haven't tested this angle), name the specific ad in the DM, and lead with the critique before the offer. Never send to more than ~20/day from one account.

**Reddit**: per this project's own memory.md, r/dropship, r/ecommerce, r/Entrepreneur all explicitly ban this launch's mechanic (self-promo + AI content). Confirmed replacements already found: r/SideProject and r/EntrepreneurRideAlong. Do not deviate from that finding.

**X build-in-public thread**: works when it documents the *build*, not the pitch — screenshots of the actual pipeline, the actual before/after clip, and a specific number (even a small one: "first order, 6 hours in") beat a generic "I built a thing, check it out." Draft below follows this.

**Remember**: every channel here converts on specificity — a named ad, a named subreddit's actual rules, a real number — never a generic version of the message.

## 4. Pricing ladder psychology

The ladder (Rush +$50, base $297, 3-pack $797, Sprint Pass $197/mo, Agency 10-pack $997) already anchors correctly: $297 sits below the $500 Billo package tier and above nothing, so it needs the flat-price + speed framing to justify itself against subscriptions that look cheaper per-unit (Arcads' $11/clip looks cheaper until you count the $110-220/mo floor and no one-time option).

Sprint Pass conversion moment is correctly placed at day 10-14 (hook fatigue window) in the launch plan, not at checkout — pushing it at checkout would compete with the base offer's simplicity. Leave that timing alone.
**Remember**: the ladder's job is to make $297 look like the obvious first step, not the whole relationship — don't front-load the retainer pitch anywhere before delivery.

## Sources
- pixis.ai, cinerads.com, ugcfast.ai, hawky.ai, sideshift.app, reloop.so, vidlo.video (UGC hook/structure benchmarks, 2026)
- eesel.ai, designrevision.com, lensgo.ai, fluxnote.io (Arcads/Billo/Icon pricing, 2026)
- matthewmetros.substack.com, dillantaylor.medium.com, redditapis.com (cold DM reply-rate benchmarks, 2026)

## Changes made to the project from this pass
- `index.html`: reworded the "4 alternate hook variants" bullet to state *why* hooks matter (was generic, now ties to the actual conversion mechanic).
- `index.html`: sharpened the "Is this actually AI?" FAQ answer to preempt the authenticity objection with the phone-shot-vs-commercial framing.
- `marketing/outbound_scripts.md`: new file, ready-to-send copy for Reddit, FB Ad Library DM, and X thread.
- This file.
