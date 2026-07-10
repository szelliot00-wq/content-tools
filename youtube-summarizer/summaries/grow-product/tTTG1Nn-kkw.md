# Everyone's Using Claude. This PM Tool Does More

Video ID: `tTTG1Nn-kkw`

## Summary
This podcast episode features Mangto (Mang), a technical designer-turned-founder, walking through his end-to-end AI-powered product management and content creation workflow centered on OpenAI's Codex. The core argument is that "technical PMs" — those who understand AI tooling, models, and agentic workflows — are the ones keeping their jobs and thriving, while non-technical PMs are being laid off. Mang demonstrates how Codex functions as an all-in-one command center connecting to local files, apps, and a fleet of simultaneous AI agents to handle everything from app planning to slide generation to avatar creation. The episode is most relevant to PMs, founders, and builders who want to leverage AI tools to 10x their output without writing code themselves.

---

## Key insights

- **Technical PMs vs. non-technical PMs**: Companies are retaining technical PMs — not those who write code, but those who understand AI models, tooling jargon (GPT 5.5, image 2.0, MCP, computer use), and agentic workflows. Non-technical PMs are being cut (e.g., 10% layoffs at Meta, similar at Oracle).
- **Codex as "ChatGPT on steroids"**: Codex is Mang's primary tool — it goes beyond chat to create HTMLs, slides, full apps, videos, and manage local files, all within a project-based interface. It is not just a chatbot but an orchestration layer.
- **Everything local = more power**: The key insight from OpenClaw/Claude Code's workflow philosophy is that keeping all files local (vs. in a cloud database) gives the AI more context, more privacy, and more processing power. Obsidian is used to organize the local markdown documents Codex generates.
- **Fleet of simultaneous agents**: Rather than one task at a time (the old Figma/VS Code model), Mang runs 20 agents simultaneously — each working on a different project or output. This "clones" the PM's cognitive capacity.
- **Token tiers match use case**: Codex has Low/Medium/High/Extra High compute settings. $20/month users should use Medium; $200/month power users running agent fleets should use Extra High for maximum accuracy.
- **Plan mode before building**: Always start with "I want to plan this" before any coding or generation task. This prevents wasted tokens, surfaces questions early, and ensures human approval of the architecture before execution.
- **Screenshot > typing > voice**: The hierarchy of context-giving: (1) Screenshots are most information-dense (a new Codex shortcut auto-captures the focused browser window), (2) Voice via Whisper Flow is faster than typing and captures more nuance, (3) Typing is the slowest and least recommended.
- **Whisper Flow for context-rich prompting**: Whisper Flow (voice-to-text tool) is used heavily because humans think faster than they type. It also learns custom dictionaries (e.g., correcting unusual names) and formats speech cleanly into prompts.
- **Skills vs. Plugins in Codex**: Plugins are deeply integrated third-party backends (Slack, Figma, Chrome, Linear). Skills are lightweight, user-creatable files (markdown/prompts) that give the AI domain-specific instructions — e.g., a "taste skill" for design quality, Swift UI skills, Playwright skills. Mang updates skills whenever he notices the AI lacking knowledge in a domain.
- **Taste skill for design quality**: A publicly available GitHub skill (design taste + front-end) that instructs the AI to apply senior designer aesthetics — better fonts, typography, layout — to generated slides and UI. It meaningfully improves output quality with no extra effort.
- **HTML is the fastest export format**: For slides and presentations, generating HTML is faster, uses fewer tokens, and gives the most control vs. PowerPoint or Keynote. From HTML, you can then export to PPTX or open in Keynote.
- **Image 2.0 for avatar/digital twin creation**: GPT Image 2.0 is used to generate photorealistic AI avatars from a headshot. The avatar can be used for UGC-style video content, Loom replacements, and team presentations — removing the need to "do your hair" or have perfect lighting.
- **AI video pipeline**: Slides → HTML/images → video via tools like Hyperframes or HeyGen. HeyGen is the recommended tool specifically for lip-synced avatar presentations. Sora/Kling is best for cinematic or creative video. Google V/Omni for general video generation.
- **Codex mobile via ChatGPT app**: A Codex button inside the ChatGPT mobile app connects to your desktop Codex instance. You can manage and continue all projects from your phone while the actual computation runs on your computer (computer must be on with screen-lock permissions enabled).
- **Computer use for QA and testing**: Computer use (AI controlling your mouse/keyboard) is used for testing user flows — the agent navigates a live app, identifies bugs, and fixes them, replicating what a QA engineer would do step by step.
- **Atlas AI browser for contextual browsing**: OpenAI's Atlas browser lets you ask AI questions about whatever you're viewing, or hand off full computer control, making web research and task execution seamless.
- **Gmail integration with trust guardrails**: Mang uses Codex's Gmail plugin to auto-reply to customer support emails and failed payment notifications. He was initially skeptical due to prompt injection risks (a concern with OpenClaw) but trusts Codex because OpenAI's accountability enforces guardrails and permission prompts.
- **PM-to-founder pathway**: The end game Mang describes is PMs starting their own companies. AI handles accounting, paperwork, marketing, and "janitor tasks." The human's job is the last 8–10%: quality assurance, domain expertise, taste, and orchestrating the agent fleet.
- **Mang's own products**: He has built Aura, New Form, and DreamCut — each with "way over 10,000 prompts" — generating over $1M/year with a team of six, without writing a single line of code in the past six months.
- **Digital twin ethics warning**: Mang flags that AI-generated avatars used to promote fake products will face FCC pushback and regulatory scrutiny. Legitimate use cases (team presentations, screen recordings with narration) are fine; deceptive commercial use is not.

---

## Use cases

- **PMs building their first app**: Use Codex's plan mode to architect an iOS/Android/web app idea before writing a line of code, validate the plan interactively, then execute.
- **Content creators and PMs making presentations**: Pull real revenue/user data from local folders, generate slides with the taste skill, export to HTML or PPTX, and iterate with screenshots.
- **Remote teams replacing Loom recordings**: Generate an AI avatar clone of yourself using Image 2.0 and HeyGen, pair with screen recordings, and produce polished team update videos without needing camera-ready appearances.
- **PMs doing QA and user flow testing**: Use computer use to have the AI agent navigate your live product, reproduce bugs, and fix them automatically.
- **Founders managing company documents**: Organize invoices, receipts, contracts, team context, and customer support tickets into local project folders so AI agents have full context for any task.
- **PMs managing customer support at scale**: Use Gmail + Codex to auto-generate smart AI replies to common support tickets or payment failure emails.
- **Non-technical PMs becoming technical**: Use plan mode, voice prompting, and screenshot-driven iteration to direct agents without knowing how to code — building the "technical PM" skillset the market now requires.
- **Indie hackers and solo founders**: Run a fleet of 20 simultaneous agents across marketing, coding, content, and customer support to operate like a larger team.
- **Designers exploring divergent app UI ideas**: Use image generation + taste skill to rapidly produce multiple design directions before committing to any implementation.
- **YouTube/newsletter creators**: Use Codex to generate video scripts, podcast prep docs, hooks, talking points, and research documents from a single voice prompt.

---

## Patterns & frameworks

**1. Plan → Question → Build (3-step pre-build protocol)**
Before any generation or coding task, always: (1) Start in plan mode ("I want to plan this"), (2) Ask clarifying questions to steer the AI before it codes, (3) Approve the plan, then execute. This prevents token waste and ensures human oversight at the architecture stage.

**2. Local-first context architecture**
All files, documents, and project assets live on your computer in organized folders (Projects > [App Name], Content, Customer Support, Company, Skills). Codex, Obsidian, and other tools read from these local folders. This maximizes AI context, keeps data private, and avoids dependence on cloud databases. Introduced broadly by OpenClaw's workflow philosophy.

**3. Fleet-of-agents model**
Instead of one task at a time, run 20+ Codex agents simultaneously across different projects or output types (slides, code, documents, images). The PM's role shifts from doing work to managing and QA-ing the agent fleet — "cloning yourself" as an orchestrator.

**4. Screenshot → Voice → Text (context hierarchy)**
When providing feedback or instructions: screenshots give the most information per token (use the auto-capture shortcut), voice via Whisper Flow is second (faster, richer than typing), and typed text is last resort. The richer the context, the fewer correction loops.

**5. Image first → HTML export → Video pipeline**
For presentation creation: (1) Generate slide images with Image 2.0 + taste skill, (2) Iterate on design with screenshot feedback, (3) Export to HTML (fastest, fewest tokens, most control), (4) Optionally convert to PPTX/Keynote, (5) Feed images/HTML into a video tool (Hyperframes, HeyGen) to produce a narrated video with avatar.

**6. Trust ladder for AI permissions**
Permission levels scale with experience and use case: New users start at Default/Standard (low trust, more prompts). As trust builds, move to Medium or High. Power users with $200/month plans and complex multi-agent workflows use Full Access + Extra High compute. Token cost and accuracy both increase with permission level.

**7. The 5-star → 11-star quality framework (borrowed from Airbnb's Brian Chesky)**
Define what a 5-star experience looks like (the baseline), then imagine 6, 7, 8, 9, 10, 11-star experiences. The PM's job is to always deliver above the 5-star baseline and keep pushing toward 11-star. As AI raises the baseline floor, the ceiling also rises — the human's role is maintaining taste and judgment above whatever the new floor is.

**8. Domain expertise as moat**
AI amplifies your existing knowledge; it doesn't replace it. The formula for founder success: be the world's best at your specific domain (coffee, PM, law, design) → deploy a fleet of agents to execute → use your domain taste for the last 8–10% of QA and decision-making. Without the domain expertise, there is no moat and no leverage.

**9. Skills as reusable AI instruction files**
Skills are lightweight markdown/prompt files stored locally that teach Codex domain-specific knowledge (design taste, Swift UI patterns, Playwright testing, animation libraries). Update them whenever you notice an AI knowledge gap. They are composable — stack a taste skill + front-end skill + copywriting skill for a landing page task.