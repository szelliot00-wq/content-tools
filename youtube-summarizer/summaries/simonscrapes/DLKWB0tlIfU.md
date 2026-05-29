# Anthropic Doesn’t Want You To Know This About Claude Code

Video ID: `DLKWB0tlIfU`

## Summary
The video argues that Claude Code (and Anthropic's tooling broadly) has drifted toward serving enterprise/developer audiences despite marketing itself as accessible to non-technical business owners. The creator walks through specific examples of this complexity creep, explains the business incentive behind it (80% of Anthropic's revenue comes from enterprise/developers), and presents a four-step framework for building a portable AI operating system that isn't locked into any single provider. It is most relevant to small business owners, solopreneurs, and non-technical operators who use or are considering Claude Code for business automation.

---

## Key insights
- **Marketing vs. reality gap**: Features like "managed agents" are marketed as "no infrastructure needed," but onboarding requires configuring cloud containers, networking rules (restricted vs. unrestricted), credential vaults, and MCP server connections — clearly developer-oriented tasks.
- **Second example — hosted routines**: Creating a remote scheduled routine in the Claude app requires connecting a GitHub repository, understanding pull requests, merges, and pushes — language and concepts unfamiliar to non-developers.
- **Revenue explains the product direction**: Anthropic crossed $30B in annualized revenue as of April 2026, with ~80% coming from enterprise and developers. They quadrupled business adoption over the past year while OpenAI grew only 0.3% in the same period.
- **The 80/20 logic**: When 80% of revenue comes from one customer segment, rational product decisions favor that segment — meaning non-technical small business users are structurally deprioritized.
- **The core risk is lock-in**: Features that only run inside Anthropic's infrastructure (managed agents, hosted environments) create dependency. If you need to switch providers, you lose your setup.
- **Claude Code's memory is weak out of the box**: Auto-memory and CLAUDE.md injection are unreliable; short-term context injection and long-term semantic recall are particularly poor. The creator built a custom memory layer combining patterns from Hermes and Memarch.
- **The real architecture is simple**: An "agentic OS" is fundamentally markdown files in folders with rules about which files to load in which context — not complex infrastructure.
- **Portability over convenience**: The tradeoff is upfront build time for long-term flexibility. Building your own layer means you can swap the underlying model/provider without rebuilding your entire workflow.
- **CLAUDE.md lock-in example**: Memory structures tied to CLAUDE.md would need to be converted to agents.md or equivalent if switching to another provider — a concrete portability risk.

---

## Use cases
- **Small business owners** using Claude Code for operations who feel overwhelmed by the technical onboarding and want a practical strategy for using AI tools without deep technical knowledge.
- **Solopreneurs and content creators** who need repeatable, scheduled workflows (e.g., weekly reviews, content generation) that run without their computer being on.
- **Consultants or agency operators** managing multiple clients who need clean context separation between clients, team members, and projects.
- **Non-technical operators** who have been burned by platform lock-in before and want to future-proof their AI tooling investment.
- **Anyone evaluating Claude Code vs. alternatives** who wants a framework for deciding what to build themselves vs. what to rely on providers to deliver.
- **Teams** that need shared knowledge bases with isolated personal/project contexts for individual members.

---

## Patterns & frameworks

**Four-step portability framework**
A process for building an AI operating system that isn't dependent on any single provider:
1. *List your actual requirements* — Write down everything you need the system to do (the creator lists 9 goals: context injection, client/project knowledge, memory/recall, repeatable processes, scheduled multi-step workflows, project-scoped planning, team/client separation, predictable output location, and always-on access).
2. *Strike off what providers will build anyway* — Identify which needs have a ~95% chance of being natively solved by major platforms within months (e.g., remote task dispatch, aggregated outputs). Don't build these yourself.
3. *Architect what they won't build for you* — Focus on bespoke needs: client/team context separation, custom memory, business-specific repeatable workflows, and domain separation between team members.
4. *Stack layers where the model is weak* — Identify gaps (e.g., long-term memory recall) and build custom layers on top, designed to be removable once a provider ships a native solution.

**Folder-based context management (Agentic OS)**
The core architecture is a folder structure of markdown files representing different context layers (voice/brand profile, ICP, client-specific plans, global processes) with a rule set governing which files are injected based on the active working context (e.g., client A's folder loads only client A's brand, projects, and processes).

**Avoid Anthropic's box rule**
A single guiding constraint: don't adopt features that only function within Anthropic's hosted infrastructure. Prefer portable implementations even if they require more upfront effort.

**Custom memory stack (Hermes + Memarch hybrid)**
Rather than relying on CLAUDE.md or auto-memory, the creator built a layered memory system combining storage patterns from the Hermes agent framework and recall patterns from Memarch, enabling smarter context injection at session start and semantic (meaning-based) long-term recall.