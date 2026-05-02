# How I Fully Automated My Video Editing (Claude & Remotion)

Video ID: `zOwtnkPTbvU`

## Summary
This video demonstrates how the creator fully automated his video editing workflow using two primary tools: Claude Code (or Cursor) and Remotion, a code-based video editing framework. The creator walks through his step-by-step process — from stripping audio, generating word-level transcriptions, cutting out bad takes and filler words, to generating and inserting motion graphic scenes — all driven by AI prompts. He shares three key productivity hacks (style guides, templates, and resource dictionaries) that reduce the need for manual creative decisions. The video is most relevant to solo content creators, YouTubers, and small media teams looking to cut video production costs and time by leveraging AI-driven workflows.

## Key insights
- **The core toolchain is Claude Code + Remotion**: Claude Code (or Cursor as an alternative) writes the code, while Remotion interprets it and provides a visual studio similar to DaVinci Resolve or Premiere Pro — but fully code-driven.
- **Audio stripping saves massive time and cost**: Stripping the MP3 from a video before sending to a transcription API (e.g., ElevenLabs) reduces file size from ~1.3 GB to ~10 MB, making transcription dramatically faster and cheaper.
- **Word-level transcription is critical**: Using ElevenLabs (or similar) to get word-level timestamps — not just sentence-level — enables precise placement of cuts, captions, and motion graphic scenes at exactly the right moments in the video.
- **Transcription stored in a Markdown file**: The transcript is saved locally in a Markdown file so it can be referenced repeatedly without regenerating it or relying on chat context, saving tokens and time.
- **AI identifies cuts automatically**: After transcription, Claude identifies long pauses, dead air, bad takes, and filler words (ums, uhs) and uses Remotion to generate a cut version of the video with those sections removed. A 20-minute video that would take a human editor ~30 minutes to cut manually is handled quickly with minimal input.
- **Remotion Studio is for visualization only**: It resembles a traditional NLE (non-linear editor) but is not designed for manual editing — it's purely for previewing the AI-generated code output.
- **Scene planning via Markdown "database"**: Claude plans motion graphic scenes (roughly one every 10 seconds) and writes them to a scene plan Markdown file, including a "created/not created" checkbox field so the AI can track progress and build scenes incrementally.
- **Build scenes in separate compositions first**: The creator recommends building each motion graphic scene as a separate Remotion composition before inserting it into the main edit, making tweaking easier and less risky.
- **Switch from Claude Code to Cursor to bypass token limits**: Claude Code consumes tokens heavily and hits limits quickly during video editing projects. Cursor (~$15/month) offers effectively unlimited usage, is noticeably faster, and can work on the same project files seamlessly.
- **Style guide reduces creative guesswork**: A `remotion-style-guide` file stored in the root Remotion folder specifies colors, typography, type scale, spacing, and shadows. Claude references this automatically, ensuring consistent brand aesthetics without repeated manual instruction.
- **Template library speeds up scene creation**: Pre-built TypeScript Remotion templates (e.g., an off-white dotted background) are stored in the project folder and indexed in a JSON dictionary with names and filenames. Claude looks up the dictionary and reuses templates directly rather than building from scratch.
- **Icon and sound effect libraries prevent hallucination**: Remotion is described as "terrible at creating icons from scratch." Pre-importing logos (e.g., the Claude icon) and sound effects into a resource folder — indexed with a description/filename dictionary — ensures accurate, on-brand assets are used without web searches or fabricated visuals.
- **The creator genuinely fired his human video editor**: He states this workflow is faster, cheaper, and produces results that meet his needs, and that the editor has moved on to other work.
- **He runs the entire process as one automated skill in practice**: For his own use, he has bundled all steps into a single Claude skill/command. The step-by-step walkthrough in the video is intentionally broken down so viewers can replicate and customize it themselves.
- **A database would be technically better than Markdown**: The creator acknowledges using Markdown files as a makeshift database is inefficient on token economy and not best practice — he is experimenting with a proper database integration for a more robust version.

## Use cases
- **Solo YouTubers or podcasters** who want to eliminate or reduce reliance on a human video editor.
- **Content creators with raw, unedited footage** full of filler words, bad takes, and dead air that needs cleaning up quickly.
- **Small marketing teams** producing regular video content who want consistent branding across edits without manual style enforcement.
- **Developers or technical content creators** comfortable with code-adjacent tools (Claude Code, Cursor, TypeScript) who want to build a repeatable, automated editing pipeline.
- **Creators who produce high volumes of videos** and need a scalable, low-cost alternative to hiring editors.
- **Anyone building AI automation workflows** looking for a real-world example of chaining AI tools (transcription APIs, LLMs, code-based rendering) into a production pipeline.
- **Creators who want motion graphics** (title cards, animated text, counters, icon overlays) without paying for motion designers or learning After Effects.

## Patterns & frameworks

### 1. Strip → Transcribe → Cut → Plan → Build → Insert Pipeline
A linear, repeatable video editing workflow:
1. **Strip audio** from video (ffmpeg) to reduce file size.
2. **Transcribe** audio at word level (ElevenLabs API) and save to Markdown.
3. **Identify and cut** bad takes, filler words, and dead air using AI + Remotion.
4. **Plan scenes** — AI generates motion graphic ideas (~1 per 10 seconds) saved to a scene plan Markdown file with a completion checkbox.
5. **Build scenes** individually as separate Remotion compositions, tweak, then insert into the main edit using transcript timestamps.
6. **Render** the final composition as an MP4.

### 2. Markdown-as-Database Pattern
Using Markdown files as lightweight, persistent state stores (transcripts, scene plans with checkboxes) so AI can track progress across sessions without relying on chat context. Acknowledged as technically imperfect but functional for this use case.

### 3. The Three Asset Pillars (Style, Templates, Resources)
A framework for reducing AI creative guesswork and improving output consistency:
- **Style Guide**: A centralized file defining brand colors, fonts, spacing, and shadows — referenced automatically by AI in every project.
- **Template Library**: Pre-built, reusable TypeScript Remotion components (backgrounds, title cards, subtitle styles) indexed in a JSON dictionary so AI can look them up and reuse them.
- **Resource Dictionary**: Pre-imported icons and sound effects with a description/filename index so AI uses exact, approved assets rather than generating or hallucinating them.

### 4. Claude Code for Setup → Cursor for Iteration
A tool-switching pattern: use Claude Code to initialize and scaffold the project (folder setup, Remotion installation, transcription), then switch to Cursor for all iterative scene-building work to avoid token limits and benefit from faster performance and unlimited usage.

### 5. Separate Composition → Validate → Insert Pattern
A quality-control loop for motion graphics: build each scene in an isolated Remotion composition, visually validate it in Remotion Studio, make any tweaks, then insert it into the main video edit with timestamp-aware placement. This mirrors a traditional "pre-comp" workflow from professional video editing.