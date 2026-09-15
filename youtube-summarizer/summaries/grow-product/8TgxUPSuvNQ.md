# Steal these 4 tools to build an AI-native product team

Video ID: `8TgxUPSuvNQ`

## Summary
Together AI's product team (valued at $8.3B after an $800M raise) walks through their complete AI-native product development workflow, from customer research to agent evaluation. The core argument is that AI should make teams *collectively* more productive, not just individuals producing more output ("slop"). They achieve this through a shared product repository of markdown context files and reusable "skills," supplemented by custom internal tools. The video is most relevant to product managers, engineering leaders, and developer experience teams at software companies looking to build a systematic, team-wide AI workflow rather than a collection of individual shortcuts.

## Key insights
- **Collective vs. individual productivity is the key distinction.** Charles (CEO) explicitly warns against AI making individuals feel productive while flooding teammates' context windows with low-quality output. The goal is outputs that advance the company, not just the individual.
- **The Together Product Repository** is a shared Git repo of markdown and YAML files containing: (1) product context organized by team/mission, (2) strategy documents updated after planning sessions, and (3) reusable "skills" — prompt templates for recurring tasks.
- **Skills have a governance hierarchy:** skills closest to a specific codebase live in that repo; team-wide skills live in the shared repo (pushed to `main` only after proving repeatable); highly niche or experimental skills stay in personal branches or never get merged.
- **The PRD has been redefined.** It is now a 1–2 page document whose only job is to trigger ideation and shared understanding — not a gating document. It defines the customer problem, lists solution options, and includes a sample user journey. The Amazon-style 20-page PRD is replaced by a prototype.
- **A UX prototype skill generates detailed prompts** for tools like Figma Make, V0, or Claude Artifacts. The prototype — not the PRD — is where most critical feedback from engineering and marketing surfaces.
- **The PR Writer skill conducts a turn-by-turn interview** with the PM, challenging assumptions and asking questions drawn from a curated question bank (e.g., "Is this a one-way-door decision?"). It ingests a UX prototype, running PC cluster, or just a plain prompt.
- **Customer research that took half a day now takes 5 minutes.** Pavit's research agent pulls from Pylon (support tickets), Linear (engineering execution), and Notion simultaneously. It surfaced 19 tickets across 14 customers for one feature, identified a partially implemented prior attempt, and provided verbatim customer quotes — all before a PRD was written.
- **Customer Insights is an MCP server** built on top of Gong, Pylon, and Slack by the Developer Experience team. A daily cron job ingests all calls, tickets, and Slack messages from the last 24 hours. It provides a daily digest of 5–10 customer insights and supports freeform chat queries.
- **Orchestrator** is a browser-based internal tool giving Charles (and casual users) a bird's-eye view across all company repos. It lets any employee spin up a sandbox, pick a model and harness, and ask questions or generate PRs — without needing to replicate the local skills and MCP servers of each team. It took a few weeks to a month to build.
- **The context hierarchy principle:** not everyone needs deep context on every team. Orchestrator serves people who want to traverse the "top" of the hierarchy; individual team repos serve those who need to go deep. Forcing a single flat shared context on everyone was explicitly rejected.
- **Agent Evals** is the final step in the product lifecycle. After shipping, the DX team writes task-based tests (e.g., "run a fine-tuning job, spin up the model as a dedicated endpoint, evaluate it, then delete it"). A sandbox runs Claude Code against the task, then evaluates success and generates improvement suggestions. It has driven dozens of documentation fixes.
- **Docs are architected agent-first.** Together injects additional context into doc pages specifically when an agent is reading them, to improve agent task completion.
- **On AI cost and productivity:** Charles estimates velocity gains are real but skeptical of 3x claims. "Discovery, debate, re-evaluation, coordination — a lot of these things don't get magically better with AI." Cost surges were mitigated by switching from Claude to their own open-weight models. Staying focused on collective productivity (rather than individual output volume) naturally caps runaway token spending.
- **The PM/engineer boundary has not fundamentally changed.** PMs still contribute unique, well-validated market insight. Engineers still contribute efficient, maintainable architectural design. What AI changes is the ease with which each side can reach into the other's domain for small and medium tasks.
- **Morning news skill:** Nicolina runs a daily AI-generated competitive intelligence report over morning coffee — it scans model labs and competitors for the last 24 hours of news and formats a readable brief.
- **Open-source harnesses used:** OpenCode (primary), Hermes (emerging). The shared repo is harness-agnostic — standard Claude markdown files work across harnesses.

## Use cases
- **Product managers** who want to cut customer discovery from a full day to under an hour by connecting support tickets, project trackers, and CRM to an AI research agent.
- **Product leaders** (heads of product, CPOs) who need a cross-portfolio, bird's-eye view of all product areas without building deep context in each one — Orchestrator pattern applies directly.
- **Platform/DX teams** looking to build internal tools that make the entire company more productive: customer insights MCP, agent eval harness, orchestrator.
- **Startups transitioning away from long-form PRDs** (e.g., Amazon-style 6- or 20-pagers) who want a leaner, prototype-first product process.
- **Teams experiencing "AI slop" problems** — high individual output but low collective signal — who need a governance model for shared context and skill curation.
- **Companies building developer-facing APIs or SDKs** who need to validate that agents can successfully use their product, not just human users.
- **Product teams onboarding new PMs** who can immediately access the full strategy, customer context, and team-specific skills without lengthy ramp-up.
- **Engineering teams** who want to do their own customer research without waiting for PM synthesis — the customer insights tool gives them direct access.
- **Any team evaluating model choice for specific tasks** — the multi-model, multi-harness approach of pairing the right model (GLM for coding, Kimi for analysis) to the right workflow task.

## Patterns & frameworks

**The Together Product Repository Pattern**
A shared Git repo of markdown/YAML files containing team context (strategy, product groupings, mission docs) and reusable skills. Anyone on the team can pull relevant context into their AI harness session. Ownership follows the work: area owners maintain their context; company-level direction is translated into markdown after planning sessions. Acts as the team's shared memory layer.

**Skills Governance Hierarchy**
A three-tier model for where prompt skills live: (1) in the specific codebase repo if they reference that code; (2) in a personal repo or branch for individual/experimental use; (3) in the shared team repo (main branch) only after proving repeatable and broadly useful. Prevents both skill sprawl and under-sharing.

**The Two-Phase PM Workflow**
Phase 1 (human-in-the-loop): Discovery and alignment — defining the problem, API surface, abstractions, customer validation. Requires judgment and cannot be automated. Phase 2 (automated): Build and ship — code writing, PR generation, design docs, test cluster validation. Triggered via a "goal" command that spawns multiple sub-agents.

**The Short PRD + Prototype Replace the Six-Pager**
The PRD is a 1–2 page trigger document: customer/business problem, solution options, sample user journey. The prototype (generated via a UX prototype skill → Figma Make or similar) replaces the bulk of a traditional long-form PRD. Critical debate happens around the prototype, not the document.

**The PR Writer Interview Skill**
A turn-by-turn conversational skill that interviews the PM on a feature, challenges assumptions using a curated question bank (one-way-door decisions, trade-offs, scope), ingests available artifacts (prototype, running PC, verbatims), and produces a draft one-pager. Solves the blank-page problem while surfacing overlooked considerations.

**The Context Hierarchy Model**
Rather than one flat shared context for the whole company, context is organized hierarchically: deep specialists swim at the bottom (full team repo + skills + MCP servers), casual cross-team collaborators traverse the top (Orchestrator). Context is matched to the depth of need, not forced on everyone.

**The Orchestrator Pattern**
An internal web tool that wraps all company repos, inherits each repo's local skills and MCP servers server-side, and lets any employee spin up a sandbox, choose a model/harness, and ask questions or generate PRs — without local environment setup. Key components: repo aggregation, sandbox/clone mechanism, inherited skills+MCPs, model gateway/router. Estimated build time: a few weeks to one month.

**Agent Eval as the Final QA Gate**
After shipping a feature, write task-based tests representing real user workflows. Run them in a sandboxed Claude Code session with access to the product API/SDK. Evaluate success, review transcripts, and collect improvement suggestions. Iterates continuously (every few hours) to validate that documentation and API design actually work for agents. Drives docs improvements, not just code fixes.

**The Collective Productivity Principle**
The meta-framework underlying everything: use AI to advance the company, not to make individuals feel productive. Centralize what benefits everyone (shared context, shared skills, shared MCPs); free individuals for what's unique to their domain. This principle is the decision filter for what gets built centrally vs. left to individual choice.