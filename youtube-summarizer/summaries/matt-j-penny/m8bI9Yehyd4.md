# This Claude Skill Creates Longform YouTube Videos Hourly (Claude Code Tutorial)

Video ID: `m8bI9Yehyd4`

## Summary
This tutorial demonstrates a Claude Code skill that automates the end-to-end creation of faceless long-form YouTube videos, from script generation through to a rendered MP4. The creator walks through both the interactive mode (where you can review and tweak before rendering) and the fully automated routine mode that runs on a schedule. The stack is deliberately cheap — targeting under $0.10 per short video — using free/open-source tooling (HyperFrames, FFmpeg) alongside cheap API services (ElevenLabs, OpenRouter with FLUX). It is most relevant to solo creators, automation enthusiasts, and anyone building faceless YouTube channels at scale without video editing skills or budget.

## Key insights
- **Cost target is under $0.10 per short video.** Image generation via FLUX 4B on OpenRouter is ~$0.01/image (1.4¢/megapixel, ~1 megapixel per image). A 2-minute video uses ~16 images, so image costs alone are ~$0.16. The "less than 10 cents" claim likely applies to very short videos with cheap voice tiers.
- **HyperFrames is the key free differentiator.** It's a free, open-source tool that converts HTML/JavaScript into MP4 via FFmpeg. Other tutorials recommend Creatormate ($109/month) or JSON-to-video (credit packs of ~$50); HyperFrames runs locally for free.
- **The render pipeline avoids AI for the final assembly.** A Python script slots assets into an HTML template and runs HyperFrames — no AI tokens consumed at render time, keeping it fast and cheap.
- **Word-level transcription is required for caption timing.** After ElevenLabs generates audio, the skill fetches a word-level transcript to know exactly when each word is spoken. This drives both caption animation timing and scene transition timing — guessing from the script alone is insufficient.
- **An HTML preview checkpoint exists before expensive generation.** The skill renders a preview HTML file showing all scenes, quotes, image prompts, fonts, colors, and estimated duration. Users can edit (e.g. remove a scene) before committing to image and audio generation.
- **Everything is cached/saved to disk.** Script, scenes, images, and audio are all written to files. This enables review, reuse as training data, and prevention of accidental regeneration. It also allows referencing past videos ("create one similar to last week's").
- **The five-stage pipeline:** Idea → Script (with scene breakdown) → Theme control (palette, font, mood) → Asset generation (audio + images) → Render (HyperFrames Python script → MP4).
- **ElevenLabs voice design API can support multi-character voices.** For narrative videos with distinct characters, you can programmatically generate custom voices per character and instruct Claude to switch between them.
- **OpenRouter makes image models hot-swappable.** A single API key accesses many image models; switching models is a one-line config change with no code refactoring.
- **Routines (scheduled automation) are built into Claude Desktop.** The skill can be wired into a Claude Code Routine set to run hourly (or any interval), generating a new video automatically without user input. Local routines require the machine to stay awake (e.g. using Amphetamine on macOS).
- **The skill can be extended to auto-publish.** Connecting to the YouTube Data API allows the pipeline to upload the finished MP4 directly to YouTube without manual intervention — though the creator recommends validating output quality before enabling this.
- **Apify scrapers can feed the topic pipeline.** Scraping trending YouTube videos via Apify and piping themes into the routine creates a feedback loop where the system creates content around what's already performing well.

## Use cases
- Faceless YouTube channel operators who want to scale output without hiring editors
- Solo creators testing niche content ideas cheaply before investing in production quality
- Marketers creating quote/inspirational content channels (Stoicism, motivation, business wisdom)
- Developers who want a reference architecture for an AI-driven media pipeline
- Anyone replacing expensive SaaS video tools (Creatormate, JSON-to-video) with a self-hosted alternative
- Teams building training datasets from structured AI-generated video content
- Storytelling channels needing multi-character voiceover (via ElevenLabs voice design API)

## Patterns & frameworks

**Five-Stage Video Pipeline**
Idea → Script → Theme → Asset Generation → Render. Each stage produces saved artifacts before the next begins, making the pipeline resumable and reviewable. The expensive stages (image + audio generation) are gated behind a human-readable HTML preview in interactive mode.

**Template + Asset Swap Pattern**
A reusable HTML/JS template defines scene structure, animations, transitions, fonts, and layout once. Per-video assets (images, audio, captions, colors) are slotted in at runtime. This avoids re-solving layout problems on every video and keeps AI involvement minimal at render time.

**Cache Everything Pattern**
All intermediate outputs (script JSON, scene files, images, audio files) are written to disk before the next stage runs. This prevents re-spending API credits on regeneration, enables mid-run recovery, supports human review, and accumulates a reusable dataset for future fine-tuning.

**Preview-Gate Pattern**
Before committing to expensive/slow operations, generate a cheap human-readable preview (HTML file) that represents the full intended output. Users can inspect, edit, and approve before triggering the costly pipeline steps. In fully automated mode, this gate is skipped.

**Hot-Swappable Model Layer (via OpenRouter)**
Route all image generation through a provider-agnostic API (OpenRouter) so the underlying model can be changed with a config value rather than code changes. This decouples model selection from pipeline logic and makes cost/quality tradeoffs easy to experiment with.