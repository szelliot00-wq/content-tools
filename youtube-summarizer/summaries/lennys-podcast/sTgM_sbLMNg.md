# What it takes to be a top PM today | Robby Stein (Google Search)

Video ID: `sTgM_sbLMNg`

## Summary
Robby Stein, VP of Product at Google Search (previously Instagram), shares a three-chapter playbook for building great products drawn from nearly 20 years of consumer product experience. His central argument is that the PM's core craft has always been decision-making — and that AI now makes the execution side of product building so accessible that taste, judgment, and deep human understanding matter more than ever. The talk is structured around three sequential phases: understanding people deeply, diagnosing root causes analytically, and delivering craft and polish. It is most relevant to PMs, founders, and builders working on consumer products, particularly in the AI era.

## Key insights
- **The PM's core skill is decision-making, not execution.** As AI commoditizes the ability to build, the differentiator becomes judgment and taste — not organizing, shipping, or project managing.
- **"Jobs to Be Done" is the foundation.** People don't use products; they hire them. The job behind a bed purchase turned out to be "don't wake me up when my partner moves" — not cooling, eco-friendliness, or price. You can't discover this without deeply contextual conversations.
- **Multimodal AI at Google Search was driven by a human insight:** People came for inspirational shopping journeys (e.g., finding a couch), but text-only chatbots couldn't convey visuals. The team invested early in multimodal retrieval to match that core need.
- **"AI Mode" on Google Search succeeded when it integrated trusted Google signals** (maps, star ratings, closing times, photos) that users expected. The missing ingredient wasn't more AI — it was the authority and familiarity users already associated with Google.
- **Root cause diagnosis is iterative and recursive.** When Instagram Stories wasn't being adopted broadly, they asked "why aren't you doing the thing?" instead of "why did you do it?" The top-ranked answer was audience anxiety ("my ex, my teacher, my aunt is on it"), not any missing feature.
- **Quantifying qualitative root causes matters.** After surfacing the audience anxiety theme from interviews, the team ran a large-scale quantitative survey (thousands of respondents) to confirm weight and priority before investing two years solving it.
- **Close Friends on Instagram took two years and many failed permutations.** A version called "Favorites" with a private profile backdoor and feed posting failed because it was confusing. The only thing that worked was isolating it entirely within Stories.
- **Reels launched in Brazil as ephemeral and failed.** The team assumed creators wouldn't want goofy dances living on their profiles forever. The actual insight: creators wanted audiences, virality, and permanence — the opposite assumption. The fix was making Reels a permanent, standalone format.
- **AI can now scale user research.** Stein describes using opted-in user feedback at scale, where a model analyzes qualitative comments (e.g., "you knew backpack sizing but didn't ask about my son's height or weight") and stack-ranks themes — surfacing the same insights that once required manual interview synthesis.
- **AI agents can act as QA and use the product autonomously.** Stein built an internal tool that sends an agent through Google Search flows, screenshots results, and evaluates them against a rubric — checking things like LaTeX rendering on math questions or whether a visual tray appears for bioluminescent queries.
- **Craft = no user pain + emotional delight.** These are the two dimensions of finish. Pain is measurable; delight is about communicating that the creators genuinely cared.
- **Google's redesigned search box is a case study in delight.** The cursor blinks through Google's four brand colors; tapping the box triggers an animated "jump" with haptic feedback. These micro-details regularly go viral organically because they signal intentionality and humanity.
- **The playbook is not new — AI just makes it more powerful.** Understand people deeply → diagnose root causes analytically → build with craft. All three steps are now faster and more scalable with AI tools.

## Use cases
- A PM trying to prioritize a roadmap who is unsure whether to invest in features vs. fundamentals — use the root-cause diagnosis loop first.
- A founder whose early product isn't getting traction — apply Jobs to Be Done interviews to uncover the real reason people aren't adopting it.
- A team scaling user research beyond what manual interviews allow — use AI to analyze transcripts, surface themes, and quantify weights across thousands of responses.
- A PM building an AI product who is focused on model capability but missing trust or familiarity signals users expect (the Google AI Mode / maps example).
- A design or PM team deciding how much to invest in motion, haptics, and micro-interactions — use Stein's "does it make people feel something?" test to justify the investment.
- A team running QA on a complex AI product — use autonomous agents to traverse user flows, screenshot outputs, and evaluate against a rubric instead of relying on manual testing.
- A PM or founder in the AI era questioning whether their role still matters — the talk directly addresses how PM value shifts from execution to judgment as AI handles more building.
- Anyone interviewing for a senior PM role who needs a coherent, defensible philosophy of product building.

## Patterns & frameworks

**Jobs to Be Done (Clayton Christensen / "Competing Against Luck")**
People hire products to do a job. To find the real job, put yourself back into the exact moment of a purchase or adoption decision — ask about the day, the context, who was there, what was happening. The goal is to surface the underlying need (e.g., "don't disturb my sleep") that feature-level thinking (cooling, price) would miss entirely. Stein recommends this as the starting point for all product thinking.

**Root Cause Diagnosis Loop**
Once you have a product, ask: "Why aren't people doing the thing that is our goal?" (the inverse of Jobs to Be Done). Collect all answers as leaf nodes, group by theme, then run a large quantitative survey to assign weights. Rank the themes. Fix the highest-priority one. Repeat recursively. Stein frames this as analogous to training epochs in ML — each pass gets you closer to product-market fit.

**The Three-Chapter PM Playbook**
1. **Understand people deeply** — discover the core job to be done through contextual interviews.
2. **Diagnose root causes** — analytically identify, rank, and fix the specific blockers preventing adoption or satisfaction.
3. **Deliver craft** — eliminate user pain and deliberately engineer emotional delight (motion, color, haptics, intentionality).

**AI-Scaled Research Agent**
Use an AI agent trained on Jobs to Be Done methodology to conduct user interviews at scale, then use a second model to analyze transcripts, source specific jobs, and quantify theme weights — replacing or augmenting manual interview synthesis.

**Autonomous QA Agent**
Deploy an agent that acts as a user (types queries, navigates flows, takes screenshots) and evaluates outputs against a rubric. Surfaces spec deviations (broken LaTeX, missing visual trays) without requiring a dedicated QA team or manual PM walkthroughs.

**Two-Dimension Craft Test**
For any product experience, ask: (1) Does it work perfectly with zero user pain? (2) Does it make the user feel something — joy, excitement, delight? Both must be true for a product to feel like its creators cared about it.