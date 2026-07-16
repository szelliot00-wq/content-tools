# How I Use ChatGPT Work and GPT-5.6 to Do Everything (Beginner Tutorial)

Video ID: `WLg9qWOf6zw`

## Summary
This beginner tutorial by a product manager with 10+ years of experience covers how to use ChatGPT Work and Codex (powered by GPT-5.6) as a personal operating system for daily computer tasks. The core argument is that Codex, combined with plugins and scheduled tasks, can act as an AI chief of staff that manages email, calendar, content prep, and website creation — reducing manual effort across dozens of workflows. The presenter walks through setup, model selection, plugin configuration, thread organization, and progressively more advanced automation. It is most relevant to non-technical knowledge workers, product managers, and creators who want to offload repetitive digital tasks without needing to code.

## Key insights
- **Chat vs. Work vs. Codex distinction is minimal**: The only real UI difference is that Codex has a "Pull Requests" page for code review; functionally they are nearly identical. The presenter recommends just using Codex.
- **GPT-5.6 has three models (Soul, Terra, Luna) with five effort levels each**: The recommended default is **Soul at medium effort** — best balance of intelligence and token efficiency. Switch to Soul at high effort only for heavy planning or long builds.
- **Custom instructions are essential personalization**: The presenter's instructions include: describe the user's background (product + creator), avoid code blocks for non-code content, be candid and push back rather than agreeing reflexively, write in plain active voice, and eliminate AI filler phrases ("This isn't about X, it's about Y," em dashes, throat-clearing).
- **Plugins are the core power unlock**: The presenter has 23 plugins installed. Minimum recommended set: Gmail, Google Calendar, Google Docs, Slides, Sheets, and Google Drive. Additional high-value plugins: Slack, Notion, Figma, RemNote, PDF tools.
- **One long-running thread per workflow beats many short threads**: Codex compacts previous messages while retaining context, enabling very long threads without confusion. Threads are organized inside projects (e.g., "Personal OS," specific products/apps).
- **Chief of staff thread for email management**: A single thread can scan the last 3 days of email, surface the top 5 action items, identify unsubscribe candidates, and even auto-click unsubscribe buttons via the browser — all without opening Gmail.
- **Voice and tone training via a slash skill**: By asking Codex to review sent emails and build a `/email` skill, the model learns personal writing style (e.g., more casual with known contacts, more formal with strangers) and applies it to future drafts.
- **Calendar booking via natural language**: Booking a meeting requires only a conversational prompt — Codex finds the contact's email, checks for scheduling conflicts (including personal commitments like school drop-off), creates the event, and adds a Google Meet link automatically.
- **Bulk calendar population**: The presenter had Codex find and add all upcoming World Cup quarterfinal-onwards matches to Google Calendar as optional events — a task that would have taken 5–10 minutes manually, done in 1–2 minutes.
- **Podcast prep skill**: Codex scans the next 7 days of calendar for podcast interviews, researches each guest (using X/Twitter posts and reference material), proposes YouTube title/thumbnail angles, and produces a complete guest-facing interview guide uploaded directly to Google Docs.
- **Scheduled tasks are the highest-leverage feature**: The presenter schedules a Friday 7 a.m. task that combines email triage (top 5 action items + unsubscribes) and calendar prep (auto-run podcast prep for any upcoming interview). People on the Codex team reportedly run daily scheduled tasks across Slack, email, and meeting transcripts to prioritize their day.
- **The pattern: manual first, then schedule**: Always do the workflow manually with Codex first to validate quality, then ask Codex to schedule it as a recurring task.
- **Phone access via "Remote" mode**: The ChatGPT mobile app has a "Remote" section that connects to desktop Codex threads — but requires the laptop to be on. The presenter uses **Amphetamine** (a Mac keep-awake utility) to keep the laptop running while away.
- **Sites feature for free web publishing**: Codex can generate and publish websites (publicly or privately) directly from a conversation. Examples: a Japan travel catalog, a safari-themed multiplication table game built with a child, and an interactive HTML-based PRD.
- **Interactive HTML PRDs over Google Docs**: The presenter is moving away from text-based PRDs toward interactive sites with tabs for product requirements, design (style guide + component library), and tech stack. Component library defined before mocking keeps designs consistent. OpenAI and Anthropic teams are reportedly doing the same internally.
- **No-AI-slop GitHub tool**: The presenter has published a free tool on GitHub that removes 20+ common AI filler phrases — useful for editing AI-generated writing.

## Use cases
- **Email triage**: Surfacing follow-up action items from the past few days without opening Gmail
- **Bulk unsubscribe**: Automatically clicking unsubscribe across multiple marketing emails in one command
- **Follow-up email drafting**: Finding old email threads and drafting context-aware replies in the sender's voice
- **Meeting scheduling**: Booking calendar events with conflict detection and auto-generated video call links
- **Event research and calendar population**: Adding recurring events (sports fixtures, conferences) to the calendar in bulk
- **Podcast/interview prep**: Researching guests, drafting questions, and producing interview guides auto-saved to Google Docs
- **Weekly AI briefing**: Scheduled Friday digest combining email action items and upcoming meeting prep
- **Mobile productivity**: Managing Codex workflows from a phone while away from the desk
- **Children's education**: Building interactive learning games (e.g., multiplication tables) tailored to a child's interests
- **Travel planning**: Creating shareable interactive travel guides instead of plain lists
- **Product planning**: Replacing static Google Doc PRDs with interactive, tabbed HTML sites covering requirements, design system, and tech stack

## Patterns & frameworks

**Soul Medium Effort as Default Model**
A simple decision rule for GPT-5.6 model selection: use Soul at medium effort for everyday tasks (best intelligence-to-token ratio), escalate to Soul at high effort for planning-heavy or long-form builds, and ignore Terra and Luna unless a specific use case demands them.

**One Thread Per Workflow**
Rather than creating new threads for every task, maintain one long-running thread per recurring workflow (e.g., one for email/calendar, one for newsletter editing, one per podcast guest). Codex's context compaction keeps threads functional indefinitely without losing continuity.

**Manual → Skill → Schedule progression**
A three-stage automation ramp: (1) do the task manually with Codex to validate output quality, (2) codify it as a named slash skill with explicit voice/style rules, (3) schedule it as a recurring task so Codex runs it proactively. Applied to email triage, podcast prep, and calendar management in the video.

**Chief of Staff Thread**
A single dedicated Codex thread that serves as the primary interface for managing email and calendar — replacing the need to open Gmail or Google Calendar directly. Combines email triage, unsubscribing, follow-up drafting, meeting booking, and scheduled weekly briefings in one persistent thread.

**Skill Creation and Testing Loop**
When training Codex on personal style (e.g., email voice), the workflow is: ask Codex to review existing examples → let it draft a named skill → test the skill on a real example → iterate until output matches desired style. The presenter explicitly warns against skipping the testing step.

**Interactive PRD Format**
A new PRD structure replacing Google Docs markdown with a multi-tab HTML site covering: (1) product requirements (problem, goal, solution, user stories), (2) design (principles, style guide, component library), and (3) tech stack with data schema and trade-off rationale. Component library is defined before mocks to enforce visual consistency.