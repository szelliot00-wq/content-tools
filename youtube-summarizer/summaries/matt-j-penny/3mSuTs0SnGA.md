# Automate CapCut Video Editing with Claude (Full Course)

Video ID: `3mSuTs0SnGA`

## Summary
This video is a full tutorial on automating video editing in CapCut using Claude (AI) and a custom integration layer called the "CapCut Bridge." The presenter walks through every major editing task — rough cuts, motion graphics, subtitles, sound effects, music, rotoscoping, AI-generated B-roll, Google image search, and color correction — demonstrating how AI can handle roughly 90% of the editing workload. The core argument is that combining AI automation with a human-editable interface (CapCut) is faster and more cost-effective than either fully manual editing or fully AI-rendered output. The video is most relevant to content creators, solo video editors, and digital marketers who produce regular talking-head or educational video content and want to reduce editing costs and time.

---

## Key insights
- **The CapCut Bridge** is a set of scripts that connects Claude (or other AI) to CapCut, allowing AI to directly manipulate the timeline, press buttons, and create projects inside the editor — not just render a finished file.
- **Recommended model: Claude Opus 5.5** for complex editing tasks; Sonnet 5.5 is acceptable for simpler setup tasks to conserve credits.
- **Deepgram** is used for audio transcription with word-level timestamps, which is essential for accurate silence/bad-take removal and precise motion graphic/sound effect placement. It is free to start.
- **The 90/10 rule**: AI does the first 90% (rough cut, motion graphics, sound, etc.); the human does the final 10% (minor timing tweaks, volume adjustments, style fixes) because small manual edits in CapCut are faster than prompting AI to re-render.
- **Editing in CapCut vs. pure AI rendering**: Using CapCut as the canvas means you can make small tweaks (volume, scale, positioning) in seconds; asking AI to do the same re-render takes minutes and costs credits.
- **Sound effects — two approaches**: (1) Pre-vetted library with a manifest/dictionary file describing each sound effect (more reliable, premium feel); (2) AI-generated via ElevenLabs (hit-or-miss, ~50% acceptable at time of recording).
- **AI music generation** (e.g., via ElevenLabs) works well for background/lo-fi instrumental music but is less reliable for viral/trending sounds — for those, a curated dictionary approach is recommended.
- **The style guide** is described as the single most important asset for consistent AI video editing — it encodes brand colors, fonts, layout preferences, and editing style. Can be created by feeding existing videos or a website to Claude and asking it to extract a style guide.
- **Skills** are reusable prompt templates/processes saved in the working folder. Examples shown: "full edit," "add motion graphics," "rotoscope," "color correct." Typing a skill name triggers the full multi-step process automatically.
- **Rotoscoping** requires telling AI the exact mechanical steps (copy clip to new layer, mute top layer, remove background, insert text between layers, animate) because "just do rotoscoping" is too vague.
- **AI B-roll generation**: Supported via Higsfield (with GPT Image 2), Top View, FAL, Kling 4.0, Sea Dance 2/2.5. You can either specify exact shots or ask AI to ideate options and then select one.
- **Brave Image Search** (requires API key, free account) enables pulling real Google images into the timeline — critical for specific people, places, or things where AI-generated images would be inaccurate or fabricated.
- **Color correction** can be dialed in manually once, then saved as a skill or baked into the full-edit pipeline so the same LUT-style settings are applied automatically every time.
- **Interactive CapCut text elements** for subtitles are preferred over burnt-in motion graphic captions because they remain editable in both CapCut and Claude without spending additional credits.
- **Verification loops**: The presenter notes that skipping Claude's self-verification loop speeds things up but introduces errors (e.g., missed glow effects not cleaned up everywhere). Building a post-edit checking skill is recommended for catching common mistakes.
- **Connecting new tools**: Any new integration (Higsfield, Top View, Brave, ElevenLabs, etc.) can be set up by simply telling Claude "help me set up [tool name]" — it walks through authentication and API key configuration automatically.

---

## Use cases
- **Solo content creators** producing regular YouTube, TikTok, or Instagram talking-head videos who want to eliminate or drastically reduce editing time.
- **Marketing teams** needing a repeatable, brand-consistent video editing pipeline without hiring full-time editors.
- **Agencies or freelancers** managing high video volume who currently spend thousands of dollars on human editors.
- **Educators and course creators** who record long raw lectures and need silence/bad-take removal and structured motion graphics without manual labor.
- **Non-technical creators** who want AI automation but still need the ability to make minor manual tweaks without re-prompting.
- **Creators who reference real people, places, or events** and need accurate images (not AI hallucinations) inserted at specific timestamps.
- **Creators building a reusable production system** — those willing to invest upfront in style guides and skills to achieve near-zero-prompt editing over time.
- **Color-grading non-experts** who want consistent look-and-feel applied automatically across all clips.

---

## Patterns & frameworks

**The 90/10 Editing Split**
AI handles the time-consuming 90% (rough cut, motion graphics, sound, music, B-roll, subtitles, color correction); the human handles the fast 10% (minor tweaks, volume sliders, style fixes). The rationale: small edits are faster by hand than by prompt; large structural edits are faster by AI than by hand.

**The Dictionary/Manifest Pattern**
For any asset library AI cannot directly perceive (sound effects, music tracks), a companion text file describes each asset by name and description. AI reads the manifest to select the correct asset without needing to "hear" or "see" it. Applicable to: sound effects, music libraries, motion graphic templates.

**The Skills System**
Reusable prompt templates saved in the project working folder. A skill encodes a multi-step process (e.g., "full edit" = rough cut → motion graphics → sound effects → music → verify). Invoking a skill by name triggers the entire pipeline. Skills accumulate over time and encode the creator's preferences, reducing prompt length and improving consistency.

**The Style Guide Asset**
A persistent document encoding brand colors, fonts, layout preferences, editing rhythm, and graphic styles. Serves as the AI's "memory" of how the creator likes their videos to look. Created once (by feeding existing videos or a website to Claude), then referenced on every edit. Acts as a substitute for briefing a human editor.

**Word-Level Timestamp Pipeline**
Raw video → strip audio → Deepgram transcription (word-level timestamps) → AI uses timestamps to identify silence/bad-take boundaries → cuts made in CapCut timeline. The same timestamp data also drives motion graphic and sound effect placement downstream.

**The Two-Layer Rotoscoping Process**
(1) Identify the target clip segment. (2) Duplicate it onto a layer above. (3) Mute the top layer. (4) Apply CapCut's background removal to the top layer. (5) Insert text/graphic between the two layers. (6) Animate text in/out. This is described as a step-by-step process that must be explicitly spelled out in the prompt because the abstract instruction "rotoscope this" is insufficient.

**The Working Folder Convention**
All Claude sessions for a given project are opened within the same dedicated folder. This folder stores the style guide, skills, asset dictionaries, and project history — giving Claude persistent context across sessions without re-briefing.