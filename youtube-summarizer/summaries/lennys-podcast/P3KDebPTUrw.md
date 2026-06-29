# OpenAI Codex lead on taste, curation, and building for AGI | Andrew Ambrosino

Video ID: `P3KDebPTUrw`

## Summary
Andrew Ambrosino, product and engineering lead for the Codex app at OpenAI, discusses how AI is fundamentally inverting the product development process — making implementation cheap and making taste, curation, and judgment the new scarce resource. He covers how team roles are collapsing and reforming around agency and taste rather than rigid functional boundaries, why design remains hard for AI, and how Codex is evolving from a developer tool toward a general-purpose knowledge work platform. The conversation is most relevant to product managers, designers, engineers, and founders navigating how to build and organize teams in an AI-native environment.

---

## Key insights

- **Implementation is no longer the expensive part — curation is.** The old product process (research → ideate → prototype → implement) was designed around expensive implementation. Now anyone can build anything instantly, so the bottleneck has flipped: the hard part is evaluating 90 simultaneous prototypes and deciding what's good, what to fold together, and what to kill.

- **Codex has 90%+ weekly active usage across all of OpenAI — not just engineers.** Marketing, comms, finance, legal, and other non-technical staff use it weekly, even though the app was originally built as a developer tool. This internal signal drove the decision to broaden Codex beyond a coding tool.

- **Codex has grown 6x in usage since January and has over 5 million weekly active users.** Andrew notes this number is likely already out of date.

- **The primal mark problem with prototypes.** Because implementation is now cheap, there's a dangerous temptation to jump straight to a prototype. But a polished-looking prototype anchors everyone's thinking too early — it becomes the "primal mark" that all subsequent decisions react to, even if the underlying product direction is wrong. The medium (doc vs. prototype) should be chosen deliberately based on what you're trying to communicate or test.

- **Taste is multi-dimensional, not just aesthetic.** Taste includes: systems thinking (how does this fit the larger system?), directional clarity (where are we going?), presentation judgment (what medium to use?), semantic coherence (does this animation match its meaning?), and the core question of "if we can build anything, what *should* we build?"

- **AI is bad at design for specific structural reasons.** (1) Design is harder to grade — it requires human taste as a feedback mechanism, making training loops more tedious. (2) Labs historically prioritized capabilities that accelerate AI research (correct code compiles; good design doesn't have the same flywheel). (3) Design requires novelty, whereas software engineering rewards over-indexing on known patterns. (4) Good design requires understanding deep code abstractions — e.g., knowing that two visually different components share semantic meaning in the codebase and should be treated as one system.

- **Release timing relative to model capability is a product variable.** The Codex app released in February would have failed if released in November — the only difference was model quality. The shape of the product was identical; the outcome was totally different. This means products can be "correct but early" and need to be re-released as models improve.

- **"Baby" versions of the product as a design tool.** OpenAI uses a dramatically simplified codebase ("baby Codex") that approximates all production interactions, making it fast to vibe-code exploratory UI changes without touching the real codebase.

- **Role collapse is real but dangerous if misapplied.** OpenAI's Codex team has seen more role collapse than most — designers write code, PMs write technical specs. But eliminating roles entirely is risky because it can erase accumulated discipline knowledge and best practices. The better framing: roles are defined by the *average* of where someone spends their time, not rigid boundaries.

- **Zone defense for product people.** In an environment of abundant, uncoordinated building, PMs should spread out across the product surface to ensure coverage, identify gaps, and steer work toward coherence — rather than clustering around the same areas.

- **Planning philosophy: precision decays with time horizon.** Short-term plans need detail. Nine-month plans should stay intentionally hazy because any precision added is false precision. Instead, prototype all candidate features, let them sit, and re-test each time models take a leap — readiness is model-dependent, not just team-dependent.

- **Andrew's daily workflow with Codex.** He uses a scheduled automation that scans 3,000 Slack channels, surfaces what needs his attention, and delivers a daily brief. He can respond by coaching the automation conversationally ("next time, worry about this instead"). He also built a Gmail filter using Codex + computer use to handle unsolicited cold email.

- **Codex extended itself into Premiere Pro.** The in-house videographer used Codex to edit videos. When Codex couldn't do everything via file editing, it autonomously built a Premiere Pro extension, installed it, and used that extension to control the app. This emerged without being designed for.

- **The "super app" direction (without the label).** The vision is Codex as a home base where you start, end, and automate work — connecting to and orchestrating other apps (Excel, Premiere Pro, Linear) rather than replacing them. It opens other apps when needed rather than trying to recreate their specialized UIs.

- **Autonomous development loops are close but not quite ready.** Andrew wants a loop that improves the app, listens to Twitter/Slack/email, and self-directs. The blockers: models tend to increase code complexity rather than reduce it, and teaching a model which features to build vs. ignore vs. reframe is unsolved. He explicitly called out: make models better at *deleting* code.

- **Andrew failed for 10–15 years before Codex.** Sold a startup for parts, spent years in heavily regulated industries where AI tools repeatedly didn't work. His current success surprised him. Key lesson: don't marry your process, marry the outcomes you're uniquely able to deliver.

---

## Use cases

- **Product managers** deciding when to write a PRD vs. build a prototype — the framework applies directly to choosing the right medium for the right stage.
- **Engineering leaders** managing teams where everyone is building uncoordinated prototypes — the curation and zone defense models provide a structure for imposing coherence.
- **Designers** trying to understand where their role is heading and how to remain relevant as AI handles more visual execution work.
- **Founders** deciding when to release an AI-powered feature — the "wait for the model" framework helps avoid shipping too early and poisoning the well for a good idea.
- **Anyone building internal AI workflows** — the Slack brief automation and Gmail filter examples are directly replicable patterns.
- **Teams evaluating role structure** — the "average of where you spend your time = your role" heuristic helps teams avoid both rigid silos and chaotic role elimination.
- **Companies scaling beyond engineering users** — Codex's internal discovery that non-engineers refused to leave a developer-focused app offers a useful case study in product-market fit signals.
- **Videographers, editors, and non-technical knowledge workers** curious about using Codex — the Premiere Pro story demonstrates the "just try it" approach to agentic task delegation.

---

## Patterns & frameworks

**The Inverted Product Process**
Traditional process: research → ideation → prototyping → implementation (expensive end). AI-native process: implementation is free and immediate, so the expensive end is now curation, taste, and steering. Teams should reorganize around evaluation and judgment rather than gatekeeping implementation.

**The Primal Mark / Medium Selection Framework**
Before creating any artifact, ask: what is this for? If it's to achieve product clarity around a vague area, write a document. If it's to stress-test an interaction pattern with real hands, build a prototype. The problem is that a polished prototype anchors all future thinking — the first mark on the canvas becomes the thing everyone reacts to, even if it was meant to be exploratory.

**Zone Defense for Product**
PMs should position themselves like defensive players covering a zone — spreading across the product surface to ensure full coverage, rather than clustering. The goal is to identify gaps in ownership, steer uncoordinated efforts, and maintain product coherence across a high-output, bottom-up building culture.

**Role as Average, Not Boundary**
Instead of defining roles by what they can't do (design stops here, engineering starts there), define them by the center of mass of where someone spends their time. This allows fluid overlap while still preserving meaningful specialization by domain.

**Release Timing as a Product Variable**
A product's shape and a model's capability are independent variables. Releasing the same shaped product at different points in model development can produce completely opposite outcomes (Codex in November vs. February). Framework: prototype features early, let them sit, and re-test with each model capability leap rather than abandoning the idea.

**Baby Product Prototyping**
Maintain a dramatically simplified version of the production codebase (baby Codex, baby Cursor) that approximates all key interactions. Use this for rapid UI exploration without touching production. This replaces or supplements Figma-level prototyping with something that runs real code.

**Home Base + Connector Model**
Rather than trying to replace every specialized tool, build the AI app as a home base that orchestrates other tools — connecting to Excel, Premiere Pro, Linear, etc. via connectors, computer use, or purpose-built extensions. The product opens other apps when needed rather than recreating their UIs. Two inverse sub-patterns: (1) Codex reaching into existing native apps, (2) users opening web apps inside Codex for agent-assisted interaction.

**Precision Decay Planning**
The shorter the time horizon, the more detail a plan needs. Long-horizon plans (9+ months) should stay intentionally hazy — false precision wastes time and anchors teams to futures that model leaps will make obsolete. Instead, maintain a backlog of candidate features, prototype them, and batch-activate them when model readiness catches up.