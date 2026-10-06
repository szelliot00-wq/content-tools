# Build an AI Language Tutor You Can Talk To (6 Steps)

Video ID: `GiaDdNvsadA`

## Summary
This video walks through building a voice-based AI language tutor app ("Tabby") that teaches Japanese through live conversation, using Google's Gemini Live APIs, Nano Banana for image generation, and tools like anti-gravity and Claude Code. The creator — a product manager — demonstrates a 6-step framework for going from raw idea to deployed web app in roughly 3 hours. The core argument is that the quality gap between "vibe-coded slop" and a genuinely useful app comes down to the iteration work done in steps 4 and 5, not the initial build. It is most relevant to product managers, indie hackers, and non-engineers who want to build personal utility apps using modern AI tooling.

---

## Key insights
- **Voice as the default UI**: The creator believes voice will become the primary way humans interact with computers and AI in the near future, and this app is a practical bet on that thesis.
- **The 3-hour build breakdown**: ~1 hour to explore, spec, and build the first version; ~2 hours iterating to improve quality — the majority of time is in refinement, not generation.
- **Don't start by building**: The creator explicitly tells the AI "don't build anything yet" in step 1, instead asking it to do research and ask 3 clarifying questions first. This surfaces key decisions early (lesson structure, phrase format, target user).
- **Spec = mocks + requirements**: The creator's "spec skill" produces both a PRD-style requirements doc and 2–3 representative screen designs side by side, making the spec far more actionable than text alone. Both mobile and desktop designs are included.
- **Human Review skill as a Google Docs-style feedback layer**: An open-source tool that opens the spec as an editable document with a feedback panel, allowing direct text edits and AI-directed design comments without going back to chat.
- **API key security**: Never paste API keys directly into the AI chat interface (risk of training data or leakage). Instead, paste them directly into the local `.env` file. The creator demonstrated this live and deleted the accidentally-exposed key immediately.
- **Tool switching by task**: Different AI tools were used for different phases — AI chat for brainstorming, anti-gravity for initial build (because it knows Google APIs best), Claude Code for iteration (because it has browser/computer use for live testing).
- **Lesson structure: teach then role-play**: Each of the 10 lessons has two phases — (1) the AI coach teaches all 10 phrases one by one, then (2) runs a simulated real-world conversation where the user must recall and use the phrases in context (e.g., navigating Tokyo in a day).
- **Phrase format**: Each phrase bubble shows Japanese script, Romanji (pronunciation), and English — a deliberate design choice surfaced during the brainstorming phase.
- **Content iteration in a separate thread**: The creator spun up a dedicated "content thread" just for lesson design, keeping it separate from the app-building thread for clarity.
- **You don't need to read Japanese to speak it**: An AI-surfaced insight that shaped the lesson content — lessons focus entirely on spoken/conversational phrases, not reading or writing.
- **Auto-added passcode on deploy**: Without being asked, the AI added a passcode to the deployed app to protect against unexpected Gemini API costs from unknown users — a positive example of AI proactive reasoning.
- **Deployment is nearly free**: Vercel's free tier covers the first few deployed projects; Google AI Studio also now supports a website hosting feature as an alternative.
- **Repurposable template**: The app architecture is language-agnostic — swap the lesson content and image prompts to build a tutor for Italian, Spanish, Chinese, etc.
- **Nano Banana for diorama art**: Gemini's image generation model was used to create consistent "diorama style" scene art (miniature, desk-toy aesthetic) for each of the 10 lessons, plus a character image for the AI coach "Yuki."

---

## Use cases
- **Travelers** wanting a quick, practical phrase-learning app for an upcoming trip to any country.
- **Product managers or solo builders** who want a repeatable framework for going from idea to shipped app using AI, without relying on a dedicated designer or engineer.
- **Indie hackers** building personal utility apps — the video explicitly frames this as a "personal app" model, not a VC-backed product.
- **Language learners** who prefer conversational practice over reading/writing drills.
- **Anyone learning to use Gemini's Live APIs** for real-time voice/speech applications.
- **Builders who want to reduce vibe-coded output quality problems** — the framework directly addresses the slop vs. craft distinction.
- **Teams without designers** who need a spec process that includes visual mockups, not just text requirements.

---

## Patterns & frameworks

**The 6-Step App Build Framework**
A repeatable process for building AI-powered apps from idea to launch:
1. *Explore with AI* — brainstorm the problem/solution, have AI do research, ask 3 clarifying questions before any building starts.
2. *Draft a spec and design* — produce a combined doc with screen mocks + requirements; use the "spec skill" or ask AI to generate 2–3 key screens alongside requirements.
3. *Build the first version* — hand the spec to AI and ask it to build the full app in one shot.
4. *Improve the app* — iterate on UX, bugs, and performance using an AI tool with browser/computer use for live testing.
5. *Improve the content* — iterate on the actual lesson/content quality in a separate dedicated thread; this is often overlooked but determines real-world usefulness.
6. *Launch* — deploy to Vercel, Google AI Studio, or any free hosting provider.

**"Don't Build Yet" Brainstorm Pattern**
In step 1, explicitly instruct the AI not to build anything — instead ask it to research first and return 3 clarifying questions. This front-loads decision-making and avoids building in the wrong direction.

**Spec Skill (Mocks + Requirements)**
A product spec format that combines a visual mockup panel (2–3 key screens, mobile and desktop) with a written requirements and tech stack panel in the same document. Faster to react to than text-only PRDs.

**Human Review Skill**
An open-source Google Docs-style interface layered on top of a spec HTML file. Supports direct text edits, design feedback via comments, and AI-agent execution of the feedback — bridging the gap between static spec and live iteration.

**Teach → Role-Play Lesson Structure**
A two-phase lesson design pattern for language learning apps: phase 1 introduces all target phrases explicitly (coach-led), phase 2 puts the learner in a simulated real-world scenario where they must recall and use the phrases in live back-and-forth conversation.

**Slop vs. Craft Distinction**
The creator's mental model for quality: the initial AI-generated build is the floor, not the ceiling. Quality is determined entirely by how much human-guided iteration happens in steps 4 and 5 — testing personally, inviting friends to test, and caring about whether the app actually accomplishes its goal.