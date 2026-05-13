# Claude Code has a new UI (pair it with Claude OS)

Video ID: `J6tPNRc9m2Q`

## Summary
This video covers Anthropic's newly released native agent management UI built directly into Claude Code, called the "agent view," currently available in research preview as of version 2.1.139 or higher. The creator demonstrates how to migrate existing terminal sessions into the dashboard, manage multiple concurrent AI agents, and organize work by status or repository. The video also explores how this native UI pairs with a pre-existing "Agentic Operating System" (a folder-based context injection architecture). It is most relevant to developers, product managers, and power users who are running multiple Claude Code agents simultaneously and struggling to manage them across fragmented terminal windows.

## Key insights
- **The core problem being solved:** As AI agents have become capable enough to execute autonomously to ~90% completion from a good prompt, users are now managing multiple agents at once, leading to chaotic multi-terminal juggling
- **Community workarounds existed before this:** Third-party solutions had already emerged — Vibe Kanban (Kanban-style UI), T-Mux (terminal-based solution), and the creator's own custom command center — indicating strong demand for a native solution
- **Version requirement:** The new agent view requires Claude Code version 2.1.139 or higher; users must run `claude --version` to check and `claude-update` to upgrade
- **Launching the agent view:** Running `claude agents` in the terminal opens a summary dashboard showing all active sessions organized by status
- **Migrating existing sessions:** Existing terminal sessions can be moved into the agent view by typing `/bg` (background command) inside a session, which closes the terminal window and adds the session to the dashboard
- **Default sorting is by status**, making it easy to see which agents need input vs. which are actively working
- **Sorting by repository:** Users can press `Ctrl+S` to switch sorting from status to repo/folder structure — useful when working across multiple codebases
- **Navigation shortcuts:** `Shift+Up` and `Shift+Down` reorder sessions; `Ctrl+T` pins priority sessions to the top of the list
- **Inline session interaction:** Pressing `Spacebar` while hovering a session shows its latest status and allows direct replies without fully entering the session; `Left/Right` arrow keys navigate in and out of session detail views
- **Current limitation — approvals:** Typing "approve" from the summary view did not successfully push through tool-use approvals; users still need to jump into individual sessions manually to approve actions
- **Current limitation — desktop app:** The agent view is terminal-only for now; the desktop app does not yet support this multi-agent interface, though the creator expects it will be added
- **Subfolder sorting gap:** Sorting by repo only works at the parent folder level, not subfolders — a limitation called out explicitly for users who organize work by client subfolders (e.g., `clients/acme-corp`)
- **Integration with Agentic OS:** The native UI pairs seamlessly with a folder-based Agentic Operating System because that system works by injecting context (brand, client, scheduled jobs) at the file/folder level — each conversation automatically benefits from that context regardless of which UI is used to manage it
- **New agent creation:** Users can spin up a new agent session directly from the dashboard by typing a task description at the bottom prompt (e.g., "Draft a LinkedIn carousel based on my last YouTube video")

## Use cases
- **Freelancers or agencies** managing work for multiple clients simultaneously, running separate Claude Code agents per client project
- **Developers** working across multiple repositories who want a consolidated view of all active coding agents without switching terminal windows
- **Product managers or content creators** delegating multiple parallel content or research tasks to AI agents (e.g., drafting social posts, summarizing videos, building systems)
- **Power users with an existing Agentic OS** who want a cleaner interface to monitor and interact with agents without losing their context-injection architecture
- **Anyone currently using third-party dashboards** like Vibe Kanban or T-Mux who wants to consolidate into a native, maintained solution
- **Teams or individuals running scheduled or long-running agentic jobs** who need to quickly identify which sessions are idle, active, or waiting for approval

## Patterns & frameworks

### Agentic Operating System (Agentic OS)
A folder-based architecture for organizing AI agent context. Rather than being a software tool, it is a structured directory system where brand context, client profiles, and scheduled job definitions are stored. Claude Code automatically pulls in the relevant context based on which folder a session is operating within. It functions as a persistent "operating system" layer beneath whatever UI or dashboard is used to manage agents — meaning it remains fully functional when combined with the new native agent view.

### Background Session Migration Pattern (`/bg` command)
A repeatable process for moving existing terminal-based Claude Code sessions into the agent view dashboard. The pattern is: open an active session → type `/bg` → the terminal closes and the session appears in the agent view. This allows users to consolidate scattered terminal windows into a single managed interface without losing session history or progress.

### Status-First Dashboard Organization
The default UX pattern of sorting agents by status (active, waiting for input, idle) rather than by task name or time created. This mirrors triage-based prioritization — the most actionable sessions (those needing input) surface to the top automatically, reducing cognitive load when managing many concurrent agents.

### Pin-and-Prioritize Navigation
A lightweight session management pattern using keyboard shortcuts (`Ctrl+T` to pin, `Shift+Up/Down` to reorder) to create a personal priority stack within the agent dashboard — analogous to starring emails or pinning tabs in a browser for high-priority work.