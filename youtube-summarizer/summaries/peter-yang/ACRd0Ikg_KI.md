# Build a Claude Code Personal OS Step by Step in 40 Minutes | Moritz Kremb

Video ID: `ACRd0Ikg_KI`

## Summary
This video features a conversation between Peter and Moritz (Twitter: @mob), where Moritz demonstrates how he built a personal AI operating system called "Claudia" using Claude Code. The video begins with a comparison of OpenClaw vs. Claude Code as personal chief-of-staff platforms, then dives into a detailed walkthrough of Claudia's folder structure, memory system, tools, routines, and skills. The centerpiece is a fully semi-automated short-form content creation pipeline that handles everything from idea capture to video posting. The video is most relevant to solo creators, indie hackers, and productivity-focused individuals who want to use AI agents to automate repetitive personal and professional workflows.

---

## Key insights

- **OpenClaw vs. Claude Code trade-offs:** OpenClaw excels at mobile access (Telegram/Discord integration), always-on heartbeat functionality (triggers every 30 minutes), easy cron job creation, and sub-agent orchestration. Claude Code excels at reliability, model quality (Opus/Sonnet), CLI access (not sandboxed like Codeium), and now has a polished desktop UI.
- **Claude Code desktop app is a game-changer:** Released roughly 10 days before filming, it replaced terminal usage for Moritz almost entirely, offering a side panel for files, plans, and markdown editing.
- **Claudia's core folder structure mirrors OpenClaw's architecture**, including: `claude.md` (master system prompt), `user.md` (personal info), `tools.md` (list of all connected tools/MCPs), `memory/` folder (daily memory files), `long-term memory file`, `.env` (API secrets), and `skills/` folder.
- **The `claude.md` file is the most critical file** — it acts as the system prompt for every session, pulls in other files by reference, and contains the memory loop instructions that tell Claudia to save one-line summaries after every interaction.
- **"Dreaming" routine:** An overnight cron/routine job that reads all daily memory files and compresses them into a long-term memory file — a lightweight but functional memory management system.
- **Tools.md is the nerve center for tool awareness:** Every time a new MCP, CLI, or API is added, Moritz just says "add this to tools.md" so the agent always knows what it can access.
- **Google Workspace CLI (GWS CLI) is described as the single most powerful tool** in the stack — it gives Claude Code full access to Google Drive, Sheets, and Docs, eliminating the need for local markdown/Obsidian files.
- **CLI access is a key Claude Code advantage over Codeium:** Claude Code can run CLI tools natively on the local machine; Codeium is sandboxed and cannot.
- **Two types of routines in Claude Code:** (1) *Local* — requires desktop app/computer to be on, can use local CLIs; (2) *Remote* — runs in the cloud via a GitHub-hosted repository, works even when the computer is off. Moritz uses a remote routine for weekly YouTube competitor tracking.
- **YouTube monitor routine:** Scrapes latest videos from specified competitor channels weekly, logs titles, views, likes, and comments into a Google Sheet for content inspiration.
- **Secrets/API keys management:** Moritz edits the `.env` file directly rather than pasting secrets into the chat. He's also setting up a dedicated 1Password vault for agents.
- **Sub-agents are overused/overrated for most people:** Moritz argues most users only need their main agent plus separate Telegram groups for context separation. He uses a separate reviewer agent only to avoid bias when evaluating his own drafted content.
- **Tool selection criteria:** Moritz now evaluates every new software tool by asking: (1) Does it have a CLI? (2) Does it have an MCP? (3) Does it at least have an API? If none of the three, he looks for an alternative.
- **Postiz CLI** is the tool used to post videos to YouTube, Instagram, and TikTok automatically. Caution advised for TikTok (API posting may hurt performance, especially on new accounts). Instagram's "Edits app" upload may also improve reach vs. API posting.
- **Memory system is simple but functional:** Daily one-line summaries per interaction, compressed nightly. Moritz acknowledges he may need a more robust system (like QMD) as file size grows.
- **GPT-4.5 (4.4 in the video's context) was notably poor** for OpenClaw use — less proactive than Opus — which accelerated Moritz's migration to Claude Code.

---

## Use cases

- **Solo content creators** who want to automate ideation, scripting, scheduling, and posting of short-form video content without a large team
- **Indie hackers/freelancers** who manage multiple tools and APIs and want a unified personal AI OS to orchestrate them
- **Productivity enthusiasts** who want an always-learning memory system that retains context across sessions without manual note-taking
- **Anyone doing repetitive file/folder management** (e.g., video upload workflows, creating Google Drive folders with correct naming conventions)
- **Newsletter writers or YouTubers** tracking competitor content for inspiration via automated weekly scraping
- **Developers or power users** migrating from OpenClaw to Claude Code who want feature parity (memory, routines, skills)
- **People managing grocery shopping or other recurring task lists** who want lightweight browser automation
- **Creators running "comment for resource" Instagram campaigns** who want to automate the Notion resource creation and ManyChat integration

---

## Patterns & frameworks

### 1. The Claude OS / "Claudia" Architecture
A personal AI operating system built on Claude Code with a layered folder structure:
- **`claude.md`** → master system prompt loaded every session; pulls in all other files
- **`user.md`** → personal context about the user
- **`tools.md`** → dynamic registry of all available CLIs, MCPs, and APIs
- **`memory/`** → daily session logs (one line per interaction) + long-term compressed memory
- **`.env`** → secrets and API keys
- **`skills/`** → reusable workflow automations (project-level or global/user-level)
- **`business/`** → domain-specific context files

### 2. The Memory Loop Pattern
After every chat interaction, the agent appends a one-line summary to a daily memory file. An overnight routine ("dreaming") compresses all daily files into a long-term memory file. This mimics OpenClaw's memory heartbeat but runs in Claude Code via routines.

### 3. Skills as Reusable Workflow Automations
Whenever a workflow is performed more than once, it gets encoded as a "skill" — a saved prompt/instruction set the agent can invoke by name (e.g., "run the video upload workflow"). Skills can be scoped to a specific project or set globally across all Claude Code projects.

### 4. The No-AI-Slop Content Flow
A semi-automated short-form video pipeline with human checkpoints:
1. **Idea capture** → via Telegram, YouTube scraper, or Twitter DMs to the bot account
2. **Weekly planning** → AI picks topics and creates a Mon–Sun schedule
3. **Script drafting** → AI generates notes → human adds detail via Whisper Flow → AI transforms notes into script style → repeat
4. **Filming** → human records on phone (~10 min per script)
5. **Video upload workflow** → skill auto-creates Drive folder named from script, human uploads files
6. **Editing** → video editor returns finished file link
7. **Posting** → Postiz CLI posts to YouTube, Instagram, TikTok with AI-generated captions
8. **Resource automation** → Notion resource + ManyChat link created automatically for "comment for resource" posts
9. **Stats tracking** → performance data logged for review

### 5. The Three-Filter Tool Evaluation Framework
Before adopting any new software tool, ask:
1. Does it have a **CLI**?
2. Does it have an **MCP**?
3. Does it have an **API**?
If none → find a different tool. This ensures every tool in the stack is agent-accessible.

### 6. Local vs. Remote Routines (Claude Code)
- **Local routines** = run on your machine when desktop app is open; full CLI/file system access
- **Remote routines** = run in the cloud via GitHub repo; always-on even when computer is off; slightly more complex to set up but enables true automation independence