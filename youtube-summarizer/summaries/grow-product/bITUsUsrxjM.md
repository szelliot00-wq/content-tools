# How Top PMs Actually Use Claude (5 Tools Explained)

Video ID: `bITUsUsrxjM`

## Summary
This video features Pavle Hearn, described as the top AI PM voice in Europe with 200K+ LinkedIn followers, walking through how advanced product managers should be using Anthropic's suite of Claude tools — specifically Claude Chat, Claude Co-work (now known as Claude Desktop with Projects), Claude Code, and Claude Dispatch. The core argument is that most PMs are drastically underusing Claude by staying in basic chat mode, equivalent to "using Photoshop only to crop photos." The episode maps out a clear if-this-then-that framework for when to use each tool, demonstrates a self-improving knowledge system built on skills and Claude.md files, and argues that the future PM must become a "super individual contributor" comfortable across engineering, strategy, and product domains. It is most relevant to product managers, product leaders, and technical builders who want to move beyond prompt-and-reply workflows into true agentic, file-aware, self-improving systems.

---

## Key insights

- **Chat is the wrong default tool for serious work.** Pavle uses chat only sporadically (e.g., quick grammar checks). The main limitations: you can't continue sessions across devices, can't hand off to coding workflows mid-session, and can't execute multi-step agentic tasks. Starting in Co-work or Code avoids these walls from the beginning.

- **Co-work is for real file manipulation and agentic workflows.** It can reorganize invoices by month, detect and remove duplicates (including image-based receipts), spawn parallel sub-agents, connect to Gmail/Slack/Google Drive via MCP connectors, and generate PowerPoint presentations — all within a virtual machine environment tied to your actual file system.

- **Claude Code is not optional for PMs.** Even non-technical PMs will increasingly work alongside engineers using Code. Co-work lacks the file explorer hierarchy view needed for large codebases, cannot run system commands on your local machine, and cannot support pre-defined sub-agent personas or hooks — all of which Code supports.

- **The same GitHub repo works across all surfaces.** Co-work, Claude Code (VS Code CLI), Code Web Sessions, and Dispatch can all point to the same GitHub repository. This means a task started on desktop can be continued on mobile via Dispatch or Web Sessions without losing context.

- **Skills = reusable agentic procedures.** A "skill" is a Markdown file with a name, description, "when to use" section, and step-by-step instructions. Agents read the description to decide whether to load the full skill — called "progressive disclosure." You can have hundreds of skills; the agent only loads relevant ones, preserving context window space.

- **Pavle's PM Skills GitHub repo hit 10,000 stars** (started at 1,300 in 72 hours). It includes plugins for product discovery, data analytics, execution, go-to-market, and market research. Key example: the `discover` workflow runs a full product discovery sequence — customer needs analysis → opportunity mapping → ideation → assumption mapping (value, usability, feasibility, viability, ethical) → experiment planning — in a single command.

- **Claude can now generate McKinsey-level PowerPoint outputs in 1–2 minutes.** A live demo showed a full product strategy deck for Amazon with a north star metric, guardrail metrics, market segments, growth strategy by segment, unit economics, and diverse icon-based layouts — generated using Pavle's product strategy skill combined with Anthropic's built-in PPTX skill.

- **The Claude.md file should be lean, not a dumping ground.** A common mistake is stuffing all instructions into claude.md, which bloats the context window on every prompt. Instead, claude.md should only explain the project purpose and how to find domain-specific knowledge files. Detailed rules, hypotheses, workflows, and examples live in separate indexed files.

- **The self-improving knowledge system works via a simple prompt in claude.md:** Before starting any task, the agent reviews existing rules and hypotheses for that domain, applies confirmed rules by default, and after each session updates or promotes/demotes hypotheses based on new data. This requires zero manual curation once set up.

- **Pavle built a second brain for his agents (not himself), starting February 2026.** He feeds it social media posts, infographics, and article drafts. The system extracts hooks, sound bites, structural patterns, and engagement rules across platforms (X, LinkedIn, Substack). It stores confirmed rules, active hypotheses, and rejected hypotheses — none of which Pavle writes himself; Claude generates them from the data.

- **Anthropic team attribution infographic was built entirely via natural language in Claude Code.** The process: identify free Anthropic accounts → scrape their recent posts/reposts → find accounts using "we" or "my team just released" language → verify via comment analysis → map each feature to the person who first announced it → fetch profile pictures from X API → iterate on HTML visualization. Pavle wrote zero code.

- **Agent Browser (from Vercel) is recommended over Chrome MCP.** Chrome MCP takes a screenshot every ~0.5–1 second, consuming $100+/hour with Opus on complex tasks. Agent Browser runs headlessly, describes page structure (buttons with IDs, layout, text) without screenshots, waits for SPA rendering, and executes JavaScript — far more token-efficient. Use case: any external system without an API (legacy CRMs, SAP, LinkedIn scraping).

- **Dispatch is the mobile-first orchestration layer.** It lets you start multiple background tasks from a single chat interface (on phone or desktop), each delegated to sub-agents. Your laptop must be online for Dispatch to work. Pavle estimates he uses Dispatch + Web Sessions ~70% of the time, chat ~5%, and Claude Code the rest.

- **Code Web Sessions are the most secure option.** Hosted on Anthropic's servers, synced to GitHub, accessible from any device including mobile. Pavle considers this the recommended approach for all personal operating systems and knowledge bases — laptop can be fully offline and agents still run.

- **N8N is still necessary for production-grade automation.** Claude Code/Co-work workflows are text files that agents interpret — there are no hard-coded guards. For production systems (e.g., customer ticket replies, data access controls), you need actual code with conditions, retry logic, and guardrails. The recommended architecture: most logic in code, LLM/agent calls only where necessary, with N8N for orchestrating hard rules.

- **Anthropic's shipping velocity is itself a signal.** Pavle tracked 74 releases in 52 weeks (host said 52 days), and Anthropic grew from $1B to $30B in 16 months. The interpretation: companies should not use AI to replace steps in existing processes, but to redesign entire processes around what AI makes possible.

- **The future PM role is a "super individual contributor"** — not PM-only, but spanning prototyping, testing, release notes, interface design, strategy, revenue modeling, and code. Roles are not merging but converging. PMs who only interview customers and write backlog items will not thrive.

---

## Use cases

- **File system organization:** Automatically sort invoices, receipts, or contracts by month/vendor, detect duplicates by content hash (not filename), handle mixed PDF and image formats.
- **Email management:** Draft replies to unanswered Gmail messages without sending; approve or edit before sending; system learns from approved replies to improve future drafts.
- **Slack management:** Draft channel replies via MCP connector; system adds a "sent by Claude" footer if auto-sent, so Pavle prefers manual approval.
- **Presentation creation:** Generate polished, icon-rich, multi-layout strategy decks (PowerPoint/PPTX) from a product strategy skill in minutes, suitable for executive or board meetings.
- **Product discovery:** Run a full discovery workflow (needs → opportunities → ideation → assumptions → experiments) with a single slash command using the PM Skills plugin.
- **Content creation system:** Build a self-learning system that analyzes social media posts, extracts hooks and structural patterns, stores rules and hypotheses by platform, and uses them to draft new content in the creator's voice.
- **Competitive/social research:** Scrape and analyze top posts from specific accounts (including engagement metrics), identify what worked and why, without writing code.
- **Legacy system access:** Use Agent Browser to interact with SAP, old CRMs, or any web UI that lacks an API — without the token cost of screenshot-based tools.
- **Codebase work alongside engineers:** PMs should use Claude Code to review PRs, understand architecture, ask questions about how things work — without writing code themselves.
- **Mobile-first async work:** Dispatch tasks while away from desk (shopping, parenting, commuting), check results later, give feedback, continue — integrating work fluidly into daily life.
- **Candidate screening:** Feed Claude a corpus of successful résumés/offers, let it extract rules, then evaluate new candidates against those rules automatically.
- **Release notes and QA:** Define sub-agent personas in Claude Code (e.g., a "tester" agent, a "release notes" agent) that run automatically on new code changes.

---

## Patterns & frameworks

**1. The Tool Selection Matrix (If-This-Then-That)**
- *Chat:* Simple one-off questions, grammar checks, email drafts with no file context. No continuity, no file access, no coding.
- *Co-work:* Real file manipulation, multi-step agentic workflows, parallel sub-agents, MCP connector integrations, presentation generation. Use when you need to work with actual files but don't need codebase-level hierarchy.
- *Claude Code (CLI/VS Code):* Codebase-aware work, pre-defined sub-agent personas, hooks, system command execution on local machine, complex folder hierarchies. Required when working with engineers or large file systems.
- *Dispatch:* Mobile-first multi-task orchestration. Start tasks from phone, delegate to background agents, receive results asynchronously. Laptop must be online.
- *Code Web Sessions:* Cloud-hosted Claude Code, synced to GitHub. Works when laptop is offline. Most secure option for personal operating systems.

**2. Progressive Disclosure for Skills**
Skills have a two-layer structure: a lightweight header (name, description, "when to use") that agents always read, and detailed instructions that are only loaded when the description matches the current task. This allows hundreds of skills to coexist without bloating the context window. Analogous to lazy loading in software.

**3. The Self-Improving Knowledge System**
A repeatable pattern for any PM domain (not just content):
1. Add a short prompt to claude.md instructing the agent to review existing rules/hypotheses before each task.
2. Maintain an index.md file that routes the agent to domain-specific knowledge files (e.g., pricing, testing, marketing).
3. After each session, the agent updates confirmed rules, promotes/demotes hypotheses, and appends new examples.
4. Over time, the system accumulates institutional knowledge that improves output quality automatically — without the PM writing rules manually.

**4. Lean Claude.md + Domain Knowledge Files Architecture**
- claude.md = project purpose + pointer to how knowledge is organized + self-improvement prompt only.
- Separate .md files per domain contain actual rules, hypotheses, templates, workflows, and examples.
- An index.md acts as a router so the agent knows where to look without scanning the entire repo.
- Prevents context window bloat; keeps every session lean and fast.

**5. The Automation Spectrum (Personal → Internal → Production)**
- *Personal automation (Claude Code/Co-work):* Analyzing tweets, drafting emails, generating infographics. Acceptable for agents to interpret text instructions loosely.
- *Internal process automation (Claude Code + hooks + sub-agents):* Code review, release notes, front-end design within a codebase. More structured, but still agent-driven.
- *Production-grade automation (N8N + Anthropic API + hard code):* Customer-facing systems, data access controls, retry logic, compliance guardrails. Must use actual code, not just prompts. LLM calls exist inside a coded workflow, not as the workflow itself. The principle: "Everything that doesn't have to be autonomous shouldn't be autonomous."

**6. The Three-Version Agent Architecture (referenced from prior N8N episode)**
- Version 1: Mostly code, one LLM call. Least autonomous, most predictable, most cost-effective.
- Version 2: Hybrid — some coded logic, some agentic steps.
- Version 3: Fully autonomous agent. In production, always default to Version 1 or 2; reserve Version 3 for contexts where autonomy is genuinely required and risk is acceptable.

**7. Second Brain for Agents (not for humans)**
Inspired by Karpathy's personal knowledge base concept but inverted: instead of building a second brain for the human to browse, build a structured knowledge base that agents read and update. The human acts as curator (feeding in raw data), while the agent acts as librarian (organizing, extracting patterns, confirming/rejecting hypotheses). Scales indefinitely without the human needing to write rules.