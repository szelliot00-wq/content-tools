# 5 Best Practices for Building AI Agent Skills

Video ID: `qYNs80FKIVc`

## Summary
This video covers five best practices for building AI agent skills — structured markdown files that teach agents how to perform specific tasks in your particular way. The hosts walk through common mistakes and concrete fixes, from writing effective trigger descriptions to hardening fragile steps with deterministic scripts. They also warn about security risks when using skills built by others.

## Key insights
- **The description is the trigger.** Agents load only skill names and descriptions at startup to avoid filling their context window, so descriptions must clearly state what the skill does *and* when to use it. Models tend to under-trigger, so lean toward slightly overselling the description.
- **Build from real expertise, not LLM-generated content.** A skill's value comes from your specific way of doing a job — things the model can't know on its own. Walk through the task by hand, capture what actually worked, and especially document "gotchas" (environment-specific surprises that defy reasonable assumptions).
- **Spend context wisely.** Once a skill is selected, its full body competes for space in the context window. Keep skill bodies under ~500 lines / 5,000 tokens. Move supplementary detail into a `references/` subdirectory that the agent only reads when needed (progressive disclosure).
- **Use deterministic scripts for fragile steps.** Anything that must be exactly right every time should be a script in a `scripts/` directory rather than natural-language instructions the model improvises from. Scripts aren't loaded into context (saving tokens) and don't guess — eliminating a whole class of inconsistency bugs.
- **Vet skills before running them.** Skills can execute code that accesses your filesystem and API keys. A 2025 audit of ~4,000 public skills found over 35% had security flaws and 13% had critical issues like prompt injection or malware. Treat a third-party skill like any other dependency: read it before you run it.