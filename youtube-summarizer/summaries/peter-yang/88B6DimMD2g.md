# Agentic Engineering, Clearly Explained in 60 Min by an Ex-Meta L8 Engineer | Kun Chen

Video ID: `88B6DimMD2g`

## Summary
Kun Chen, a former Meta L8 engineer turned solo AI builder, walks through his end-to-end workflow for building products almost entirely with AI agents. His core argument is that the bottleneck in agentic development is no longer coding — it's planning and validation — and that engineers must restructure their time and workflows accordingly. He demonstrates custom tooling (Lavish, Treehouse, No Mistakes) he built to eliminate friction and scale parallel agent sessions. The video is most relevant to software engineers, technical founders, and solo builders who want to dramatically increase output using agent coding tools like Claude Code, OpenCode, or Codex.

---

## Key insights

- **The three-phase workflow is standard; what's different is time allocation.** Planning is human-led (with agent assistance), coding is entirely agents, and validation is mostly agents with human judgment on ambiguous cases.
- **Planning quality directly controls how long agents can run autonomously.** A one-line prompt forces frequent human re-engagement; a detailed spec or measurable goal allows agents to run longer without interruption.
- **Parallelism is the primary lever for output.** Kun typically runs 5+ active terminal sessions with 20–30 agents running concurrently, context-switching between them like a manager overseeing a large scope rather than an individual contributor.
- **HTML artifacts over markdown for planning collaboration.** Inspired by the "HTML over Markdown" article, Kun built Lavish to generate rich, interactive HTML planning artifacts. These are easier to scan than walls of text, support inline annotations/feedback, and enable clickable option selection (e.g., "I choose Option C") that sends structured feedback back to the agent.
- **Fresh context windows produce better code reviews.** Asking the same agent that wrote the code to review it produces biased results — it saw every step and assumes correctness. A separate agent with only intent summary + diff catches significantly more edge cases.
- **Never review code line-by-line; use agents for PR review.** At 20–40 PRs/day, line-by-line review makes the human the bottleneck. Instead, Kun's "No Mistakes" tool handles branch creation, rebasing on main, code review, automated testing, documentation linting, risk assessment, and PR creation — all automatically.
- **Sub-agents are primarily for context window management, not just parallelism.** The main reason to spawn sub-agents is to prevent the main session's context window from bloating with exploratory/investigative work that isn't useful long-term. Also useful for running many independent experiments (e.g., 200 benchmark runs × 8 programming languages).
- **Agent testing instructions belong in AGENTS.md and should mirror how you'd test manually.** By default agents write shallow unit tests. Explicit instructions for end-to-end testing (e.g., using Playwright to drive an Electron app) dramatically improve validation quality. The principle: if you do it manually, document it so the agent does it instead.
- **Risk-tiered PR review.** No Mistakes categorizes issues as (1) obvious bugs — auto-fixed silently, or (2) bugs with product implications — escalated to human for judgment. PRs are tagged low/medium/high risk, and Kun calibrates how much attention he gives each accordingly.
- **Work trees require too much cognitive overhead without tooling.** Standard `git worktree add` requires naming, dependency reinstallation, and mental tracking of which tree is which. His tool Treehouse manages a pool of pre-configured worktrees, eliminating all of that overhead with a single `treehouse` command.
- **Team velocity assumptions are broken.** The average engineer ships 10–15 PRs/month; Kun ships 20–40/day. Existing team processes (PR reviews, QA handoffs, etc.) were designed for the former cadence and cannot scale to the latter without fundamental restructuring. Some startups have already stopped doing peer PR reviews.
- **Claude Code's `/insights` slash command** can analyze past sessions and proactively recommend workflow automations, memory file improvements, and new skills — directly addressing the meta-problem of discovering what to automate.
- **Tokens on a subscription should be spent, not hoarded.** The scarcity mindset leads to under-utilization. The goal isn't to burn tokens — it's to force yourself to find workflows that scale output, which requires running more agents in parallel.

---

## Use cases

- **Solo technical founders** building multiple products simultaneously who need to maximize daily output without a team
- **Engineers exploring agentic workflows** who want a structured plan/code/validate framework rather than ad-hoc prompting
- **Anyone doing front-end or UI work** who wants automated end-to-end visual validation instead of manually opening and checking their app
- **Engineers running benchmarks or experiments** (e.g., comparing models, languages, or techniques) who need to parallelize dozens of independent runs
- **Teams rethinking PR review processes** as agent-generated code volumes outpace human review capacity
- **Developers building internal tooling** — Lavish, Treehouse, and No Mistakes are all open-source tools that can be adopted directly
- **People transitioning from big tech to solo building** who want to replicate team-like rigor (code review, CI, documentation) without actual teammates
- **Non-technical or less experienced builders** who want a simple principle: "if you're doing something manually, ask the agent to do it instead"

---

## Patterns & frameworks

**Plan → Code → Validate Loop**
The core workflow structure. Planning is human-intensive and produces a detailed spec or measurable goal. Coding is fully delegated to agents. Validation is agent-run with human escalation only on ambiguous or high-risk items. The loop between code and validate can run autonomously, extending how long agents work without human input.

**Prompt Depth Spectrum**
A gradient from "short prompt → next action prompt → spec → measurable goal." Moving rightward along this spectrum enables agents to run for longer autonomous periods. A measurable goal is the ideal endpoint because it lets agents self-validate against a benchmark.

**Parallelism as a Forcing Function**
Deliberately running multiple concurrent agent sessions forces you to stop being in the loop on any single task. This is both a productivity multiplier and a mindset shift — from individual contributor to manager of parallel workstreams.

**Fresh Context Window Review**
A named practice: never ask the authoring agent to review its own work. Spawn a new agent, give it only the intent summary and the diff, and let it review with no prior bias. Tested empirically by Kun — fresh-context reviews catch materially more issues.

**No Mistakes Pipeline**
A sequential automated validation pipeline triggered after any agent coding session:
1. Create branch + commit (agent names both)
2. Parse session to extract intent
3. Rebase on latest main
4. Code review (high-recall, heavily prompt-engineered)
5. Automated tests with evidence artifacts (screenshots/video)
6. Documentation linting
7. PR creation with risk assessment

Auto-fixes obvious bugs; escalates product-implication bugs to the human.

**Lavish (HTML-over-Markdown Planning)**
A planning collaboration tool where agents generate interactive HTML artifacts instead of markdown text walls. Supports inline annotations, clickable option selection, and two-way agent feedback — keeping planning interactive without constant terminal context-switching. Invoked via `npx lavish-axi` within any agent session.

**Treehouse (Managed Worktree Pool)**
A zero-overhead worktree manager that maintains a pool of pre-configured git worktrees with dependencies pre-installed. Typing `treehouse` drops you into a ready-to-use isolated environment, eliminating naming, dependency setup, and mental tracking overhead.

**Manual-to-Automated Delegation Heuristic**
A simple rule: any time you find yourself doing something manually (opening the app, checking a screen, writing a branch name), document how you'd do it and delegate it to the agent. Applied recursively, this progressively removes the human from routine workflow steps.