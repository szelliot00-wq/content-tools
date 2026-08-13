# How OpenAI makes product decisions and builds at speed —  Blaine Billingsley (OpenAI)

Video ID: `71lzRMZ-VOI`

## Summary
This episode features Blaine Billingsley, a designer at OpenAI with prior experience at Gmail, Airbnb, YouTube, and Slack, discussing how he and a single engineer built OpenAI's product design plugin for ChatGPT. The conversation covers how LLMs are changing the practice of product and design work — from ideation and prototyping to evaluation and team structure. The core argument is that the fundamental principles of good design (rapid ideation, volume of ideas, sharing early, not being precious) remain unchanged, but AI dramatically compresses the time and cost of executing those principles. It is most relevant to product managers, designers, and builders at startups or fast-moving teams who are trying to understand how AI tools change their day-to-day workflow and team dynamics.

## Key insights
- **The design plugin was built by just two people** — Blaine (designer/subject matter expert) and one engineer — with no formal roadmap, NDA'd external users, or structured research process in the early stages. Everything was experience- and vibes-based initially.
- **The role of a designer has fundamentally shifted toward output evaluation.** A major new part of Blaine's job is defining what "good" looks like, writing evals, running them heuristically, and grading outputs — something categorically absent from traditional design roles.
- **LLMs can generate 80 ideas in 8 minutes** — what used to require a full team in a design sprint (crazy eights: 8 ideas in 8 minutes) can now be done solo at 10x scale while you're at lunch. The "make a thousand pots" principle applies: volume always beats trying to find the perfect idea.
- **The cost of imagining is now near zero.** You can start with a Homer Simpson supercar concept and refine it — wild, throwaway ideation is no longer expensive. This shifts the bottleneck from ideation to refinement and judgment.
- **The "second 80%" problem is still real.** Getting to a prototype is dramatically faster, but going from prototype to production remains grueling. Blaine's team had to rewrite everything mid-project when the ChatGPT desktop app and Codex were merged in about three weeks, with no prior warning.
- **Evals are the new spreadsheet.** Early on, Blaine's team hill-climbed on a narrow set of prompts, then an internal colleague tried a marketing website style they'd never considered and it failed badly. The lesson: share with a third person as fast as possible to widen the aperture; throwaway eval sets are more immediately useful than a fixed golden set.
- **OpenAI has no traditional roadmap process.** Priorities emerge and "everyone swarms." Alignment comes from a single clear company goal that everyone can articulate, rather than OKRs or quarterly planning cycles. This works at speed but carries risks as companies scale or growth plateaus.
- **Roles are blurring.** Blaine describes being "either the worst engineer on the team or we're all project managers." Specialization still exists (he can dial in a UI in 10 minutes; his engineer can fix a failing CI test faster), but the boundaries are much softer. There was no dedicated PM on this project.
- **Junior designers are thriving** — they don't carry the baggage and presumptions of experience, and some of the best work Blaine has seen recently comes from very junior people. Experience still buys taste and judgment, but the runway to being effective is much shorter now.
- **Group rituals must be actively preserved.** Working with AI agents risks operating in your own world. Blaine notes that the science shows individual ideation followed by group sharing beats pure group brainstorming, but the sharing rituals must be protected intentionally. With a two-person team, this happened naturally; at scale it requires deliberate effort.
- **Real user research was minimal pre-launch.** The team only got a couple of companies to test the plugin literally days before launch. Post-launch, they worked from prompt classifications (not raw prompts, due to privacy) to infer what users were actually doing.
- **Failure modes matter as much as success.** Borrowed from his Gmail days ("declaring bankruptcy"), Blaine emphasizes knowing the worst-case output and being okay with it — especially at massive scale where you can't anticipate every use case.
- **The plugin's core capabilities:** web browsing for inspiration, FigJam mood board generation and organization, generating 10+ distinct design style variants, mocking up full UI flows in React, sharing prototypes via ChatGPT Sites, and auditing entire product surfaces via automated screenshots.

## Use cases
- **Solo founders or small teams (1–2 people)** who need to cover ground typically requiring a full design sprint team.
- **Designers at any level** looking to use ChatGPT as a daily driver — specifically for inspiration gathering, rapid style exploration, flow prototyping, and component auditing.
- **Non-designers who need design** (e.g., engineers, marketers, PMs) who want to mock up ideas without Figma expertise.
- **Design system managers** who want to audit component usage across a product surface without manually screenshotting every screen.
- **Product teams onboarding to evals** — specifically those moving from traditional A/B testing or user research to LLM-graded output quality.
- **Org leaders** trying to maintain alignment in fast-moving, low-process environments without formal roadmaps or OKRs.
- **People transitioning into AI-era product/design roles** who need to understand what to unlearn (rigid role boundaries, precious ideation) and what to learn (evals, volume-based creativity, judgment over execution).

## Patterns & frameworks

**Make a thousand pots (volume > perfection)**
Derived from a pottery parable: the group that makes 1,000 pots always produces better work than the group trying to make one perfect pot. Applied here: use LLMs to generate massive volumes of ideas/mockups rather than laboring over a single direction. The best ideas emerge from the pile.

**Crazy Eights at scale**
The classic design sprint exercise (8 sketches in 8 minutes, one per minute) is reimagined: an LLM can produce 80 coherent ideas in 8 minutes. The exercise's original purpose — forcing volume and avoiding preciousness — is preserved but massively amplified. Blaine delegates the generation phase to the LLM while he's in a meeting, then returns to curate.

**The "second 80%" rule**
The first 80% of building (concept → working prototype) now takes a day or a weekend. The remaining 80% (hardening, integrating, shipping to production) is still weeks of grueling work. Useful as a reality check to prevent teams from thinking a ChatGPT prototype is production-ready.

**Declaring bankruptcy (failure-mode-first design)**
From Blaine's Gmail/Inbox days: before shipping, deliberately ask "what is the worst thing this product will do?" and make sure that failure mode is known and acceptable. Especially important at scale where you cannot cover every use case — focus as much on bounding failure as on optimizing success.

**Throwaway eval sets > golden sets (for active development)**
Two-phase eval strategy: (1) a golden regression set to ensure nothing breaks as you iterate — built up over time; (2) throwaway sets tied to what you're currently building, covering wide scenario variety. The throwaway sets are more immediately valuable during active development. Share with a third person as fast as possible to expose blind spots.

**Fork and go wide / go deep decision**
When a prototype is generated, explicitly decide at each iteration whether to go wide (generate more variants, stay in ideation) or go deep (pick one direction and flesh out the full flow). Blaine treats this as a conscious phase gate rather than letting the tool dictate direction.

**Jazz band model for teams**
Roles on a product team are like instruments in a jazz ensemble: what matters is not the specific instrument (title/role) but whether it fits the band's current need (soloist vs. accompanist, high vs. low end). Teams should organize around strengths and fit rather than formal job descriptions. Especially apt in AI-era teams where role boundaries are dissolving.

**Individual ideation → group share (avoid groupthink)**
Scientifically validated pattern Blaine references: the best group creative output comes from individuals going away to ideate independently and then reconvening to share — not from brainstorming together in a room. AI accelerates the solo phase dramatically, but the group sharing ritual must be actively maintained or collaboration collapses.