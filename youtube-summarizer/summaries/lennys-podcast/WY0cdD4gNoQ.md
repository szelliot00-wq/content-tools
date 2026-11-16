# Meta’s Muse: Inside the launch of the most successful consumer product this year | Mona Sarantakos

Video ID: `WY0cdD4gNoQ`

## Summary
This episode of Lenny's Podcast features Mona Sarantakos, VP of Product at Meta Super Intelligence Labs and head of product for Muse — Meta's personal AI agent that became the fastest-growing AI consumer product of all time. Mona walks through the full origin story of Muse, from a weekend spent with Open Claude on a Raspberry Pi to launching a product that now sits atop the App Store. The conversation covers the product principles, team culture, design decisions, and hard-won lessons that shaped Muse into what it is. It is most relevant to PMs, founders, and product builders working on AI-native consumer products.

---

## Key insights

- **Origin was a Nat Friedman ping, not a formal initiative.** In late January, Nat Friedman messaged the team saying he was using Open Claude and they needed to try it. Mona spent an entire weekend with it on a Raspberry Pi, connecting it to her email, calendar, and home automation. That Monday morning newsletter summarizing her kids' week was the "magic moment" that convinced her this was the future.

- **The product went through three distinct build phases:** (1) figuring out what the product even was, (2) getting to a working end-to-end prototype by spring, and (3) a long final stretch focused entirely on reliability, safety, and security — which is what consumed most of the seven months before launch.

- **"Trust is a must" was the guiding principle for the delayed launch.** The team believed that if they shipped too early and had a catastrophic failure, users would never trust the agent again. Because Muse has access to personal context and can take real-world actions (purchases, emails, etc.), the safety bar had to be self-defined — existing industry benchmarks weren't sufficient.

- **Safety evals were layered into a hierarchy:** core safety evals (prompt injection, harm) that anything must pass; capability evals (browser use, task completion); behavioral evals (personality, intent understanding, follow-up questions); and use-case-level evals (shopping, health, finance). System prompts and behavioral specs must be handwritten — not AI-generated.

- **Jolly the avatar nearly died many times.** Lead designer Alex Cornell created it as a one-shot temporary placeholder (named after his daughter "Jolly Bug"). Every few months someone in leadership would say there's no way they'd ship with a stuffed animal. It survived because: (a) a full animation/avatar system had been built around it, (b) Mark Zuckerberg personally loved it, and (c) the team held a core principle that a corporate logo would "break the spell" for a product meant to feel deeply personal.

- **The chat bubble UX was deliberately non-obvious.** Most AI products were moving toward large canvas/essay-form responses. The team chose chat bubbles to make Muse feel like communicating with a real personal assistant via messaging. This created a cascade of hard downstream decisions (how to break up long responses, whether carousels feel weird in a chat thread, etc.) that the team is still working through.

- **Main chat vs. side chat was the most polarizing internal debate.** The team originally shipped with just one main chat thread, reasoning that a true personal assistant maintains one continuous context. Employee reaction was fierce — people fought in comment threads about it. They eventually added side chats due to demand, but Mona remains personally committed to the main chat approach.

- **Agent swarms replaced traditional dashboards for user insight.** Swarms of agents analyze production conversations, surface patterns, generate synthetic data, and return structured "dumps" of insight. This was critical because Muse generates long, multi-turn conversations — a data type that didn't exist in Meta's prior AI products (which were mostly single-turn). Mona makes all her PMs use this approach because it creates empathy, not just metrics.

- **Shopping emerged as a surprise top use case.** Mona expected personal productivity, health, and personal finance to dominate. Home automation — big during the Open Claude days — underperformed. Shopping came out of nowhere, driven partly by head of engineering Christina Wod's obsessive dog-fooding. The team had to retroactively build evals around it.

- **Mark Zuckerberg's key contribution was reframing the product from task completion to life goals.** Early on the team was laser-focused on whether Muse could complete individual tasks. Zuckerberg pulled them out of that and said the core purpose is helping users achieve their goals and improve their lives. This unlocked the "dreaming and study" concept (Muse proactively thinking about how to help you while you sleep) and led to the Goals tab in the UI.

- **The board meeting prototype almost didn't work.** The team decided at the last minute to show the prototype at a board meeting that had a completely different pre-read. The prototype broke an hour before the meeting. It was fixed five minutes before showtime. Mona says she thinks about the alternate universe where it stayed broken.

- **The team was tiny — about 10 people initially, under 100 total at launch (including functions).** Only four PMs built the entire product. The small size was deliberate: it kept decision-making fast, communication tight, and trust high. Post-launch, they're growing slightly but are "obsessive" about not becoming a large team.

- **Activation remains the hardest problem.** The biggest lever is word of mouth — people literally handing their phone to a friend showing how they use it. Second is getting users past the first prompt (most people type "hi" or "what's the weather"). The Ideas Tab with pre-packaged "starter packs" was built to address this. Early adopters needed less hand-holding; later cohorts now require tiered onboarding variants.

- **The role of PM has fundamentally changed.** The biggest shift is from abstract specification documents to rapid concrete prototyping — anyone can now build something in 24 hours to have a real conversation about. Product taste is now the most valuable PM skill, because engineers are increasingly product-minded themselves and AI slop is easy to ship. The PM's job is to hold the bar and represent the consumer.

- **Two Muses talking to each other was a memorable (and cautionary) early experiment.** Two team members put their Muse agents in a group chat. One agent revealed the other user had been to a doctor's appointment the previous day — a discretion failure that immediately surfaced as a hard problem for any multi-agent/multiplayer context. The agents also got into a passive-aggressive fight with each other, which Mona describes as "one of the most hilarious things in the world."

---

## Use cases

- **Consumer AI product builders** trying to understand what it takes to build a trusted, personal AI agent at scale
- **PMs navigating when to launch** vs. when to keep iterating — especially in high-trust, high-stakes product categories
- **Design leaders** thinking about how to make AI products feel personal rather than corporate
- **Teams building AI evals** looking for a framework to structure safety, capability, behavioral, and use-case evaluation layers
- **Founders and early-stage teams** deciding how small to keep a core team and when/how to involve leadership
- **Product teams** trying to increase activation and onboarding for a complex, multi-capability product
- **Anyone building agentic products** grappling with non-determinism, long-running multi-turn context, and user trust
- **PMs interviewing for or growing into leadership** looking for what high product taste looks like in practice

---

## Patterns & frameworks

**"Trust is a must"**
Internal mantra at Muse. The principle that in an agentic product with personal context and real-world actions, a single early catastrophic failure can permanently destroy user trust. This drove the team to hold a very high quality bar before launch even as competitors shipped faster.

**Zero-basing**
Meta's internal term for starting a product over rather than iterating on something that isn't working. Used on Meta AI before Muse was conceived. The question is: keep optimizing, or start fresh?

**Three-phase build structure**
(1) Discovery/prototyping — figure out what the product is, don't worry about reliability yet. (2) Functional completeness — working end-to-end product. (3) Reliability, safety, and security gate — the bar you must clear before shipping anything with personal context.

**Layered eval hierarchy**
Priority evals (must always pass, e.g. safety/prompt injection) → Capability evals (browser, task completion) → Behavioral evals (personality, intent understanding) → Use-case evals (shopping, health, finance). Each layer has sub-evals. New features open new eval vectors.

**Agent swarms for user insight**
Deploy swarms of agents to analyze production conversations, identify patterns, surface problems, and generate synthetic training data. Replaces (or augments) dashboard-only analytics with empathy-generating qualitative insight at scale. Used for both ongoing monitoring and fast debugging of suspected issues.

**"Let them cook"**
Engineering culture principle: give talented, high-taste engineers a kernel of an idea and unstructured time to prototype. Don't over-specify. React to what emerges rather than writing a full spec upfront. Works best with a talent-dense, product-minded engineering team.

**Main chat / unified context model**
Design principle that a personal agent with long-running memory should have one continuous conversation context, mirroring how a real personal assistant operates. Controversial internally but grounded in the product principle that the agent knows everything about you across time.

**"The product is yours, Meta fades away"**
Core product principle that shaped design decisions including keeping Jolly instead of a corporate logo. If the agent is meant to be your personal agent, the brand of the company building it should recede. This principle also made it easier to defend unconventional decisions in internal debates.

**Tiered onboarding by user cohort**
Early adopters who understand agents need different onboarding than mainstream users who don't know how Muse differs from a chatbot. The team now serves onboarding variants based on inferred familiarity level rather than a one-size-fits-all first-run experience.