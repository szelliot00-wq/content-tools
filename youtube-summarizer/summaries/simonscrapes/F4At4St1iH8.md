# Claude Code Agentic OS… It Remembers Everything

Video ID: `F4At4St1iH8`

## Summary
The video argues that Claude Code's built-in memory is critically insufficient for professional or team use — it stores almost nothing automatically, injects minimal context at session start, and has no meaningful semantic search. The creator spent months reverse-engineering several open-source memory frameworks (GBrain, Hermes, Memarch) and cherry-picked the best mechanisms from each to build a custom "Agent OS" with four pillars: cited recall, session-injected snapshots, semantic vector search, and scoped team access. The result is a multi-tier memory pipeline that runs on a local or cloud-hosted Postgres + PGVector database and can retroactively index months of prior Claude Code sessions. It is most relevant to freelancers, agencies, and product/dev teams using Claude Code across multiple clients and long-running projects.

## Key insights
- **Claude Code's auto-memory is nearly useless in practice.** After months of use, the creator's project had only two files in the auto-memory folder — one index entry and one project. Unless you explicitly say "remember this," almost nothing is captured.
- **Three questions define any memory system:** (1) Where/how does it store information? (2) What gets injected at session start? (3) How does it recall the right thing on demand? Claude Code is weak on all three by default.
- **Citation is a trust requirement, not a nice-to-have.** When memory conveys a teammate's decisions rather than your own, you need to know the source, the exact words used, and the date it was agreed — not just a fact asserted by the model.
- **Frozen snapshots beat full-context injection.** Loading thousands of lines of context at session start causes "context rot." The better pattern (from Hermes) is a small, capped, curated snapshot of what actually matters right now.
- **Semantic search finds what keyword search misses.** Searching "payment processing" should surface "Stripe" even though the two share no words. Vector embeddings enable this; keyword-only search (Claude Code's default) cannot do it reliably.
- **Hybrid search (vector + keyword) is the practical sweet spot.** Running both in parallel gives breadth (semantic relevance) and precision (exact term matches).
- **Reranking + synthesis is the final retrieval layer.** Raw vector results get reranked by relevance, then a model writes a cited, synthesized answer — and explicitly admits when it cannot find an answer, which is critical for reliability.
- **The three-tier retrieval hierarchy:** (1) Read short-term injected context already in the window; (2) if not found, run vector + keyword search over long-term store and pull top 5–10 results; (3) rerank and synthesize with citations.
- **Everything is embedded long-term regardless of short-term promotion.** Even if a fact is not promoted to the capped snapshot, it is chunked, vectorized, and stored — so nothing is permanently lost.
- **Retroactive indexing solves the cold-start problem.** The system can ingest all existing session history and generate both short- and long-term memories from it, so you don't start from zero on day one.
- **Memarch was replaced by PGLite + PGVector** for three reasons: no external dependencies (runs locally), works on Windows (Memarch required a cloud account on Windows), and supports row-level security for scoped team access.
- **Row-level security enforces memory scoping in the database itself**, not at the application layer. Every row is tagged (system / team / client / private), and every query is filtered by the identity of the requester — the database enforces it, not a prompt.
- **A junior team member on a specific client sees:** their system context, shared team context, that client's data, and their own private work — nothing else, enforced at the DB layer.
- **Non-technical team members contribute via Notion or Google Drive** for files like brand context and CLAUDE.md; Claude Code handles skills and memory functions; GitHub handles version control and backup automatically.
- **The stop hook triggers after every turn** to evaluate whether a new fact should be promoted to short-term memory and to embed everything into the long-term vector store regardless.
- **Short-term memory deduplication happens on every write** — the system checks whether a new fact duplicates or overwrites an existing entry before saving.

## Use cases
- **Freelancers managing multiple clients** who need strict context isolation between engagements and reliable recall of decisions made months ago
- **Small agencies or product teams** where multiple people need shared memory but with different access levels per client or project
- **Founders or PMs** using Claude Code as a day-to-day business operating system, tracking pricing decisions, product direction, and client commitments over time
- **Solo developers** who want session-to-session continuity without manually re-explaining context every time
- **Teams onboarding new members** who need to quickly surface historical decisions and reasoning without digging through raw chat logs
- **Anyone with months of existing Claude Code session history** who wants to retroactively make that history searchable and useful

## Patterns & frameworks

**Four pillars of "perfect memory" (the creator's synthesis)**
A composite model assembled from four open-source projects: cited recall (GBrain), session injection via frozen snapshots (Hermes), semantic long-term search (Memarch/vector DBs), and scoped team access (GBrain's "company brain"). Each pillar solves one gap in Claude Code's default behavior.

**Frozen snapshot injection (from Hermes)**
At session start, a stop hook injects a fixed, capped set of curated context files (soul.md, user.md, memory.md, today.md) rather than dumping everything. This prevents context bloat while ensuring the most relevant recent facts are always available. The snapshot is size-bounded to avoid "context rot."

**Stop hook → dual-write pipeline**
After every conversational turn, a hook evaluates the exchange: if it contains a durable fact (decision, preference, price change, environment factor), it is promoted to the short-term capped memory file. Simultaneously and unconditionally, everything is chunked, embedded as vectors, and written to the long-term store.

**Three-tier retrieval**
Tier 1: read what is already injected in the context window. Tier 2 (if needed): convert the query to vectors and run hybrid vector + keyword search over the long-term store, returning top 5–10 results. Tier 3: rerank those results, then synthesize a cited answer that names the source, the relevant passage, and the date — and explicitly states when no answer is found.

**Semantic + keyword hybrid search (from Memarch)**
Queries are executed as both a vector similarity search (finds conceptually related content regardless of shared words) and a keyword search (finds exact term matches). Results are merged and reranked, giving both recall breadth and precision.

**Row-level security scoping (from GBrain's "company brain")**
Every memory row in the Postgres database is tagged with a scope label (system, team, client, private). Every query is automatically filtered to return only rows the requesting user is permitted to see. Authorization is enforced at the database layer, not by prompt engineering.

**Decision tree for choosing a memory framework**
The creator proposes three sequential questions to select the right framework components: (1) Verbatim storage vs. summarized/chunked? (2) No injection vs. partial frozen snapshot vs. full context load at session start? (3) Keyword recall vs. semantic/hybrid recall, and raw chunks vs. cited synthesized answers?

**Retroactive back-catalog indexing**
A one-time ingestion process that reads all prior Claude Code session history and generates both short-term and long-term memories from it, solving the cold-start problem so the system is immediately useful from the first day of installation.