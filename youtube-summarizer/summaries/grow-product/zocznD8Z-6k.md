# How to build a Company Operating System with Hermes and OpenClaw

Video ID: `zocznD8Z-6k`

## Summary
This episode features Mikael Shaglov, CPO at OX Classifieds (formerly CPO at Azerbaijan's largest e-commerce marketplace and GPM at Bolt), who demonstrates a fully operational AI-powered company operating system built on OpenClaw and Hermes agentic scaffolding. The central argument is that CPOs should own and architect the agentic infrastructure of their organizations — not delegate it to engineering or AI ops — because doing so compresses PM overhead by ~50% and lets teams focus entirely on customer discovery. The video is a practical, screen-share-heavy walkthrough of the architecture, memory layers, tooling, use cases, and hiring implications of running an AI-native product org. It is most relevant to CPOs, VPs of Product, and senior PMs who want to move from using AI as a productivity assistant to using it as an autonomous organizational collaborator.

## Key insights

- **Knowledge leakage is the core problem AI solves for orgs.** When a domain expert leaves, they take irreplaceable context with them. A centralized, persistent AI knowledge graph eliminates that single point of failure by continuously capturing and indexing organizational knowledge.

- **"Product context coverage" is a real KPI.** Mikael tracks a percentage metric — currently at 54% — that represents how much of the company's industry, business model, customer segments, and growth drivers the AI understands. At 54%, it can operate as a capable junior PM. At 70–90%, he expects it to assist with strategy-level decisions.

- **Three-layer memory architecture is the key to robustness:**
  1. **Knowledge graph** — a visual web of interconnected nodes (contacts, projects, customers, metrics, personal reflections) built in Fable with a two-line prompt.
  2. **Vector database** — every piece of incoming knowledge is immediately vectorized, enabling fuzzy/semantic retrieval for the ~75% of queries that aren't exact keyword matches.
  3. **Raw conversation + meeting transcripts** — stored as unprocessed MD files daily. Critically, Mikael tested summarization vs. raw storage and found summarization caused 20–25% worse recall, because it imposes templates that lose granular nuance.

- **Hermes auto-generates skills and improved recall by 31%.** Unlike OpenClaw alone, Hermes detects recurring task patterns and automatically creates reusable skill modules. Mikael tested across 5 core topic areas (market, business model, product/growth levers, funnel, etc.) with 10 questions each, and found a 31% accuracy improvement when skills were present vs. absent.

- **The SOUL.md file can run 800 lines; CLAUDE.md stays under 100.** CLAUDE.md has the highest priority context in OpenClaw; SOUL.md is second priority and acts as a massive library of imperatives. Mikael includes rules for: no fabrications, think before acting, facts over guesswork, and explicitly banning "fake helpful" behavior (e.g., the agent explaining how to open Google Calendar instead of admitting it can't book the meeting).

- **50% of a typical PM's time was spent on process overhead.** Mikael estimates this based on his career history. Status reports, stakeholder updates, demos, and calendar management are all now handled by the agent, freeing PMs to focus exclusively on discovery.

- **Agents are building most of OX's features.** The system is hooked into Google Workspace, Granola, Confluence, Jira, Slack, LinkedIn Recruiter, their CRM (Greenhouse), and Figma. Any stakeholder can interact with the agent directly in Slack to validate feature requests before ever reaching a PM.

- **The agent acts as a feature request gatekeeper.** Stakeholders submit requests to the agent instead of harassing PMs. The agent asks clarifying questions, evaluates against priorities and ROI, and either politely rejects the request, escalates to the correct PM (with org structure mapped internally), or adds it to the backlog.

- **The board skill is a real use case.** Granola transcribes board meetings; Hermes auto-generates a "board skill" that models each director's mental model and investment principles. Before any strategy defense, Mikael runs his pitch deck through this skill to get pre-emptive brutal feedback.

- **Access control is role-based.** The board skill is only available to Mikael and the executive committee. Each user's access rights determine which tools and context they can retrieve. Personal one-on-ones are excluded from transcription by default unless the employee opts in.

- **Intelligent model routing optimizes token spend.** An agentic orchestrator decides which model to use per request: high-sensitivity or high-blast-radius tasks get Claude Opus (Fable); status reports and low-complexity execution tasks get Claude Sonnet 4.8. Engineers separately use a blend including GPT-4.5/o3 for epic decomposition and locally deployed open-source models for simple tasks.

- **The design system is autonomously maintained.** The entire OX design system was generated from prompts and is continuously updated by the agent when engineers hardcode components or gaps are detected in product/engineering conversations. A designer reviews changes rather than executes them.

- **Recruiting is ~70–75% automated.** The agent handles LinkedIn Recruiter outreach, CRM (Greenhouse) updates, interview transcript analysis, third-party candidate evaluation, rejection letter drafting with specific improvement feedback derived from Granola transcripts, and funnel gap analysis.

- **PM-to-engineer ratio will blur, not just shrink.** Mikael predicts the distinction between PM, engineer, and designer roles will erode. All three will be "orchestrators" accountable for quality and token budget in their respective domains.

- **AI-native PM hiring test.** Mikael screens PM candidates with one question: "Which parts of your daily work have you automated using AI?" Responses range from "I use ChatGPT via the web interface" (low maturity) to candidates who have built full agentic systems that manage their professional life (high maturity). The latter get significantly more points.

- **CPOs must own the agentic scaffolding, not delegate it.** Delegating to engineering or AI ops slows the feedback-to-deployment loop and removes skin in the game. Mikael makes changes directly in Claude Code or the Claude app on his phone in real time based on daily feedback.

## Use cases

- **Status reporting:** Any stakeholder can query the agent in Slack for project status (e.g., "What's the status of the auto spare parts catalog integration?") and receive a clean, factual response sourced from Jira, Confluence, and Granola transcripts.
- **Feature request triage:** Stakeholders submit feature ideas to the agent instead of PMs. The agent qualifies, challenges, rejects, or escalates requests with full rationale.
- **Backlog management:** The agent reads each team's spreadsheet-based backlogs, evaluates ROI, and can write entries directly based on validated requests.
- **Board deck preparation:** CPOs run strategy decks through a "board skill" that simulates board member reactions before the actual meeting.
- **Calendar and email management:** The agent surfaces a daily digest of urgent emails and Slack messages, proposes calendar slots for multi-timezone exec meetings, and books them directly.
- **Recruiting pipeline management:** End-to-end: sourcing via LinkedIn Recruiter, CRM updates, interview assessment, tailored rejection emails with improvement feedback.
- **Organizational health monitoring:** The knowledge graph visualizes siloed teams, weak stakeholder connections, and gaps in customer discovery — surfacing management insights without a single analyst.
- **Evaluating team performance:** Product context coverage per team and per PM serves as a leading indicator of customer discovery quality.
- **Design system maintenance:** Automatically detects missing components from engineering/product conversations and adds them to Figma with designer review.
- **Recall and eval benchmarking:** CPOs can run their own recall tests across core topic areas to measure agent accuracy with vs. without skills, and track improvement over time.

## Patterns & frameworks

**Product Context Coverage Metric**
A single percentage KPI representing how much of the company's industry, business model, customers, and growth drivers the AI has internalized. Measured by prompting the AI directly and asking it to self-assess across explicit sub-categories. Directional, not a single source of truth — each org should define their own version. Mikael tracks it as a personal CPO KPI.

**Three-Layer Memory Architecture**
- Layer 1: Knowledge graph (visual, interconnected, Fable-generated)
- Layer 2: Vector database (fuzzy/semantic retrieval)
- Layer 3: Raw transcript store (no summarization — preserves granular detail and improves recall by 20–25% vs. summarized storage)
Combined, these create a persistent, compounding knowledge base that improves daily.

**Hybrid Search (Exact + Vector)**
When processing a query, the agent first attempts exact keyword matching (~25% of cases). On failure, it falls back to vector search (~75% of cases). This two-pass approach avoids overloading the context window with irrelevant data while maintaining high recall on ambiguous, fuzzy queries.

**Hermes Skill Auto-Generation**
Hermes detects recurring task patterns and automatically creates named skill modules (e.g., "board skill," "team hiring evaluation," "immigration case building"). Skills encode domain-specific reasoning and retrieval patterns. Measured to improve recall accuracy by 31% across tested topic areas. The system also autonomously decides when a new skill is warranted, removing the meta-work of skill management from the CPO.

**Imperative Library (SOUL.md)**
A 700–800 line document of behavioral rules loaded into every agent prompt. Key imperatives include: no fabrications, think before acting, facts over guesswork, no "fake helpful" responses, and maintaining a specific voice. Each imperative is regression-tested against benchmark queries before being added to production.

**Agentic CPO Role Model**
A shift from "procedural scaffolding" (hiring principles, planning cadences, review ceremonies) to "agentic orchestration" (owning the AI architecture, training teams to use it, measuring context coverage and recall, iterating on agent behavior in real time). The CPO becomes the system's primary owner and feedback loop.

**Role-Based Access Control for Agent Context**
Each employee's identity maps to a defined scope of tools and retrievable context. Sensitive context (board meetings, executive strategy) is gated at the agent level. Personal meetings are excluded from the knowledge graph by default — employees opt in rather than opt out.

**Recall Benchmarking Methodology**
1. Ask the agent which topics it is most frequently queried on.
2. Generate 10 representative questions per topic.
3. Run a controlled experiment: agent without skills (control) vs. agent with skills (treatment).
4. Score accuracy per question, per topic.
5. Once methodology is validated, delegate ongoing evals fully to the system.

**"Old Paradigm vs. AI-Native" Team Staffing**
High complexity / high blast-radius domains (monetization, search ML, algorithms): unchanged staffing, dedicated human owners. Customer-facing domains: one PM can own 3–4 domains simultaneously. The PM-engineer-designer triad blurs into shared orchestrators of quality and token budget within their respective disciplines.