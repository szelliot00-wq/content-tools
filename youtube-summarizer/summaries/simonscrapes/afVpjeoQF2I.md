# Anthropic Just Built It’s Own Agentic OS

Video ID: `afVpjeoQF2I`

## Summary
This video covers Anthropic's newly announced overhaul of Projects in Claude Code, which the creator frames as Anthropic building its own version of the "Agentic OS" that many power users have been hand-crafting themselves. The core argument is that Anthropic is productizing the orchestrator/sub-agent architecture, RAG-based context management, and team permission systems that advanced users have been building manually on top of Claude. The video is most relevant to product managers, AI power users, and teams who have been building or considering custom AI operating systems for their workflows.

## Key insights
- **Projects are no longer just folders of chats** — a project is now a single long-running conversation that acts as an orchestrator, delegating work to sub-threads rather than doing the work itself.
- **Thread architecture mirrors agent OS design** — each thread is a full Claude Code cloud session on its own branch, and threads can themselves spin out sub-agents and workflows, creating a multi-level delegation tree.
- **Cloud-native execution** — threads run in the cloud and continue after you close your laptop, removing the need to keep a session open to let work complete.
- **Automatic context injection per thread** — every thread is auto-populated with project repos, uploaded files, project instructions, and a `memory.md` file that carries decisions across conversations.
- **RAG is now built in** — instead of loading every file into every context window, Claude gets a "project knowledge search tool" that pulls only relevant content. When the project shrinks back under the context limit, it reverts to loading everything directly. No user setup required.
- **Context wall problem addressed** — previously, hitting the context limit meant pruning files, splitting projects, or starting new conversations; the retrieval layer is the direct fix for this.
- **Team collaboration and permissions** — on Team and Enterprise plans, project owners can assign view or edit access by email or org-wide, enabling shared context with controlled write access across teammates.
- **Library tab for outputs** — a new library tab collects both files you added and files Claude produced, preventing outputs from getting lost across sessions.
- **Current limitations**: Claude Code only (not Chat or Co-Work yet), cloud-only (no local files or local tools), the main conversation cannot directly use MCP connectors (only threads can), and simple tasks may still consume disproportionate tokens as their own threads.
- **Pro and Max plans only** — not yet widely rolled out; the creator themselves does not yet have access.
- **67% of the creator's community** had specifically requested team OS functionality inside an Agentic OS setup, validating Anthropic's direction.

## Use cases
- **Teams collaborating on a large project** where different members handle different workstreams and need shared, permissioned context without duplicating work.
- **Solo power users** who have been manually managing multi-session workflows and want native orchestration without custom tooling.
- **Content or marketing teams** running parallel creative workstreams (e.g., one thread for copywriting, one for research) under a single project umbrella.
- **Developers building products on Claude** who want to understand the platform's direction before investing further in custom agent infrastructure.
- **Enterprise teams** that need role-based access control over AI-managed project context (view vs. edit permissions).
- **Anyone hitting the context window limit** regularly on large projects who needs seamless retrieval without manual file pruning.
- **Operators of "Agent OS"-style setups** evaluating whether to migrate to Anthropic's native solution or continue maintaining a custom stack.

## Patterns & frameworks

**Orchestrator / Sub-agent Architecture**
The main project conversation acts as a team lead — it receives a goal, decides whether to create a new thread or route to an existing one, and delegates execution. Threads are the workers. Threads can further spawn their own sub-agents and workflows. This mirrors the hand-built "orchestrator + sub-agent routing" pattern that the creator's community has been building manually.

**Agent OS (Agentic Operating System)**
A custom-built framework the creator's community developed, consisting of: a memory layer (distinguishing personal vs. shared data), skill encodings (how the business actually does work), refined brand context (not just a folder of PDFs), and team permissions mapped to real org structure. Anthropic's new Projects is framed as the MVP version of this concept, now productized.

**RAG in Projects (Retrieval-Augmented Generation)**
Rather than loading all project files into every context window, Claude uses a search tool to pull only the relevant files for a given query. When the total project size drops back under the context limit, it falls back to loading everything directly. This is automatic — no pipeline setup required from the user.

**Memory.md as Cross-Thread Decision Log**
A `memory.md` file is maintained at the project level and automatically shared across all threads. It functions as a persistent, cross-conversation decision log so that threads started at different times are aware of prior decisions made elsewhere in the project.

**Library Tab as Output Registry**
All files Claude produces across threads are collected in a single Library tab, functioning as a project-level output registry that prevents work from being lost across fragmented sessions.