# Claude Changed Completely - Every NEW Concept Explained

Video ID: `YAuWBqZ_gjs`

## Summary
This video covers 15 significant changes to Claude and AI coding tools (Claude Code, Cursor, Codex) over the past 10 months that most users have missed. The core argument is that Claude's out-of-the-box capabilities have improved so dramatically that many previously essential customizations — detailed skills/prompts, manual model switching, plan mode — are now counterproductive or unnecessary. It is most relevant to power users, AI workflow builders, and product/ops teams using Claude Code or similar agentic AI tools to automate work.

## Key insights
- **Skills/prompts are mostly bloated:** 7 of 9 popular Claude skill packs tested no better than a dummy file of equal length. Skills should now only contain corrections to what Claude gets wrong, not full SOPs.
- **Anthropic's own advice:** Try every job without a skill first. Write down only what Claude gets wrong, and add only that back into the skill.
- **The Skill Eval plugin** runs your job side-by-side with and without a skill so you can see which instructions are redundant.
- **Model switching destroys cache:** Each model keeps its own cache. Switching from Opus → Haiku mid-session forces a full re-read of conversation history at full price on both models — potentially an order of magnitude more expensive than staying on one model.
- **Cheaper models can be more expensive per job:** Haiku 5.5 required more requests than larger models and took nearly twice as long as Sonnet on long sessions, negating its per-token cost advantage.
- **Anthropic recommends starting on Opus 5.5** for most work and reducing effort level rather than switching to a smaller model for easy questions. You can also just tell Claude "give me a quick answer" and it will skip deep reasoning.
- **The Advisor setting** (largely unknown) lets a cheaper model do main work while a stronger model (Opus or Fable) is consulted only when needed — and switching via `/advisor opus` does NOT break the cache.
- **Plan mode is being deprecated** by its own creators. Boris Cherny (creator of Claude Code) and TK (Claude Code team) both said the models no longer need it. TK proposed replacing it with Shift+Tab effort controls.
- **The planning concept still matters** — but as a written file, not a mode. For large/unclear jobs, have Claude interview you, write a plan to a file, then start fresh to build it.
- **/goal command caveat:** The checker model only reads the conversation — it doesn't open files or run code. Goals must produce deterministic proof visible in the chat (e.g., "show me the test output"), not vague conditions like "the report is finished."
- **Context window size hurts recall:** On Anthropic's own Opus 4.6 test, finding 8 hidden details scored 93% at 250K tokens but only 76% at 1M tokens. Bigger context = more room to lose details.
- **Projects changed in September:** Now a single long orchestrator conversation that spins up full Claude Code sessions as threads underneath. Threads keep running after you close your laptop, but default to Opus on high effort — check and adjust in project settings.
- **Sub-agents vs. forks:** Sub-agents start fresh (no conversation history, no cache share). Forks copy the full conversation and share the cache, making the first turn cheaper. Fork mode has been on by default since August.
- **Ultra Code / dynamic workflows** can spin up dozens of agents in parallel, cross-check findings, and return a single result. Deep research is the primary example. Recommend setting dynamic workflow size to "small" (fewer than 5 agents) in `/config` to prevent runaway token usage.
- **Hooks are now prompt- or agent-based**, not just scripts. A stop hook can trigger a second model to read your brand voice doc and the latest output, then either allow Claude to stop or send a correction back as the next instruction — turning nondeterministic behavior into a guarantee.
- **Routines can now be event-triggered**, not just time-scheduled — any tool that sends a web request (e.g., a new GitHub PR) can start a cloud agent. OpenAI is moving the same direction with MCP events announced at their late-September dev day.
- **Cloud sessions** let any Claude Code task run on a remote machine at no extra charge. Start from claude.ai/code, the desktop app, or `claude --cloud`. Use `claude --teleport` to pull the session back to your laptop.
- **Usage limit pausing:** Claude now waits when it hits a usage limit mid-task and resumes automatically when the limit resets, completing the job — but this consumes the next token window without asking.

## Use cases
- **Content/copywriting workflows:** Trim over-specified writing skills down to only genuine corrections; let Claude handle style defaults natively.
- **Recurring weekly jobs:** Record a skill via the desktop app's watch mode instead of writing one manually; it auto-captures only the corrections.
- **Long agentic sessions:** Stay on one model start-to-finish to preserve cache and avoid re-ingestion costs.
- **Technical teams doing code review:** Use event-triggered routines tied to GitHub PR creation to auto-run agents without manual scheduling.
- **Research tasks requiring many sources:** Use `/deep-research` or Ultra Code dynamic workflows for multi-angle, cross-checked research.
- **Quality control on outputs:** Attach a stop hook that reads brand/style guidelines and blocks Claude from finishing until the output passes.
- **Running jobs unattended:** Use cloud sessions for tasks that need to run while your laptop is off; use routines for recurring or event-driven automation.
- **Non-technical users planning builds:** Use Claude to interview you and write a plan file before building, rather than using plan mode as a blocking gate.
- **API/token cost optimization:** Use the Advisor setting to get Opus-level reasoning only on hard sub-problems, without cache-busting the session.

## Patterns & frameworks

**Skill as corrections list (not SOP)**
Old approach: write a detailed step-by-step manual for Claude. New approach: run the job without any skill, note only what Claude gets wrong, and add only those corrections into a minimal skill. Skills shrink dramatically as models improve.

**Try-before-you-skill loop**
1. Attempt the job with no skill. 2. Note failures. 3. Add only failures to the skill. 4. Run the Skill Eval plugin to confirm the skill beats no-skill. 5. Remove any instruction the skill handles no better than the default.

**Effort-down before model-down**
Instead of switching to a cheaper model for easy questions, reduce the effort level or tell Claude to skip reasoning. Preserves cache, avoids re-ingestion cost, and is often just as fast.

**Orchestrator + worker architecture**
One main conversation acts as orchestrator (briefs, delegates, tracks goals). Worker threads/sub-agents handle execution. Sub-agents return only outputs; forks share full history. The orchestrator never needs to see the working details, only the results.

**Deterministic stop hooks**
Attach a prompt hook (fast, reads conversation only) or agent hook (slower, can open files) to the stop event. The hook either approves completion or returns a specific correction as Claude's next instruction — converting a soft instruction into a hard guarantee.

**Event-driven routines**
Set a routine with a name, prompt, repo, and API trigger. Any web request to the generated URL starts a fresh cloud run. Strip connectors to only what the job needs. Enables reactive (event-based) automation vs. time-scheduled automation.

**Goal with deterministic proof**
Structure `/goal` conditions so the required evidence appears explicitly in the chat — e.g., test output, script pass/fail — not as a subjective state the checker model must infer from Claude's own claims.