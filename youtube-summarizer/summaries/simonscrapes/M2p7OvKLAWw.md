# 12 Hidden Settings to Enable in Claude Code

Video ID: `M2p7OvKLAWw`

## Summary
This video walks through 12 Claude Code settings — all single-line changes to `~/.claude/settings.json` — that most users have never enabled. The presenter argues that default Claude Code configuration leaves significant productivity, cost, and privacy value on the table. The video is most relevant to developers and AI-assisted engineers who use Claude Code daily and want tighter control over cost, permissions, data privacy, and workflow interruptions. A bonus 13th insight addresses a fundamental shift in prompting philosophy for modern frontier models.

## Key insights
- **Notification sound (Tip 1):** Enable desktop notifications via `/config` → "local notifications" to avoid losing time when Claude is waiting on permission prompts. A third-party library called "Claude Sounds" (by Dave Schumacher) offers humorous audio alerts as an alternative hook.
- **Mobile push notifications (Tip 2):** Add `"agentPushNotifyEnabled": true` to `settings.json` to receive phone pings during remote terminal sessions when Claude needs input, enabling truly async workflows.
- **Tailored allow lists via `/fewer-permission-prompts` (Tip 3):** This slash command scans your 50 most recent transcripts, identifies tool calls you always approve, and generates a targeted allow list — giving you the speed of auto-approve without blanket permission skipping.
- **Deny rules (Tip 4):** Add deny rules to `settings.json` that are checked before allow rules — recommended starting pair is blocking reads of `.env` files (protecting API keys) and blocking `git push *` (keeping publish power with the human).
- **Opus Plan mode (Tip 5):** Use `/model` to select an "Opus Plan" preset that runs Opus in plan mode, then automatically drops to Sonnet during execution — aligning expensive reasoning with planning and cheap throughput with building. A `FablePlan` equivalent is an open issue but not yet implemented.
- **Effort level trap (Tip 6):** Independent testing across 20 rounds per level found that below `max`, output quality and correctness barely change. Extra tokens at high effort levels buy re-verification and caveats, not better answers. Recommendation: use default for routine work, `high` for genuinely hard problems, and almost never touch `max` — especially with Fable 5, which is usage-credit-based.
- **Disable telemetry and surveys (Tip 7):** Four ENV lines in `settings.json` reduce noise and data sharing: `CLAUDE_CODE_DISABLE_FEEDBACK_SURVEY`, `DISABLE_TELEMETRY`, `DISABLE_ERROR_REPORTING`, and `DISABLE_NON_ESSENTIAL_MODEL_CALLS`. Also toggle off "Help improve AI models" in claude.ai privacy settings.
- **Extend conversation history (Tip 8):** Default retention is 30 days; Claude deletes older history silently. Add `"cleanupPeriodDays": 365` (or higher) to `settings.json` to preserve history. Setting it to `0` wipes everything — use a large number.
- **Auto-compact threshold (Tip 9):** Claude waits until ~95% context fill before compacting by default, but context quality degrades around 70–80% ("context rot"). Set `CLAUDE_AUTO_COMPACT_PERCENTAGE_OVERRIDE` in the ENV section to `75` to trigger compression before quality loss.
- **Status line UI (Tip 10):** Run `/statusline` (e.g., "show model name and context percentage with a progress bar") to add a live status bar showing cost, context fill percentage, and model name — making tips 8 and 9 actionable in real time.
- **Prompt stash shortcut (Tip 11):** `Ctrl+S` mid-typing stashes the current prompt (acts like cut), freeing you to ask a prerequisite question first, then paste the original back with `Cmd+V`. The stashed prompt auto-populates the next input window.
- **Disable spinner tips (Tip 11 freebie):** Add `"spinnerTipsEnabled": false` to `settings.json` to remove the rotating tips shown during task execution — reduces distraction.
- **Remove AI attribution from commits (Tip 12):** By default, Claude Code appends "Generated with AI / Co-authored by AI" to every commit. Add blank `commit` and `PR` attribution strings in `settings.json` to suppress this. (Context: Claude Code reportedly authored ~4% of all GitHub commits in recent months.)
- **Prompting philosophy inversion (Tip 13/bonus):** Anthropic's own guidance for frontier models now explicitly discourages long, hyper-specific prompts. Instead: give the outcome, the context, and a "done looks like" criterion — no step-by-step instructions. This is termed "loop engineering."

## Use cases
- **Daily Claude Code users** burning through weekly token limits in 2 days — tips 5, 6, and 9 directly address cost and context efficiency.
- **Developers working on client projects** who need data privacy guarantees — tip 7 (telemetry/survey opt-outs) and tip 4 (deny rules for `.env` files) are critical.
- **Remote or async workers** who run long tasks and step away — tips 1 and 2 (notifications) eliminate the "came back and it was waiting" failure mode.
- **Teams using auto-approve mode** who want guardrails without slowing down — tips 3 and 4 layer a tailored allow list with hard deny rules.
- **Anyone who has lost conversation history** after 30 days — tip 8 prevents silent data loss.
- **Engineers obsessing over prompt engineering** with modern models (Fable 5, Claude 4.x) — the bonus tip reframes the bottleneck as context-closing, not prompt length.
- **Developers concerned about public attribution** of AI-generated code on GitHub — tip 12 removes the automatic co-author tag.

## Patterns & frameworks

**Big model / small model split**
Use the most capable model (Opus or Fable) for high-stakes, low-volume tasks — planning, reviewing, diagnosing hard problems — where a mistake is expensive. Drop to Sonnet or Haiku for high-volume, low-stakes execution — reading files, implementing plans, ingesting documents. The Opus Plan preset automates this switch within a session.

**Deny → Ask → Allow rule hierarchy**
Permission evaluation in `settings.json` follows a fixed priority: deny rules are checked first and cannot be overridden by any allow rule at any level. This lets users layer blanket auto-approve (allow) with hard stops (deny) for sensitive operations like `.env` reads or `git push`.

**Context rot threshold model**
Context quality doesn't degrade linearly — it falls off sharply around 70–80% fill. Setting auto-compact to trigger at 75% (via `CLAUDE_AUTO_COMPACT_PERCENTAGE_OVERRIDE`) keeps the session in the high-quality zone. The status line (tip 10) makes this observable so manual compaction is also possible.

**Loop engineering (bonus framework)**
A shift in how to work with frontier models: rather than writing longer, more prescriptive prompts, give the model a goal + context + "done criteria" and let it self-direct. Named "loop engineering" — running structured loops before (planning), during (execution checkpoints), and after (review) implementation. Credited to Tarik from the Claude Code team whose field guide reached 2M views in 3 days. The bottleneck is no longer model capability but the human's ability to close the gap between the ask and what actually needs to happen.

**Effort level calibration**
A tested framework (20 rounds per effort level) showing that effort/thinking budget above `high` purchases re-verification tokens, not correctness gains. The recommended default: `automatic` for routine work, `high` for genuinely hard problems, `max` almost never — particularly important now that Fable 5 operates on usage credits rather than a flat subscription.