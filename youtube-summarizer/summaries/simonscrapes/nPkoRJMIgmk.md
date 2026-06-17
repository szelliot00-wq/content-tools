# You’re Only Using 10% of Claude Code (I’m Being Serious)

Video ID: `nPkoRJMIgmk`

## Summary
This video argues that most Claude Code users are only using a fraction of its capabilities because they haven't enabled the features that allow it to run autonomously without constant human oversight. The presenter walks through four progressive phases: enabling continuous autonomous operation, maintaining output quality on large tasks, accessing Claude from mobile/remote devices, and expanding what users think is automatable. It is most relevant to product managers, operators, and knowledge workers who want to offload repetitive admin, ops, and outreach tasks to an AI agent that runs in the background.

## Key insights
- **Auto mode eliminates 90% of approval friction.** Activated with Shift+Tab twice, it uses a background safety classifier to auto-approve safe actions and only pauses for genuinely risky ones (e.g., deleting files). Previously users had to choose between approving everything manually or skipping all permissions dangerously.
- **`/goal` redefines "done."** A normal Claude prompt lets Claude decide when it's finished, often stopping early. `/goal` lets the user define a completion condition; a second independent Claude agent audits the work before the goal can close, forcing continued iteration until the condition is truly met.
- **`/loop` and `/routines` add scheduling cadence.** `/loop` runs tasks on short recurring intervals; `/routines` handles longer schedules (e.g., weekly). Combined with `/goal`, this creates fully automated recurring workflows — e.g., clearing an inbox daily until it's empty, without any human present.
- **Context rot degrades quality on long tasks.** As context window fills, Claude loses recall and judgment. The fix is to keep plans inside project folders (not throwaway directories) so they survive context compaction and can be re-fed explicitly.
- **The `/effort` slider controls reasoning depth.** Options range from low to max to "Ultra Code." Higher effort spends more tokens on thinking, producing better results for complex problems — but at significant token cost, so it should only be used when the task warrants it.
- **Ultra Code spins up multi-agent workflows.** It writes a bespoke orchestration plan for the task, fans out to specialized sub-agents (each with a fresh context window), and coordinates them via an orchestrator. Example: a deep research task fans out to 4 agents each covering one source, with a 5th synthesizing findings and a 6th doing claim validation.
- **Built-in mobile access has a session-drop problem.** Remote control and Channels (Telegram/Discord) both drop the session after ~10 minutes of inactivity or disconnection — work stops when you leave.
- **The VPS + tmux workaround enables always-on operation.** Running Claude Code on a ~$15/month VPS with tmux keeps the session alive continuously. Combined with Channels, this allows dispatching tasks from a phone and walking away — work continues without the laptop being open.
- **Connectors provide zero-code app integrations.** Inside the desktop app's Customize > Connectors menu, there are hundreds of pre-built plug-and-play connections to common apps. Users authorize once with normal login credentials and interact in plain English.
- **Browser automation ("computer use") handles apps with no API.** Claude can take screenshots, navigate, and click through any browser-based or desktop app. The demo showed it autonomously reading 24 hours of community posts, categorizing them into three priority groups (needs me today / can wait / wins to celebrate), and returning direct links — taking ~15 minutes to complete.
- **The presenter's framing:** the bottleneck is no longer missing features — it's the user's mental model of what's automatable. Almost everything repetitive is now within reach.

## Use cases
- **Community managers** who want a daily digest of member posts, triaged by urgency, without manually reading everything.
- **Founders and operators** running repetitive inbox triage, CRM updates, or outreach sequences that currently require daily manual attention.
- **Product managers** who want research synthesized across multiple sources (competitor analysis, user feedback, market data) without sitting through the process.
- **Anyone using legacy enterprise software** with no API access — Claude's browser automation can perform repetitive clicks and data entry on their behalf.
- **Remote or async workers** who want to dispatch tasks from a phone and have results waiting when they return.
- **Teams doing recurring quality checks** (e.g., weekly content audits, daily reporting) that currently require human initiation each cycle.
- **Solo operators** who want an autonomous back-office running ops, admin, and outreach while they focus on higher-leverage work.

## Patterns & frameworks

**Auto Mode (Shift+Tab twice)**
A middle-ground permission system using a background safety classifier. Safe actions pass automatically; only genuinely dangerous actions (file deletion, etc.) trigger a manual approval prompt. Replaces the binary choice between full auto-skip and full manual approval.

**`/goal` + Completion Criteria Loop**
Define "done" explicitly rather than letting Claude self-declare. A second independent agent audits the work before the goal closes. Claude iterates until the user-defined condition is satisfied. Prevents premature task termination.

**`/loop` + `/routines` Cadence Scheduling**
`/loop` for short-interval recurring tasks (under 3 days); `/routines` for longer schedules (weekly, monthly). Combined with `/goal`, creates a fully autonomous recurring workflow with a defined completion state.

**Effort Slider (`/effort`)**
A token-budget dial from low → max → Ultra Code. Higher settings allocate more tokens to reasoning/thinking, improving output quality for complex tasks at the cost of speed and token spend. Designed to be used selectively.

**Ultra Code / Multi-Agent Orchestration**
Claude writes a bespoke workflow for the task, fans out work to specialized sub-agents (each with a clean context window), and coordinates via an orchestrator. Based on Anthropic's six canonical workflow patterns (e.g., fan-out research, claim + validation pairs). Solves both context degradation and single-window throughput limits.

**VPS + tmux + Channels Stack**
Infrastructure pattern for always-on autonomous operation: cheap VPS (~$15/month) runs Claude Code persistently; tmux keeps the session alive across disconnects; Channels (Telegram/Discord) provides the mobile dispatch interface. Approximates a background agent server without a dedicated hosting platform.

**Plan-in-Project-Folder Pattern**
Save planning artifacts inside the project directory (not the default throwaway folder) so the plan survives context compaction. Re-feed the plan file to Claude to maintain orientation across long multi-turn tasks.