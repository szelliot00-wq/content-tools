# Full Tutorial: Make Professional Launch Videos for Free with Hyperframes | Bin Liu & Jake Moran

Video ID: `iqb5Rd6KKr8`

## Summary
This tutorial interviews Ben Liu (VP of Product Engineering at HeyGen) and Jake Moran (PMM on the HyperFrames team) about HyperFrames, a free tool that generates professional MP4 launch videos from HTML, CSS, and JavaScript code — driven entirely by AI coding agents. The core argument is that because LLMs are natively fluent in HTML/CSS/JS, they can express both information and visual aesthetics through code, making video creation accessible to engineers and PMs without video editing skills. HeyGen built HyperFrames after discovering that agents writing JSON/XML for traditional video editors had no visual intelligence — switching to code as the foundation solved both the generation and the human-editing feedback loop. The video is most relevant to product managers, engineers, and founders who want to produce launch videos quickly and cheaply without learning tools like After Effects or CapCut.

## Key insights
- **HyperFrames is completely free** — the core tool, the GitHub repo, the skills, and even TTS via a local model are all open source and free to use.
- **A full 1-minute Spotify launch video was generated in one shot** by pointing Claude Code (with Fable 5) at spotify.com and using the "website to video" skill — the agent handled screenshots, storyboarding, copy, and audio automatically.
- **The tool outputs rendered MP4, MOV, or WebM**, and also supports transparent background WebM for use in professional editing tools like Premiere. Because the source is HTML, it can also theoretically be exported as an interactive webpage.
- **Why HTML and not JSON/XML**: Earlier versions of HeyGen's video agent wrote JSON blobs for a traditional video editor. The problem: agents have no way to know if a JSON will look good visually. HTML/CSS/JS is "LLM's native language" — models can express visual aesthetics through it, not just data structure.
- **The temporal vs. spatial aesthetics distinction**: LLMs are good at spatial aesthetics (landing pages, top-to-bottom layout), but video requires temporal aesthetics — information is fed over time and eyes don't move. HyperFrames addresses this through internal evals, benchmarks, self-check loops, and skills that train agents on this distinction. They are also working with frontier labs to improve model training on this.
- **HyperFrames Studio** lets humans edit visually without touching code — but every change made in the UI is written back to code, so the agent always knows what changed and can continue collaborating meaningfully.
- **Jake's workflow for new product launches** (no existing website to scrape): create a project folder with context docs, screenshots of UI, reference visuals, and a frame.md or design.md file for brand aesthetics. First prompt generates a table of key events (the storyboard copy). Second step pulls reusable components from the open-source launch video repo. Third step generates a storyboard.html (one static frame per scene) for fast visual alignment before committing to a full render.
- **Component reuse is a major speed lever** — Jake reused the same Claude prompt box component across three consecutive videos, only changing the frame.md for each. The visual output looked completely different each time.
- **HeyGen has open sourced ~50 reusable components** and the full source code of every launch video they've made. Agents can be pointed at these repos to pull specific effects ("grab the text animation from video X for my intro").
- **Model recommendations**: Fable 5 and GPT-5.5 for top quality; Gemini for quality-to-cost balance. HeyGen's own internal agent runs on Gemini. HyperFrames also supports 11 Labs and HeyGen for TTS as alternatives to the free local model.
- **HeyGen produced 20–25 launches in 2 months**, each with a launch video, largely made by Jake alone using these workflows — typically within a day of the launch date.
- **Agent-to-video use case**: HeyGen internally asks Claude Code to review commits from the last 7 days and generate a 30-second video summary for the team — replacing walls of agent text output with watchable video summaries.
- **Integration paths**: Install via `hyperframes.ai/quickstart`, the Codex plugin store (under "Creativity"), or Claude MCP connectors (search "HyperFrames" in Claude's app connections).
- **frame.md vs. design.md**: design.md is a standard brand guideline (fonts, hex codes) for webpages. frame.md is HyperFrames' extension that pushes agents to maximize the frame, use larger elements, and prioritize motion — better suited for video output. Generated at hyperframes.dev/design.

## Use cases
- **Founders and startups** launching a product who previously would spend $30,000+ on a professional launch video.
- **Engineers** who understand the product deeply but don't want to learn After Effects, CapCut, or any video editing tool.
- **Product managers** creating launch assets for frequent, fast-moving release cycles (e.g., 25 launches in 2 months).
- **Teams using AI coding agents** (Claude Code, Codex, Hermes) who want the agent's output summarized as a short video instead of walls of text.
- **Real estate, education, and internal training** content creators needing professional motion graphics cheaply.
- **Developers sharing GitHub repos or OSS projects** on Twitter who want a polished visual launch without hiring a video editor.
- **Video professionals** who want HyperFrames to handle motion graphics layers (exported as transparent WebM) that they composite in Premiere or similar tools.
- **Parents or consumers** who want to turn personal photos/videos (e.g., kids' playground footage) into polished reels — the agent can clip specific timestamps from MP4s.

## Patterns & frameworks

**Website-to-Video Skill (7-step agent workflow)**
A pre-built, open-source skill that instructs any coding agent to: (1) capture screenshots and assets from a target URL, (2) organize them into a structured folder, (3) write a storyboard scene-by-scene, (4) build HTML/CSS/JS scene by scene following the storyboard, (5) apply brand aesthetics, (6) render via HyperFrames, (7) export as MP4. Triggered by a single prompt like "make a launch video for spotify.com."

**Jake's Manual Launch Video Workflow (for new features with no website)**
1. Create a project folder with context docs, UI screenshots, and reference visuals.
2. Add a frame.md (brand + video-specific aesthetic direction).
3. Prompt agent to produce a "table of key events" — the scene-by-scene copy outline. Iterate on copy only.
4. Pull reusable components from the open-source launch video repo (e.g., the Claude prompt box).
5. Generate a storyboard.html — one static frame per scene — to align on aesthetics before full render.
6. Prompt agent to convert storyboard into a full HyperFrames video, preview in Studio.
7. Do last-mile edits in Studio (UI changes write back to code), then export.

**Spatial vs. Temporal Aesthetics (mental model)**
Spatial aesthetics: how visual elements are arranged in 2D space (webpages, layouts) — LLMs are already strong here. Temporal aesthetics: how information is revealed and experienced over time in video — eyes don't move, content is fed sequentially. LLMs are weak at this by default. HyperFrames addresses the gap via skills, evals, and self-check loops embedded in the agent workflow.

**Code as the Agentic Video Foundation (architectural pattern)**
Rather than having agents manipulate proprietary JSON/XML video formats (which have no visual grounding), HyperFrames uses HTML/CSS/JS as the single source of truth. This creates a bidirectional loop: the agent writes code → renders to video; human edits in Studio UI → changes compile back to code → agent can diff and continue. The foundation makes the human-agent collaboration loop coherent and persistent.

**Component Reuse + frame.md Swapping (speed pattern)**
Build or find a strong base component (e.g., a prompt box, a text animation). Save it. For each new video, point the agent at the same component but apply a new frame.md. The structure is reused; the aesthetic is regenerated. Faster first-try success rate than building net-new each time.