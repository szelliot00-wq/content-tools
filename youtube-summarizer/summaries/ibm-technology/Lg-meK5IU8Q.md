# What AI Agent Skills Are and How They Work

Video ID: `Lg-meK5IU8Q`

## Summary
This video explains what AI agent skills are, why they were created, and how they work technically. Skills are designed to give AI agents **procedural knowledge** — step-by-step workflows for specific tasks — which LLMs inherently lack despite their broad factual knowledge. The video covers the structure of a skill file, how agents load and trigger skills efficiently, how skills compare to other AI knowledge methods, and important security considerations.

## Key insights
- **Skills solve the procedural knowledge gap:** LLMs know many facts but don't inherently know *how* to perform specific, multi-step workflows (e.g., a 47-step financial report process). Skills inject that "how-to" knowledge.
- **A skill is simply a `skill.md` markdown file** stored in a folder, with a YAML front matter containing at minimum a `name` and `description`, followed by plain-text step-by-step instructions in the body.
- **The description field acts as a trigger condition:** It tells the agent *when* to apply the skill. A well-written description is critical because the LLM uses its own reasoning to match tasks to relevant skills.
- **Optional folders extend a skill's capabilities:** A skill folder can include `scripts/` (executable JS, Python, or Bash), `references/` (additional documentation), and `assets/` (templates, data files).
- **Progressive disclosure keeps skills efficient** across three tiers: (1) only metadata (name + description) loads at startup, (2) full instructions load when a match is found, and (3) resources load only when actually needed — preventing context window overload even with hundreds of skills.
- **Skills complement other AI knowledge methods**, not replace them: MCP provides tool/API access, RAG handles factual lookups, and fine-tuning bakes knowledge into model weights. Skills uniquely handle *procedural* knowledge.
- **Skills map to human procedural memory** from cognitive science — paralleling how human memory includes semantic (facts), episodic (experiences), and procedural (how-to) types.
- **It's an open standard:** The `skill.md` format is published at `agentskills.io` under an Apache 2.0 license and is adopted by major platforms like Claude Code and OpenAI Codex, making skills portable across platforms.
- **Security is a real concern:** Skills can include scripts with access to file systems, environment variables, and API keys. Known risks include prompt injection, tool poisoning, and hidden malware — so skills should be reviewed carefully before use, just like any software dependency.