# OpenAI PM Reveals How He Uses Codex to Do Product Work | Rohan Varma

Video ID: `fAdFE7y6K2o`

## Summary
Rohan Varma, a PM on the OpenAI Codex team, walks through how Codex has fundamentally restructured his day-to-day product work — not just making existing tasks faster, but enabling entirely new workflows that would have been impractical before. The core argument is that PMs should delegate aggressively to Codex across information synthesis, artifact generation, and automation, freeing up time for high-value work like customer conversations and strategic decisions. The video includes live demo walkthroughs of real workflows Rohan uses. It is most relevant to PMs, operators, and knowledge workers looking to move beyond basic AI assistance toward full delegation and automation.

## Key insights
- **Codex has inverted the product development lifecycle.** Instead of planning upfront so engineers only work on the right things, teams now build first and decide what to ship afterward. A real example: engineer Adam Fraser showed up one morning having already built an in-app browser. The prototype became the starting point, not a spec doc.
- **PMs at OpenAI operate with a 4–8 week rolling plan, not a 12-month roadmap.** Rohan actively argues the word "roadmap" is misleading — the real question is: what are the priorities this month, and what will they be next month?
- **Codex is Rohan's only way to keep track of what engineers are building.** With one or two engineers per product line moving extremely fast, there are constant micro-decisions being made autonomously. Rohan uses Codex to gather context on-demand rather than maintaining constant awareness.
- **Three-to-four-times daily output multiplier.** Rohan estimates he gets 3–4x more done per day than he would without Codex, primarily through context compression and automated task execution.
- **Slack-to-Linear automation pipeline.** Rohan built a workflow where Codex reads Slack channels, synthesizes customer feedback and bugs, and uploads structured tickets to Linear — then set Codex to automate this process continuously without further prompting.
- **Codex can set up and manage its own automations.** A key unlock: Codex knows how to create, modify, and delete its own scheduled automations. Example: Rohan asked Codex to watch for a specific Slack reply from a colleague, draft a client email when that reply arrived, and then self-delete the automation once the trigger fired.
- **ImageGen inside Codex is a faster prototyping tool than writing React code.** Rohan gave Codex a screenshot of the Codex composer UI and asked it to generate 4–5 redesign ideas. The results were good enough to serve as design mocks and be immediately turned into a shareable prototype site — he called it an "AGI moment."
- **Disposable software as a workflow.** Rohan regularly asks Codex to spin up one-off local web apps on the fly — e.g., a prioritized visual list of Slack messages to respond to, or a list of commitments he made in the past 24 hours. If the app proves useful, he sets an automation to refresh it hourly.
- **Living project state sites replace static docs.** For each project Slack channel, Rohan has Codex generate a continuously updated website summarizing the full project state, refreshed every few hours. This solves the classic problem that any document is immediately out of date the moment it's written.
- **Codex as personal chief of staff.** At the start of each week, Rohan has Codex review his calendar, identify meetings that can be consolidated or canceled, and carve out focus blocks.
- **PR nursing workflow.** Codex can be told to watch a PR, wait for CI, fix CI failures, respond to human review comments, and ping Rohan on Slack only when the PR is ready to merge — reducing ~10 interaction points to one.
- **Skill creator to create skills.** Codex has a built-in "skill creator" skill. After a productive multi-turn workflow, Rohan tells Codex to review the thread and generate a reusable skill so the pattern is templated for future use.
- **The 10x ambition rule.** Rohan's heuristic: aim for something that seems 10x more ambitious than you think is possible — Codex will probably accomplish 90% of it. Then reset and aim 10x higher again.
- **Only the top 5–10% of enterprise engineers are maximally leveraging Codex.** The big product opportunity is closing the ambition gap — helping non-developers and mainstream engineers understand what can actually be delegated.
- **Running 5–6 parallel threads is normal, but fully delegated.** The mental model is managing a team member: you fire off work and check back when you have a free moment, not maintaining constant state on every task.
- **Cloud automations are not yet native** (as of recording), but mobile support and remote Codex instances exist. Local automations stop when the laptop is closed — acknowledged as a current limitation with a fix in the pipeline.

## Use cases
- **PMs onboarding to a new project mid-sprint** — Codex can ingest Notion, Linear, email, and Google Drive to build a full context brief in under 20 minutes.
- **Synthesizing high-volume customer feedback** — reading hundreds of Slack messages, bug reports, and Twitter mentions daily and distilling them into structured Linear tickets automatically.
- **Fast design iteration without a designer in the room** — using ImageGen inside Codex with a reference screenshot to generate multiple UI redesign options, then converting the best one into a shareable prototype.
- **Tracking commitments across a busy meeting day** — asking Codex to scan the past day's messages and surface all promises made, with a prioritized action list.
- **Automating event-triggered follow-ups** — e.g., watch for a reply from a specific colleague, draft a response email, then clean up the automation.
- **Keeping project documentation current automatically** — generating living project state sites per Slack channel, updated every few hours.
- **Managing a PR from push to merge** — Codex nurses the PR through CI, reviewer comments, and fixes, notifying the human only at the final merge decision.
- **Performance reviews and contribution summaries** — asking Codex to scan all activity over the past three months and compile an accurate contribution list.
- **Calendar optimization** — weekly review of meetings to find consolidation and cancellation opportunities, freeing focus blocks.
- **Marketing asset production at shipping speed** — DevEx teams using Codex skills to auto-generate demo videos and visual graphics when the engineering team ships faster than marketing can keep up.

## Patterns & frameworks

**The Inverted Product Development Lifecycle**
Traditional: plan → spec → engineer → ship. OpenAI's model: engineer builds an MVP (often overnight), PM evaluates what to ship and how. Planning effort moves from the front of the process to the back. Reduces wasted planning on ideas that would have died in prototyping anyway.

**The Delegation Paradigm (vs. Pair Programming)**
Mental model: treat Codex like a direct report you manage asynchronously, not a coding partner you supervise in real time. Fire off work, don't maintain constant awareness of what it's doing, and check the "unreads" when you have a free moment. Constant state maintenance is the anti-pattern.

**The 4–8 Week Rolling Roadmap**
Replace the 12-month roadmap with a tighter planning horizon: know the priorities for the next 4–8 weeks clearly, execute against them, and reset priorities at the end of each cycle. Codex enables this because building is fast enough that long-horizon planning creates more waste than value.

**The Automation Escalation Loop**
1. Do a task manually (or via a one-off Codex chat).
2. Ask Codex to repeat it on a schedule.
3. Ask Codex to set up the automation itself.
4. Optionally: ask Codex to trigger the automation on an event rather than a schedule, and self-delete once the condition is met.
This pattern converts any repeatable workflow into a zero-maintenance background process.

**Skill Templating from Live Threads**
After a productive multi-turn Codex session that produced a good output, use the Skill Creator skill to tell Codex: "review this thread and create a skill so future interactions are consistent." Converts one-off prompt engineering into reusable, reliable workflows without manual documentation.

**The Ambition Ratchet**
Heuristic for calibrating task scope: assume Codex can do 10x more than feels reasonable. Assign that task. It will likely complete 90% of it. Then recalibrate expectations upward again. The ceiling keeps rising; the right response is to keep aiming higher rather than anchoring to what worked last week.

**The "What Was Missing?" Debugging Loop**
When Codex fails a task, don't default to doing it manually. Instead ask: what context or information did Codex lack that I implicitly had? Provide that context. This iterative loop progressively increases automation coverage by surfacing and closing knowledge gaps.

**Living Documentation (Self-Updating Project Sites)**
Replace static PRDs and docs — which become stale immediately — with continuously auto-updated web pages driven by Codex pulling from Slack channels every few hours. The document becomes a living artifact rather than a snapshot, making it useful for onboarding and ongoing reference.