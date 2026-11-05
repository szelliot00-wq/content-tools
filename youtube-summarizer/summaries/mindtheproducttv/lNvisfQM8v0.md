# How to close the gap between discovery and delivery | Jenny Martin

Video ID: `lNvisfQM8v0`

## Summary
Jenny Martin, a collaboration coach and former software delivery leader, discusses her OOPSY framework — a navigation tool that bridges product discovery and delivery. The framework, developed over 10 years and recently formalized in a book, draws from BDD (behavior-driven development), lean thinking, and agile practices to help teams stay aligned on outcomes while actually shipping working software. The conversation covers all five layers of OOPSY (Outcomes, Outputs, Process, Scenarios, Inputs), why the framework is unique in joining product thinking with engineering practices, and how it has organically spread across large tech organizations. It is most relevant to product managers, engineers, and delivery leads who want to close the gap between defining what to build and actually building it well.

## Key insights
- The biggest problem in most software teams is that people are "furiously building things without quite knowing why" — OOPSY was created to solve that by anchoring work to outcomes from the start.
- OOPSY is not a new invention — it synthesizes existing best practices (BDD, story mapping, lean, specification by example) into a single coherent flow, removing the religious ceremony of agile without losing the principles.
- The **Asteroids analogy** (borrowed from Jeff Patton, originally from NJ Michael James) captures OOPSY's iterative analysis approach: break down only what you need right now, leave large "asteroids" unexplored until you're ready, or you'll be overwhelmed by millions of tiny fast-moving fragments.
- **Outcomes** are defined as "a meaningful change in the real world that creates value for somebody" — not a revenue number on a spreadsheet. A KPI can be part of the chain of reasoning, but it is not the outcome itself.
- **Outputs** are the verifiable things the system produces that deliver the outcome — e.g., a payslip, a bank balance update, search results on screen. This is distinct from process steps. Finding the right 20% of outputs delivers ~80% of the value (Pareto principle applied at every layer).
- **Process** maps to the user story level — the interactions a user takes to generate an output (e.g., open app → search → receive results). OOPSY helps identify when a story is too large by forcing it through the output/process distinction.
- **Scenarios** are rooted in BDD and specification by example — defining concrete, collaborative examples upfront to test behavior. Jenny distinguishes these from AI evals: scenarios work best for deterministic, quantitative outcomes; evals are better for qualitative/non-deterministic AI outputs.
- **Inputs** are the specific, realistic test data and preconditions that accompany a test scenario. Jenny's experience as a tester showed that ambiguous requirements collapse when real data is introduced — a startup she worked with caught a fundamental data assumption error by showing exact test data to a retail client, saving 3–4 months of wasted work.
- OOPSY can operate at any level of granularity — from portfolio/initiative planning down to splitting a single backlog item — because analysis (breaking things down) is fractal in nature.
- Jenny's Lego Serious Play training exercises consistently produce the same two Lego metaphors from teams worldwide: (1) a customer/stakeholder on a pedestal facing the wrong way, and (2) a wall between engineering and product/business. These are universal pain points OOPSY directly addresses.
- Jeff Patton DM'd Jenny after discovering a major US client had adopted OOPSY to underpin their entire development framework — she had not known, illustrating that frameworks can spread organically from a single blog post.
- The most common failure point: teams struggle most with **outcomes** (going fast in the wrong direction is the dominant problem in the AI era), and secondarily with **outputs** (confusing a process step for a system output).

## Use cases
- **Product managers** who want to connect outcome-based thinking directly to engineering delivery without losing either side.
- **Engineering teams** frustrated by backlogs full of stories with no clear "why" or no clear definition of done.
- **Delivery leads / scrum masters** who observe that teams follow agile ceremonies (standups, Jira, backlogs) but still don't know what they're actually working toward.
- **Teams starting a greenfield initiative** who need a lightweight way to explore complexity without over-specifying upfront (avoid the 700-page functional spec).
- **Teams working on well-understood problems** who need to quickly confirm scope and move fast.
- **Story splitting** — OOPSY provides a principled way to break large stories into vertical slices by output or process step.
- **Stakeholder alignment conversations** — the output/input examples can be shown to business stakeholders to surface false assumptions early (as in the retail API example).
- **Organizations transitioning from waterfall** who want structured thinking without returning to big-upfront-design.
- **AI product teams** using evals — the Scenarios and Inputs layers can complement AI evals by pinning down the deterministic, quantitative parts of system behavior.
- **Facilitators and coaches** running workshops who need a conversation structure that works from strategy level down to task level.

## Patterns & frameworks

**OOPSY Framework (Jenny Martin)**
A five-layer navigation and analysis tool for product delivery. Each layer is also a prioritization opportunity (apply Pareto: focus on the 20% that drives 80% of value):
1. **O — Outcomes**: The meaningful, real-world change you are creating for a customer. Anchors all downstream work to purpose.
2. **O — Outputs**: The verifiable artifacts or system behaviors that prove the outcome is being delivered (e.g., payslip, search results). Not process steps — things the system produces.
3. **P — Process**: The user/system interactions that generate the outputs. This is closest to the user story level and is the natural story-splitting layer.
4. **S — Scenarios**: Concrete examples (BDD/specification-by-example style) that define expected behavior and guide collaboration across product, design, and engineering.
5. **I — Inputs**: Specific, realistic test data and preconditions that make scenarios unambiguous and testable, surfacing hidden assumptions before build.

**The Asteroids Analogy (NJ Michael James, via Jeff Patton)**
A metaphor for iterative analysis: in the arcade game Asteroids, blowing up all asteroids at once creates an unmanageable swarm of tiny fast pieces. Good agile/product work means blowing up one large asteroid at a time, fully clearing it, then moving to the next. Leave large, unexplored "asteroids" (scope areas) untouched until you are ready to work on them. Avoids analysis paralysis and scope overwhelm.

**Specification by Example / BDD (Behavior-Driven Development)**
A practice of defining system behavior through concrete, collaboratively written examples before development begins. Used in OOPSY's Scenarios and Inputs layers to create clear, testable targets for development and avoid ambiguity from abstract requirements.

**Opening Game / Midgame / End Game (Jeff Patton's Story Mapping)**
OOPSY embeds this horizon-of-value structure at the Outputs layer — each release horizon tells a complete, incrementally growing story of value, avoiding the rework and waste that can occur when story mapping is done without output-level thinking.

**Pareto Principle applied iteratively**
At each OOPSY layer, teams are encouraged to identify the ~20% of items (outcomes, outputs, processes, scenarios) that deliver ~80% of the value, rather than exhaustively specifying everything before starting.