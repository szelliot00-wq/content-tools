# 8 ChatGPT Skills That Save Me 5 Hours a Week

Video ID: `PZHBW6yld5U`

## Summary
The video walks through a creator's three-step system for using ChatGPT to automate a weekly podcast production workflow, reducing a multi-day manual process to one that saves roughly 5 hours per week. The creator (Peter Yang) argues that rather than using AI ad-hoc, you should map your entire workflow, build reusable "skills" (custom AI instructions) for each phase, and chain those skills together into an end-to-end automated pipeline. He demonstrates this concretely by walking through how he produced a real podcast episode with Ethan (product lead at OpenAI) on ChatGPT for personal finance. The video is most relevant to content creators, podcasters, YouTubers, and knowledge workers who have repetitive multi-step workflows they want to systematically offload to AI.

---

## Key insights
- The creator reduced a **15-step podcast production process** from multiple days of work to roughly 90% automated, saving at least 5 hours per week.
- The core insight is treating AI not as a one-off tool but as a **system of reusable skills** — custom instruction sets that can be called, chained, and improved over time.
- **Phase 1 (Podcast Prep):** ChatGPT researches the guest, scans YouTube for well-performing videos in the niche to validate the episode idea, and drafts a structured interview guide with questions and example answers — all from a single prompt.
- **Phase 2 (Podcast Edit):** Using the **Riverside MCP** (Model Context Protocol integration), ChatGPT reads the auto-generated transcript, writes intro reel options, identifies clip candidates with timestamps, flags moments to cut (technical difficulties, dead air), and packages everything into a **Linear ticket** for the video editing team.
- **Phase 3 (Podcast Production):** The most complex skill orchestrates sub-skills to produce: a Substack newsletter post, YouTube/Spotify show notes (with timestamps auto-derived from the uploaded video), thumbnail/title combinations for A/B testing, social media teasers and posts (with image selection), and scheduled clips — all in sequence.
- He uses **GPT-4o medium** for all of this — not frontier/reasoning models — because it is "plenty good enough" and saves on token costs.
- A key workflow improvement technique: before making manual edits to AI output, **ask AI to take a snapshot**, then make your edits, then have AI compare before/after to extract the delta. You then feed those changes back into the skill as updated instructions so it doesn't repeat the same mistakes.
- The creator explicitly rejects fully autonomous output: he reviews every step, applies his own taste and judgment, and gives feedback to iterate — the goal is speed without sacrificing quality ("I don't want it to just pump out slop").
- **Skill improvement is ongoing**: after each episode, changes made during production are summarized into a numbered list, reviewed one by one, and accepted or declined before being written back into the skill — a deliberate feedback loop.
- The more **MCPs and plugins** you connect to ChatGPT (e.g., Riverside for recording/clips, Figma for thumbnails, Typefully for scheduling, Linear for project management, browser-use for YouTube settings), the more steps AI can own end-to-end.
- Thumbnail/title packaging still takes 30–40 minutes even with AI because it requires subjective taste — but AI accelerates the research and option-generation phase substantially.
- He acknowledges a meta-lesson: even with the system built, he still personally drives it all, and he notes he probably needs to hire a human operator to run the AI system so he can step back further.

---

## Use cases
- **Podcasters and YouTubers** who produce episodes on a regular cadence and have repetitive pre/post-production tasks.
- **Content marketers** who need to repurpose a single piece of content (video/audio) into multiple formats: newsletter, social posts, clips, show notes.
- **Solo creators** who lack a large team but need to produce at a team-level output volume.
- **Knowledge workers with repeating workflows** — weekly reports, client deliverables, research briefs — who want to map and systematically automate their manual steps.
- **Anyone using project management tools** (Linear, Notion, Asana) who wants AI to auto-generate and populate task tickets from source content.
- **Social media managers** who need to schedule posts, find images, write copy, and manage multiple platforms from one workflow.
- **People building AI "skills" or custom GPTs** who want a practical, production-tested methodology for structuring and iterating on those instructions.

---

## Patterns & frameworks

**The Three-Step Automation Framework**
The central repeatable process: (1) Map every manual step of a workflow exhaustively — don't skip anything; (2) Build AI skills (custom instruction sets) for each phase or cluster of steps; (3) Chain the skills together so they can be called in sequence to automate the full workflow end-to-end. The author treats this as universally applicable beyond podcasting.

**The Skill-per-Phase Pattern**
Instead of one giant prompt, the workflow is decomposed into discrete, named skills — `podcast-prep`, `podcast-edit`, `podcast-production` — each with clear trigger conditions and step-by-step instructions. The top-level `podcast-production` skill acts as an **orchestration layer** that calls the sub-skills in the right order depending on where in the production sequence you are.

**Snapshot-Delta-Update Loop**
A specific technique for improving skills over time: (1) Have AI snapshot the current output before manual edits; (2) Make your manual edits; (3) Have AI diff the two versions and list all changes; (4) Review each change and accept/decline; (5) Write accepted changes back into the skill's instructions. This prevents regression and continuously improves one-shot accuracy.

**Validate Before You Produce**
Before committing to producing an episode, the prep skill checks whether the topic has existing high-performing YouTube content. If there's no audience interest, the episode may not be worth making. This front-loads strategic judgment into the workflow rather than discovering a weak topic after recording.

**Human-in-the-Loop Taste Layer**
The framework explicitly preserves human review at every stage rather than running fully autonomously. AI handles generation and research; the creator handles judgment, feedback, and final approval. The framing is: AI removes the *time cost* of doing work, but the creator's taste and craft are still applied to the output.