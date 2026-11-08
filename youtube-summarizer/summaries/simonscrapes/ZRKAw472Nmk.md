# Claude Pros Don’t Pay for Max. They Do These 5 Things Instead.

Video ID: `ZRKAw472Nmk`

## Summary
This video targets Claude Code users on Pro/Max plans who are hitting usage limits, arguing that optimization habits — not upgrading plans — are the real solution. The creator walks through six concrete practices centered on context management, caching behavior, and token hygiene. The core insight is that most limit exhaustion comes from inefficient context reuse: stale caches, bloated CLAUDE.md files, unnecessary sub-agents, and habits like returning to old chats. It is most relevant to developers and power users who rely on Claude Code daily for multi-session, long-running tasks.

## Key insights
- `/compact` is expensive on old conversations: it forces Claude to re-read the entire chat after cache expiry. One Pro user burned 11% of their 5-hour limit just running `/compact` without doing any actual work.
- `/clear` costs nothing but loses all context — the goal is a middle path between the two.
- Anthropic's own long-running agents use a `claude_progress.txt` + GitHub commit pattern between sessions, which is the model for the "handoff.md" approach.
- Prompt cache lasts ~1 hour on a subscription. Returning to a chat after more than an hour means the first new message re-reads the entire conversation at full token cost — one Reddit user calculated this as 5x more token usage for a single restart.
- Switching models or changing effort level (e.g., from Max to Normal) mid-session also invalidates the cache, compounding the cost.
- Pre-loaded context (CLAUDE.md, skills, plugins, memory files) is paid for on every single message before you type a word. Keeping CLAUDE.md under 200 lines is a specific recommendation.
- MCP tool schemas are no longer a problem — they only load when Claude actually needs them, unlike before.
- Sub-agents share the same usage limit. Custom always-on sub-agents add context overhead; it's better to let Claude decide when to spin one up.
- Sub-agent prompt cache TTL defaults to 5 minutes. For long-running sub-agent jobs, setting the environment variable `SUBAGENT_PROMPT_CACHE_TTL` to 1 hour prevents repeated cache misses.
- `/usage` command shows a breakdown of which skills, sub-agents, plugins, and MCP servers are consuming your limit. Pressing `W` shows the full week. Pressing `F` lets Claude auto-fix identified issues.
- The `/usage` output specifically flags items consuming >10% of usage with tailored recommendations (e.g., "trim your CLAUDE.md — 49,000 tokens used per request").
- `/loop` and scheduled tasks each start a new turn, re-sending the full chat each time they fire — `/usage` gives each loop its own row so you can measure and optimize it.
- Claude Projects (new desktop view) handles much of this automatically: each job gets its own thread, and the main conversation acts as an orchestrator pulling from project memory rather than full history.

## Use cases
- Developers hitting the 5-hour Pro limit and considering upgrading to Max
- Anyone running multi-day projects in Claude Code who habitually returns to old chats the next morning
- Teams using `/loop`, scheduled tasks, or slash goals that fire repeatedly within long sessions
- Users who have accumulated many installed plugins or skills they no longer actively use
- Developers running long test suites or log analysis via sub-agents
- Anyone whose CLAUDE.md has grown organically over time and now contains finished-project notes or old context
- Power users who switch models or effort levels mid-task without realizing the cache cost
- People debugging why their limits seem to have shrunk without Anthropic changing anything

## Patterns & frameworks

**Handoff Document Pattern**
Write a `handoff.md` before ending a session. It should contain: the goal, what's been completed, what comes next, files touched, decisions made, and what didn't work. Then run `/clear` and start the next session by pointing Claude at the handoff file. Mirrors Anthropic's own internal agent pattern (`claude_progress.txt` + GitHub commit per session).

**Save Context to Files, Not Chat History**
Any information you'd return to a chat to retrieve (e.g., agreed pricing tiers, architectural decisions) should be saved to a named `.md` file at the end of the session. The next session opens fresh and reads only that file — avoiding re-sending the entire prior conversation.

**Pre-Session Context Audit**
Before starting work, run `/context` to see exactly what is pre-loaded. Trim CLAUDE.md to under 200 lines, uninstall forgotten plugins, and move workflows into skills. Ensures you're not paying for dead weight on every message.

**Cache-Aware Session Management**
Treat the 1-hour cache window as a hard boundary. Either finish a task step before stepping away, or write the handoff doc and close the chat. Never "continue" a chat that's been idle for more than an hour without first considering the re-read cost.

**Minimal Sub-Agent Output Contract**
When delegating to a sub-agent, explicitly constrain what it reports back (e.g., "run the test suite and return only failing tests with error messages"). This keeps the main orchestrator context small while the expensive work stays contained in the sub-agent.

**Usage-Driven Optimization Loop**
Use `/usage` regularly to identify the actual cost drivers rather than guessing. The tool surfaces specific, actionable recommendations and shows cache miss counts — turning optimization from intuition into measurement.