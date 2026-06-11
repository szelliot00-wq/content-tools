# I Built The Best Claude Memory System (Beats Hermes)

Video ID: `H9BUkgDf5Y4`

## Summary
The video presents a custom-built memory system for Claude Code (agentic AI) that synthesizes the best ideas from four open-source memory frameworks: Hermes, GBrain, Memarch, and others. The author argues that no single framework adequately handles all three jobs of memory — storage, injection, and recall — so he cherry-picked the strongest component from each. The resulting system beats Claude Code's out-of-the-box memory on every dimension, offering automatic capture, capped context injection, and hybrid semantic+keyword search with cited answers. It is most relevant to developers, AI power users, and teams building or operating Claude Code-based workflows who need reliable, scalable, and transparent memory.

---

## Key insights
- **Claude Code's native memory has three distinct weaknesses:** storage is agent-decided (leaky — if the agent doesn't flag something, it's lost), injection is unbounded (no token cap, so context bloats), and recall is essentially nonexistent (no search mechanism; you'd have to resume the exact original session).
- **Memory has three jobs:** storage (saving facts), injection (loading context at session start), and recall (finding old information on demand). Every design choice in a memory system maps to one of these three.
- **Storage design has two independent variables:** who triggers the save (agent vs. automatic hook) and what format is saved (verbatim vs. summarized). Verbatim is bulky; summarized risks losing context; automatic hooks remove dependence on agent judgment.
- **Memarch was chosen for storage** because it fires a hook after every turn, summarizes with a cheap fast model (Haiku), and appends to a daily log — automatic and lean, without needing agent awareness.
- **Hermes was chosen for injection** because it takes a frozen snapshot of key memory files (identity, user profile, recent memories) at session start, capped at ~1,300 tokens, and the snapshot is cached so tokens are only paid once per session — not re-injected on every turn.
- **Memarch was also chosen as the base for recall** because it indexes all stored content as vectors locally (zero API cost), enabling hybrid search — both semantic (by meaning) and keyword (exact words). This is a three-tier system: it checks the injected snapshot first (tier 0) before doing deeper search.
- **GBrain (built by Gary Tan of Y Combinator) contributed two recall enhancements:** a reranker that does a second pass over retrieved chunks to surface the best matches first, and answer synthesis that returns a written response with citations (source file/conversation) rather than raw chunks.
- **The "admit what you don't know" principle** is built in: if the information isn't in the memory store, the system says so rather than hallucinating a confident answer — critical for real client work.
- **The system is modular by design:** each component (storage hook, injection snapshot, recall search) is a swappable block, making it portable across Claude Code, Codex, and other harnesses.
- **Team memory introduces a harder problem:** shared vs. private memory. Two approaches exist — (1) one database per person built only from files they're permitted to access (simple but isolated), or (2) one shared Postgres database (e.g., on Supabase) with row-level security, where every memory row is tagged by client/project/department and filtered by the querying user's access token (harder to set up but gives a true shared team brain).
- **The author's preferred team approach** is the shared Postgres/Supabase store with row-level security, which he describes as significantly more complex but far more powerful for multi-user teams working across clients.

---

## Use cases
- **Solo developers or AI power users** who want Claude Code to reliably remember decisions, preferences, and context across sessions without manual effort.
- **Freelancers or consultants** managing multiple clients who need to retrieve past decisions by meaning, not just exact keywords (e.g., "what did we decide about the pricing model for client X?").
- **Teams using Claude Code collaboratively** who need some memory shared (e.g., client context, project decisions) and some private (personal preferences, individual notes).
- **Anyone building agentic workflows** who needs the AI to cite its sources and admit uncertainty rather than hallucinating answers based on stale or missing context.
- **AI tooling builders** who want to understand the design space of memory systems and pick components intentionally rather than accepting a black-box solution.
- **Operators of long-running projects** where decisions made months ago need to be surfaced reliably in future sessions without manually curating memory files.

---

## Patterns & frameworks

**Memarch (storage + recall base)**
An open-source memory library used for two purposes here: (1) automatic post-turn hooks that summarize conversation turns with a fast/cheap model and append to a daily log, and (2) local vector indexing of all stored content enabling hybrid keyword+semantic search with zero API cost.

**Hermes (injection layer)**
A memory framework that solves context injection via a frozen snapshot at session start — a fixed set of high-priority memory files (identity, profile, recent memories) capped at ~1,300 tokens and cached for the session. Ensures relevant context is always present without bloating the context window.

**GBrain / "Company Brain" (recall synthesis + team architecture)**
Built by Gary Tan (YC). Contributes two things: (1) a reranker that does a second pass over retrieved chunks to reorder by relevance, and (2) answer synthesis that returns a written answer with citations instead of raw text chunks. Also provides the architectural model for team memory: one central store with row-level security, each user getting a scoped slice based on their access token.

**Three-tier recall system**
A layered search pattern: Tier 0 checks the injected frozen snapshot first. If found, search stops. If not, it escalates through deeper tiers until it reaches full hybrid (semantic + keyword) search across the entire indexed memory store.

**Storage decision matrix**
A mental model with two axes for evaluating any memory storage approach: (1) trigger mechanism — agent-decided vs. automatic hook; (2) format — verbatim vs. summarized. The chosen design here is automatic + summarized (Memarch's approach).

**Shared vs. isolated team memory (two-path architecture)**
A decision framework for team deployments: isolated path (one DB per person, built only from permitted files — simple but siloed) vs. shared path (one central DB with row-level security tagged by client/project/department — complex but enables a true shared team brain).