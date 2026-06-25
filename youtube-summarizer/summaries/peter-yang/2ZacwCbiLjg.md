# Hermes Full Course: Build Your 24/7 AI Chief of Staff in 45 Minutes

Video ID: `2ZacwCbiLjg`

## Summary
This video is a complete beginner-to-intermediate course on setting up Hermes, an AI personal assistant agent, as a 24/7 "AI chief of staff." The instructor walks through installation, Telegram integration, voice replies, Google Workspace setup, and automated cron job routines. The core argument is that Hermes is more reliable and practical than alternatives like OpenClaude because it lives in messaging apps, has persistent memory, and can be made proactive through scheduled routines. It is most relevant to knowledge workers, solopreneurs, and creators who want an always-on personal AI assistant to manage email, calendar, documents, and weekly reviews.

## Key insights
- **Hermes vs. alternatives**: Hermes is preferred over OpenClaude due to stability (no breakage across updates), native messaging app integration (Telegram, WhatsApp, Slack), persistent memory, and auto-skill creation.
- **Hardware recommendation**: A Mac mini is the recommended installation platform because it runs 24/7 — critical for always-on routines and cron jobs. A VPS (~$5/month) is cheaper but requires more setup. A main laptop also works.
- **Separate credentials for safety**: The instructor creates a separate Mac username and Gmail account for Hermes ("Zoe / hayzoe@gmail.com"), granting it read-only Gmail/Calendar access and write access only to specific Drive folders — preventing accidental emails or data deletion.
- **Model choice tradeoffs**: GPT is recommended for most users ($20/month via ChatGPT subscription). Claude API works well but gets expensive fast. Hermes' own 300+ model subscription is unnecessary for most users. The instructor uses GPT-5.5 with high effort and fast mode enabled.
- **Telegram setup requires three steps**: Create a bot via BotFather (`/newbot`), get your own Telegram user ID via UserInfoBot, paste both into Hermes desktop, then restart the gateway.
- **Gateway concept**: The gateway is Hermes' bridge to messaging apps. Key troubleshooting commands: `hermes doctor --fix` and `hermes gateway restart`. Codex or Claude Code can also be used to diagnose Hermes folder issues.
- **Personalization via interview**: Ask Hermes to ask you 5 questions to learn your preferences — it saves results to `user.md`. Personality/tone is stored in `soul.md`, which the instructor populates with a custom file ("you're not a chatbot, you're becoming someone").
- **Voice replies are simple to enable**: Just tell Hermes "turn on voice replies" in Telegram — it handles the rest. Over 300 voice options available via Edge TTS (default: US Aria). Can switch between voice-only and text-only mode on demand.
- **Recommended UX tweaks**: Turn off message streaming (so responses appear all at once), suppress system/command messages for a more human feel, use WhisperFlow for voice dictation input.
- **Google Workspace setup is the most painful but most valuable integration**: Requires creating a Google Cloud project, enabling APIs individually (Gmail, Calendar, Drive, Docs, Sheets), setting up OAuth consent screen, downloading a JSON credentials file, adding yourself as a test user, and pasting an auth URL back into Hermes. Once done, Hermes can read emails, schedule meetings, and edit Docs/Sheets.
- **Google Workspace demo results**: Hermes summarized inbox action items, scheduled a Google Calendar event on command, and updated + reformatted a Google Doc vacation itinerary — though it required a follow-up prompt to fix formatting.
- **WhatsApp integration** requires a second phone number (Google Voice works) to avoid confusion with personal contacts.
- **Slack advantage over Telegram**: Slack supports threaded conversations, allowing multiple simultaneous commands — more structured than Telegram's one-at-a-time flow.
- **Granola (meeting notes app)** is the easiest integration — one MCP line connects it. Enables querying past meeting action items and prep for upcoming meetings.
- **GitHub integration** is used primarily for backing up the entire Hermes setup to a private repo, not for coding workflows (Codex/Claude Code are preferred for that).
- **YouTube integration** uses either the YouTube API (via Google Cloud Console) or `yt-dlp` to extract video transcripts for research.
- **Cron job creation process is always three steps**: (1) Build a skill, (2) test it manually to verify output quality, (3) ask Hermes to schedule it as a recurring cron job.
- **Weekend Planner cron job**: Searches for family-friendly Bay Area activities (within 30–60 min of a specific location, for kids aged 4 and 8), sent every Friday at 8 a.m. — no tool integrations required, uses web search only.
- **Morning Briefing cron job**: Pulls from Google Calendar and Gmail to surface top 3 action items, upcoming meetings, and open email threads needing response.
- **Business Review cron job**: Integrates Google Workspace, Mercury (income/expenses), YouTube (channel outlier videos), Substack (via browser automation), Granola (meeting notes), and Google Docs (strategy context) into a weekly email summary.
- **Health Review cron job**: Pulls weight data from Withings API and workout data from a custom vibe-coded fitness app with MCP, delivers a weekly email with training consistency and body composition trends.

## Use cases
- **Solopreneurs and creators** who want automated weekly business/health/content reviews delivered by email
- **Knowledge workers** managing high email/calendar volume who want daily briefings and meeting scheduling via chat
- **Remote workers** who prefer managing tasks from a phone while walking or away from desk
- **Families** wanting automated weekend activity recommendations based on location and kids' ages
- **Anyone running a Mac mini** as a home server who wants to maximize it with always-on AI routines
- **Non-technical users** who want an AI assistant without writing code — all setup is done via natural language commands to Hermes itself
- **Fitness-conscious users** who track weight and workouts and want automated weekly progress summaries
- **Team leads or managers** who want Slack-integrated AI that can handle threaded, parallel task queues

## Patterns & frameworks

**The "Separate Credentials" Safety Pattern**
Give Hermes its own OS user account and Gmail address. Grant only the minimum permissions needed (read-only email, write access to specific Drive folders only). This prevents accidental destructive actions while still enabling powerful integrations.

**The Gateway Model**
Hermes uses a persistent "gateway" process to bridge messaging apps (Telegram, WhatsApp, Slack) to the AI model. Understanding this explains most connectivity issues — nearly all bugs are fixed by restarting the gateway (`hermes gateway restart`) or running `hermes doctor --fix`.

**The Three-Step Cron Job Pattern**
For any proactive automation: (1) Build a skill and define what it should do, (2) run the skill manually and iterate until the output is good, (3) ask Hermes to schedule it as a cron job at a specific day/time. This applies universally — from a simple weekend planner to a complex multi-source business review.

**The Interview-Then-Save Personalization Model**
Have Hermes ask you structured questions (e.g., "ask me 5 questions") to capture preferences, then verify the answers were saved to `user.md`. Separately, populate `soul.md` with a personality definition to shape tone and behavior across all interactions.

**The Skill-First Automation Philosophy**
Never create a scheduled routine without first building and testing a standalone skill. The skill is the reusable unit; the cron job is just the scheduler. Testing manually first prevents bad output being delivered on autopilot.

**The Layered Integration Stack**
The recommended integration order reflects value vs. setup cost: (1) Voice replies [easy, high value], (2) Google Workspace [hard, highest value], (3) Messaging apps [medium], (4) Niche tools like Granola, GitHub, YouTube [easy, incremental value]. This creates a compounding stack where later integrations (cron jobs) leverage earlier ones (Gmail, Calendar).