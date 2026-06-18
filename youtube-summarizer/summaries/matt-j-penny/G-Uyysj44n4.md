# I Tried 600 Claude Skills. I Can't Live Without These 8

Video ID: `G-Uyysj44n4`

## Summary
The creator shares 8 Claude Code skills he considers essential after testing over 600 over 9 months, framing them around a central argument: generic, off-the-shelf AI skills provide modest value, but personalized skills built around your own business processes are transformative. He demonstrates each skill with live walkthroughs and consistently emphasizes customization and compounding value over time. The video doubles as a pitch for his Applied AI Mastermind course, which includes a library of ~650 skills. It is most relevant to content creators, solopreneurs, and small business owners who want to automate repeatable workflows using AI agents.

## Key insights
- **Most AI skills are not worth your time.** Out of 600+ tested, only a small subset deliver real, recurring value — the rest are novelties.
- **The "Last 30 Days" skill** scrapes Reddit, X, YouTube, Hacker News, Polymarket, and other platforms to surface timely trends and sentiment from the past 30 days — solving the core problem that LLMs are limited to training data or shallow web searches.
- **Combining skills multiplies value.** Example given: pair the Last 30 Days research skill with a social media post creator skill to produce timely, high-quality posts far faster than either skill alone.
- **The Compound Engineering skill** inverts the typical "vibe coding" problem where added features increase complexity and bugs. Its workflow — brainstorm → plan → build → review → compound — learns from each session so subsequent builds become easier, not harder.
- **The Front-End Slide skill** generates HTML-based slide decks (with animations, interactive elements, images) in ~1–2 minutes. The key unlock is building a personal style guide so the tool learns your preferences over time, reducing iteration rounds with each use.
- **Hyperframes edits video at ~1/1000th the cost of a human editor.** The creator fired a human editor in favor of it, citing ~$0.20 per video vs. ~$200 for a human. Quality is described as "close enough," not equal. Videos are built in HTML, making edits as simple as text instructions.
- **The Notebook LM skill** wraps Google's Notebook LM in an agentic interface, allowing you to programmatically create notebooks, pull data sources (e.g., via Apify web scraping), and query them — all within a single prompt, without touching the Notebook LM UI.
- **Matt's Metrics** is a fully bespoke skill connecting all his business data (website, YouTube, newsletter, mastermind) into one queryable interface — enabling questions like "which of my recent YouTube videos outperformed average, and what patterns explain that?"
- **The MCP Builder** is described as the most important skill for business owners. It creates a single data and tool layer accessible by any AI agent (Claude, Grok, Cursor, Codex, etc.), so switching to a better future AI tool requires only re-pointing it at the existing MCP rather than rebuilding everything.
- **The Post Uploader** is a bespoke YouTube upload automation: given an MP4, it strips audio, transcribes it, flags editing errors (stutters, repeated phrases, dead air), writes a description, generates chapters, and suggests titles and thumbnail ideas — saving ~20 minutes per upload, several times a week.
- **The Skill Creator skill** is the meta-tool that ties everything together. Feed it an existing SOP (standard operating procedure) and optionally a similar skill from a database, and it generates a personalized skill built around your exact workflow.
- **20 minutes saved per task adds up fast.** The creator estimates that stacking multiple small time-savings (20 min here, 30 min there) returns 6–8 hours per week that can be reinvested in revenue-generating activities.
- **Personalization is the holy grail.** A skill that knows your tone, format, standards, customers, and products is categorically more valuable than a generic downloaded skill. The goal is to build tools around your business, not adapt your business to fit the tool.

## Use cases
- **Content creators / YouTubers** — automating video editing (Hyperframes), upload metadata generation (Post Uploader), and slide creation for courses or explainer videos (Front-End Slide).
- **Marketers and social media managers** — using Last 30 Days to find trending topics and sentiment, then feeding output into a post-creation skill for timely, relevant content.
- **Solopreneurs and small business owners** — building a personal metrics dashboard (Matt's Metrics model) to query all business data in one place and identify what's working.
- **Consultants and agency owners** — using Notebook LM skill to ingest client data or research sources and query them programmatically; creating client-facing slide decks from the output.
- **Anyone with documented SOPs** — feeding existing standard operating procedures into the Skill Creator to produce automated, bespoke workflows.
- **Builders using multiple AI tools** — using the MCP Builder to create a shared data/tool layer so switching between Claude, Grok, Cursor, or future tools requires no rebuild.
- **Researchers or knowledge workers** — using the Notebook LM skill combined with Apify scraping to auto-build research notebooks and query them without manual data entry.

## Patterns & frameworks

**Compound Engineering Loop**
A 5-stage development cycle: Brainstorm → Plan → Build → Review → Compound. The "Compound" stage is the differentiator — it encodes learnings back into the system so each subsequent build starts from a stronger baseline. Explicitly designed to counter the "vibe coding" anti-pattern where complexity and bugs accumulate over time.

**Skill Personalization Ladder**
A progression from generic → customized → bespoke. Generic skills (downloaded from a library) save some time. Customized skills (generic + your style guide or preferences layered in) save more. Fully bespoke skills (built around your specific SOPs, customers, tone, and data) are described as the "holy grail" — offering the highest time savings and lowest friction.

**SOP-to-Skill Pipeline**
The repeatable process for automating any existing workflow: (1) identify a high-time-cost manual process, (2) document or locate its SOP, (3) find the nearest existing skill in a library as a starting template, (4) run it through the Skill Creator skill with your SOP layered in, (5) deploy and iterate. Output is a skill that no one else has, tuned to your exact way of working.

**MCP as an AI-Agnostic Data Layer**
Rather than building workflows that are tightly coupled to one AI tool, the MCP (Model Context Protocol) pattern centralizes all data and tools in a single interface. Any AI agent — current or future — can be pointed at it. This is positioned as future-proofing against the rapid turnover of best-in-class AI tools.

**Skill Chaining / Composability**
Multiple skills are treated as modular building blocks that can be piped together. Example pattern: Last 30 Days (research) → Social Media Post Creator (output). Another: Notebook LM skill (query) → Front-End Slide skill (presentation). The value of any individual skill increases when it can feed into or receive output from another.

**Style Guide as Memory**
For output-quality skills (slides, video, writing), the creator uses a persistent style guide document that the skill reads on each invocation. Over time, this guide is refined so the tool's output converges on the desired result faster, reducing manual editing rounds — effectively giving the skill long-term memory about aesthetic and format preferences.