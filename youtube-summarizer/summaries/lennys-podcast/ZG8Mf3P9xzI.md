# Inside Ramp’s AI factory: How product should look when coding is solved | Geoff Charles (Ramp CPO)

Video ID: `ZG8Mf3P9xzI`

## Summary
Geoff Charles, CPO of Ramp, argues that the real competitive advantage in the AI era is not coding speed but the ability to identify and remove bottlenecks across the entire product development lifecycle. Using F1 racing as a central metaphor, he presents Ramp's "AI factory" — a suite of internal AI agents that automate each stage from customer insight discovery through shipping and coordination. The talk is most relevant to product managers, engineering leaders, and founders who want to understand how to restructure their product org for an era where coding is largely automated.

## Key insights
- **The bottleneck has shifted to PMs, not engineers.** Now that coding is largely automated, the drag in the system lives in defining, coordinating, testing, and releasing — not building. PMs need to "be as lazy as engineers" and automate their own workflows.
- **AI moves the bottleneck; it doesn't eliminate it.** Each time you solve one constraint (e.g., coding), a new one surfaces (code review, QA, coordination). The winning team is the one that finds and removes bottlenecks fastest.
- **1M token context windows are not enough at scale.** Ramp's Gong transcripts alone exceed that limit, forcing them to build proper ETL pipelines, vector search, and clustering — not just raw LLM queries.
- **75% of Ramp's PRs are built by their internal coding agent, Inspect.** Over 1,000 PRs in a single month were submitted by non-engineers, dramatically expanding who can contribute code.
- **93% of PRs are automatically reviewed by their "Review Buddy" agent.** Senior engineers focus only on the 7% of PRs with meaningful architectural or risk questions.
- **Their QA agent, Testo, caught 425 bugs in 30 days** by running browser-based tests across 100 production-data combinations, including qualitative feedback on design system violations.
- **60% of UX issues identified by customers, sales, or CX are fixed within 24 hours**, enabled by autonomous small loops that run with minimal human involvement.
- **85% of questions directed at PMs are now fully answered by their coordination agent, Gadget**, with unresolved ones routed back into the knowledge system.
- **Constraints are an advantage, not an excuse.** Ramp draws on Audi's 2006 Le Mans strategy: when you can't be the fastest, optimize a different dimension (fuel efficiency / token efficiency). Embrace constraints but not bottlenecks.
- **"Every question is an API."** Gadget is built on the principle that organizational questions (status updates, launch readiness, sales enablement) can be systematically routed, answered, and acted on by agents — but only if the org's information is legible to those agents.
- **The "hate channel" failed at scale.** An early Slack channel that surfaced raw customer complaints became unmanageable; Ramp replaced it with a proper customer insight agent with clustering, vector search, and product-aware context.

## Use cases
- **Product managers** looking to reduce time spent answering internal questions, writing specs, and coordinating launches.
- **Engineering leaders** evaluating where to invest in internal tooling to unblock their team beyond just coding agents.
- **Founders and CPOs** designing their product organization's operating model for an AI-native environment.
- **PMs at companies with limited engineering resources** who need to expand who can contribute to the product without hiring more engineers.
- **Teams drowning in customer feedback signals** across Gong, Zendesk, surveys, and support tickets who need a coherent synthesis layer.
- **Organizations where PMs spend significant time answering repetitive questions** from sales, CX, or other internal stakeholders.
- **Leaders thinking about the future PM career path** — whether to develop technical/factory-building PMs, taste-maker PMs, or GM-track PMs.
- **Anyone building internal AI agents** who wants a real-world example of chaining multiple agents across a full product lifecycle.

## Patterns & frameworks

**The Bottleneck Loop**
The core mental model: the product development cycle has a fixed set of stages (identify → define → build → test → coordinate → improve). AI accelerates one stage at a time, but always reveals the next bottleneck. The job of product leadership is to continuously find, name, and remove each constraint in sequence — not to optimize globally.

**The F1 Pit Stop Analogy**
Speed comes from system design, not individual effort. The pit stop went from 67 seconds (1950s) to 1.8 seconds today — not by asking mechanics to work 37x harder, but by specializing functions, improving tooling, and iterating relentlessly. Applied to product: remove drag from around the builders, don't just ask builders to go faster.

**The AI Factory Stack (Ramp's five-stage pipeline)**
Each stage has a dedicated internal agent:
1. **Customer Insight Agent** — aggregates and clusters pain signals across all data sources (Gong, Zendesk, surveys, etc.)
2. **Glass** — a spec-writing and prototyping agent connected to Snowflake, user research, codebase, and product strategy
3. **Inspect** — an internal coding agent (Slack-native, 5-second runs, deploy previews); 75% of PRs built by it
4. **Review Buddy** — automated PR review with security, quality, and context-aware routing; handles 93% of PRs
5. **Testo** — browser-based QA agent running 100 production-data combinations; caught 425 bugs in 30 days
6. **Gadget** — coordination agent that answers internal questions, updates roadmaps, pings late owners, and writes launch content

**"Every Question Is an API"**
Organizational coordination questions (project status, launch readiness, feature availability, pricing) are treated as structured API calls. Gadget routes, answers, and acts on them — but only works because the org's data (Notion, Linear, Slack) is structured and legible to agents.

**The Autonomous Small Loop**
For low-complexity issues (UX bugs, minor features), a fully automated loop runs end-to-end: triage → backlog match → dedup → rank → code → test → CI/CD → knowledge base update. Humans are kept minimally in the loop via Slack confirmations. This frees PM attention for high-leverage work.

**Three Future PM Archetypes**
1. **The Factory Builder (Technical PM)** — identifies bottlenecks and ships internal tooling that accelerates the entire product org
2. **The Taste Maker** — holds the steering wheel on product quality, design principles, and judgment calls AI cannot make
3. **The GM** — expands ownership beyond product into marketing, sales, growth, and operations; owns full business outcomes

**Embrace Constraints, Not Bottlenecks**
Borrowed from Audi's 2006 Le Mans strategy: when you can't win on the dominant dimension, find a different dimension to be world-class on. Constraints force focus. Bottlenecks, however, should always be attacked and removed.