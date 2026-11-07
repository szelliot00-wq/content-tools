# The Components of Agent Memory

Source: https://www.anthropic.com/research/components-of-agent-memory

## Summary
This Anthropic engineering article explores how AI agents can store and manage memory across sessions, drawing parallels to human memory consolidation during sleep. The core concept is "dreaming" — a process where agents use idle time to review session transcripts and reorganize their memory notes into more accurate and useful representations. The article presents benchmark results across Claude model generations showing how memory architecture and dreaming improve long-horizon task performance.

## Key takeaways
- **Agent memory is distinct from training or in-context learning** — it refers to knowledge persisted between sessions in external stores like folders of notes or wikis.
- **"Dreaming" (offline reflection on transcripts) corrects stale or incorrect memory** — demonstrated concretely when Claude fixed a wrong map note in Pokémon and successfully navigated Mt. Moon on the corrected run.
- **Salience judgment matters more than quantity** — Fable 5 wrote 10 memory files and earned 4 Pokémon badges; Sonnet 3.7 wrote 413 files and earned 1, spending more time managing memory than playing.
- **Stronger models need less steering** — Opus 5 and Sonnet 5.5 formed learning loops autonomously; older models like Sonnet 4.6 needed explicit prompts to even read their memory files before answering.
- **Specific memory rules can backfire** — telling models to "record only failures" reduced memory gains for Opus 5 and Opus 4.7; general guidance outperformed rigid rules for frontier models.
- **Wikis built through dreaming improve performance on multi-document tasks** — on merger questions requiring cross-document synthesis, wiki + search scored 87% vs. 73% for search alone; but wikis showed no gain on tasks answerable from a single document.
- **The injected context layer must stay small** — only the highest-value memories should be preloaded into every session, with the rest indexed and retrieved on demand to avoid token waste and instruction-following degradation.