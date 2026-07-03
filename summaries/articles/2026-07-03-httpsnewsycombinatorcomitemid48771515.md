# Ask HN: Is anyone experimenting with different ways of using LLMs for coding?

Source: https://news.ycombinator.com/item?id=48771515

## Summary
A Hacker News thread where a developer expresses frustration with the stop-start nature of current LLM coding tools (Claude Code, Codex), noting they disrupt flow state rather than enabling it. Commenters share varying perspectives on orchestration, context management, and alternative interaction models. The discussion surfaces skepticism about agent orchestration hype alongside practical advice on prompt design and tooling philosophy.

## Key takeaways
- The prompt-response loop breaks flow state; the original poster believes a "tab model" (continuous, inline completion) is a more promising direction than discrete prompting.
- One commenter (Jimmc414) argues against heavy orchestration scaffolding — trust the model, write cleaner specs (intent, I/O contracts, constraints, preconditions), and let it self-verify against clear exit criteria.
- "Context rot" is a real concern: storing too much in memory dilutes intent; prefer lazy-loading context (e.g., markdown files the model greps on demand) over always-on memory.
- Skills are undervalued relative to agents — skills expand what the model can do, while agents primarily serve context preservation.
- Agent orchestration frameworks are proliferating but producing few documented success stories; one commenter suspects they mostly burn tokens without proportional gains.
- At least one developer is experimenting with a JSX-based templating language to automate context management and branching for large/complex tasks, finding it reduces time spent on manual context piping.