# From Agile to SIGNAL: launching AI products without the chaos: Elena Luneva at ProductTank SF

Video ID: `i0lidQ42yXw`

## Summary
Elena Luneva, a fractional CPTO with 20+ years in product (Nextdoor, Liquid Space, Brain Trust), argues that the Agile operating system is fundamentally broken for the AI era and proposes a replacement framework called SIGNAL. Her core argument is that while the cost of building software has collapsed (more people can build more things faster with AI), the cost of deciding what to build and safely shipping it has not — and Agile's binary "did it work in the demo?" definition of done is dangerously inadequate for non-deterministic AI systems. The talk is most relevant to product managers, CPOs, and engineering leaders who are either launching AI/LLM-powered products or who have AI agents involved in their development process.

---

## Key insights

- **The building cost has collapsed; the ownership cost has not.** AI lets individuals and teams generate far more prototypes and ideas than before, but deciding what to build and getting it safely to production is just as hard — or harder. Mike Krieger (CPO of Anthropic) is quoted: "The bottlenecks have shifted from engineering writing code to decision making what to build and merge queues."

- **Survey data reveals a readiness gap.** In her research with product and engineering leaders: 85% said they have no clear path from prototype to production; 75% lack evaluation criteria for AI behavioral changes in production; 43% lack risk mitigations and observability for AI-specific risks.

- **Agile has three specific failure modes with AI:** (1) The sprint demo/"definition of done" is binary and doesn't account for behavioral drift; (2) sprint cadence was designed for human-paced builds, not agent-accelerated ones; (3) MVPs get shipped and abandoned, but non-deterministic systems change over time and require ongoing attention.

- **Non-deterministic systems drift in production.** Real example from Brain Trust: a voice interviewing agent worked excellently — better than human recruiters — until a model swap made it "snarky." It told nurses "are you sure you know how to do your job?" This wasn't tracked in observability. The same input now produces different outputs, and that can degrade silently.

- **New dimensions of quality to track:** accuracy, impact, latency, and drift. Previously software either worked or it didn't. Now it can degrade along any of these axes without a deploy.

- **Prompts are the product; the PRD lives in the code.** Because LLMs are highly sensitive to prompts, the prompt is functionally the spec. This creates a traceability obligation — you can no longer audit a PRD or rely on if/then statements in code. Leaders and PMs who aren't reading the code (or using agents to surface it) are flying blind.

- **The "most testable behavior" (MTB) concept replaces MVP.** Instead of asking "does this work?", you ask "what is the most testable behavior that combines an evaluation metric with a business KPI?" This creates a gate for prioritizing the flood of AI-generated prototypes.

- **Healthcare example on behavior rate thresholds:** An 85% accuracy rate is not acceptable for a healthcare AI product. The "definition of done" must be defined as a behavior rate over a specific distribution, not a binary pass/fail.

- **LLMs don't learn in production — you have to teach them.** LLMs run off fixed training and eval sets. Real-world edge cases that emerge after launch don't feed back in automatically. Leaders must build feedback loops that deliberately reintroduce real-world failures into evals.

- **Agent-on-agent oversight is emerging.** Luneva observes a trend: agents doing tasks → chaining of agents → agents overseeing agents → fewer humans overseeing the agent layer. Tools like LangSmith are becoming necessary just to trace what's happening in these systems.

- **QA must evolve from acceptance criteria checking to instrumented observability.** Manual QA (a human pressing buttons to verify specs) can largely be automated via Claude Code, Playwright, and similar tools. But the bigger shift is that non-deterministic outputs require a permanent observability layer, not a one-time QA sprint. More instrumentation means more signals, which means more feedback to process — requiring agent-assisted evaluation pipelines.

- **Communication overhead is a hidden bottleneck.** As more things can be built faster, leaders face more demand for updates and decisions. Luneva notes product leaders spend ~4 hours/week on product updates alone. AI agents can be used to extract this information from code and package it for stakeholders — removing humans from the regurgitation loop.

- **Timeless PM skills remain valuable:** Systems thinking, community and human connection (which AI cannot replicate), and the ability to learn and adapt. Product management itself has only existed ~20 years and has always evolved (data PM → growth PM → AI PM); those who can communicate across functions and translate technology to business outcomes remain in demand.

---

## Use cases

- **AI product teams launching LLM-powered features** who are using Agile and discovering that "it passed the demo" is not a sufficient ship criteria.
- **PMs or CPOs flooded with AI prototypes** who need a structured gate for deciding what gets built and what reaches production.
- **Teams that experienced silent AI degradation** (e.g., model upgrades by the provider changing behavior without notice) and need a monitoring/trigger system.
- **Healthcare, civic tech, or other high-stakes domains** where a suboptimal AI output has real-world consequences and standard QA acceptance criteria are insufficient.
- **Engineering teams adopting agentic development** (Claude Code, Copilot, etc.) who need to rethink QA, test coverage, and definition of done for agent-accelerated build cycles.
- **Enterprise PMs buying/integrating AI products** (not building them) who need to specify behavioral requirements when evaluating vendors and define KPIs tied to business outcomes rather than features shipped.
- **Fractional or portfolio leaders** managing multiple product lines or clients who need event-triggered (rather than sprint-triggered) review cadences.
- **AI-hesitant clients (nonprofit, civic tech, government)** where trust is fragile — the instrumentation-first mindset helps demonstrate rigor and security to skeptical stakeholders.
- **Leaders who are a bottleneck** on their team's decision-making and want to pre-authorize triggers so teams (or agents) can act without waiting for them.

---

## Patterns & frameworks

**SIGNAL Framework**
Luneva's replacement for Agile in AI product contexts. Each letter maps to a practice:

| Letter | Name | What it means |
|--------|------|---------------|
| **S** | Specify the behavior | Define behavior with an MTB (Most Testable Behavior) — combines an eval metric with a business KPI. Prompts are the product; trace them like specs. |
| **I** | Instrument before you ship | Instrument observability and evaluation before release, not after. If you ship without this, you've already lost traceability. |
| **G** | Guard with evals and constraints | Define what agents (and agentic code) are permitted/supervised/blocked from doing. Set a "golden test set" and feedback loop before launch. |
| **N** | Name the triggers | Pre-author event-based triggers that cause behavioral reassessment — model upgrades, distribution shifts, anomaly thresholds — so reviews aren't only sprint-cadence-driven. |
| **A** | Assess the distribution | A system that works on your test set may fail on 30%+ of real workload. Use agents to generate adversarial datasets and test across the real distribution, not just your curated eval set. |
| **L** | Living evaluation | Post-ship is not done. AI systems drift; your observability, evals, and go-to-market messaging must continuously reflect what's actually in production. |

---

**MTB — Most Testable Behavior (replaces MVP)**
A mental model for scoping AI feature releases. Instead of "minimum viable product," ask: what is the smallest unit of behavior that (a) can be evaluated against a clear metric and (b) ties to a business KPI? This creates a repeatable gate for prioritizing prototypes and defining when something is truly "shippable."

---

**Event-Triggered Cadence (replaces Sprint Cadence)**
Agile ties reviews to a fixed time interval (every 1–2 weeks). SIGNAL adds event-triggered checkpoints: model upgrades, prompt changes, distribution anomalies, or new user segments can all invalidate previously validated behavior between sprints. These triggers should be named in advance and, where possible, run automatically by agents rather than waiting for a scheduled review.

---

**Behavior Rate as Definition of Done**
Rather than binary pass/fail, define "done" as achieving a target behavior rate over a specified input distribution (e.g., "correct response on 99% of cases in the healthcare intake distribution"). This makes acceptance criteria continuous and domain-appropriate rather than demo-dependent.

---

**Progressive Agent Authorization**
For teams working alongside coding agents, define explicit permission tiers for what an agent can do autonomously: prototype stage → eval stage → code review → ship. This preserves human oversight at the right gates without requiring humans to be in every loop — and prevents agents from shipping untested work.

---

**Start Small, Show, Then Scale**
Luneva's practical advice for SIGNAL adoption: don't try to instrument everything at once. Pick one project, pick one letter, make it work, and use it as an example for the rest of the team. The sequence she suggests as a common starting point: (1) move to Claude Code, (2) shift QA to agentic tools, (3) get PMs building prototypes rather than writing PRDs.