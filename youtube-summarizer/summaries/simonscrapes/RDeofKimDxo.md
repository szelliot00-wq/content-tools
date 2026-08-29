# 37 Cheat Codes to Level Up In Claude Code in 19 Minutes

Video ID: `RDeofKimDxo`

## Summary
This video walks through 37 practical tips and shortcuts for power-users of Claude Code, covering terminal keyboard shortcuts, token/cost optimization, session management, skill configuration, and desktop app features. The presenter's core argument is that most users are leaving significant efficiency gains on the table by not knowing built-in features that are already available. It is most relevant to developers and content creators who use Claude Code daily and want to reduce costs, speed up workflows, and manage complex multi-session projects more effectively.

## Key insights
- **Simple English skill**: Installs a writing style inspired by Boeing instruction manuals — designed so a tired mechanic cannot misread it. Dramatically reduces response verbosity and reading time.
- **Stop Slop** (16,000 GitHub stars): Scores AI-generated drafts out of 50 across dimensions like rhythm, trust, authenticity, and density. If the score is below 35, it rewrites the content. Designed for newer models that don't need 100 examples to get it right.
- **Caveman** (100,000 GitHub stars): Reduces agent output tokens dramatically — example given is 69 tokens → 19 tokens. Also converts skills into invocable images. Best for cutting costs on high-volume usage.
- **Built-in concise output style**: Available natively via `/config` → output style → concise. Claude leads with results and drops running commentary while keeping full detail on errors/warnings.
- **Control+R**: Searches all prompts from the current session (like Ctrl+F for your prompt history). Control+S widens scope to the full project, then again to every project on the machine — lets you retrieve a prompt written 3 weeks ago in a different repo.
- **Control+T**: Shows a live breakdown of all active subagents and tasks currently running. Also accessible via `/tasks`.
- **Control+S mid-prompt**: Stashes your in-progress prompt so you can run a different command first, then Control+V to paste the original prompt back.
- **Control+G**: Opens your current prompt and Claude's last response in an external editor for easier editing. Requires enabling "show last response in external editor" in `/config`.
- **Option+T**: Toggles extended thinking mode on or off per turn — useful for skipping deep reasoning on simple tasks.
- **Control+O**: Expands all collapsed tool calls into one full, clickable log for complete visibility.
- **/focus**: Strips all logs and shows only the prompt, a result summary, and the direct response.
- **Control+B**: Sends the current running task to the background, outputting to a file Claude can read later, keeping the terminal session free.
- **Rewind vs. Clear**: Using `/clear` erases context but rewind can restore it. For broken outputs (e.g., a bad webpage build), always rewind to the last good point rather than trying to patch the broken output. Rewind does NOT restore files deleted via bash — those require Git.
- **Control+A in resume**: Expands session scope from the current repo to all repos on the machine (20 sessions → 49 in the example). Control+W shows the full worktree history across any terminal window.
- **Large session resume warning**: Sessions older than 1 hour with 100k+ tokens will prompt you to resume from a summary instead of reloading the full history (which is the most expensive single request possible).
- **Session renaming**: Run `rename` to give sessions human-readable names, making it far easier to find and resume the right session later.
- **@ symbol for file targeting**: In multi-window setups, use `@filename` to point Claude at a specific file, ensuring it reads exactly the right one rather than searching.
- **`claude --teleport`**: Imports Claude.ai web sessions into the local Claude Code terminal.
- **CC Usage repo**: Reads local Claude Code logs (plus Codex, Gemini, Goose, etc.) and reports token usage, model breakdown, and costs across time periods.
- **/recap**: Generates a one-line session recap and suggests next actions — useful when returning to an old conversation.
- **Avoid switching models mid-session**: Switching from Opus to Sonnet mid-session rebuilds the cache, costing you the cached tokens. Instead, add "give me a quick answer" to skip deep reasoning for that turn without touching the cache.
- **`clearContextOnPlanAccept: true` in settings.json**: After a plan is accepted, clears the exploratory context (file reads, background thinking) that went into creating the plan, but keeps the plan itself in a separate file. Saves significant tokens.
- **Claude desktop memory system**: Memory is now saved to individual topic-specific files (cooking, work areas, people, etc.) and merged across chats and co-work sessions. Supports importing memory from other AI providers (ChatGPT, Codex, etc.).
- **Path-specific rules in CLAUDE.md**: Assign rules to specific file paths (e.g., `source/api/**`). Those rules only load when Claude encounters files at that path, rather than loading into every session. Rules folder also follows symlinks, so one shared rules directory can be pointed to from multiple repos.
- **HTML comments in CLAUDE.md**: Comments written in HTML comment format (`<!-- -->`) are completely ignored by Claude (zero tokens). Use these for human notes; only use readable headers/text if they're meant to guide Claude.
- **Handoff prompt pattern**: Instead of asking Claude to "summarize progress," ask it to "write the next instructions as a prompt for the next session." The output naturally points at files, lists what didn't work, and starts with actionable instructions — paste directly into a new session.
- **Nesting skills 5 levels deep**: A single prompt can invoke up to 5 skills chained together (e.g., generate UGC script + long-form article + pass through humanizer skill).
- **Skill description structure**: Must include (1) a one-line summary of what the skill does, (2) trigger phrases that activate it, and (3) anti-triggers — phrases that should NOT activate it. Prevents Claude from confusing overlapping skills.
- **Avoid the built-in front-end design skill**: Creates generic-looking output. Instead, use Claude Design to build a proper design system (colors, typography, components, layout rules) first, then generate from that.
- **/permissions mid-session**: Running `/permissions` in the middle of a task immediately overrides the session's permission settings (e.g., switching from manual to auto mode) without requiring a full restart or context reload.
- **Image annotation in desktop app**: You can annotate screenshots with markup (e.g., draw a red circle) and instruct Claude with spatial references like "remove red circle," which it then acts on directly.
- **Memory import**: In desktop app settings, Claude provides a ready-made prompt to extract memory from other tools (another Claude install, ChatGPT, Codex, co-work sessions) and import it into the current memory system.
- **Project-scoped scheduled tasks**: Scheduled tasks can now be created within a specific project context in the desktop app, giving them automatic access to that project's files and settings without manual configuration.

## Use cases
- Developers running long multi-agent sessions who need to manage context costs and token usage
- Teams working across multiple repos who want shared, centralized rule sets
- Content creators using Claude to write and edit, wanting to remove AI-sounding language
- Power users managing many sessions who need fast retrieval of past prompts or sessions
- Anyone building modular skill libraries who needs reliable skill activation
- Developers switching machines who need to migrate memory or session context
- Engineers building websites or UI who want professional, non-generic design output
- Users running automated/background tasks who want project-aware scheduling
- Anyone resuming old sessions who wants cost-effective re-entry into large conversation histories

## Patterns & frameworks

**Token efficiency stack**: A layered approach to reducing token costs — install Caveman or use concise mode for output, use "give me a quick answer" instead of switching models mid-session (to avoid cache rebuilding), enable `clearContextOnPlanAccept`, and use path-specific CLAUDE.md rules to avoid loading all rules in every session.

**Rewind-first error recovery**: When a task produces a broken or incorrect output, the correct pattern is always to rewind to the last known-good state and regenerate — never attempt to patch a broken output forward. Exception: rewind cannot restore bash-deleted files; use Git for those.

**Session handoff prompt pattern** (from Paul's Programming Notes): Rather than asking for a human-readable summary at end of session, ask Claude to write the continuation as a prompt for the next session. A prompt naturally does the right things — it points at files, notes failed approaches, and opens with actionable instructions.

**Skill isolation framework**: Structure each skill description with three elements — (1) a one-line functional summary, (2) explicit trigger phrases, (3) explicit anti-trigger phrases — to ensure skills activate correctly and don't bleed into each other when multiple similar skills exist.

**Path-scoped rules architecture**: Store rules not in a flat CLAUDE.md but in separate files keyed to file paths. Rules load only when Claude encounters relevant files, keeping session context lean. Combine with a top-level symlinked rules directory to share standards across multiple repos without duplication.

**Design-system-first UI generation**: Rather than using the built-in front-end design skill, generate a full design system specification first (colors, typography, component shapes, layout rules) and then use that as the generative foundation. Produces professional, differentiated output instead of generic AI-looking websites.