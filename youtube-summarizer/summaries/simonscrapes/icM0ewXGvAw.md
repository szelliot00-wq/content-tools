# 19 Claude Code Mistakes "Pro" Users Are Still Making

Video ID: `icM0ewXGvAw`

## Summary
This video covers 19 common mistakes that even experienced Claude Code users make, many of which stem from outdated advice that has been invalidated by recent model and platform updates. The core argument is that the rules for effective Claude use have been substantially rewritten in the last six months, and most users are still operating on stale mental models. The presenter walks through prompt construction, tool/connector configuration, context window management, caching behavior, verification strategies, and hidden CLI commands. It is most relevant to power users, developers, and professionals who use Claude Code regularly and want to reduce costs, improve output quality, and avoid common efficiency traps.

## Key insights
- **Personas don't work:** A study of 162 personas across 2,500 prompts found no performance improvement from adding role/persona lines (e.g., "You are a senior copywriter with 20 years of experience"). Anthropic's own team cut their system prompt by ~80% and no longer recommends stuffing it with examples.
- **Replace persona lines with three specific elements:** (1) where to look for context, (2) a "definition of done" describing what finished output looks like, and (3) a self-check instruction using phrasing like "before you finish, verify your answer against…"
- **Avoid "do not" instructions:** Negative instructions (e.g., "do not return as markdown") confuse the model when they conflict with the task. Replace them with positive directives (e.g., "write as smooth flowing text paragraphs").
- **Routines run with full tool access by default:** This is both a security risk and a cost issue. You can remove connector access per routine in the desktop app, both when setting up new routines and retroactively on existing ones.
- **Tool definitions load into context by default:** With "tool access" set to auto, all connector schemas load upfront on every message, costing some users thousands of tokens per session. Fix: switch to "load tools when needed" via Chat Mode > Connectors > Tool Access.
- **MCP server advice has changed:** Previous advice to remove infrequently used MCP servers is now outdated. Tool Search is on by default, meaning only tool names (~120 tokens) load at session start; full schemas are pulled on demand. Use `/context` to verify costs, and `/mcp` to see what's loaded on demand.
- **Skills don't transfer between Claude Code and Claude Co-work:** Skills built in the terminal live under `.claude/skills/` and are accessible in Claude Code but not Co-work. For Co-work, you must re-add them as a zip file or recreate them in the customize window. Also, skills added mid-session in Co-work require a restart to take effect.
- **Sub-agents cost ~7x more tokens than standard sessions:** Each sub-agent maintains its own context window (uncached), runs as a separate Claude instance, and doesn't inherit conversation history, output style, auto-memory, or already-read files. Sub-agents are best for broad searches and parallel investigation; keep high-context specific tasks in the main session.
- **Fast mode caveats:** Fast mode runs on Opus at 2.5x speed but requires API usage credits (not subscription). It stays on by default across sessions until you type "fast off." Critically, enabling fast mode mid-conversation uncaches all existing cached context, meaning you pay the full uncached input price for the entire prior conversation.
- **Don't edit CLAUDE.md mid-session:** The file is read once at session start and held in memory. Changes made during an active session are ignored until you compact, clear, or restart the session.
- **CLAUDE.md length directly degrades performance:** Anthropic has tested and confirmed that if Claude keeps violating a rule, the file is probably too long. Best-performing instruction files are ~300–350 words. Capitalizing rules or marking them "IMPORTANT" is not the fix — shortening the file is. Claude Code's own system prompt has ~50 instructions; models reliably follow 150–200 instructions. Run `/doctor` and ask it to "propose trims to my CLAUDE.md that won't impact performance" to get specific cut suggestions.
- **Sub-agents receive less context than most people assume:** They get their own system prompt, the task you gave them, and the CLAUDE.md hierarchy — but not conversation history, output style, auto-memory, or already-read files. Built-in explore and plan agents skip CLAUDE.md entirely. Critical constraints must be restated directly in the sub-agent's prompt.
- **Autocompact behavior has changed:** It no longer triggers at 95% of context. Without a custom setting, it compacts when the conversation hits the model's context limit. You can now set a fixed token threshold (e.g., `autocompact 100k`) instead of a percentage.
- **Large context windows reduce retrieval accuracy:** Anthropic's own benchmark on Opus 4.6 showed 93% retrieval accuracy at 256k tokens, dropping to 76% at 1 million tokens — roughly a 1-in-4 failure rate. A larger context window is not equivalent to more usable memory.
- **Compaction is not all-or-nothing:** Pressing Escape twice enters rewind mode, letting you jump to a prior point in the conversation. From there you can "summarize up to here," selectively compacting only the earlier portion while keeping later context intact.
- **Control+G opens the plan in VS Code for direct editing:** In plan mode, hitting Control+G opens the plan in the browser/VS Code for direct editing, avoiding the token cost of asking Claude to revise it via chat.
- **Switching to a cheaper model mid-conversation can cost more:** If you're 100k tokens into a conversation with Opus and switch to Haiku, you pay to rebuild the prompt cache for Haiku. Switching back to Opus rebuilds it again. Each model has its own cache; switching always means paying uncached input prices.
- **Verification is the single highest-impact practice:** Anthropic's own power user guide calls it the most impactful tip. Four escalating levels: (1) ask for the check in the same prompt, (2) `forwardgoal` re-evaluating after every turn, (3) stop hooks that block turn completion until a script passes, (4) adversarial review agents. Adversarial agents must be constrained to flag only correctness/requirement issues, or they will keep finding problems indefinitely.
- **Conversation history only persists 30 days by default:** Older sessions are wiped. To extend retention, add `"cleanupPeriodDays": 365` to `settings.json`. Setting it to 0 does not mean unlimited — it wipes everything on arrival. Auto-memory files are exempt from this sweep.
- **Five underused CLI commands:** `/doctor` (full setup health check — finds unused skills/MCPs/plugins, dedupes CLAUDE.md, shows context costs), `/insights` (generates an HTML report analyzing up to 200 recent sessions), `/btw` (asks a side question without interrupting the main conversation), Escape to close `/btw` while it's still running, and `/branch` (copies the current conversation at a point so you can take it in a new direction without losing the original).

## Use cases
- **Prompt writers and marketers** who have been adding persona lines to every prompt and want to reclaim those tokens for genuinely useful instructions.
- **Developers running Claude Code routines** who want to reduce security surface area and unnecessary token costs from auto-loaded connectors.
- **Heavy MCP server users** who were trimming their MCP list based on old advice and can now add servers freely.
- **Users working across both Claude Code (terminal/VS Code) and Claude Co-work (desktop app)** who need to understand that skills don't transfer automatically.
- **Anyone delegating tasks to sub-agents** who needs to understand exactly what context those agents receive (and don't receive).
- **Users experimenting with fast mode** who risk unknowingly incurring large costs from cache invalidation mid-conversation.
- **Users with long or frequently violated CLAUDE.md files** who want to diagnose why Claude ignores certain rules.
- **Developers managing large codebases** who need to understand context window retrieval degradation before relying on 1M+ token windows.
- **Power users who want self-correcting workflows** and need to implement verification loops rather than acting as the human error-checker themselves.
- **Anyone who has lost conversation history** and wants to configure longer retention in `settings.json`.
- **Users in plan mode** who want to directly edit generated plans without burning tokens on back-and-forth revision requests.
- **Cost-conscious users** switching models mid-session who need to understand the cache rebuilding cost before doing so.

## Patterns & frameworks

**Three-element prompt structure (replaces persona lines)**
A prompt construction pattern from Anthropic's own guidance. Instead of role/persona openers, use: (1) *Where to look* — direct Claude to specific files or context sources; (2) *Definition of done* — describe what finished output looks like; (3) *Self-check* — "before you finish, verify your answer against [criteria]." Same word count as a persona prompt, but every word is acted upon.

**Positive instruction framing**
Replace "do not do X" with "do Y instead." Negative constraints conflict with task instructions and confuse the model. The pattern is: identify the undesired behavior → describe the desired behavior directly → remove the negative framing entirely.

**Context cost triage (tools/connectors)**
A two-part configuration pattern: (1) for connectors, switch from "tools always loaded" to "load tools when needed"; (2) for routines, audit and remove connector access that isn't required. Use `/context` to measure actual token costs per MCP server.

**Sub-agent use heuristic**
Sub-agents are cost-effective for *looking* (broad searches, parallel read-only investigation) and expensive for *doing* (tasks requiring high context). For high-context work, keep it in the main session or fork the conversation instead of delegating to a sub-agent.

**Four-level verification ladder**
An escalating framework for building self-correcting Claude workflows:
1. **Inline check** — ask for verification in the same prompt
2. **Forward/goal** — a separate evaluator rechecks a condition after every turn
3. **Stop hooks** — scripts that physically block a turn from completing until a condition passes
4. **Adversarial review agent** — a separate agent tasked with finding gaps; must be scoped to correctness/requirements only, or it loops indefinitely

**Constrained adversarial reviewer**
A pattern for adversarial agents: instruct the reviewer to flag only issues that affect correctness or stated requirements, and treat everything else as optional. Without this constraint, the agent will manufacture problems to satisfy its mandate.

**Selective compaction via rewind mode**
Instead of all-or-nothing context compaction, press Escape twice to enter rewind mode, navigate to a prior conversation point, and choose "summarize up to here." This lets you compact only the early portion of a conversation while preserving later context in full.

**CLAUDE.md length-as-performance diagnostic**
A diagnostic heuristic: if Claude repeatedly violates a rule despite it being in CLAUDE.md, the file is too long — not the rule too weak. Fix by shortening the file. Target: under 300–350 words. Use `/doctor` + "propose trims" to get specific suggestions automatically.

**Cache-aware model switching rule**
Never switch models mid-conversation when you have a large cached context, because switching invalidates the cache for both models. The rule: if the context is large and cached, cheaper is actually more expensive. Stay on the current model unless starting a fresh session.