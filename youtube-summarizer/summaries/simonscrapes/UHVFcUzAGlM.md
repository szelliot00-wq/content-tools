# Every Claude Code Memory System Compared (So You Don't Have To)

Video ID: `UHVFcUzAGlM`

## Summary
This video systematically compares every major Claude Code memory system available, organizing them into six progressive levels that build on each other. The creator's core argument is that these tools are not competitors — they solve different problems depending on scale, use case, and how many AI tools you work across. The video is grounded in the creator's personal experience building an "agentic operating system" (a business brain running across all their AI tools). It is most relevant to power users of Claude Code, solo operators, developers, and business owners who want persistent, scalable AI memory without unnecessary complexity.

---

## Key insights

- **Every memory system answers the same question:** When Claude gets a task, how does it pull the right context at the right time? The only two variables are *where* memory is stored (file structure, database type) and *how* Claude retrieves it (auto-injected vs. actively searched).

- **Level 1 — Native Claude Code tools (claude.md + auto-memory):** Claude.md is a plain markdown file always loaded into every session, functioning like a system prompt. It can exist at the project folder, root folder, or individual project level, with local files overriding parent-level rules. Auto-memory creates a `memory.md` index file per project that quietly captures notes and feedback in the background. Anthropic's unreleased internal framework "Chyros" (found in leaked source code) suggests an always-on daemon is coming to improve this further.

- **The #1 claude.md mistake:** Stuffing too much into it (full brand guides, complete client lists, tone-of-voice documents). This causes "context rot" — the LLM's degrading recall as context window fills up. Rule of thumb: **keep claude.md under 200 lines** and reference external files for heavy content.

- **Level 2 — Structured memory with session-start hooks:** Based on frameworks by Pavel Hurin and John Connelly, this adds a formal memory directory structure (`claude/memory/general.md`, domain-specific files, tool-specific files like `slack.md`) and a session-start hook that auto-injects the memory index before the first tool call — removing reliance on Claude spontaneously reading it. After 5 days of usage, one user's memory files grew ~90% in count but the index files stayed lean. This also opens the door to **team memory sharing** by syncing domain files across teammates.

- **Context rot is the central problem** being solved at every level. As memory files grow, keyword search degrades and giant single files (like `general.md`) become inefficient. Each level is essentially a more sophisticated solution to this bottleneck.

- **Level 3 — Semantic vector search via MemSearch (by Zilliz):** Ports OpenClaw's memory architecture into Claude Code with a two-line install. Uses the `user_prompt_submit` hook to automatically inject the **top 3 semantic matches** from memory files into every prompt — no manual searching required. Stores everything in plain readable markdown. Adds the OpenClaw "dreaming" concept: a background process that reads daily notes, scores them, and promotes recurring ones into long-term `memory.md`, discarding stale content.

- **Claude Mem (alternative to MemSearch):** MCP-based plugin with a 3-tier storage model (summaries, timeline, observations), a dashboard, team collaboration, cost tracking, and privacy labels. Key difference: Claude must *actively decide* to call the search tool rather than auto-injection. Also stores everything in the background rather than readable markdown. Considered overkill for most individual use cases.

- **Level 4 — Verbatim word-for-word recall via Mem Palace:** A proper local RAG system claimed to have the highest published benchmark score of any memory system. Stores conversations *verbatim* — nothing is summarized, so nothing is theoretically lost. Uses a hierarchical index in a compressed symbolic language ("AA dialect") that an LLM can scan at a glance — structured as Wings → Rooms → Closets → Drawers. Uses two databases: an SQL database for entities/relationships and a ChromaDB vector database for searchable conversation chunks. Retrieval demonstrated at **42 milliseconds**. Hooks fire on session end and pre-compaction to silently file and index information. Supports retrospective mining of past sessions. Downside: not human-readable markdown.

- **Level 5 — Interconnected knowledge base (Karpathy's LLM Wiki / Recall):** Shifts from *conversation memory* to *knowledge synthesis*. Two folders: `raw/` (source documents Claude reads but never writes to) and `wiki/` (Claude owns entirely, maintains cross-references). Visualized in Obsidian as a knowledge graph. Best for: deep research on interconnected topics, processing saved articles/videos/podcasts. Creator's honest take: **limited direct operational use** for business project work. Recall is the hosted version — zero setup, browser extension, MCP access, works on phone — but data lives on their servers and it's built for content consumption, not operational memory. LightRAG is the enterprise-grade alternative but called "completely overkill for 99% of business owners."

- **Level 6 — Cross-tool universal memory (Open Brain / Mem0):** The only system where *all AI tools share the same memory in real time*. Open Brain uses a Postgres database hosted on Supabase with one table called `thoughts` (text chunk + embedding vector + tags + timestamp). An MCP server connects Claude Code to Supabase edge functions, and any AI tool (ChatGPT, Claude Desktop, Cursor) can query the same brain. Cost: **~$0.10–$0.30/month** on Supabase free tier. Setup takes 30–45 minutes. Downside: external database query adds latency; data not stored locally. Mem0 (mem.ai) is the production-ready alternative — used by 100,000+ developers, sub-one-minute setup, self-improving — but data lives permanently on their servers.

- **Levels stack:** Levels 1, 2, and 3 can be run simultaneously with compatible folder structures. Claude Code can be asked to integrate them.

- **Creator's personal choice:** Implementing up to Level 3 in their agentic OS — OpenClaw memory conventions plus semantic search and hooks for context injection. Explicitly skipping Levels 4–6 for their primary workflow.

---

## Use cases

- **Complete beginner to Claude Code:** Start with Level 1 — set up `claude.md` properly and let auto-memory run. Takes ~10 minutes and delivers immediate improvement.
- **Solo operator or freelancer using Claude Code daily for 1+ month:** Add Level 2 (John Connelly's hook system) for reliable memory injection and structured domain/tool files.
- **Teams sharing a Claude Code setup:** Level 2's domain file syncing allows teammates to share tool-specific and project-specific memory files.
- **Power user with months of accumulated context losing old decisions:** Move to Level 3 (MemSearch) for semantic search, or Level 4 (Mem Palace) if verbatim recall of exact wording is critical (e.g., "what exactly did we decide about client X's pricing in March?").
- **Researchers or heavy content consumers** (articles, podcasts, YouTube, PDFs): Level 5 — Karpathy's LLM Wiki or Recall for building an interconnected knowledge graph.
- **Users who work across multiple AI tools** (ChatGPT on phone, Claude Code at desk, Cursor in IDE): Level 6 — Open Brain or Mem0 for a single shared memory layer across all tools.
- **AI product developers shipping applications:** Mem0 (mem.ai) is appropriate for production-grade cross-tool memory in shipped products.
- **Non-technical users wanting passive knowledge organization:** Recall (hosted service) with zero setup and browser extension.
- **Business owners building an "agentic OS"** — an AI brain spanning all business functions: Levels 1–3 stacked together.

---

## Patterns & frameworks

**1. Six-Level Memory Stack**
The core organizing framework of the video. Each level builds on the previous, solving a specific failure mode:
- L1: Native tools (claude.md + auto-memory)
- L2: Structured memory + session-start hooks
- L3: Semantic vector search (MemSearch)
- L4: Verbatim RAG (Mem Palace)
- L5: Knowledge graph (LLM Wiki / Recall)
- L6: Cross-tool universal memory (Open Brain / Mem0)

**2. Context Rot**
The phenomenon where LLM recall degrades as context window fills. Named explicitly as the root problem all memory systems are solving. Mitigation: keep index files lean (<200 lines), reference external files rather than embedding full content inline.

**3. Index + Reference File Pattern**
Rather than one giant memory file, maintain a lean index file (memory.md or claude.md) that *points to* separate domain-specific or topic-specific markdown files. Files are only loaded when relevant. Prevents context rot and keeps retrieval efficient.

**4. OpenClaw Memory Architecture (Short-term → Long-term via Dreaming)**
Three-layer model:
- `memory.md` = long-term durable facts (loaded every session)
- Daily note files = running log (today + yesterday auto-loaded; older files stay on disk but not in context)
- "Dreaming" = background process that scores daily notes, promotes recurring insights to long-term memory, and discards stale content
This mimics human memory consolidation during sleep.

**5. Hook-Based Auto-Injection**
Using Claude Code's built-in hook system (session start, user prompt submit, session end, pre-compaction) to automatically inject memory context at the right moment without relying on Claude to spontaneously read or search for it. Key hooks used:
- `session_start` → inject memory index
- `user_prompt_submit` → inject top semantic matches (MemSearch)
- `session_end` / `pre-compaction` → silently file and index new information (Mem Palace)

**6. Mem Palace (Wing → Room → Closet → Drawer)**
An ancient memory method adapted for AI. A hierarchical spatial index that stores verbatim text in nested structures:
- Wing = people, projects, topics
- Room = days, sessions, threads
- Closet = sub-topics, bundles
- Drawer = verbatim text
The index is written in a compressed symbolic "AA dialect" that lets the model scan thousands of entries in a single pass (~42ms retrieval demonstrated).

**7. Raw / Wiki Folder Split (Karpathy's LLM Wiki Pattern)**
Two-folder architecture for knowledge base building:
- `raw/` = source documents (Claude reads, never writes)
- `wiki/` = Claude-owned wiki (Claude writes, maintains, cross-references; human never writes here)
Ensures clean separation between inputs and synthesized knowledge.

**8. Open Brain Architecture (Universal Memory Layer)**
One Postgres database (Supabase) with a `thoughts` table (text + embedding + tags + timestamp). MCP server bridges Claude Code to Supabase edge functions. Any AI tool connects to the same database. Future-proof: new AI tools plug into the existing brain with no migration. Pattern: own your data, pay ~$0.10–$0.30/month, portable across the entire AI tool ecosystem.