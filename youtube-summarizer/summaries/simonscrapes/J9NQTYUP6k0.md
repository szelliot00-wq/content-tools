# How the Top 1% Use Claude Code Differently

Video ID: `J9NQTYUP6k0`

## Summary
This video challenges outdated Claude Code conventions (like plan mode and "think hard" prompts) and replaces them with current best practices used by top practitioners as of late 2025. The core argument is that newer models (Opus 5.5, etc.) are capable enough to make most manual orchestration unnecessary — the user's job shifts from directing Claude step-by-step to defining outcomes, guardrails, and validation criteria, then reviewing evidence. It is most relevant to power users, indie hackers, product managers, and developers who use Claude Code daily for automation and agentic workflows.

---

## Key insights

- **Plan mode is obsolete.** Boris Churnney (who built plan mode) stopped using it because newer models plan internally while working. He now writes: task description, guardrails, and a definition of done — then reviews output after, not before.
- **"Think hard / ultra think" prompts no longer work.** These are now read as plain English. Thinking depth is controlled by the "effort level" setting in the UI. Opus 5.5 on Medium matches or beats Opus 5 on High for coding and knowledge work. The advice: leave it on the recommended default and don't touch it.
- **Verification scripts 2–3x quality.** Giving Claude a runnable check (e.g., a `check_report` script) that returns pass/fail against your definition of done dramatically improves output quality. Newer models already self-check without being told; adding "double-check your work" to the prompt just wastes tokens.
- **`/goal` replaces manual "continue" prompts.** After every turn, a small model (Haiku) reads your goal and decides if it's met. If not, Claude takes another turn automatically. Caveat: the judge only sees chat text — it can't run files or commands independently — so a vague goal causes premature completion. A good goal has: one end state, how to prove it, what must not change, and a turn limit (e.g., stop after 15 turns).
- **`claude.md` should be under 200 lines and act as a contents page/index.** Anthropic deleted 80%+ of Claude Code's own internal instructions when Opus 5 shipped because they were patching old model weaknesses. Your `claude.md` should only contain: (1) tools/commands Claude can't guess, (2) things you do differently from default, (3) recurring gotchas, (4) hard boundaries. Everything else becomes a pointer to another file.
- **Reference files via path + trigger, not `@` imports.** Using `@file` loads the whole file into every session. Instead, write the path in backticks with a condition: *"read the client brief before any client work."* This enables progressive disclosure — Claude only loads context when it needs it.
- **All reference files must be pointed to directly from `claude.md`.** Files only reachable through another file get only their first 100 lines previewed. Any file over 100 lines needs a table of contents at the top.
- **Build skills by reverse-engineering failures, not by documenting process.** Run Claude on the task with no skill first. Write down only where it went wrong. The skill becomes a list of corrections, not a full process manual. Most of Anthropic's own best skills started as just a few lines fixing one gotcha.
- **Shared "skill packs" are largely ineffective.** A developer ran 450 tests on 9 popular skill packs using Opus 5.5. Only 2 of 9 outperformed a dummy file of the same length — meaning 7 out of 9 added tokens without improving output. Use `/plugin eval` to test skill vs. no-skill performance on your actual tasks.
- **Hooks replace CAPS rules for guaranteed behavior.** Writing "NEVER email the client" in all-caps no longer reliably works. Instead, write a deterministic hook (a small executable script) that runs at a defined moment (e.g., before every tool use) and blocks the action. Hooks consume no AI tokens and always fire.
- **Sub-agent teams are now self-assembled by Claude.** You no longer need to build orchestrator/agent files by hand. Opus 5.5 hands work to sub-agents more readily than any prior model. Your role is to set a cap on how many sub-agents can be spun up to control cost and scope. `ultra` mode can spin out unlimited sub-agent trees — use with caution.
- **Claude Code Projects enable async, always-on automation.** Projects maintain a persistent conversation, spin up parallel agents, and keep running when your machine is off. Combined with scheduled tasks or event triggers (e.g., a new CRM lead added), they enable fully unattended workflows. Codex now supports MCP events so connected apps can trigger Codex runs on external events.

---

## Use cases

- **Weekly recurring reports:** Automate client report generation from CRM exports with a validation script that checks figures and template completeness.
- **Social media content production:** Run carousel/short-form content generation in the background; only approve final outputs in a custom UI.
- **CRM-triggered workflows:** Automatically process new leads or to-do items when they're added, without manual initiation.
- **Prompt/instruction auditing:** Use `/doctor prompt audit` to clean up outdated `claude.md` files, broken paths, and contradictory rules accumulated over months.
- **Skill library hygiene:** Use `/skill doctor` and `/plugin eval` to identify unused or ineffective skills and trim token overhead.
- **Agentic product or operations teams:** Any role that has repetitive multi-step workflows (research, drafting, data QA) that can be defined with a clear definition of done.
- **Developers building Claude-powered tools:** Setting up hooks, sub-agent caps, and goal-driven loops for reliable, cost-controlled autonomous operation.

---

## Patterns & frameworks

**Output + One-Page Explainer (instead of upfront planning)**
Instead of reviewing a plan before work starts, you ask Claude for a visual summary of what it did and what assumptions it made *after* the task completes. The brief contains: task, guardrails, definition of done. The deliverable is: output + one-page explainer.

**Definition of Done → Runnable Check**
Take the "definition of done" line from your brief and turn it into an executable script or deterministic document (e.g., brand voice doc) that Claude can run to validate its own output. Pass/fail replaces subjective review.

**`/goal` Loop**
Set a goal with one end state, proof condition, a "what must not change" constraint, and a turn limit. A Haiku judge evaluates after every turn; Claude loops until the check passes or the turn limit is hit. Frees the user from manual "continue" prompting.

**`claude.md` as Index / Contents Page**
Treat `claude.md` as a pointer document, not a process manual. It holds only always-true facts and references. All other context lives in separate files loaded on-demand via path + trigger conditions — progressive disclosure of context.

**Skill as Correction Log (not Process Manual)**
Run the task without any skill first. Document only what went wrong. Build the skill purely from those corrections. Skills are small and specific; they are not documentation of the whole process.

**Hooks as Deterministic Guardrails**
Replace capitalized instructions in `claude.md` with executable hooks that fire at defined moments (before tool use, after turn, etc.). No AI tokens consumed; always enforced regardless of model behavior.

**Sub-Agent Cap Pattern**
Rather than manually wiring agent teams, let Claude self-assemble its helpers. Set a maximum sub-agent count in config to cap cost and scope. Reserve explicit sub-agent instructions only for steps involving MCP connectors, large research steps, or context-isolation needs.

**Skill Evaluation: Skill vs. No-Skill Baseline**
Before keeping any skill, run `/plugin eval` to compare Claude's performance on the task with and without the skill. If scores are equal, the skill is pure overhead and should be deleted.