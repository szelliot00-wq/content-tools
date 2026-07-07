# How to build a product team OS with Emma Burrows (ex Stripe UK CTO)

Video ID: `kWJgs1kCcOQ`

## Summary
Emma Burrows, former Stripe UK CTO and co-founder/CEO of Resonant, presents a framework for building an AI-powered "product brain" that automates the operational and administrative burden of product management. Her core argument is that while software engineering has already undergone a transformation from using AI as a copilot to orchestrating autonomous agents, product management has not yet made that leap — and the tooling gap is causing PMs to get stuck in day-to-day noise instead of strategic thinking. The talk demonstrates a working system built on a GitHub-backed wiki that ingests data from tools like Granola, Linear, and GitHub, then runs configurable workflows triggered via Slack to handle everything from ticket scoping to writing and shipping code. It is most relevant to PMs, engineering leaders, and founders at startups or fast-moving teams who want to reduce PM toil and move toward AI-orchestrated product development.

## Key insights
- **The engineering-to-PM AI gap:** Engineering has moved from AI-assisted line-by-line coding (Copilot) all the way to autonomous agent orchestration (Cursor, Claude Code, OpenClaude). Product management is still largely in the "using ChatGPT to draft things" phase — nobody has built the equivalent orchestration layer for PM work.
- **The product brain is a self-maintaining wiki:** Rather than a static document, the product brain continuously ingests inputs (meeting notes from Granola, tickets from Linear, PRs from GitHub) and synthesizes them into an auto-updating wiki stored in a GitHub repo. If it isn't self-maintaining, it goes stale and becomes useless.
- **GitHub repo as the backbone:** The product brain is stored as a GitHub repo specifically so team members can audit, edit, and inject manual inputs. This also makes it traversable by engineering agents, allowing it to be linked into the main codebase via symlinks.
- **Slack as the human-agent interface:** Workflows are triggered via Slack, allowing anyone (PMs, salespeople, engineers) to submit requests in natural language. The agent responds with strategic context, scoping recommendations, and in some cases actually writes and submits the PR.
- **End-to-end ticket automation demonstrated live:** Emma showed a live example where a customer request (a UX confusion issue) was submitted as a Linear ticket, the agent assessed strategic fit, concluded it was a small well-scoped fix, wrote a full spec, and opened a PR — all without PM intervention.
- **Agent judgment improves over time via session memory:** When the agent makes a wrong call (e.g., recommending shipping a ticket separately when it should be folded into a larger PRD), the PM's correction is stored back into the wiki's principles section. This creates a feedback loop that improves agent judgment over time.
- **Librarian agent for context rot:** A lower-frequency "librarian" agent periodically runs over the product brain to keep the wiki fresh and well-structured, separate from the higher-frequency input-processing agents.
- **Trust boundaries and workflow customization:** Organizations should configure automations based on their culture and risk tolerance. Most forward-looking companies are not yet pushing all the way to auto-shipping code to production, but are using the system for things like customer insight reports, pre-meeting summaries, and enabling salespeople to spin up prototypes independently.
- **Sales-led vs. product-led growth shapes the system:** For sales-led orgs, the primary input is sales team feedback. For product-led orgs, analytics data (e.g., PostHog) is more central. The product brain should be configured to reflect how the specific organization actually generates signal.
- **PII and anonymization:** Customer data and company names do end up in the system (e.g., "Company Y requested Feature Z"). Anonymization is possible but reduces usefulness. The bigger concern from clients has been about customer insights being stored in a new location (GitHub) rather than PII in tickets specifically.
- **Avoiding over-automation pitfalls:** The agent is prompted with the organization's product taste and judgment specifically to prevent it from becoming a route for salespeople to ship whatever their customers want without strategic filtering. The goal is quick wins for clear small tasks, not uncritical feature factories.
- **Token budget awareness:** The cadence of ingestion jobs should match how frequently the organization actually updates its tools — running every hour against a rarely-updated Linear board wastes tokens without adding value.

## Use cases
- **PM teams drowning in backlog triage:** Automating the initial assessment of whether an incoming ticket is well-scoped, a duplicate, or needs to be folded into a larger initiative.
- **Sales-to-engineering communication:** Allowing salespeople to submit feature requests or questions via Slack and get immediate, strategically-informed responses without pulling in a PM or engineer.
- **Weekly planning and insight reports:** Auto-generating customer insight summaries or engineering progress updates ahead of planning meetings.
- **Small bug/UX fixes:** Shipping clearly-scoped, low-risk improvements end-to-end (spec → PR) without PM involvement, freeing PM time for strategic work.
- **Cross-team alignment:** Giving PMs a way to query what adjacent product teams are working on and surface potential dependencies proactively.
- **Design review gating:** Configuring the agent to ping a specific designer (or design system rules) when a change has substantial UX impact, before shipping.
- **Strategic document critique and roadmap shaping:** Using the product brain in a co-pilot mode (e.g., with Claude) to critique PRDs, challenge roadmap assumptions, or synthesize strategy documents.
- **Large enterprises aligning strategy:** For bigger orgs less ready for full automation, the product brain's primary value is as a single source of truth for strategic context and decision alignment rather than automation.

## Patterns & frameworks

**The Product Brain**
A self-maintaining GitHub-backed wiki that continuously ingests data from product tooling (meeting notes, tickets, analytics, repos), synthesizes it into structured knowledge (customer insights, product principles, feature context), and serves as the shared context layer for all downstream agent workflows. Analogous to how CLAUDE.md and memory systems work for coding agents, but at the team/organization level.

**Using AI → Orchestrating Agents (the 2×2 progression)**
A maturity model borrowed from how engineering evolved: left axis is passive AI use (drafting, editing), right axis is active agent orchestration (autonomous multi-step workflows). The argument is PMs are stuck on the left and need tooling and process to move right, the same way engineers moved from Copilot to Cursor to Claude Code.

**The Software/Product Factory Loop**
An extension of "loop engineering" (software factories that self-ship code given good QA): adds an outer loop where customer inputs are processed by the product brain and fed into the software factory, aiming for a system that can close the loop from customer signal → ideation → shipped code → analytics → back to customer signal.

**Layered Trust / Workflow Gradations**
Rather than flipping to full automation, teams should configure workflows that match their current trust level: (1) insight reports and summaries (low risk, high acceptance), (2) ticket scoping and PRD drafting (medium), (3) prototype generation for sales (medium), (4) full code-to-production shipping (high, only for the most advanced teams). Each level builds confidence for the next.

**Session → Principles Feedback Loop**
When a PM overrides an agent recommendation, that session (the Slack exchange, the agent's recommendation, the human correction) is stored in the product brain and distilled into the wiki's principles section. Over time this tunes the agent's judgment to match the PM's product taste without requiring manual prompt engineering.

**Librarian Agent Pattern**
A low-frequency meta-agent that runs over the knowledge base periodically (not on every ingestion cycle) with the sole job of reorganizing, pruning stale content, and ensuring the wiki structure matches how the team actually uses it — distinct from the high-frequency input-processing agents.