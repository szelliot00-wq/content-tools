# How To Use Remotion Better Than 99% Of People (AI Video Editing)

Video ID: `6bZrTSUR0RM`

## Summary
This video breaks down a comprehensive system for using Remotion (a code-based video editing tool) alongside Claude AI to produce professional-quality edited videos cheaply and quickly. The creator claims to have replaced human editors entirely, achieving 10x speed and 1000x cost reduction. The core argument is that raw Remotion prompting produces mediocre results — the real unlock comes from layering in the right APIs, assets, skills, and a template-driven pre-editor workflow. It is most relevant to content creators, marketers, and AI practitioners who want to automate video production at scale.

## Key insights
- Simply prompting Claude to "edit this video" produces poor results; structured setup with eight specific connectors and assets is required to get professional output.
- **Word-level timestamps** (not just plain transcripts) are essential — they allow graphics, subtitles, and b-roll to sync precisely with what is being said. Deepgram is the recommended provider (essentially free and fast); ElevenLabs is an alternative.
- **AI image and video generation** can be wired directly into Remotion via APIs (e.g., Kai.ai, Higgs Field, OpenArt), enabling commands like "add AI b-roll in relevant places" to work end-to-end automatically. Recommended models include Seedance 2.5, MiniMax H3, and GPT Image 2.
- **Brave Image Search** integration lets Remotion pull real images from the web — useful for historical figures, specific people (e.g., Elon Musk), or cost-sensitive b-roll situations where AI generation is unnecessary.
- **Voice cloning** can be connected via Inworld (preferred for quality and price) or ElevenLabs. HeyGen can be added if full avatar cloning is desired.
- A **pre-curated b-roll and asset bank** (images, videos, sound effects, icons) is more cost-effective and quality-controlled than generating assets on the fly, since the creator has already vetted each asset.
- A **dictionary** (JSON file) is critical for any asset bank — it maps each file name to a description and usage context so the AI can select the right asset without needing to visually inspect every file with a vision model.
- AI is notoriously bad at generating icons and logos; a curated icon library with a dictionary prevents distorted or incorrect brand logos from appearing in videos.
- **Claude skills** extend Remotion's capabilities automatically in the background without needing to mention them explicitly in prompts. Key skills used: front-end slides (for motion graphic quality), Open Montage (smooth flowing graphics), Rotoscoping (subject/background separation), Apple Design (smooth, organic animation timing), and Liquid Background (premium visual backgrounds).
- The biggest quality lever is **eliminating mistakes rather than perfecting good parts** — one obviously wrong segment ruins an otherwise strong video.
- The **pre-editor tool** is the creator's core workflow innovation: upload raw footage → transcribe with word-level timestamps → trim bad takes/pauses → annotate the timeline with specific overlays and templates manually → export a detailed prompt → send to Claude in the Remotion folder. This produces near-zero-mistake first-pass outputs.
- AI struggles with **creative decisions** (what b-roll fits here, what graphic style to use) but excels at **logical execution** (do exactly what is specified). The template system offloads creative decisions to the human, letting AI handle execution.
- **Rotoscoping** (placing elements between subject and background) is rarely seen in AI videos, making it an easy differentiator for production quality.

## Use cases
- Content creators who record talking-head or screen-capture videos and want to automate post-production entirely.
- Marketers producing high volumes of branded video content who need consistent style at low cost.
- Solo creators who cannot afford or don't want human video editors.
- AI practitioners building automated content pipelines for clients or products.
- Educators or course creators who publish frequent video content and need repeatable, on-brand templates.
- Anyone needing accurate subtitle generation with word-level sync (e.g., accessibility, social media captions).
- Teams producing videos about specific real-world people, events, or brands where AI-generated images would be unreliable.

## Patterns & frameworks

**The Eight Connectors & Assets Framework**
A checklist of eight inputs that must be wired into Remotion before expecting professional output: (1) style.md and frames.md files, (2) word-level transcription API, (3) AI image/video generation API, (4) Brave Image Search, (5) voice-over/voice-clone API, (6) curated b-roll bank, (7) sound effects bank, (8) icon/logo library — each asset bank accompanied by a JSON dictionary.

**The Dictionary Pattern**
For any pre-built asset library (b-roll, sound effects, icons), create a companion JSON file that maps each filename to a description and recommended usage context. This replaces the need for a vision model to inspect assets at runtime and dramatically improves AI's ability to select the correct asset.

**Skills-as-Background-Enhancers**
Claude skills (front-end slides, Open Montage, Rotoscoping, Apple Design, Liquid Background) are installed once and operate automatically on every subsequent Remotion prompt without explicit invocation — a "set and forget" quality layer.

**The Pre-Editor Workflow (Template-Driven Video Production)**
A five-stage pipeline: (1) upload raw footage, (2) transcribe with word-level timestamps, (3) trim bad takes and pauses, (4) manually annotate the timeline by selecting templates and specifying overlay content for each segment, (5) export the full specification as a structured prompt and send to Claude. The key insight is that humans handle the creative/selection layer while AI handles execution — reversing the typical failure mode of asking AI to be creative.

**Eliminate-Mistakes-First Principle**
Rather than trying to make good segments great, the system prioritizes ensuring zero obviously-wrong moments exist. A single bad segment undermines the entire video regardless of other quality, so the workflow is optimized around first-pass correctness over iterative refinement.