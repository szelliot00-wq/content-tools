# Context Engineering for AI Agents: 4 Failure Modes to Avoid

Video ID: `BwXremQ-i6I`

## Summary
The video explains "context rot" — the phenomenon where AI agents become less reliable as their context window fills up — and introduces the concept of context engineering as the practice of deliberately managing what enters the context window. It identifies four specific failure modes that degrade agent performance in long-running tasks, then proposes a targeted fix for each, with the counterintuitive common thread that agents improve by holding *less* information, not more.

## Key insights
- **Context rot is universal:** A study of 18 frontier models found all of them degraded in reliability as context window size increased — bigger windows don't automatically mean better performance.
- **Attention is the real constraint:** A model doesn't "look up" context like a database; every token competes for a finite attention budget, so more tokens means each one gets less reliable attention.
- **Failure mode 1 — Context poisoning:** A wrong conclusion written into the context gets treated as ground truth, silently corrupting all subsequent reasoning. Fix: **validate** conclusions against real data before committing them to context.
- **Failure mode 2 — Context distraction:** A long history of past actions becomes a stronger pattern than the model's training, causing the agent to repeat prior actions rather than reason about what the task actually needs next. Fix: **compact** — summarize the history and discard the full log; better yet, offload detailed state to persistent files pulled in only when needed.
- **Failure mode 3 — Context confusion:** Too many tool definitions in the window make the model worse at choosing the right tool (demonstrated by a benchmark where cutting from 46 to 19 tools turned a failure into a pass). Fix: **curate** — load only the tools the specific task requires.
- **Failure mode 4 — Context clash:** Contradictory information coexisting in the window (e.g., an original wrong note and a later correction) forces the model to resolve conflicts instead of acting. Fix: **prune** — delete superseded information, or start a fresh context window restating only the current correct state.
- **The unifying principle:** All four fixes involve deliberately discarding information. An agent handles long tasks better by keeping its context lean, not exhaustive.