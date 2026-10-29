# The New Claude Is Way More Than It Looks

Video ID: `KjuANoI8HDw`

## Summary
This video is a detailed walkthrough of the redesigned Claude desktop app, focusing on the new Projects feature and several supporting UX improvements. The presenter argues that the app has evolved from a fragmented, tool-switching experience into a unified workspace where context (instructions, memory, files, connectors) is set up once and shared across all work. The core framework is: delegate multi-step work to threads, steer from a main conversation, and never lose output to scattered chats. It is most relevant to solo professionals, content creators, and non-technical power users who want to replace manual task coordination with Claude-managed workflows.

## Key insights
- **Projects are now multi-threaded workflows**: A project spawns a separate Claude thread per task from a single message. Each thread is a full Claude session that reports back to the main conversation when done.
- **Shared context across threads**: Project instructions and memory are injected into every thread. A correction made in one thread is inherited by all subsequent threads — no more copy-pasting the same background into five separate chats.
- **The main conversation stays clean**: Because actual work happens in threads, the main chat doesn't fill up with detail, keeping it useful for steering and status checks across the full project lifetime.
- **Cloud-run threads persist after closing the laptop**: Threads run in the cloud by default, meaning work continues when you're offline. You can check in and redirect from your phone via the remote control switch.
- **Local threads for file-access tasks**: If a job requires files on your computer, you can explicitly run that thread locally instead of in the cloud.
- **Library collects all outputs**: Every file added to or created within a project accumulates in one project library — eliminates the problem of losing drafts across 15 different chats.
- **Side chats for off-topic questions**: A side chat opens in a separate pane, can read the full main chat for context, but writes nothing back into it. Multiple side chats can be open simultaneously and are saved. A side chat can optionally push a message back to the main chat (e.g., sending only the fixes that matter from a review).
- **In-chat to-do list**: When Claude makes a plan, it renders a checklist inside the chat and ticks items off in real time — replaces the opaque "thinking" experience.
- **Cards panel beside the chat**: Three cards show (1) environment — folder, local vs. cloud, remote control toggle; (2) context — how full the session is, what's consuming space, and a compact button; (3) connectors and outputs — every file made or used.
- **Chat sections and split view**: Chats can be organized into named sidebar sections via drag-and-drop. Two chats can be opened side by side with split view, either by dragging from the sidebar or via the three-dot menu.
- **Artifacts are now first-class outputs**: Docs (Google Docs-style with tabs), Slides (exportable to PowerPoint), Design (canvas for social posts/landing pages), and Dashboards (live data from connectors, paid beta) all live in a unified artifacts view. All support commenting, version history, and shareable links.
- **Control + O cycles verbosity**: Switches between normal, thinking, and verbose modes — lets non-technical users hide implementation detail.
- **Resource cost warning**: Every thread defaults to Opus on high effort, which burns usage limits fastest. Check project settings before starting.
- **Plan availability**: Projects (cloud threads + shared memory) are Pro and Max only. Team plan users get "nested sessions" — same concept but locally run, with a brief passed per sub-session rather than shared memory.
- **Cowork folded into Chat**: The previously separate Cowork product is now part of Chat, reducing the number of Claude entry points from three to two (Chat/Projects and Claude Code).
- **Known limitations**: The main project conversation cannot use connectors directly (it delegates to a thread). Threads don't automatically load skills and settings from your computer — you must enable skills in your Claude account for threads to pick them up.

## Use cases
- **Content creators**: Planning, drafting, and scheduling a week's worth of content (videos, social posts, LinkedIn hooks) in one project message with parallel threads.
- **Solo operators / consultants**: Running multi-deliverable client work (research + deck + email) without manually coordinating across separate chats.
- **Non-technical professionals**: Using the redesigned UI (to-do cards, artifacts, built-in browser, file editor) without needing to touch Claude Code or a terminal.
- **Remote/async workers**: Starting a project on a laptop, then monitoring and steering threads from a phone while the cloud continues the work.
- **Teams on Pro/Max**: Setting up shared project instructions once so every collaborator's threads inherit the same context and corrections.
- **Knowledge workers managing many ongoing chats**: Using chat sections and split view to organize and monitor multiple parallel workstreams without losing track of outputs.
- **Anyone producing structured deliverables**: Using Docs, Slides, or Design artifacts to produce shareable, version-tracked outputs directly inside Claude rather than exporting to other tools.

## Patterns & frameworks

**The Thread Delegation Model**
One main conversation acts as a "team lead" interface. You send a single high-level message; Claude breaks it into tasks and spawns one thread per task. Each thread operates independently but reports status back up. The main conversation retains a high-level view without accumulating low-level detail. Pattern: *brief once at the top, execute in parallel below, review from the top*.

**Set Context Once, Use Everywhere**
Project instructions, memory, files, and connectors are defined at the project level and flow into every thread automatically. Corrections propagate forward. This replaces the manual pattern of copy-pasting background into every new chat. Pattern: *single source of truth for context, not per-chat re-briefing*.

**Side Chat as Interrupt Handler**
Instead of inserting off-topic questions into an active work session (which pollutes context and disrupts flow), a side chat handles the tangent in isolation. It reads the main chat for context but writes nothing back unless you explicitly send a message. Pattern: *read-only observer that can optionally inject a targeted response*.

**Output Centralization via Library + Artifacts**
Every file produced by any thread or session accumulates in the project library. Every document, deck, or design is an artifact with version history and a shareable link. Pattern: *work produces persistent, addressable outputs rather than transient chat messages*.

**Verbosity Toggle (Control + O)**
A three-state switch (normal → thinking → verbose) controls how much of Claude's internal reasoning is exposed. Lets the same tool serve both technical and non-technical users. Pattern: *progressive disclosure of complexity*.