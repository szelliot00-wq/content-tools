# This Claude Code Skill Automates Social Media Posting

Video ID: `GQfayD4FUg0`

## Summary
This video demonstrates a Claude Code "skill" (an AI-powered automation system) that handles end-to-end social media content creation and publishing. The creator, Matt, walks through how the tool researches a topic, drafts posts across six platforms, generates images, stores content in Notion for review, and then publishes via a scheduling tool called Blotato. The core argument is that ~90% of social media work can be automated while keeping a human review step to catch AI errors. It is most relevant to content creators, solo marketers, small business owners, and anyone who previously spent significant manual time on social media management.

## Key insights
- **The skill automates the full pipeline**: research → content drafting → image generation → Notion storage → human review → scheduled publishing, all triggered from a single prompt in Claude Desktop
- **Grok is used for research** (specifically Grok 4.1 Fast via OpenRouter) because it has the best web search capability and is dramatically cheaper than Claude Opus — $0.20/1M tokens in and $0.50/1M tokens out vs. $5/$25 for Opus 4.7, making it over 10x cheaper
- **Grok 4.1 Fast is being phased out**; the creator recommends migrating to Grok 420 as the next best alternative
- **Image generation uses Nana Banana 2 (technically Gemini 3.1 Flash Image Preview)** via OpenRouter — described as the highest-ranking image model but also the cheapest; the skill defaults to generating two infographic images but can be scaled up
- **OpenRouter is used as a unified API layer** so only one API key is needed to access all models (Grok, Nana Banana 2, Claude), eliminating the need to manage multiple API credentials
- **Claude handles the actual writing** because it remains the best writing model and the task isn't compute-intensive enough to justify concern over cost
- **Six content formats are produced by default**: X (Twitter) posts, Facebook posts, email newsletter, Instagram carousel, TikTok carousel, and YouTube script
- **An HTML preview is generated in real time** inside Claude's right panel, showing mockups of each post format so the user can visually review before publishing
- **Notion serves as the human-in-the-loop editing layer**: content is pushed to Notion, the user edits or deletes items there, and when publishing is triggered, the skill reads the updated Notion content and posts those changes
- **Blotato is the publishing/scheduling tool**; it handles image hosting and post scheduling. Litterbox (a temporary 72-hour file host) serves as a backup image host if Blotato is unavailable
- **Two local config files customize output quality**: `brand_guidelines` (voice, colors, fonts, aesthetics, do's/don'ts) and `content_formats` (platform-specific formatting instructions) — these are editable to tailor output to any brand
- **The skill is installable via a GitHub repo URL** pasted directly into Claude with the instruction to "install this skill locally," ideally in a dedicated folder
- **Human review is explicitly recommended** — the creator warns against auto-firing posts due to hallucinations and unexpected AI behavior
- **Voice input is a supported workflow**: tools like Whisper Flow or Super Whisper can be used to dictate ideas directly into Claude instead of typing
- **Future extensibility is flagged**: the system can be connected to HeyGen for AI video generation and HyperFrames for motion graphics to produce full YouTube videos

## Use cases
- **Solo content creators** who need to repurpose a single piece of content (e.g., a tweet or news article) into posts across multiple platforms simultaneously
- **Small business owners** who lack a dedicated marketing team but need consistent social media presence
- **Former or current marketing agency operators** looking to dramatically reduce the hours spent on manual content production
- **Developers or technical marketers** who want a customizable, self-hosted content automation template they can modify for specific brand voices or platforms
- **Newsletter writers** who want to auto-generate accompanying social content from the same source material
- **Anyone managing multiple brand accounts** who needs a scalable, repeatable workflow with a built-in review checkpoint
- **Marketers experimenting with AI toolchains** who want to learn how to chain multiple models (research model + writing model + image model) for cost-efficient output

## Patterns & frameworks

### Two-Mode Architecture: Create Mode → Publish Mode
The skill is split into two distinct operational phases. **Create Mode** handles all content generation (research, writing, image creation, Notion upload, HTML preview). **Publish Mode** is triggered separately by the user after review and handles reading updated Notion content, retrieving image URLs from Blotato, and scheduling/publishing posts. This separation intentionally inserts a human review gate between creation and publication.

### Tiered Model Selection by Task Type
A cost-and-capability optimization pattern: assign each task in the pipeline to the cheapest model that can do it well. Research → Grok (cheap + best web search). Image generation → Nana Banana 2 (cheapest high-quality image model). Writing → Claude (best writer, used only where necessary). This prevents over-spending on a single premium model for every step.

### Local Config Files as Brand Memory
Rather than re-prompting brand context every session, two persistent local files (`brand_guidelines` and `content_formats`) encode brand identity and platform-specific formatting rules. These files are read by the skill automatically, acting as persistent "memory" that shapes every piece of output without user intervention.

### Notion as the Human-in-the-Loop Buffer
Content is pushed to Notion not just for storage but as a structured editing interface between AI output and live publishing. The publish step explicitly reads from Notion, meaning any edits made there are automatically incorporated — creating a clean handoff pattern where AI drafts and humans refine before anything goes live.

### "Explain This Skill" Meta-Prompt for Learning
A reusable learning pattern: navigate to any skill's local folder in Claude Code and prompt "explain this skill and give me a visualization with diagrams." Claude will generate an HTML overview of how the skill works without modifying it — useful for onboarding, debugging, or understanding any unfamiliar automation.