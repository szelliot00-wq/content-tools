# ChatGPT vs Claude vs Grok vs Gemini: The Best AI for 10 Use Cases (August 2026)

Video ID: `nAhQs8Fd_9g`

## Summary
This video compares ChatGPT, Claude, Grok, and Gemini across 10 practical use cases through live demos, declaring a winner for each. The presenter, Peter, argues that the "best AI" is highly use-case-dependent and that his preferences have shifted significantly — ChatGPT has displaced Claude as his default tool for most tasks. The video is most relevant to knowledge workers, content creators, and non-technical builders who use AI daily for productivity, not to engineers reading code.

## Key insights
- **ChatGPT wins 6 of 10 categories**: everyday answers, writing/editing, coding, browser/computer use, voice chat, image generation, and personal agents — a major reversal from a few months ago when Claude dominated.
- **Claude still wins design and planning**: Claude Code and Claude Design produce more functional, animated prototypes and slides. Claude Fable 5 can generate full product launch videos from text instructions.
- **Grok surprised on design**: Grok generated the most visually impressive zero-shot app prototype by combining layout quality with built-in image generation, beating ChatGPT and Claude on raw first-pass output.
- **Gemini wins video generation**: When asked to make a "crazy Japanese ramen commercial" using a photo of the presenter, Gemini's output was entertaining and coherent; Grok's was distorted and unsettling.
- **Claude's personality has degraded**: The presenter finds Opus 5 too judgmental and over-reliant on phrases like "here's the honest truth." He preferred Opus 4.6's personality. ChatGPT fixed its most annoying habit (appending "I can also do X" to every response) and now feels more natural.
- **Claude's writing has picked up "Claudisms"**: Phrases like "the uncomfortable reality" and "this is X not Y" have made Claude's writing feel formulaic, pushing the presenter to ChatGPT for editing.
- **Claude Fable caught a planning detail ChatGPT missed**: When given the same planning document, Fable identified a specific operational gap (losing a video ops/VA hire after August 19th) that ChatGPT overlooked — evidence Fable reasons more carefully about complex, nuanced decisions.
- **ChatGPT's browser use is transformative**: A cited example shows someone preparing a full US immigration package (normally hours or days of work) in minutes by having ChatGPT scrape 7 years of tax returns, bank statements, and documents.
- **Voice orchestration in ChatGPT desktop app**: The presenter uses a live voice thread to orchestrate multiple other agent threads simultaneously — e.g., starting a newsletter edit, a chief-of-staff follow-up, and a skill-development check in one spoken sentence.
- **Grok is preferred by at least one senior engineer**: The presenter's friend (a former L8 engineer) prefers Grok over GPT-4 for coding because GPT-4 and Opus tend to over-engineer, making 500K-line changes when small, targeted edits are needed.
- **Claude lacks image generation**: This is called out as a concrete competitive disadvantage in design, infographic creation, and any visual workflow.
- **Custom instructions meaningfully improve AI personality**: Adding three directives to ChatGPT (be candid, write in active voice, avoid AI slop words like "delve/foster/leverage") produces noticeably better outputs.
- **Personal agent race is about the harness, not the model**: ChatGPT desktop app wins because of browser use, voice, and mobile. GrokBot has cleaner UX and a dedicated cloud computer per agent but is less flexible (single thread per agent). Gemini's "Spark" integrates with Google Workspace but lacks plugins. Claude Code is playing catch-up.
- **The "no AI slop" skill has 5,000+ GitHub stars**: A free open-source tool the presenter built that strips common AI filler patterns from outputs.
- **$20/month ChatGPT plan is called the best value**: Access to all the winning features at that price tier is described as a genuinely good deal for most users.

## Use cases

- **Non-technical builders** shipping apps or tools without reading code — use ChatGPT (GPT-4 So) for end-to-end coding with browser-based self-testing.
- **Content creators** producing newsletters, blog posts, or social media — use ChatGPT with a personal writing style skill to match your voice.
- **Slide deck creation** — use Claude with a brand/style template for more animated, polished HTML slides.
- **Product or app prototyping** — use Grok for a quick, visually impressive first pass with real images; use Claude Design for a more guided, clarifying-question-driven workflow.
- **Strategic planning and difficult decisions** — use Claude Fable for nuanced analysis of complex documents where missing a detail has real consequences.
- **Immigration paperwork, government forms, healthcare portals** — use ChatGPT's browser use to automate navigation and form-filling.
- **Social media cross-posting** — use ChatGPT browser use to draft and post across X, LinkedIn, Threads, and Substack simultaneously, with platform-specific nuance (e.g., handle tagging).
- **Video production** — use Claude Fable 5 with the HyperFrames skill for animated product launch videos; use Gemini for short fun/family video generation.
- **Infographic creation from long-form text** — use ChatGPT if it has context on your brand guidelines; Gemini's "nano banana" model is a capable alternative with proper instruction.
- **Hands-free afternoon work sessions** — use ChatGPT voice in the desktop app to dictate instructions while walking or resting, having it orchestrate multiple named threads in parallel.
- **Engineers making targeted code changes** — consider Grok over ChatGPT/Claude to avoid over-engineered, bloated diffs.

## Patterns & frameworks

**Skill files (personal AI skills)**
Reusable prompt templates stored as files and referenced in conversations. The presenter uses a "newsletter skill" (writing style guide built from personal examples), a "slide skill" (brand/HTML template), a "social post skill," a "video intro skill," and a "human review skill." Each encodes domain-specific instructions so the model consistently follows a repeatable process without re-prompting from scratch. Skills are composable — the newsletter skill calls the "no AI slop" skill internally.

**Plan with Fable, build with GPT**
A two-phase AI workflow for product development: use Claude Fable for upfront strategic planning and long-horizon thinking, then hand off implementation to ChatGPT (GPT-4 So) for agentic coding with browser-based self-testing. Keeps the smartest model on the hardest reasoning and the most autonomous model on execution.

**Voice orchestration thread**
A meta-agent pattern where a single live voice conversation in the ChatGPT desktop app acts as a controller, issuing instructions to multiple named specialist threads (newsletter, chief of staff, skill dev). Enables hands-free, ambient work orchestration — speak once, multiple agents act.

**Custom instruction personality tuning**
Three-directive framework added to ChatGPT settings to suppress sycophancy and AI filler: (1) be candid, tell me what I need to hear not what I want to hear; (2) write in active voice, minimize hedging and grand claims; (3) never use AI slop words. Applied once in settings, it persists across all conversations.

**Harness-first personal agent evaluation**
A mental model for evaluating AI assistants: the model matters less than the harness (the surrounding app, tool integrations, memory, voice, mobile access, browser use). Used to explain why ChatGPT desktop wins the personal agent category despite Claude Fable being the "smartest" model — capabilities only matter if the harness can surface and act on them.

**Zero-to-one visual prototype test**
The presenter's benchmark for design tools: give each model the identical prompt cold (no brand context, no clarifying questions) and judge purely on first-pass visual quality, layout coherence, image integration, and interactivity. Grok won this benchmark in August 2026.