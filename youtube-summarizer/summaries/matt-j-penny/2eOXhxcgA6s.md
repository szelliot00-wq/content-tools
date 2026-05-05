# I Built a Claude Skill That Instantly WATCHES Any Video

Video ID: `2eOXhxcgA6s`

## Summary
This video introduces a custom Claude Code skill called "Peek" that enables AI to truly *watch* videos — analyzing both audio and visual content — rather than just reading transcripts. The creator demonstrates the tool by correctly identifying on-screen visuals at a specific timestamp in a YouTube video, something Gemini failed to do (and hallucinated instead). The video covers the problem, a live demo, setup instructions, and a technical breakdown of how the skill works under the hood. It is most relevant to content creators, researchers, developers, and anyone who works heavily with video content and wants deeper AI-assisted analysis.

## Key insights
- **The core problem with existing AI video tools:** Tools like Gemini claim to watch videos but often hallucinate details, particularly visual ones. In the demo, Gemini completely fabricated what was on screen at the 2:52 mark of a YouTube video without even flagging that it couldn't actually see it.
- **The "Peek" skill genuinely analyzes visuals:** Unlike transcript-only tools, this skill captures screenshots from the video at timed intervals and sends them to a vision model for description, giving AI true visual awareness of the content.
- **Screenshot polling rate adapts to video length:** For longer videos, a screenshot is captured every few seconds. For ~10-minute videos, it's every second. For short clips, it can go up to 10 frames per second — useful for analyzing motion graphics in fine detail.
- **Dual-component processing (audio + visual):** The skill separates video into two streams. Audio is transcribed (via YouTube's native captions, Deepgram, or a fallback via Super Data). Visuals are processed by extracting frames with ffmpeg and describing them with a vision model.
- **ffmpeg is used for both audio stripping and frame extraction:** It strips the MP3 from the MP4 (reducing file size from ~1GB to ~10MB for API calls) and also rips still frames from the video for visual analysis.
- **YT-DLP enables broad platform support:** The skill can download videos from YouTube, X (Twitter), Instagram, TikTok, and more — essentially any platform where right-click save-as would work manually.
- **Gemini 2.5 Flash (via OpenRouter) is used for vision — not Claude:** Despite running inside Claude Code, Claude's vision is intentionally avoided because it is token-expensive. Gemini 2.5 Flash is described as "super economical," and images are sent in batches to further reduce cost, making the total spend "basically nothing."
- **Timestamps are synchronized across audio and visual:** The tool maintains timestamps for every frame so that visual descriptions can be matched precisely to what is being said at any given moment.
- **Three-tier transcription fallback system:** (1) Native YouTube captions grabbed directly, (2) Deepgram API transcription of the extracted MP3, (3) Super Data as a last-resort fallback.
- **Deepgram offers $200 in free credits on signup**, making it essentially free for most use cases.
- **The skill is one of 643 Claude Code skills** the creator has built and made publicly available for free via GitHub.
- **Setup requires only two API keys:** OpenRouter (for Gemini vision model access) and Deepgram (for audio transcription). Both are added to the `settings.json` env section in Claude Code.

## Use cases
- **Research:** Capturing both spoken and visual information from educational or informational videos, avoiding the data loss that comes from transcript-only analysis.
- **YouTube content analysis:** Analyzing competitor or inspirational videos holistically — understanding talking head vs. motion graphic ratios, layout choices, visual pacing, and graphic styles.
- **Video translation/localization:** Identifying not just spoken language but also on-screen text (e.g., English titles or captions) that need to be replaced when translating a video into another language.
- **Video duplication or recreation:** Replicating both the audio script and the visual structure of a video, including when and how motion graphics appear.
- **Understanding complex visual content:** Asking specific questions about what is shown on screen at a precise timestamp (e.g., "What do these percentages mean at 2:52?").
- **Motion graphic analysis:** Using high frame-rate capture (up to 10fps) on short clips to understand exactly how an animation or graphic is constructed.
- **Developers building video AI tools:** The technical breakdown serves as a blueprint for anyone wanting to build or customize similar video-understanding pipelines.

## Patterns & frameworks
- **Dual-Stream Video Decomposition:** The core architectural pattern separates any video into two independent streams — audio (transcription) and visual (frame descriptions) — processes each with the best-fit tool, then recombines them with synchronized timestamps. This is the foundational design pattern of the entire skill.
- **Adaptive Polling Rate:** A dynamic frame-capture strategy where screenshot frequency scales inversely with video length. Longer video = fewer frames per second (efficiency focus); shorter clip = more frames per second (detail focus). This balances cost and granularity automatically.
- **Tiered Fallback Transcription:** A three-layer redundancy pattern for audio: try the cheapest/fastest method first (native captions), fall back to a paid API (Deepgram), and use a third-party service (Super Data) only if both prior methods fail. This maximizes reliability while minimizing cost.
- **Vision-via-Frames Proxy Pattern:** Since LLMs cannot natively process video, the skill uses the mental model that "video is just a collection of images" and proxies video understanding through batch image description with a vision model — a reusable pattern applicable to any video AI workflow.
- **Cost-Optimized Model Routing:** Using OpenRouter to route vision tasks to the cheapest capable model (Gemini 2.5 Flash) rather than defaulting to the host model (Claude), and batching image requests — a deliberate cost-engineering pattern for token-heavy multimodal workloads.