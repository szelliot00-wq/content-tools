# Stop planning for 2027: how OpenAI builds product 90 days at a time | Tara Sesha and Nan Yu (OpenAI)

Video ID: `-ciSTkEVy30`

## Summary
This talk features Tara Sesha and Nan Yu from OpenAI, interviewed by Claire (the moderator), at what appears to be a product conference. They discuss how OpenAI builds product in 90-day cycles rather than annual plans, the philosophy behind shipping imperfect things fast, the design challenges of agentic experiences, and how classic PM skills are evolving. It is most relevant to product managers, designers, and founders building AI-native products — especially those navigating the tension between quality, speed, and rapidly shifting model capabilities.

## Key insights
- **Ship imperfect things for empirical learning.** Tara, coming from Stripe's culture of deep polish, had to fundamentally shift her mindset. The ChatGPT "toggle" (switching between chat and agentic mode) was explicitly called an imperfect solution, but getting agentic capabilities into the hands of 1B+ users outweighed the cost of imperfection.
- **Plan 2–3 months out, not years.** Tara keeps a personal doc of things she incorrectly predicted to remind herself how bad long-range forecasting is. The sweet spot is building for where models will be in 60–90 days — not anchored to today, not so futuristic the product is unusable.
- **Annual planning is market-dependent.** Stripe can do multi-year planning because payments market dynamics are stable and legible. OpenAI cannot — the pace of the market determines the right planning cadence. This is not universal advice; it's context-sensitive.
- **Give enterprises what they need, not what they ask for.** Enterprises said they couldn't absorb change, yet OpenAI pushed agents to them anyway — because staying in chat-only mode would have caused them to get leapfrogged by competitors. Classic "build what users need, not what they say they need."
- **Capability overhang is the real constraint.** Nan's framing: models can do far more than users currently take advantage of. The binding limit isn't capability — it's users' ability to absorb and discover what's possible.
- **Internal dogfooding as a quality bar.** Tara's team ships features internally first and watches for retention, delight, and surprising utility. There's no hard numeric bar — it's a feel for whether something is unlocking genuinely new value.
- **The "last mile" problem is worse than a non-starter.** Nan argues that a tool that gets 99% done and then fails is worse UX than one that never starts — the unfulfilled promise is more frustrating. Computer use wins because it always completes the job, even if slowly or expensively.
- **Single vs. multi-agent architecture depends on use case, not philosophy.** Both speakers landed on: data permissions, memory segmentation, credential handling (service account vs. user account), and context isolation (the "Severance" analogy for a private Slack channel) are the practical product questions that determine architecture — not abstract philosophical preference.
- **The "chief of staff" agent pattern emerges naturally.** When users manage many agents, they organically create a meta-agent to orchestrate the others. Nan notes this is users "cheating" the 40-agent problem by collapsing it into managing one.
- **Platform layering over binary build-vs-ecosystem.** Tara described ChatGPT's approach as offering hooks at multiple layers: native platform features → first/third-party plugins → computer use as a fallback. No single layer is expected to handle everything.
- **Working with research requires a completely different skillset.** Tara's advice: bring hyper-specific user sessions and use cases, write evals, and show researchers concrete model failure modes. That eval loop — not PMs writing PRDs — is how you influence post-training.
- **The "DMable PM" is becoming table stakes for consumer AI products.** Direct, ongoing user relationships that previously existed in dev-tools/enterprise contexts now matter at consumer scale. Subtle agentic failures (e.g., "Astra had an attitude") require follow-up questions and rich context that only direct user relationships surface.
- **User predictability of agent behavior is a new quality bar.** When agents act semi-autonomously, users must be able to anticipate what will happen. The old escape hatch of a settings popup or a modal no longer works.
- **Onboarding has become disproportionately important.** Nan flagged this as newly elevated — the empty input box problem (users have a powerful tool and don't know what to do with it) is a primary driver of capability underutilization.
- **Privacy and data transparency are newly non-negotiable.** Tara called out that users need to understand how their data is used and what norms govern the product, especially when agents act on their behalf.
- **Voice and self-driving (proactive product initiation) are the near-term bets.** Tara is "so bullish on voice" — cites reduced tech support burden for family, intuitive for non-technical users, and OpenAI's internal onboarding using it. Nan's bet is on products that onboard themselves — smart enough to guide users rather than presenting an empty box.

## Use cases
- **PMs at AI companies struggling with planning cadence** — whether to commit to annual OKRs or shift to rolling 90-day cycles.
- **Enterprise product teams** deciding whether to hold back agents to avoid overwhelming customers, or push them forward aggressively.
- **Founders launching imperfect V1 products** who need mental permission to ship before everything is polished.
- **PMs and designers building agentic or multi-agent products** — specifically around identity, memory segmentation, and permission architecture.
- **Product leaders new to working with ML/research teams** who need a framework for how to collaborate and add value (evals, specific session data).
- **Consumer product teams** thinking about whether and how to be directly accessible to users at scale.
- **Platform teams** deciding what to build natively vs. expose as hooks for third-party integrations.
- **Anyone building onboarding for AI tools** where capability overhang means users don't naturally discover product value.
- **PMs in established, slower-moving industries** (like payments) evaluating whether the "no long-range planning" advice actually applies to their context.

## Patterns & frameworks

**The 90-Day Planning Horizon**
Build for where models will be in 2–3 months. Not the present (you'll ship something already obsolete) and not years out (predictions are almost always wrong). Planning cadence should match market pace — fast-moving AI markets justify short cycles; stable markets may still warrant longer ones.

**Ship → Empirical Evidence → Iterate Loop**
Rather than optimizing a priori, get the feature to real users as quickly as possible, observe actual behavior, and iterate. Theoretical modeling is less valuable than session-level data. The toggle is the canonical example: imperfect solution, but the empirical learning it unlocked was worth the UX cost.

**Internal Dogfooding Quality Gate**
Before external release, ship internally and watch for: retention, delight, surprising utility, and novel use case unlocking. Not a numeric threshold — a qualitative sense that the product is adding, not just shipping.

**The Layered Platform Model**
Structure AI product capabilities in layers: (1) native platform features, (2) first/third-party plugin hooks, (3) computer use as a universal fallback. Users traverse layers until their goal is met. No layer needs to be comprehensive on its own.

**Capability Overhang as the Binding Constraint**
The real product problem isn't what models can do — it's the gap between model capability and user awareness/adoption. Product work should focus on closing that gap through onboarding, discoverability, and intuitive interfaces.

**Evals as the PM's Currency with Research**
When collaborating with ML research/post-training teams, PMs add the most value by: bringing specific user sessions showing failure modes, writing evals that reproduce those failures with given prompts/skills, and showing researchers a reproducible path to the desired model behavior. Generic PRD-style "users want X" is insufficient.

**The "Guest in Your Home" Experience Standard (Charles Eames quote)**
The bar for a well-designed agentic experience: users should feel like guests whose needs have been anticipated and quietly provided for. Applied to AI products, this means the model and product surface should proactively scaffold what users need before they know to ask — Nan's "self-driving onboarding" prediction is the direct extension of this principle.

**Three Core Skills for Agentic Product Building**
1. User empathy / mental model mapping (human nature, how people naturally organize tasks)
2. Systems and platform thinking (permissions, memory, credentials, composability)
3. Relentless empirical iteration (try, take the pain, try again — not just analyze)