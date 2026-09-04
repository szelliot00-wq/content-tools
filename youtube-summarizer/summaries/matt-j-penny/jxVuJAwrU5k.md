# Claude Edited This Entire Video in DaVinci Resolve (Full Setup Guide)

Video ID: `jxVuJAwrU5k`

## Summary
This video demonstrates a complete AI-powered video editing workflow using Claude (Anthropic's AI assistant) connected to DaVinci Resolve via a custom scripting layer, with Remotion for motion graphics and Google Gemini for AI-generated video clips. The creator, Matt, walks through how he edited the video's own intro using this system — taking a 2-minute 24-second raw recording down to a 36-second polished intro without manual editing. The core argument is that with the right setup, templates, and prompt engineering, non-editors can produce professional video content almost entirely through AI. It is most relevant to content creators, YouTubers, and marketers who want to automate or drastically accelerate their video production process.

## Key insights
- **Three-tool stack**: The system uses (1) DaVinci Resolve for cuts and basic text overlays, (2) Remotion to generate motion graphics from HTML/code, and (3) Google Gemini (Omni) for AI-generated video clips or visual effects
- **The connector is the key**: A downloadable folder of scripts acts as a bridge between Claude and DaVinci Resolve, telling Claude which APIs and interactions to use — available free via a link in the video description
- **Model choice matters**: Sonnet 5 is recommended as a starting point; upgrading to Opus 5 or Fable 5/5.1 produces noticeably better results, especially with complex edits
- **Edit time**: Simple edits may take ~10 minutes; complex full-video edits can take up to a couple of hours
- **Why Remotion instead of pure DaVinci**: DaVinci requires pre-made visual assets; Remotion generates visuals from HTML code, which AI excels at writing — making complex animated overlays (like a Claude interface mockup) achievable without any pre-built assets
- **Template system is the secret weapon**: Pre-built visual templates dramatically improve reliability and output quality. Claude's job is reduced to swapping in the correct text/content, not designing from scratch — this reduces errors, cost, and iteration cycles
- **Voice input yields better prompts**: Matt uses a voice transcription tool (his own "Cisero") to dictate prompts rather than typing, noting that speaking produces more context-rich, natural prompts that get better results
- **Manual edits still have a place**: Small changes (e.g., changing text color) are faster to do manually in DaVinci than prompting Claude to do them, especially at scale where token costs and time add up
- **The "pre-editor" tool**: A proprietary tool (inside Matt's paid mastermind) that transcribes raw video, highlights cut sections in red, lets the creator assign overlay templates to specific moments, and then auto-generates the full prompt to feed into Claude
- **The Google Omni integration**: Claude uses computer-use capability to screenshot the DaVinci editor, sends the screenshot to Google Omni via an API tool called "Kai," and receives back a generated video clip that is then inserted into the DaVinci timeline
- **Not fully autonomous yet**: Choosing which overlays to apply and when still requires human judgment — Matt goes through the transcript manually selecting templates per section. He notes full AI autonomy for this step is in development

## Use cases
- **Solo content creators** who want to produce polished YouTube videos without hiring an editor
- **Marketers and agencies** producing high volumes of video content who want to reduce per-video editing time
- **Non-editors** who have the raw footage but lack DaVinci Resolve skills — the AI handles the technical editing layer
- **Creators with established visual styles** who have built a library of branded templates and want consistent output at scale
- **AI/tech-savvy creators** comfortable with prompt engineering who want to push the limits of AI-driven production pipelines
- **Businesses doing video marketing** (tutorials, demos, social content) where speed and volume matter more than bespoke artistry

## Patterns & frameworks

**Template-First Editing**
Rather than asking AI to design visuals from scratch, pre-build a library of branded visual templates. Claude's job is only to select the right template and swap in context-specific content (text, timestamps). This reduces hallucinations, lowers cost, speeds up execution, and produces more consistent branded output.

**Three-Layer AI Editing Stack**
A tiered tool architecture: DaVinci Resolve handles structural edits (cuts, timeline assembly, text overlays); Remotion handles dynamic/coded motion graphics; external AI models (Google Omni) handle generative video clips. Each tool is used for what it does best rather than forcing one tool to do everything.

**Prompt-as-Edit-Script**
The editing prompt is a structured document specifying: (1) source video path, (2) exact timecodes to keep/cut, (3) overlay assignments with template references and content instructions. This prompt is generated by a pre-editor tool rather than written by hand, making it reproducible and scalable.

**Pre-Editor → Claude → DaVinci Pipeline**
A linear production pipeline: raw video → pre-editor tool (transcription + cut selection + template assignment + prompt generation) → Claude (executes edits via DaVinci scripting layer) → DaVinci timeline (final output). Human judgment is concentrated at the pre-editor stage; execution is fully automated.

**Voice-to-Prompt Workflow**
Using a voice transcription tool to dictate prompts rather than typing them. The rationale is that spoken language naturally includes more contextual detail ("yapping"), which produces richer prompts and better AI outputs — a generalizable principle for any AI-assisted workflow.