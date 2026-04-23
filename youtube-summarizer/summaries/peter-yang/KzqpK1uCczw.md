# How to Build for AI Agents and a Claude Code Second Brain in 25 Min | Ryan Wiggins

Video ID: `KzqpK1uCczw`

## Summary
This video features a conversation between host Peter and Ryan Wiggins, a product lead at Mercury (a banking platform for startups), covering two main topics: Mercury's Model Context Protocol (MCP) integration and Ryan's personal AI-powered "second brain" built on Claude Code. Ryan argues that product teams must meet customers wherever they are — and in the 2020s, that means APIs and conversational interfaces. The video is most relevant to product managers, startup founders, and technical builders interested in AI tooling, agent-ready product design, and personal productivity systems using AI.

---

## Key Insights

- **Mercury's MCP is a read-only API connector** available in the Claude app store that lets users ask natural language questions about their business finances (e.g., "Where can I save money?" or "What are my top monthly expenses?"). It uses OAuth for seamless login rather than requiring config file edits.
- **The MCP is read-only by design** for safety and user control, even though Mercury's full API supports both read and write operations matching the web and mobile app functionality.
- **Real-world MCP use cases include**: an animation studio discovering tax breaks they didn't know about, and a growing scoreboard of users who have saved over $1,000 through spend analysis. Users also pull business identity data like EIN and business address directly through the MCP.
- **Mercury serves 1 in 3 startups in the US**, giving it strong signal on AI tool adoption trends. Data shows that for the past 3–4 years, new startups chose OpenAI first, but this has recently shifted toward Anthropic/Claude.
- **MCP as a distribution layer**: Ryan argues MCP is analogous to third-party apps on Apple's App Store — it's the accessible integration layer that opens new consumer-facing AI platforms (ChatGPT, Claude) to business services. OpenAI and Anthropic both supporting MCP makes it a de facto standard.
- **Mercury CLI is coming soon** (announced in this video as breaking news), targeting power users and developers who want more flexible, lower-context tooling compared to MCP.
- **Ryan's "Second Brain" system** is built on Claude Code and consists of ~5 million words of personal and company knowledge (strategy docs, specs, queries, meeting transcripts) stored on a local file system, indexed using QMD/Toby's local indexing, and injected via Claude hooks into every query he runs.
- **The second brain integrates with**: Notion (meeting transcripts), Slack, Linear, GitHub, Metabase, and Omni (BI tool), allowing multi-agent workflows that run full analyses, summarize the day, and surface action items.
- **The coaching use case is a standout**: Ryan feeds meeting transcripts into the system, which then cross-references his performance review feedback (e.g., "you jump to solutions too fast") and flags when that behavior appears in real meetings — creating a high-frequency accountability loop his manager and people partner have noticed positively.
- **Daily and weekly workflow structure**: Every morning, the system generates a brief covering calendar, Linear, GitHub, and Slack. Every evening, it summarizes meetings and extracts action points. Weekly start and end rituals are also built in.
- **Internal AI data analyst at Mercury**: Built by prototyping locally first, this agent now answers ~80–90% of cross-functional (XFN) data questions that teams were asking (e.g., application volume, sales conversion by product). It also surfaces gaps in data infrastructure by analyzing what questions people are asking.
- **Disposable front-end prototyping**: Mercury built a demo environment (demo.mercury.com) that any PM or designer can quickly edit to prototype ideas without touching the backend, collapsing the time from idea to stakeholder alignment. This is replacing long written specs and alignment meetings.
- **AI tool switching costs are real**: Ryan notes he has tried switching his second brain setup from Claude to Codex but found it difficult due to memory, configuration, and trained context accumulation — suggesting that deep AI workflow integration creates meaningful lock-in.
- **First model choice drives downstream decisions**: Ryan theorizes that whichever AI platform a startup adopts first (OpenAI vs. Anthropic) cascades into subsequent tooling, licensing, and enterprise product choices — making early adoption a strategic moment.
- **MCP success metrics mirror traditional product funnels**: Discovery → activation (error rates during setup) → engagement (repeat sessions) → retention → expansion. Post-setup retention is reportedly strong, with users settling into daily, weekly, or monthly workflows.

---

## Use cases

- **Startup founders** wanting to understand cash flow, identify tax savings, or pull business identity data without logging into a banking dashboard
- **Finance and ops teams** using natural language to analyze spend and generate financial reports via Claude
- **Product managers** looking to build an AI-powered personal knowledge base and coaching system using Claude Code
- **Product managers and designers** wanting to prototype faster using disposable front-end environments instead of writing lengthy specs
- **Data teams and analysts** trying to democratize data access across a company using an AI data analyst agent
- **Engineering and product leaders** evaluating whether to build an MCP, a CLI, or a full API — and understanding the tradeoffs
- **Executives** who want a daily/weekly AI-powered debrief system tied to their tools (Slack, Linear, Notion, GitHub)
- **Anyone receiving recurring performance feedback** who wants a system to hold them accountable in real time against that feedback
- **Builders evaluating AI platform strategy** (OpenAI vs. Anthropic) thinking about lock-in, ecosystem, and first-mover decisions

---

## Patterns & Frameworks

### 1. "Meet Customers Where They Are" — Platform Evolution Framework
**What it is**: A mental model for how technology companies must evolve their interface layer across decades.
**How it works**: 1950s = bank branch → 1970s = ATM → 1990s = website → 2010s = mobile app → 2020s = APIs + conversational interfaces. Ryan uses this to argue that building an MCP is not cannibalization of the core product — it's the next required interface layer. Any company not showing up in the AI agent layer is making the same mistake as banks that ignored mobile.

---

### 2. The "Second Brain / Mission Control" System
**What it is**: A personal AI operating system built on Claude Code that combines a knowledge base, memory, hooks, skills, MCP integrations, and multi-agent workflows.
**How it works**:
- **Context layer**: ~5M words of company docs, specs, queries, and meeting notes stored locally
- **Indexing**: QMD/Toby's local indexing for semantic (concept-based, not keyword) search
- **Injection**: Claude hooks automatically inject relevant context into every query
- **Skills**: Reusable patterns for analysis, app building, and learning
- **MCP integrations**: Connected to Slack, Linear, Notion, GitHub, Metabase, Omni
- **Multi-agent workflows**: Full analysis pipelines that run, discuss, and report autonomously
- **Daily ritual**: Morning brief + evening debrief with action items and performance coaching

---

### 3. Prototype-First Product Development
**What it is**: Replacing written specs and alignment meetings with quickly editable disposable front-end prototypes.
**How it works**: Mercury built a shareable demo environment (demo.mercury.com) that PMs and designers can edit without backend changes. Ideas go from concept → visual prototype → stakeholder feedback loop much faster than traditional spec-writing workflows. Collapses ideation-to-alignment time significantly.

---

### 4. MCP as "Third-Party App Store" Mental Model
**What it is**: Framing MCP not as a technical protocol but as a distribution and discovery layer — analogous to the Apple App Store for AI platforms.
**How it works**: Just as Apple's App Store opened iOS to third-party developers and unlocked new product categories, MCP opens ChatGPT and Claude to business services like Mercury. Because both OpenAI and Anthropic have standardized on MCP, it becomes the common integration layer. This makes building an MCP a go-to-market and distribution decision, not just an engineering one.

---

### 5. AI Funnel Metrics for Agent Products
**What it is**: Adapting traditional product funnel thinking to measure agent/MCP product performance.
**How it works**: Discovery → Activation (setup success, error rate) → Engagement (sessions per user) → Retention (continued use over time) → Expansion (new use cases or integrations). The key insight is that once users successfully set up the MCP, retention is high because it integrates into recurring workflows (weekly spend review, monthly tax analysis).

---

### 6. Prototype Locally → Validate → Ship Internally
**What it is**: A low-risk AI agent development process used to build Mercury's internal AI data analyst.
**How it works**: Build a working agent prototype locally (Claude Code + real data), validate accuracy (targeting 80–90% question coverage), build confidence in reliability, then peel it off and ship it internally to the broader company. This reduces the risk of shipping unreliable AI tools and gives you a real accuracy benchmark before broader rollout.