# What Is Loop Engineering? Building Better AI Agents

Video ID: `DQBqh6gcx7U`

## Summary
The video introduces "loop engineering" as the practice of designing automated systems that repeatedly prompt AI agents, check their work, and iterate toward a goal — contrasting it with manual prompt engineering. It walks through the core loop stages (goal → action → observe → adjust), then covers the infrastructure built around that loop: triggers, context management, persistent state (the "spine"), tool access, and sub-agents. The video closes by arguing that despite automation, meaningful human involvement remains essential to avoid compounding technical and organizational debt.

## Key insights
- **Loop engineering vs. prompt engineering**: Prompt engineering is manual, one-shot prompting; loop engineering designs the system that handles prompting automatically, cycling until a goal is met.
- **The four loop stages**: Goal → Action → Observe → Adjust. Each iteration checks whether the goal is met and continues or terminates accordingly.
- **Goals must be verifiable**: Vague goals like "make checkout faster" have no stopping condition; a good goal is specific and testable, e.g. "stop when all unit tests pass."
- **Triggers start the loop**: Loops can be initiated by a schedule (e.g. a cron job) or an event-driven hook (e.g. a pull request opening or a file change).
- **Context management is non-trivial**: Each loop iteration generates context (test output, file contents) that can pile up and dilute agent focus — compaction and skill-based progressive disclosure help manage this.
- **The spine is persistent state**: A record (e.g. markdown files) of what the agent tried and whether it worked, informing future iterations rather than starting blind each time.
- **Sub-agents act as checkers**: A second agent with its own context and possibly a different underlying model verifies the primary agent's output, acting as a coworker rather than just the same agent self-reviewing.
- **Comprehension debt**: As agents write more code and humans review less of it, the gap between what exists and what humans understand grows — this is a silent, compounding risk.
- **Intent debt**: Agents can read *what* a system does but not *why*, so without documented intent (e.g. an `agent.md` file), an agent may make technically correct but strategically harmful changes.
- **Cognitive surrender**: Blindly accepting agent output without review is the most dangerous failure mode — it accelerates both comprehension debt and intent debt simultaneously.
- **The right amount of human involvement**: Humans should write the goal with a stopping condition, document the project's intent where the agent can see it, and actually read the agent's output — minimal, but irreplaceable.