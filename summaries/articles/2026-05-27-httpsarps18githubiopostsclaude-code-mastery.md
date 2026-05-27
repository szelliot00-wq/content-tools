# Claude Code as a Daily Driver: Claude.md, Skills, Subagents, Plugins, and MCPs

Source: https://arps18.github.io/posts/claude-code-mastery/

## Summary
This article by Arpan Patel is a comprehensive guide to using Claude Code as a power user rather than a casual one. It covers the full configuration system (`.claude/` directory, `CLAUDE.md`, skills, subagents, plugins, and MCPs), drawing heavily on practices from Boris Cherny and the Anthropic team. The core thesis is that the real productivity gains come not from better prompts, but from investing in setup, configuration, and tooling that compounds over time.

## Key takeaways
- **Give Claude a way to verify its own work** — this alone yields a 2-3x quality improvement; without it, you are the only feedback loop
- **`CLAUDE.md` is compounding infrastructure** — keep it short, and whenever Claude makes a mistake, append a rule with "Update CLAUDE.md so you do not repeat this"; the file becomes a curated list of every project gotcha
- **`CLAUDE.local.md`** is gitignored and personal — use it to capture recurring PR review feedback so Claude applies those rules automatically next session
- **Skills** (`~/.claude/skills/<name>/SKILL.md`) are the unit of reusable expertise; if you prompt the same instructions twice, write a skill instead
- **Subagents** (`.claude/agents/*.md`) run in their own context windows with scoped tool permissions — use them to keep your main session clean and to chain writer/reviewer patterns
- **Plugins** bundle skills, hooks, subagents, and MCPs into installable units; the language server plugin is consistently called the highest-impact single install
- **MCPs** make Claude system-aware — key ones include GitHub, Context7 (live library docs), Sentry, Linear, Playwright, Figma, and Postgres; resist installing too many as bloated tool lists hurt decision quality
- **Parallel sessions** (3-5 worktrees, each with its own Claude) is described as the single biggest productivity unlock most users underestimate
- **`/goal`** sets a verifiable completion condition (e.g., "all tests pass") and Claude keeps iterating until it's true — pair with auto mode and `/schedule` to walk away and return to a finished PR
- **`/rewind`** creates per-prompt checkpoints; when Claude goes wrong, rewind and re-prompt instead of polluting context with "that didn't work"
- **Reference, don't describe** — use `@src/auth/login.py` instead of describing files, and pipe errors directly (`cat error.log | claude`)
- **Treat Claude like a delegate, not a pair programmer** — write a crisp brief upfront, then let it run