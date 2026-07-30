# Turn Any Content Into Shorts in 2 Clicks With NotebookLM

Video ID: `x988XnaJyV0`

## Summary
This video demonstrates how to use Google's NotebookLM (now rebranded as Gemini Notebook) to generate short-form vertical videos from any source content in just a few clicks. The presenter walks through the manual workflow, then escalates to a fully automated pipeline using Claude with MCP, Apify for research, and FFmpeg for watermark removal. The core argument is that while the output isn't perfectly polished, the speed and zero-cost production make it viable for content creators and marketers who prioritize scale over perfection. It is most relevant to solo creators, AI marketers, and agency operators looking to automate short-form content pipelines.

## Key insights
- NotebookLM accepts diverse source types: YouTube URLs, Google Drive documents, PDFs, and pasted text — then generates videos, podcasts, slide decks, mind maps, infographics, quizzes, and more from those sources.
- The "Video Overview > Short" feature generates a complete short-form video including script, voiceover, and visuals — no manual scene direction, image generation, or editing required.
- You can supply a custom topic/focus prompt (e.g., "headline stats and benefits of Kimi K3, with a call to action to click the link") rather than accepting the AI's default suggestions.
- Multiple sources can be combined into one notebook, allowing AI to synthesize information across many YouTube videos or documents into a single cohesive short.
- Generated videos include a bottom-right watermark and a 2-second "Google NotebookLM" end screen by default; both can be removed using FFmpeg (crop bottom 45 pixels, trim last 2 seconds).
- Google accounts have daily generation limits, but this is circumvented by cycling across multiple free Google accounts.
- The entire pipeline can be automated via Claude + MCP: install the NotebookLM MCP/CLI, connect Apify as a scraper, and Claude will research YouTube videos on a topic, populate a notebook, and generate the short — all from a single prompt.
- The automated prompt example used: research YouTube videos from the last 3 months on open-source/local AI models via Apify, create a NotebookLM short-form video on recent progressions and implications.
- The presenter estimates a comparable manually edited short would cost $30–$50 to outsource; this workflow produces it for free.
- The process can be scheduled as a routine (e.g., via Hermes Agent) to run every morning, autonomously finding new content on a topic and producing fresh videos with no human input.
- The presenter uses a personal tool called Cicero (available to mastermind members) to convert voice to text for prompting, described as a "massive power-up."

## Use cases
- **Content creators** who want to repurpose long-form YouTube videos into short-form clips at scale without hiring editors.
- **Marketing agencies** producing social media shorts for multiple clients, cycling across Google accounts to stay within free tier limits.
- **Solopreneurs** who want a fully automated daily content pipeline around a niche topic (e.g., green energy news, AI model releases).
- **Thought leaders** who want to extract and redistribute key insights from third-party YouTube videos or research documents as branded shorts.
- **AI tool educators** wanting to quickly demonstrate new tool releases (as shown with the Kimi K3 and Open Claw/Hermes Agent examples).
- **Businesses** wanting low-cost explainer or promotional shorts without a video production budget.
- Anyone building **agentic content workflows** where Claude or another LLM orchestrates research, content creation, and post-processing end-to-end.

## Patterns & frameworks

**Manual NotebookLM Short Workflow**
1. Open notebooklm.google, create a new notebook.
2. Add sources (YouTube URL, PDF, text, etc.).
3. Click "Video Overview" → "Short."
4. Either accept AI-suggested topics or enter a custom focus prompt including a call to action.
5. Generate and download.

**Watermark Removal Pattern (FFmpeg)**
A two-step post-processing fix: (1) crop the bottom 45 pixels to remove the persistent watermark, (2) trim the last 2 seconds to remove the NotebookLM end screen. Can be appended to the generation prompt so it runs automatically as one step.

**Fully Automated Research-to-Video Pipeline**
A multi-tool agentic pattern: Apify (web scraper) → NotebookLM MCP → FFmpeg post-processing, all orchestrated by Claude from a single natural language prompt. The mental model is: *research → synthesize → produce → clean*, with no human in the loop after the initial prompt.

**Scale via Account Rotation**
A workaround pattern for free-tier rate limits: maintain multiple Google accounts and cycle between them to effectively achieve unlimited daily generation volume at zero cost.

**Scheduled Autonomous Content Agent**
A cron-style pattern where an agent (e.g., Hermes Agent) fires the full pipeline on a schedule — e.g., every morning, research the latest news on a topic and publish finished shorts — enabling a fully hands-off content operation.