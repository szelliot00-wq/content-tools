# I Built a Claude System That Makes Context Loss Impossible

Video ID: `t6azkOJwx5M`

## Summary
This video examines why Claude's default memory system fails to reliably recall past decisions, using Anthropic's own Pokémon memory experiment as evidence that quality beats quantity in memory design. The creator walks through Claude's built-in memory architecture (auto memory, project memory, dreaming), identifies the core gap — decisions made in conversation that Claude never chose to save — and presents a custom memory system built into their "Agentic OS" that solves it via semantic search and automatic session logging. The video is most relevant to product managers, solo founders, and developers who run Claude on complex, multi-month projects with multiple clients and need reliable recall of past decisions.

## Key insights
- In Anthropic's Pokémon test, the model with 9 memory files earned 4 badges; the model with 400+ files earned only 1 — fewer, better-targeted notes outperform bulk archiving.
- Claude's built-in memory in Claude Code loads only the first 200 lines or 25 KB of `memory.md` per session; anything beyond that is invisible unless Claude actively retrieves it.
- Claude transcripts are wiped every 30 days, so decisions made in conversation that weren't saved to memory are permanently lost within a month.
- Keyword search is the core recall failure mode: asking "what did we land on for the community plan?" won't match a transcript that says "third pricing tier at $37" because the words don't overlap.
- **Dreaming** (currently in research preview, API-only for managed agents) reads up to 100 past sessions plus current memory, merges duplicates, removes contradicted or outdated notes, and adds new learnings — without touching the original. It improved recall from notes alone from 13% to 48% over 128 sessions in testing.
- A wrong note is worse than no note: in the Pokémon test, one incorrect note about Mount Moon caused Claude to make the same mistake three times before dreaming corrected it.
- The creator found a hidden `auto dream` toggle in `/memory` in Claude Code labeled "off/never" — expected to become a standard feature soon.
- Claude code now saves four structured memory types: user identity, feedback given, project context, and references to where things live — skipping anything derivable from files.
- The custom Agentic OS system uses a hook to save every single conversation turn to a long-term store automatically, bypassing Claude's judgment about what's "worth" saving.
- The system uses PGLite with pgvector running locally for semantic + keyword search, re-ranks results, and returns answers with file, line number, and date citations.
- When nothing is found, the system explicitly says so — building trust by distinguishing "not found" from "made something up."
- The system retroactively ingests existing session history on install, so users don't start from zero on day one.

## Use cases
- **Multi-client agencies or freelancers** who make decisions across different projects over months and can't afford to re-litigate old choices.
- **Solo founders or PMs** tracking evolving product decisions (pricing tiers, feature scoping, positioning) across dozens of sessions.
- **Developer teams using Claude Code** daily who need continuity between threads without manually re-summarizing prior decisions.
- **Anyone running agentic workflows** where a stale or wrong memory note will cause repeated downstream errors.
- **Consultants or researchers** who need citable, dated recall of when and where a decision was made.
- **Power users frustrated by Claude hallucinating decisions** it was never actually told — the "found nothing" response is as valuable as a correct answer.

## Patterns & frameworks

**Storage / Injection / Recall triad**
Every memory system answers three questions: what gets stored, what gets loaded automatically at session start, and how the system finds things that weren't pre-loaded. Used as a diagnostic lens to evaluate any memory architecture.

**Quality-over-quantity memory principle**
Drawn from Anthropic's Pokémon experiment: a small number of accurate, well-chosen notes beats a large archive. Applies to both what Claude saves and how the index is curated.

**Dreaming (Anthropic research preview)**
A cleanup process that reads past sessions + current memory, merges duplicates, removes outdated notes, and writes a fresh version without touching the original. Acts as a periodic "garbage collection" for memory. Currently API-only for managed agents.

**Three-system synthesis (Hermes + G-brain + Mem)**
The creator reverse-engineered three leading memory systems and extracted one strength from each:
- *Hermes*: inject a small capped snapshot of recent decisions at session start
- *Gary Tan's G-brain*: return answers with citations, and explicitly say when nothing was found
- *Mem*: search by meaning (semantic), not just keywords

**Snapshot + long-term store architecture**
The Agentic OS combines: (1) a hook that saves every turn unconditionally to a long-term store, (2) Claude's judgment to promote key items into a capped 2,000-character snapshot loaded at session start, and (3) semantic + keyword search with re-ranking for deep recall. Separates "save everything" from "curate what's surfaced" — resolving the tension between Anthropic's findings and rule-based filtering.

**Tiered adoption recommendation**
The video closes with a progression model for when to add complexity:
1. Tidy `CLAUDE.md` + periodic dreaming = enough for most users
2. Add semantic search only when working across clients over months and keyword search starts failing