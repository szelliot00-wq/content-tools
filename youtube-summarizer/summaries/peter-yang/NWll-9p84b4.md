# How to Edit YouTube Shorts With AI (Free Skill)

Video ID: `NWll-9p84b4`

## Summary
This video introduces a free, open-source Claude Code skill called "video short scale" that automates the editing of raw recordings into polished YouTube Shorts using AI. The creator walks through a four-step workflow: installing the skill, uploading a raw recording for an AI draft edit, giving frame-by-frame feedback via a built-in review interface, and rendering a final polished short. The video is sponsored by Google Gemini and demonstrates integrations with tools like FFmpeg, yt-dlp, HyperFrames, Veo (AI video), and Lyria (AI music). It is most relevant to content creators, marketers, and developers looking to streamline short-form video production using AI tooling.

## Key insights
- The skill is free and open-source at `github.com/petergyang/videoshort`, installable via a single slash command in Claude Code (Anti-Gravity)
- YouTube Shorts alone receives over 200 billion views per day, and platforms like X are paying creators thousands of dollars to produce shorts — making short-form video editing a core marketing skill
- The skill automatically handles: A-roll (talking head), punch shots (tighter framing), split-screen (speaker + B-roll), and full-screen B-roll — mixing these formats for visual variety
- B-roll is sourced automatically from YouTube, X, and other sites using yt-dlp; the skill pulls contextually relevant clips based on the script
- AI-generated video (via Google Veo) and background music (via Google Lyria) can be added for a few cents or fractions of a cent using a Gemini API key
- The Gemini API key should never be pasted directly into chat — always store it in a `.env` file to prevent key leakage through model training data
- A built-in frame-by-frame review interface (with light/dark mode) lets users leave timestamped comments on specific scenes, which AI then acts on in the next iteration
- The skill includes an automated self-evaluation (`eval.md`) that checks its own output before presenting results — e.g., "Does the hook land in the first 3 seconds?" and "Does each visual show something the words don't say?"
- A separate cleanup prompt (useful for longer videos) strips filler words ("alright," "so," "right"), shortens pauses to under 1 second, removes false starts, and reduces jump cuts — a customizable template the creator built for his own workflow
- The skill is not a one-shot solution; multiple rounds of feedback are typically needed to get from raw recording to publish-ready short
- Best practices from the `skill.md` file include: capture attention in the first 3 seconds, show visually what words can't convey, prioritize real footage over UI screenshots, and avoid anything too small to read on mobile
- The creator credits YouTuber Nate Hurk for many of the short-form video best practices baked into the skill file
- The creator also has other free open-source skills: "no AI slop" (12,000 GitHub stars) for removing generic AI writing, and "human review" for line-by-line document feedback similar to Google Docs

## Use cases
- **Content creators** who record talking-head videos and want to produce polished shorts without manual editing skills
- **Marketers** building short-form video as a distribution channel across YouTube, Instagram, and X
- **Solo developers or indie hackers** who want to repurpose long-form content (tutorials, demos) into short clips with minimal effort
- **AI tool builders** looking for a reference implementation of a skill that combines video processing, LLM feedback loops, and multimodal AI generation
- **Educators and course creators** who want to turn raw lecture recordings into engaging short-form clips with captions and motion graphics
- **Anyone producing longer videos** who wants to automate filler-word removal, pause shortening, and retake cleanup via a reusable prompt
- **Teams or freelancers** doing content production at scale who want a repeatable, low-cost pipeline for short-form video

## Patterns & frameworks

**Four-Step Video Short Workflow**
A repeatable production pipeline: (1) Install the skill, (2) Upload raw recording and get an AI draft edit with a scene-by-scene plan, (3) Give frame-by-frame feedback via a built-in review UI, (4) Approve and render the final short. Designed to iterate in multiple rounds rather than produce a perfect one-shot output.

**Scene-Type Mix Pattern**
The skill structures every short as a deliberate mix of four scene types — A-roll (speaker full screen), punch (tighter crop), split (speaker bottom + B-roll top), and full-screen B-roll. This prevents visual monotony and mirrors professional short-form editing conventions.

**AI Self-Evaluation (`eval.md`)**
Before presenting output to the user, the skill runs an internal checklist (hook lands in 3 seconds, visuals show what words don't say, etc.). This "AI checks its own work" pattern reduces back-and-forth by catching obvious failures before human review.

**Secure API Key Handling via `.env`**
Rather than pasting credentials into chat (where they could appear in model training data), the pattern is to ask the AI to open the `.env` file and paste the key there directly. A security-first habit applicable to any agentic workflow involving API keys.

**Filler/Retake Cleanup Prompt**
A custom reusable prompt that: shortens pauses to ≤1 second, strikes through repeat phrases and false starts, removes stutters and self-corrections, and cuts named filler words — all without creating choppy jump cuts. The creator treats this as a personal, iterable template rather than a fixed rule set.

**Source-First B-roll Strategy**
The skill searches for real footage online (YouTube, X, Veo blog) before generating AI video, following the principle of prioritizing authentic footage over synthetic content. AI-generated video (Veo) fills gaps where no suitable real footage exists.