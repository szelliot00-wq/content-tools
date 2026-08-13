# Claude + Remotion Just RETIRED video editors... (Full Remotion Tutorial)

Video ID: `-Ut8Jm0O_oA`

## Summary
This tutorial demonstrates how to use Remotion (a code-based video rendering framework) with Claude to automate video editing entirely through AI prompting. The presenter walks through setup, basic animation creation, and progressively more complex edits on a real recorded video — including silence removal, subtitles, motion graphics, AI-generated images, and AI-generated video clips. The core argument is that AI video editing is 10x faster and ~1,000x cheaper than human editors, but raw AI output requires a structured, template-driven workflow to be consistently good. The video is most relevant to content creators, solo operators, and marketers who produce regular video content and want to reduce editing costs and time.

## Key insights
- Remotion is a JavaScript-based video rendering library that Claude can write code for, enabling fully programmatic video creation and editing via natural language prompts.
- Setting up Remotion involves installing it from its GitHub repo into a local working folder, then pointing Claude at that folder for all subsequent video work.
- Voice transcription (the presenter uses a tool called Cicero) produces better AI outputs than typing because speech is naturally more verbose, giving Claude more context to work with.
- Claude runs a self-verification loop after generating video code — it checks its own output and attempts fixes before presenting the result.
- Silence and bad-take removal is typically the first editing step: Claude can strip leading/trailing pauses and fumbled sections from raw footage.
- Subtitles can be generated with a single bare prompt ("add subtitles"), though more specific prompts yield branded, stylized results (word-level highlighting, custom fonts, colors).
- Motion graphics can be inserted at specific timestamps tied to spoken words (e.g., a bar chart animation triggered when the speaker says "10 times faster and a thousand times cheaper").
- AI image generation (OpenAI GPT Image 2 via a connector called "Kai AI") can be triggered directly from within the Remotion/Claude workflow to create B-roll imagery from a text description.
- AI-generated images can then be passed as reference frames to a video generation model (Google Gemini/Omni via Kai) to produce short animated video clips, automatically muting the clip's native audio when inserted.
- The biggest failure mode with raw AI editing is "AI slop" — when AI makes all creative decisions freely, quality is inconsistent and fixing bad outputs costs more time than it saves.
- The presenter's solution is a "pre-editor tool" that forces human curation before handing off to AI, preventing bad outputs rather than fixing them after the fact.
- The pre-editor tool works by: (1) transcribing the video, (2) letting the user browse motion graphic templates, (3) selecting transcript segments and assigning templates with specific instructions, and (4) exporting a structured prompt that Claude/Remotion executes reliably.
- Templates are the "secret sauce" — they constrain AI creativity to a known-good design, so AI only fills in the content (text, timing) rather than inventing the visual style.
- The tool also supports rotoscoping effects (e.g., a word appearing behind the on-screen subject) through template selection.
- The workflow is compatible with both Remotion and Hyperframes, which the presenter describes as functionally similar tools.
- The presenter claims everything visible in the tutorial video itself was AI-edited using this exact workflow.

## Use cases
- Solo content creators who publish regularly and can't afford or don't want to manage a human video editor.
- Marketers producing high volumes of short-form or long-form video content (ads, explainers, social clips).
- Entrepreneurs or coaches who record talking-head videos and want automated post-production (silence removal, subtitles, B-roll, motion graphics).
- Anyone needing to add branded motion graphics at specific moments in a video without knowing video editing software.
- Creators who want AI-generated B-roll (images or video) inserted automatically at relevant moments in their footage.
- Teams that need a repeatable, quality-controlled video editing pipeline that doesn't depend on a single human editor.
- People building or scaling a content business who want to cut per-video production costs dramatically.

## Patterns & frameworks

**Template-Driven AI Editing (Pre-Editor Workflow)**
The presenter's core framework. Instead of prompting AI freely to "edit this video," the human first curates all creative decisions using a tool that maps transcript segments to pre-approved visual templates. The resulting structured prompt is then fed to Remotion/Claude, which fills in content but does not invent style. This inverts the typical AI workflow: human sets the creative constraints, AI does the execution. Outcome is consistent, on-brand output with minimal revision.

**Progressive Complexity Prompting**
Start with the simplest edit (silence removal), verify it, then layer on additional edits one at a time (subtitles → motion graphics → AI images → AI video). Each step builds on the last inside the same Remotion project, rather than attempting a fully-specified edit in one shot. Reduces error surface and makes debugging easier.

**Tool Chaining via a Connector Layer ("Kai AI")**
External AI services (image generation, video generation) are connected to the Claude/Remotion pipeline through an intermediary connector. Claude generates the prompt, passes it to the external model, retrieves the asset, and inserts it into the video timeline automatically. This pattern extends Remotion's native capabilities to any API-accessible AI service.

**Self-Verification Loop**
After generating video code, Claude automatically reviews its own output for errors and attempts corrections before surfacing the result. This is a built-in quality gate that reduces the number of human review cycles needed for basic correctness issues.

**Voice-First Prompting**
Using voice transcription rather than typing for prompts consistently produces better AI outputs because spoken language is naturally more descriptive and contextually rich. Framed as a general principle applicable beyond video editing to any AI task.