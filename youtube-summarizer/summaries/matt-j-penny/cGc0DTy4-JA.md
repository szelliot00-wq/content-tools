# This Claude Skill Finally Solves Video Editing (Full Breakdown)

Video ID: `cGc0DTy4-JA`

## Summary
This video demonstrates a Claude-based AI skill called the "Full Edit Skill" that automates end-to-end video editing, from rough cuts to motion graphics, sound effects, and music. The presenter, Matt, walks through a live example of uploading a raw 1-minute video, triggering the skill with a single word ("full edit"), and receiving a polished, branded output in minutes. He then breaks down the six-step technical process behind how the skill works so viewers can build it themselves. The video is most relevant to content creators, YouTube educators, and business owners who currently spend significant time or money on video editing.

## Key insights
- The skill is triggered by typing a single word ("full edit") after dropping a raw video into Claude — no additional prompts required for a first pass.
- The presenter used Opus 5.5 specifically, claiming it outperforms other models (including GPT-6 from OpenAI) for video editing and motion graphics tasks.
- The estimated cost of editing a video with this AI system is approximately **$0.05** — compared to previously paying editors **thousands of dollars** and waiting days for turnaround.
- Building the system yourself is estimated to take **30–40 hours** of setup and fine-tuning; a pre-built version is available via the presenter's "Applied AI Mastermind" membership.
- **Word-level timestamps** are essential — not just a transcript, but timestamps for each individual word — so the AI knows exactly when to make cuts and insert motion graphics. Deepgram (free tier with ~$200 credit on signup) is the recommended tool; ElevenLabs is an alternative.
- The "video manifest" is described as the single most important component: a detailed style document that tells Claude how to plan the edit (fonts, colors, spacing, clip timing, subtitle style, motion graphic templates, sound effect density, etc.).
- A separate, fresh agent should be used to QA-check the video rather than the same agent that built it — the analogy used is that it's harder to spot your own exam errors than someone else's.
- Motion graphics are generated using **Remotion** (primarily) and **Hyperframe** (supplementary), and can be full-screen, overlay, lower-thirds, or icon-based.
- For music and sound effects, the system can either generate them on-the-fly (using ElevenLabs) or draw from a pre-approved bank of assets — the presenter notes AI-generated audio is now "right on the cusp" of being good enough to fully replace curated assets.
- For viral short-form content, the presenter recommends maintaining a bank of approved/trending songs rather than generating music, with AI selecting from that bank.
- The system supports iterative refinement via natural language prompts within the same chat (e.g., "make the payoff section full screen") without any separate workflow or trickery.
- Claude can optionally record its own screen and insert screen-share footage into the edited video.
- The presenter also has a separate "manifest creation skill" that auto-generates the video manifest by analyzing existing videos, asking style questions, or examining reference videos/images.

## Use cases
- **Solo content creators** who currently edit their own videos in tools like CapCut and want to reclaim hours per week.
- **YouTube educators or thought leaders** producing multiple long-form videos per week who need consistent branded output at scale.
- **Business owners** paying freelance or agency video editors and looking to dramatically reduce that cost.
- **Agencies or media teams** wanting to standardize a client's editing style and automate production.
- **Creators transitioning to short-form content** (Shorts, Reels, TikTok) who want to pull from trending audio banks while automating all other editing.
- **Non-technical founders or marketers** who can record raw video but lack editing skill — the system may produce better output than their manual editing.
- **Anyone building AI automation workflows** who wants a concrete example of a multi-agent, multi-tool production pipeline.

## Patterns & frameworks

**The 6-Step Full Edit Pipeline**
A repeatable end-to-end process for AI-driven video editing:
1. **Rough Cut** — Transcribe audio with word-level timestamps (via Deepgram), then use AI to identify and remove silences and bad takes (false starts, mispronunciations, near-duplicate sentences).
2. **Plan Creation** — AI reads the video manifest and generates a detailed edit plan: where to place motion graphics, what they look like, timing, colors, fonts, templates to use.
3. **Edit & Motion Graphics Creation** — AI executes the plan using Remotion and Hyperframe to render overlays, full-screen graphics, lower-thirds, and icons.
4. **QA Check Loop** — A *separate, fresh agent* reviews the compiled video for errors (overlapping elements, bad renders, timing mismatches) and fixes them, looping until no errors remain.
5. **Music & Sound Effects** — Added after QA to avoid re-syncing if edits change; either AI-generated (ElevenLabs) or selected from a pre-approved asset bank.
6. **Final Render** — All elements compiled into a finished MP4.

**The Video Manifest**
A style-and-preference document (Matt calls it "a plan for the plan") that acts as the AI's editorial brief. It encodes: cut pacing, clip spacing, font/color/spacing preferences, subtitle style, motion graphic templates (e.g., number callout templates), and sound effect density. This is the highest-leverage artifact in the system — the presenter recommends spending a full day building it out. It can be auto-generated from existing videos, Q&A sessions, or reference material via a companion skill.

**Fresh-Agent QA Pattern**
Using a second agent with no prior context to review work produced by the first agent. Based on the observation that the creating agent has a blind spot for its own errors (analogous to self-proofing an exam), while a context-free agent can spot mistakes more reliably. This is a transferable pattern for any multi-step AI production workflow.

**Prompt-Then-Refine (Single-Chat Iteration)**
The initial "full edit" prompt produces a complete draft; the user then issues natural language change requests within the same chat session (e.g., "make X full screen"). No separate tools, re-uploads, or workflows are needed for revisions — the entire session is conversational and stateful.