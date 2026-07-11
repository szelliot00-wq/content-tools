# I Rebuilt Hermes’s Best Feature in Claude Code (Steal This)

Video ID: `9CiOwbmOKdU`

## Summary
The video argues that the primary reason users are switching from Claude Code to Hermes Agent is persistent memory, not integrations or other features. The creator analyzes Hermes's memory architecture, identifies its limitations, and presents a rebuilt version implemented natively inside Claude Code using local files and a vector database. The result is a portable, subscription-plan-compatible memory system that improves on Hermes's recall capabilities with semantic search, source citation, and historical import. This is most relevant to power users of Claude Code who want long-term context continuity without managing a separate runtime or subscription.

## Key insights
- Hermes Agent grew from 0 to 211,000 GitHub stars in 5 months (launched February 2026); a Kilo analysis of 1,300 Reddit comments found ~30% of switchers cite memory as the reason
- Claude Code's built-in memory (as of July 2026) saves only occasional facts to a memory.md index, injects almost nothing at session start, and recalls by keyword search across the last 30 days of session files — all three phases are weak
- Any memory system can be evaluated across three dimensions: **storage** (what gets saved and where), **injection** (what is loaded at session start), and **recall** (how past information is retrieved)
- Hermes's core memory is simpler than it appears: a few injected markdown files, a character-capped summary agent, and an SQLite FTS5 keyword search over past sessions — easily replicable
- Hermes's self-rewriting loop (its headline feature) is also its biggest risk: it has a track record of overwriting correct information, leading users to bolt on approval gates and rollback systems
- Hermes has hard character limits that compress or replace memory entries; one user built a plugin specifically to stop standing instructions from being overwritten
- Hermes cannot import prior Claude Code conversation history — your memory database starts empty on day one regardless of how long you've been using Claude Code
- The rebuilt system uses a 2,500-character-capped memory.md for short-term injection at every session start, loaded silently alongside a soul/profile file and today's memories
- Storage is automated via a post-turn hook: after every turn, the system decides whether anything warrants saving as a durable fact and promotes it into the capped memory.md, checking for duplicates and prioritizing recency
- A meta memory write skill lets users define and edit the rules for what gets saved — the agent follows those rules rather than making arbitrary decisions
- Every turn generates a summary filed long-term alongside a full session transcript, enabling complete recall of any conversation at any point
- Recall is semantic, not keyword-based: conversations are embedded as vectors in a local PGLite + pgvector setup, searched by meaning and keyword, re-ranked for relevance, and context-expanded to pull neighboring conversation turns
- When recalling, the system cites the exact source transcript, date, who decided something, and the verbatim context — inspired by Garry Tan's "GBrain" concept
- Historical import is handled via `npm run memory import sessions`, which uses Claude Haiku to summarize existing session history, embed it into long-term storage, and archive full transcripts in JSON — covering up to 30 days of existing Claude Code history
- A "TeamOS" feature (currently in beta) scopes memory by project and team member, tagging every memory by owner and filtering queries so each person only sees what they're authorized to see
- The system is portable (plain files and folders), inexpensive (no VPS or second model billing), and local (no external security surface)

## Use cases
- Power users of Claude Code who lose context between sessions and want decisions from months ago to be accurately recalled
- Freelancers or consultants managing multiple clients who need memory isolated per client or project
- Teams using Claude Code collaboratively who want shared memory with per-member access controls
- Anyone who has been using Claude Code for months and doesn't want to lose that accumulated context when adopting a memory system
- Users considering switching to Hermes Agent primarily for memory, who want to evaluate a native alternative first
- Developers who want full ownership and portability of their AI memory (across Claude Code, Codex, or future tools) without depending on a third-party runtime
- People who need cited, source-traceable recall — e.g., knowing exactly which conversation a decision came from and who made it

## Patterns & frameworks

**Storage / Injection / Recall framework**
A three-question lens for evaluating any AI memory system: (1) How and where is information saved after a conversation? (2) What is automatically loaded at the start of each session? (3) When you ask about something old, how does the system find it and how reliably does it return the right answer?

**Frozen Snapshot (Injection)**
A size-capped file (2,500 characters here) containing curated, high-priority facts — current clients, active decisions, pricing — that loads silently at every session start. Prevents important standing context from requiring explicit recall each time.

**Post-Turn Hook (Automated Storage)**
A hook that fires after every conversation turn, evaluates the content, and promotes durable facts (decisions, preferences, price changes) into the short-term memory file. Deduplicates and replaces stale entries. Removes the user from the decision of what to remember.

**Recall Ladder**
A multi-stage retrieval process that searches by semantic meaning (vector embeddings) and keyword, re-ranks results for relevance, expands context to neighboring conversation turns, and surfaces cited transcripts with dates and attribution. Gets progressively deeper until it finds the most relevant match.

**Meta Memory Write Skill**
A user-editable rules file that defines what the agent is allowed to save to memory. Keeps the agent's saving behavior transparent and customizable rather than opaque.

**GBrain-inspired Citation**
When recalling any fact, the system returns the exact source transcript, the date, the speaker, and verbatim context — so users know whether a decision was theirs, a teammate's, or inferred, and can trace its origin.

**TeamOS (Scoped Memory)**
A memory architecture where every saved memory is tagged by owner/project, and every query is filtered by the identity of who is asking — enabling one shared memory store with per-member access control for team use.