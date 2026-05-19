# Master Claude Memory to Get Ahead of 99% of People

Video ID: `rFWxRZ5D-lM`

## Summary
This video breaks down the current state of Claude Code's built-in memory system, compares it to two advanced open-source alternatives (memarch and Hermes), and proposes a hybrid setup that combines the best elements of each. The core argument is that memory systems must answer three questions — how is information stored, how is it injected into context, and how is it recalled — and Claude Code's defaults are weak on all three, especially recall. The video is most relevant to developers and power users running multi-project or multi-client workloads in Claude Code who need reliable long-term memory without burning excessive tokens.

## Key insights
- Claude Code's automemory is selective and sparse — it only saves information it judges "memory-worthy," stores it as `.md` files in a per-project folder, and promotes frequently repeated preferences to a global `~/.claude/memory` folder. In practice, it saves very little.
- The `/memory` command in Claude Code terminal lets you view user memory (CLAUDE.md), project memory, and the automemory folder with its index of saved files.
- **memarch** uses a stop hook that fires after *every* turn, calls Haiku (cheap/fast) to summarize the turn into bullets, and appends everything to a `memory/date` file with session anchors. It then chunks, hashes, embeds, and stores everything in a local Milvus vector database — zero API cost, runs on CPU.
- memarch stores markdown as the source of truth; the vector database is rebuildable from markdown if lost. Capturing everything is intentional — completeness over curation.
- **Hermes** takes the opposite philosophy: the agent itself decides what to save using add/replace/remove tools, writing to a character-capped `memory.md` (environment facts, decisions) and `user.md` (user preferences and working style). The cap enforces consolidation rather than sprawl.
- Hermes also saves raw transcripts to a background database and runs a curator every 7 days to prune and consolidate — unlike memarch which keeps raw transcripts permanently.
- For injection, Claude Code's default is: inject full `CLAUDE.md` at session start, then use a pre-tool-use hook to check the memory index and selectively load relevant memory files as additional context mid-conversation.
- memarch has **no injection layer** — it relies entirely on Claude Code's default CLAUDE.md injection. Its value is purely in storage and recall.
- Hermes injects a "frozen snapshot" at session start: CLAUDE.md + `memory.md` + `user.md` + `soul.md` ≈ 1,300 tokens. This is cached per session ID, so it doesn't cost tokens on every message — only once per session.
- Anything written to memory files *during* a session is saved to disk but only loaded into the *next* session's frozen snapshot, not the current one.
- Claude Code's recall is its biggest weakness: if something wasn't saved to automemory, it's effectively lost. Recovering it requires trolling through past raw conversations with no systematic methodology.
- memarch uses a **three-tier retrieval system**: Tier 1 — hybrid search (dense vectors for semantic meaning + BM25 for keywords) returns closest matches; Tier 2 — "expand" adds metadata and surrounding context for a match; Tier 3 — raw session dialogue as a last resort. Each tier costs more tokens.
- Hermes recall checks the already-injected `memory.md` first (zero cost, instant, already in context) before doing any database search. If not found there, it searches the session database by keyword, returns the top 3 matching sessions, and summarizes them using Gemini Flash.
- Hermes is strong on exact keyword recall but weak on semantic/meaning-based recall (e.g., searching "pricing" won't surface "revenue").
- The recommended hybrid adds a "Tier 0" before memarch's tier system: check what's already in the injected context window (memory.md + daily log) before hitting the vector database.
- A nightly job to run `memarch index` consolidates all daily transcripts into the vector database — keeps the database clean without manual intervention.

## Use cases
- Developers managing multiple clients or projects simultaneously who need to recall past decisions (e.g., "what did we decide about pricing last Tuesday?")
- Teams where context accumulates over months — project URLs, stack decisions, client preferences — that would otherwise be lost between sessions
- Anyone frustrated by Claude Code "forgetting" things it was told in previous sessions
- Power users who want to keep CLAUDE.md lean (under 200 lines) but still have rich context available on demand
- Use cases where semantic search matters — finding past discussions about "revenue" when the original used the word "monetization"
- Automated workflows where a stop hook can run silently after every turn without user intervention
- Long-running agentic setups where the agent needs to self-manage memory (add/replace/remove) rather than relying on the user to curate it

## Patterns & frameworks

**Three questions every memory system must answer**
A diagnostic framework: (1) How/when does information get stored? (2) How/when does it get injected into context? (3) How/when does it get recalled? Evaluating any memory system against these three dimensions reveals where its strengths and gaps lie.

**Store → Inject → Recall lifecycle**
The full conversation memory lifecycle. Storage captures information during a session. Injection pushes the right subset into the context window at session start (and optionally mid-session). Recall retrieves older information on demand when it isn't already in context.

**Frozen snapshot injection (Hermes pattern)**
At session start, load a fixed set of curated markdown files (memory.md, user.md, soul.md) alongside CLAUDE.md. The snapshot is cached per session ID, so the token cost is paid once not per-message. Files updated during a session take effect only in the *next* session — this keeps the current context window stable.

**Three-tier progressive retrieval (memarch pattern)**
Only go deeper if the shallower tier doesn't answer the question: Tier 1 = hybrid vector+keyword search (fast, cheap); Tier 2 = expand with metadata and surrounding context; Tier 3 = raw session dialogue (slow, expensive, most complete). Applies the principle of progressive disclosure to token spend.

**Tier 0 check (Hermes + memarch hybrid)**
Before executing any database query, check what's already loaded in the current context window. If memory.md or the daily log already contains the answer, the cost is zero and the response is instant. This sits above Tier 1 in the retrieval stack.

**Automatic capture + curated facts (combined storage strategy)**
Don't choose between completeness and curation — use both. A stop hook captures everything verbatim (completeness, good for recall). A separate agent-managed memory.md/user.md stores only high-signal facts (curation, good for injection). Each serves a different downstream purpose.

**Character-capped memory files (Hermes consolidation mechanism)**
Setting a hard character cap on memory.md forces the agent to consolidate rather than append indefinitely. When the cap is approached, older or lower-value entries must be replaced — enforcing recency and relevance bias automatically.