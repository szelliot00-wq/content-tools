# Step-by-Step AI Motion Graphics: Fable 5 vs GPT 5.6

Video ID: `yH2oLU4MzoM`

## Summary
This video walks through a step-by-step process for creating AI-generated motion graphics using a tool called Hyperframes, which generates HTML-based animations that can be rendered as video overlays. The presenter compares two AI models — Anthropic's Fable 5 and OpenAI's GPT 5.6 — across two approaches: raw one-shot generation versus a structured "pre-editor + template" method they developed. The core argument is that raw AI output is mediocre, but combining a curated asset library with pre-built templates dramatically improves quality, reduces variability between models, and enables cheaper, faster production. The video is most relevant to solo content creators, video editors, and AI practitioners looking to automate or accelerate short-form video production.

## Key insights
- **Hyperframes** is a free skill/plugin that enables AI agents (Claude, OpenAI, etc.) to generate motion graphics by writing HTML, which is then rendered in "Hyperframe Studio."
- **Raw one-shot AI output is insufficient for publication.** Both Fable 5 and GPT 5.6 produced acceptable but clearly AI-generated results when given no additional structure — graphics obscured faces, layout was poor, and GPT 5.6 failed on several elements entirely.
- **Eight foundational assets** should be connected to Hyperframes before starting any project: (1) video source, (2) AI video generation API (e.g., Fal or Ky AI), (3) AI voiceover API (ElevenLabs), (4) word-level transcription API (Deepgram — offers ~$200–$300 free credit), (5) sound effects dictionary, (6) stock footage dictionary, (7) icons dictionary, (8) a design/brand MD file.
- **Dictionaries outperform real-time AI perception.** For sound effects, stock footage, and icons, manually curating a dictionary (file name + description + usage context) is far more reliable than having AI analyze media files directly. AI picks from the dictionary rather than "listening" or "looking" at assets.
- **Word-level timestamps (via Deepgram) are critical** for accurately timing motion graphics to spoken content — the system knows *exactly* when each word is said rather than guessing.
- **The pre-editor tool is the key differentiator.** The presenter built a custom web UI where you: upload/transcribe the video, select time ranges, browse a template library, assign a template to each range, and add light natural-language instructions (e.g., "swap icons for Anthropic and OpenAI logos"). The tool then compiles everything into a single structured prompt.
- **Templates eliminate most of the model's creative burden.** Instead of asking the AI to design from scratch, it only needs to swap in correct content — text, icons, colors — within a fixed visual structure. This is faster and more consistent.
- **Template method reduces inter-model variability.** In the raw test, Fable 5 and GPT 5.6 produced noticeably different results. After applying the pre-editor/template method, outputs from both models were nearly indistinguishable — meaning you can use a cheaper model and still get high-quality results.
- **Cost and speed comparison:** The AI approach (even with manual template selection) is described as ~10x faster than a human editor and ~1000x cheaper. A comparable human-edited clip might cost ~$30; the AI approach costs a fraction of that.
- **Verification loops matter.** The presenter appended "please run a verification loop to check for errors" to both model prompts before rendering, treating error-checking as a standard step in the workflow.
- **Future automation planned:** The presenter is logging which templates are used for which transcript phrases, with the goal of eventually training a skill to automate template selection — removing the last manual step.
- **Voice input (Cicero tool)** is highlighted as a significant productivity multiplier when working with AI agents throughout the video creation process.

## Use cases
- **Solo video creators** who publish regularly and want to add polished motion graphics without hiring an editor or learning After Effects.
- **Content agencies** looking to scale video production cheaply across multiple clients.
- **Marketers** creating short-form educational or explainer clips with branded overlays.
- **AI practitioners and developers** wanting to understand how to build a structured, template-driven pipeline around generative AI tools.
- **Anyone comparing Anthropic vs. OpenAI** for a specific creative coding task (motion graphics generation via HTML).
- **Creators with an existing brand identity** who want to enforce visual consistency across AI-generated content using a design file and asset dictionaries.
- **Budget-conscious producers** who want near-professional output without the cost of premium human editing services.

## Patterns & frameworks

**The Eight-Asset Foundation**
Before any video project begins, connect eight resources to Hyperframes: video source, AI video API, voiceover API, word-level transcription API, sound effects dictionary, stock footage dictionary, icons dictionary, and a brand/design MD file. This setup front-loads the configuration cost so every subsequent project runs faster and with higher consistency.

**Dictionary-Based Asset Selection**
Rather than having AI perceive or analyze media files in real time, curate a plain-text dictionary for each asset category (sound effects, stock footage, icons) that lists the file name, a description, and recommended use cases. The AI reads the dictionary and selects — a much more reliable and computationally tractable task than audio/visual analysis.

**Three-Stage Progression (Raw → Guided → Template-Driven)**
The video demonstrates a deliberate quality ladder: (1) raw one-shot prompting produces mediocre output; (2) iterative prompting with some guidance improves things but is slow; (3) the pre-editor + template method produces near-publish-ready output in roughly one minute of manual overlay assignment. The framework argues you should skip stages 1 and 2 and go straight to stage 3.

**Pre-Editor + Template Workflow**
A structured pipeline consisting of: upload video → transcribe with word-level timestamps → mark bad takes → select time ranges → assign pre-built templates to each range → add brief natural-language customization instructions → export as a single compiled prompt → send to AI model → render in Hyperframe Studio. Templates act as guardrails, constraining AI output to known-good visual structures.

**Model-Agnostic Template Guard Rails**
By giving the AI a template to fill rather than a blank canvas to design, the creative variance between models collapses. This means: (a) you can swap in a cheaper model without sacrificing output quality, and (b) brand consistency is preserved regardless of which AI provider you use.

**Feedback-Loop Data Collection for Future Automation**
Every manual template assignment is logged (template ID + transcript phrase + timestamp). Over time this dataset can train a skill to automate the selection step — turning a human-in-the-loop process into a fully automated one. This is a deliberate "harvest now, automate later" pattern.