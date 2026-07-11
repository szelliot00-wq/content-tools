# I Made Vox-Style Motion Graphics Using Only Claude Code & Omni

Video ID: `dqtfk8iINXI`

## Summary
This video demonstrates a step-by-step pipeline for creating Vox-style explainer videos using Claude (Fable 5), GPT Image 2, and Google Omni — all orchestrated through a single API (Kai AI). The creator built a reusable workflow that takes a topic, generates a punchy script, creates images, animates them into video clips, and stitches them together with FFmpeg — all for roughly $1. It is most relevant to content creators, marketers, and AI enthusiasts who want to produce professional-looking short-form video content with minimal manual effort.

## Key insights
- **Vox-style definition first**: Before prompting anything, the creator reverse-engineered Vox's editing style by pulling ~10 YouTube videos about it into NotebookLM, which synthesized a comprehensive style guide and animation prompt template.
- **Two-prompt system**: The pipeline uses two distinct prompts — a *style prompt* (for image generation) and an *animation prompt* (for video motion/effects) — derived from the Vox style research.
- **Script is the anchor**: The script is generated first and refined before any media is created, because it drives everything downstream. The creator iterated on punchy, concise copy ("This ship has been at war for 260 years") before touching images or video.
- **Image-first, then video**: GPT Image 2 generates a still image per scene first. That image is then fed into Google Omni to produce the animated video clip. This is cheaper and faster to iterate on than jumping straight to video generation.
- **Last-frame continuity trick**: To maintain visual coherence between clips, FFmpeg extracts the last frame of each completed video clip, Claude analyzes it, and that frame becomes the starting reference for planning and generating the next clip. Without this, prompts for later scenes become disconnected from the actual visual output.
- **Three-scene structure**: A 30-second video is broken into three ~10-second segments, each generated separately, then stitched together with FFmpeg into one final file.
- **One-shot mode available**: The entire pipeline can run unattended — just say "create a video about X" and walk away for ~10 minutes. Step-by-step mode is shown in the video for teaching purposes and quality control.
- **Cost**: The full 30-second video cost just over $1 to produce end-to-end.
- **Speed tradeoff**: Claude/Fable 5 produces high-quality results but is slow. The creator recommends Codex, Cursor, or Grok models if speed matters more than quality.
- **Single API layer (Kai AI)**: Rather than managing separate API keys for OpenAI and Google, the creator routes everything through Kai AI, which unifies billing and credentials.
- **Downloadable pipeline**: The full workflow — skills, prompts, style guides — is available for free via a link in the description; users only need to add their own Kai/FAL API key.

## Use cases
- **Marketing teams** producing short explainer or brand videos at low cost without video editors
- **Content creators** wanting to replicate the Vox documentary aesthetic for educational YouTube content
- **Solo entrepreneurs or consultants** demoing AI capabilities to clients using a tangible, impressive output
- **Agencies** building repeatable AI content pipelines for clients across topics (history, product explainers, company stories)
- **AI/no-code enthusiasts** learning how to chain image generation → video generation → video editing via a single Claude workflow
- **Anyone wanting to create long-form AI video** (the pipeline scales — the creator notes you can make 30-minute videos the same way)

## Patterns & frameworks

**Vox Style Research → Prompt Synthesis Pipeline**
Use a multi-source research aggregator (Ampify + NotebookLM) to distill a consistent visual/editorial style from reference content into reusable style and animation prompts. Separates "what does this style look like" from "how do I prompt it."

**Sequential Scene Workflow (Image → Video → Last Frame → Repeat)**
1. Generate a still image for Scene N using GPT Image 2
2. Animate that image into a video clip using Google Omni
3. Extract the last frame of the clip with FFmpeg
4. Feed that frame to Claude to plan Scene N+1
5. Repeat until all scenes are done, then stitch with FFmpeg
This ensures visual continuity across clips without manual intervention.

**Step-by-step vs. One-shot mode**
The same pipeline supports two operating modes: guided (human checks each output before proceeding — better for quality control and learning) and automated (single prompt runs the whole thing unattended — better for speed and iteration). The workflow file enables both.

**Cheap-to-iterate image gate**
Always refine and approve the still image before generating video, because image regeneration is far cheaper and faster than video regeneration. Front-load creative decisions at the image stage.