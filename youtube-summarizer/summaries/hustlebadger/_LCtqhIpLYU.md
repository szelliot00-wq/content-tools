# AI Landscape for PMs in 2026

Video ID: `_LCtqhIpLYU`

## Summary
This talk by Ed from Hustlebadger distills practical AI tooling knowledge gained from training hundreds of product managers and other professionals. Ed organizes the AI landscape into three main categories — AI chatbots, agent building platforms, and local agents — and argues that local agents (like Claude desktop/code) represent where the future of knowledge work is heading. The talk covers how all these tools share the same underlying technology (foundational models + context windows), practical techniques for getting better outputs, how to build and evaluate AI agents, and how PMs can apply these tools to their day-to-day work. It is most relevant to product managers, operations professionals, and non-technical knowledge workers who want to move beyond basic AI chatbot use.

## Key insights
- **All AI tools run on the same underlying technology**: every input — whether a user prompt, a skill, a local file, or a CLAUDE.md — is converted to plain text → tokens → sent to a foundational model → returned as tokens → converted back. Understanding this means prompting skills transfer across all platforms.
- **Three tool categories, not dozens**: AI chatbots (ChatGPT, Claude web, Gemini), agent building platforms (Zapier, n8n, Make, Relay, Gumloop), and local agents (Claude desktop, Codex, Cursor, terminal). Prototyping tools (Lovable, v0, Figma Make) are being absorbed into local agents as those mature.
- **Local agents are eating the other categories**: people who get comfortable with Claude desktop or Codex are using prototyping tools and browser chatbots less, because local agents give better context awareness and more capability out of the box.
- **Context is everything for LLM output quality**: without context, LLMs return "beige" answers — the average of all human knowledge. Good context + clear objectives = dramatically better results.
- **Voice input is underutilized**: speaking is faster than typing, and LLMs handle stream-of-consciousness rambling well. Tools: native microphone button, OS-level hotkey dictation, Super Whisper / Whisper Flow (which uses a small LLM to clean up raw dictation).
- **Screenshots as context**: dropping a screenshot into a chat window is highly effective for debugging and problem-solving. Example: a typo in Spotify API credentials ("client credential" vs. "client credentials") was caught instantly from a screenshot.
- **LLMs default to asking too many questions** — this is a deliberate engagement tactic. Explicitly cap the number of questions (e.g., "ask me five questions") to avoid this.
- **Step-by-step working dramatically improves output quality**: it forces deeper model reasoning and gives you course-correction opportunities throughout the task rather than only at the end.
- **The briefing technique**: start by telling the LLM the problem, any references, your tentative ideas (flagged as uncertain), and ask it to research and clarify. Then get 2–3 high-level approaches with trade-offs before committing to a plan.
- **Skills are saved prompts**: you can teach a local agent a repeatable process once, save it as a skill with a keyword trigger, and call it without re-briefing. Example: "contact lookup" pulls a full relationship summary and next-action recommendation.
- **Local agents are better than web chatbots** because they already have access to local files, can be briefed once and remember it persistently, and can connect to other apps via MCP tool documentation passed through the context window.
- **Multi-chat parallel work**: local agents can take several minutes on complex tasks. Experienced users spin up 3–4 simultaneous chats and context-switch between them, matching the number of active chats to their cognitive capacity that day.
- **The agentic workflow spectrum**: deterministic (if-this-then-that), agentic workflow (linear flow with LLM enrichment steps), true agent (nonlinear flow where the LLM decides which tools to call). Each step right increases power but also increases output variability.
- **Real example of an agentic workflow**: 4 hours before any calendar meeting with an external guest → look up email history, recent meetings, LinkedIn profile → send a personalized briefing email. Built in an agent platform, runs automatically.
- **Agents require constant human supervision**: "There are no agents without humans." Production-grade agents need ongoing error analysis, prompt tuning, and maintenance — this is a known limitation, not a temporary one.
- **Workflows vs. agents use-case split**: workflows suit simple repeatable internal processes (lead enrichment, support ticket classification, PDF conversion) and can be built by non-technical staff. True agents are only worth building for customer-facing products or core competitive differentiators, and require specialist time investment.
- **Data privacy trade-off**: more data = more useful outputs. Sensitive data (passwords, SSNs) should never go into LLMs. A practical anonymization pattern: strip PII → replace with random identifiers → send to LLM → de-anonymize the response locally.
- **Getting started with local agents**: build something trivial first (retro game, weather app, to-do list) to learn the tool before attempting real work. The barrier is mental, not technical.
- **CLAUDE.md / instructions files** should be kept lean: who you are, core principles, and an index pointing the harness to relevant files. They are injected into every conversation's context window.

## Use cases
- **PMs writing recurring reports**: map out every step of your weekly status report, identify which steps Claude can automate (pulling Jira tickets, scanning emails), and build a workflow or skill around it.
- **Sales pipeline management**: use a "contact lookup" skill in Claude desktop to surface relationship history, last touchpoints, and next recommended actions before every call.
- **Pre-meeting research automation**: agent building platform workflow that fires 4 hours before each external calendar meeting, researches attendees, and emails you a briefing.
- **Lead enrichment**: agentic workflow that takes inbound lead form data, researches the company online, enriches the CRM record, and sends a truly personalized follow-up email.
- **Rapid UI/design exploration**: ask a local agent to mock up 4 variations of a UI element in HTML — takes ~1 minute and surfaces options you can react to rather than specify upfront.
- **Internal helper tools**: build tools that only run on your own machine (markdown editor, AI-powered to-do list, route planning app) — no deployment, no maintenance burden for others.
- **API debugging**: screenshot error states and drop into a chatbot to diagnose issues (e.g., catching a typo in API credentials).
- **Content creation with brand context**: upload tone-of-voice docs, past posts, and style guidelines into a ChatGPT project so every content prompt benefits from persistent context.
- **Job application pipeline**: scrape job listings via API or custom scraper, display in a custom UI, use Claude to tailor CVs and cover letters per application.
- **Data analysis with privacy constraints**: anonymize PII locally, send clean data to an LLM for analysis, de-anonymize the result — keeps sensitive data off external servers while still using AI processing.
- **Eval/QA for AI agents**: any team building internal AI tooling that needs measurable, repeatable quality assurance before and after changes to prompts or data.

## Patterns & frameworks

**Three-category AI tool taxonomy**
Chatbots (browser Q&A) → Agent building platforms (drag-and-drop workflow automation) → Local agents (desktop harness with file/tool access). Use this to decide where to invest time rather than evaluating tool-by-tool.

**The agentic workflow spectrum**
A left-to-right spectrum from fully deterministic (fixed if/then logic) through agentic workflows (linear flow with LLM enrichment steps) to true agents (nonlinear, LLM decides tool calls). Complexity and output variability both increase as you move right; use the simplest option that solves the problem.

**Step-by-step working method (heavyweight prompting process)**
1. Brief the LLM: problem statement, references, tentative ideas (flagged as uncertain), request for research and clarifying questions.
2. Get 2–3 high-level approaches with trade-offs.
3. Provide feedback and get a numbered plan.
4. Work through each step one at a time, requesting detailed guidance per step.
Scale the depth of this process to task complexity.

**Context injection techniques**
- Voice input (native mic, OS hotkey, Super Whisper/Whisper Flow)
- Screenshot drops for visual/debugging context
- File uploads or project libraries for persistent brand/style context
- "What do you know about X?" to prime the model with its own research
- "Ask me N questions" structured interview to surface requirements you haven't articulated

**Skills as saved playbooks**
Teach a local agent a process once during a conversation → at the end, say "save this as a skill" → assign a keyword trigger → call the skill in future sessions without re-briefing. Equivalent to a reusable saved prompt with a specific invocation pattern.

**Personal operating system pattern**
Combine: a local markdown file (persistent memory/to-do list) + skills (saved processes) + MCP tool connections (calendar, email, notes) + a scheduled skill that re-prioritizes the to-do list daily based on live data. Creates an always-on context layer around your most important recurring work.

**Eval framework (QA for probabilistic systems)**
1. Generate test cases covering all user intent dimensions (trip length, budget, group type, etc.).
2. Run all test cases through the agent; collect outputs.
3. Human-review outputs and annotate good/bad responses with failure reasons.
4. Cluster failures into 5–6 distinct failure modes.
5. Design one eval per failure mode: deterministic code check if testable by rule, or LLM-as-judge (narrow binary pass/fail prompt) if subjective.
6. Track pass rates as a percentage benchmark; rerun after any agent change to measure improvement vs. noise.