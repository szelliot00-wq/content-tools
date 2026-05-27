# The Four Types of Memory Every AI Agent Needs

Video ID: `BacJ6sEhqMo`

## Summary
The video introduces the CoALA framework (Cognitive Architectures for Language Agents) from Princeton, which maps four types of memory that well-designed AI agents need. Drawing an analogy to human memory, the presenter explains how each memory type serves a distinct role in making agents more capable than simple chatbots. The video also covers which memory types are appropriate for different agent complexity levels.

## Key insights
- **Working memory** is the context window — fast and immediately accessible but volatile and size-limited. Performance degrades when too much is stuffed in, especially content buried in the middle.
- **Semantic memory** is the agent's persistent knowledge base (facts, rules, conventions). In practice this is often just Markdown files (e.g., `CLAUDE.md`) loaded at session start, not necessarily complex vector databases.
- **Procedural memory** defines *how* to do things via agent skills (`skill.md` files). Skills use progressive disclosure — the agent loads only a lightweight index upfront, then pulls full instructions only when a matching task arises.
- **Episodic memory** is distilled experience from past sessions. Production systems don't just store raw transcripts — they accumulate compressed, useful notes (e.g., "last time we debugged auth, the issue was in the middleware layer").
- **Not every agent needs all four.** A simple reflex agent only needs working memory; a narrow support agent adds procedural; a full coding agent benefits from all four.
- **Forgetting is an unsolved engineering problem** for episodic memory — deciding what to delete, when information becomes stale, and how to handle context like job changes is genuinely hard.
- The key distinction between a chatbot and an agent is persistent memory: an agent's responses are shaped by accumulated knowledge, experience, and learned mistakes.