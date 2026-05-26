# I got an inside look at how OpenAI PMs ship code

Video ID: `8suwvrF0Lv0`

## Summary
Ryan Leopo, a team lead on OpenAI's frontier team, breaks down how his team built a million-line codebase where zero lines were written by humans — using Codex as the primary code author. The central argument is that code is no longer the scarce resource it once was, which fundamentally changes how product teams should be structured, how work should be scheduled, and how PMs, designers, and engineers collaborate. The video is most relevant to engineering leaders, PMs, and designers at software companies who want to understand how to restructure their team workflows around AI coding agents in the next 1–2 years.

## Key insights
- **"Code is a liability"**: Code has historically been expensive to produce (synchronous human throughput), validate, and deploy — so organizations built entire processes around protecting it. With models like GPT-5/Codex, code generation is now trivially cheap and arbitrarily parallelizable, which invalidates most of those legacy organizational structures.
- **Zero human-written lines**: Ryan's team built a ~1 million line codebase (including ~250,000 lines of markdown for agent prompts) without a single line written by a human engineer. This was an explicit, enforced constraint — engineers were "in the backseat of the Uber."
- **The new EPD model**: Engineers, PMs, and designers all contribute directly to the same codebase. PMs write PRDs in Markdown that compile to shipped PRs. Designers contribute UI code. Engineers encode leverage into the harness rather than writing features. This creates higher empathy and fewer lossy handoffs.
- **The "harness" is the key unlock**: The harness is the collection of mechanisms in the repository that give Codex the right context at every phase of implementation — agents.md, a docs tree, tests that encode taste, review agents, and observability tooling. It is not a product; it lives in the repo itself.
- **PRD → shipped PR in one week**: A real example: a PM wrote a PRD for a "skills library" feature (durable user knowledge injection into the agent) at the start of a week. By demo day at the end of the week, with zero synchronous engineer involvement, the feature was demoed and shipped to customers the following week.
- **Painted door technique for designers**: When a designer wanted to build a scheduling/cron UI feature, the team found the backend work created spaghetti. Solution: separate the UI layer (designer's domain) from the backend with a "painted door" — fully implemented UI with a no-op backend — plus product instrumentation to gather real usage signal before committing to backend work.
- **Validation must be cheap**: The harness includes a local observability stack (like giving Codex its own Datadog), UI driven via a browser shell with Chrome DevTools, and end-to-end integration tests. Codex can close the loop — click buttons, observe side effects, attest the feature works — without human shoulder-surfing.
- **350 million tokens on a single PR**: A refactor that would have taken 3 weeks took 3–4 days over a single 60-hour Codex CLI session. Ryan provided only 2 additional prompts after the first. He physically buckled his laptop into his car to keep the session alive during his commute.
- **GPT-5.2 was the inflection point**: When GPT-5.2 launched (while Ryan was on winter break), the team immediately saw 1–2 more PRs per engineer per day with zero additional investment. This triggered a shift from sequential to parallel agent execution.
- **Symphony orchestrator**: An agent orchestrator Ryan's team built and open-sourced (blogged about) that takes Linear tickets, advances them through states, feeds ticket text to Codex, and expects a PR back. It is deliberately simple — no magic — yet delivered a 10x increase in PRs per engineer per week on top of the model uplift.
- **Billion tokens/day benchmark**: Ryan's view is that if a team isn't running ~1 billion tokens/day, they are leaving leverage on the table. At ~$2–3K per engineer per day, the ROI argument is: more tokens = smarter outputs = more product shipped. Token spend is a proxy for agent utilization.
- **The new engineering job = staff engineer mindset**: The role shifts from writing code to empowering agents to write code. This mirrors the staff engineer role: not producing all the code, but enabling the team (now including AI agents) to produce it. Ryan's team runs an internal experiment where teams are told they've been assigned "5 interns named Codex" and success is judged on how effectively they use them.
- **Single-agent > multi-agent**: Counterintuitively, Ryan argues the optimal number of agents in a multi-agent system is one. A single agent with full context over design, backend, and frontend produces higher quality output than multiple agents with lossy handoffs between them.
- **Context window is the scarce resource**: Agents.md is forcibly injected into every Codex session but consumes context budget. The solution is to put a map in agents.md pointing to a larger docs tree, letting the model decide what to pull in rather than front-loading everything.
- **Tests as prompt injection**: Failing tests are used to inject context into Codex at the moment it needs it — for example, a test that fails if any user-facing string uses straight quotes instead of curly quotes (the designer's typography requirement). This aligns agent behavior with team taste without burning context upfront.
- **Docs are first-class code artifacts**: Every design doc, Google Doc, implementation plan (exec plans), and LLM.txt reference manual (from Stripe, OpenAI, UV, internal design system) lives in the repo. Cross-linked markdown files have build checks that fail if links break when a doc is updated. Codex maintains this documentation tree automatically.

## Use cases
- **Engineering leaders** wanting to build a business case for high AI token spend (~$2–3K/engineer/day)
- **PMs** who want to write PRDs in Markdown and have them compile directly to shipped features without synchronous engineering involvement
- **Designers** who want to contribute UI code safely within a structured package layering system, using "painted door" patterns to test interaction concepts before backend work is committed
- **Tech leads** in brownfield codebases who need a concrete Monday morning roadmap for incrementally building a "harness" around an existing codebase
- **Teams doing large refactors** that would normally take weeks and require deep synchronous engineering effort
- **Product teams prototyping new product surfaces** who need high-signal usage data before investing in backend infrastructure
- **Engineering leaders managing team growth** who want to scale output without proportional headcount growth
- **Any team** experiencing lossy handoffs between PM, design, and engineering — where feedback channels are slow and coordination is expensive
- **Teams evaluating AI coding stacks** (OpenAI vs. Anthropic) for full agentic software engineering workflows

## Patterns & frameworks

**The Harness**
A repository-native system for giving a coding agent the right context at every phase of the SDLC. Three phases: (1) pre-implementation — agents.md operating model + docs tree; (2) in-implementation — code patterns as prompts, taste-encoding tests/lints, local observability stack, UI automation via browser shell; (3) post-implementation — persona-oriented review agents (frontend architect, reliability engineer, etc.) that leave structured PR feedback as a CI matrix job.

**Agents.md Operating Model**
A file at the repo root that is forcibly injected into every Codex session. Contains a 3–5 step operating loop (ground in docs → implement → validate → review) and a map of where resources live in the repo. Deliberately kept lean to conserve context budget; the model decides what to pull in from the larger docs tree.

**Exec Plan**
A skill (available on the OpenAI cookbook) given to Codex to write phased implementation plans with milestones and deliverables before starting a task. Every exec plan ever produced is kept in the repo as a durable log of implementation decisions.

**Painted Door**
A product experimentation pattern where the UI for a feature is fully implemented (by the designer, using the agent) with a no-op backend stub. Product instrumentation is added to collect real usage signal. This gives engineering high-confidence signal on whether to prioritize backend work before any backend investment is made.

**PRD as Code Input → App as Compiled Output**
PMs write PRDs in Markdown. These are given to Codex as the task input. The output is a deployed application change. The "compilation" step is Codex navigating the docs tree, writing code consistent with the harness, passing tests and review agents, and producing a PR. No synchronous engineer involvement required for the happy path.

**Package Layering / Hard Separation**
The codebase is structured into strictly separated packages (database, config, business logic, UI) enforced by code-level package boundaries. Business logic always exports high-fidelity fakes for testing. This prevents the "ball of mud" failure mode and makes it safe for non-engineers to contribute within defined layers (e.g., designers work in the UI layer only, PMs in business logic and UI, engineers across all layers).

**Reviewer Agents as CI Matrix**
Persona-oriented markdown documents (frontend-architect.md, reliability-engineer.md, etc.) are used as system prompts for automated review agents that run as a matrix CI job on every PR. Each persona reviews the diff against its guardrails and leaves structured feedback directly on the PR, replacing synchronous code review for the majority of issues.

**Token Billionaire Mindset**
A forcing function / north star: aim for 1 billion tokens/day per engineer. This pressures teams to find ways to run agents more autonomously, in parallel, and over longer time horizons — rather than using AI as synchronous autocomplete. Unused GPU capacity = unused engineering capacity.

**5 Interns Named Codex**
An internal management experiment: teams are told they have been assigned 5 interns named Codex, and part of their performance evaluation is how effectively they utilize this capacity. Reframes agent utilization as a management and systems-thinking challenge rather than a tooling challenge.

**Symphony Orchestrator**
An agent orchestrator (open-sourced by Ryan's team) that reads Linear tickets, advances them through workflow states, passes ticket text to Codex, and expects a PR as output. Deliberately simple. Enabled a 10x increase in PRs/engineer/week on top of the model capability uplift from GPT-5.2.