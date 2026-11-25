# Learn 95% of Google Antigravity in 17 Minutes (with Gemini 4 Neon)

Video ID: `7I8B7CQky0Y`

## Summary
This video is a beginner-to-pro tutorial on using **Antigravity**, Google's AI coding/agent tool powered by **Gemini 4 Neon**, structured as a 5-step course. The presenter builds a real open-source project — a "video explainer" skill that generates 60-second explainer videos in three styles (motion, illustrated, 3D) — to demonstrate each feature hands-on. The core argument is that getting great AI output requires iterative feedback and taste, not one-shot prompting. It's most relevant to product managers, indie developers, and technical creators who want to build and ship AI-powered tools quickly.

## Key insights
- **Model selection**: Use Gemini 4 Neon on medium or high settings ~99% of the time — faster than Carbon, smarter than Hydrogen, good at most tasks
- **Orchestrator mode**: Pairs Neon for planning with a cheaper model (Hydrogen) for implementation — saves tokens without sacrificing quality
- **Thread organization**: Group threads by *status* (not project) to surface the most recently active work first
- **Voice-first planning**: Use live voice mode to brainstorm like talking to a smart colleague; dictate into Antigravity and read output as text
- **`/grill-me` command**: Built-in skill that asks clarifying questions before building — reveals hidden decisions (e.g., free local TTS vs. Gemini API) and aligns the plan
- **Iteration over one-shots**: The black hole explainer took 3 versions to get right — V1 looked like slides, V2 improved motion, V3 added sound design, parallax, and web-sourced visuals
- **"Give me your 3 best ideas"**: A reliable tactic to get the model to surface improvements it wouldn't volunteer — the model often has better ideas than the user
- **`/swarm` command**: Spins up multiple parallel agents (e.g., a director + 3 act agents) to build complex multi-part outputs simultaneously
- **`by the way` command**: Lets you ask a side question mid-swarm without interrupting the running agents
- **Browser use**: Antigravity can navigate the browser, watch videos, and extract stylistic understanding — useful for style replication and form-filling
- **Remote control**: The Antigravity web app (antigravity.google.com) works as a mobile remote for all threads; can be pinned as a PWA to the home screen
- **Plugin integrations**: Connect Gmail, Google Calendar, Workspace apps, Figma, Linear, etc. at setup
- **Automations**: Schedule recurring agent runs (e.g., every Monday at 9am) to auto-generate content on a cadence

## Use cases
- **Indie developers** building and shipping open-source AI tools or skills
- **Product managers** planning features by voice and iterating on specs with AI
- **Content creators** who want to auto-generate polished explainer videos on any topic
- **Parents or educators** wanting weekly auto-generated educational content for kids
- **Anyone doing web research or style replication** who wants the AI to watch/read source material itself
- **Teams running parallel workstreams** who want multiple agents working simultaneously on sub-tasks
- **Remote/async workers** who want to monitor and direct AI agents from their phone

## Patterns & frameworks

**5-Step Build Loop**
Setup → Plan → Build → Iterate → Launch. A repeatable workflow for taking any AI tool idea from zero to shipped open-source project.

**Orchestrator Mode**
A two-tier model pattern: Neon handles high-level planning and decision-making; a cheaper model (Hydrogen) executes the simpler implementation steps. Reduces token cost without sacrificing intelligence where it matters.

**`/grill-me` → Plan Alignment**
Before building, run `/grill-me` to have the AI ask clarifying questions. This surfaces hidden decisions, educates the builder on available options, and prevents rework caused by misaligned assumptions.

**Iterative Taste Feedback Loop**
Run → judge honestly → give specific feedback → ask for the model's own top ideas → repeat. The presenter explicitly rejects the "one-shot" mentality: even the best models need multiple rounds of human taste applied to reach quality output.

**Swarm Pattern**
Use `/swarm` to define a director agent and N parallel sub-agents for work that has independent parallel tracks (e.g., building 3 video styles simultaneously). Use `by the way` to inject side queries without blocking the swarm.

**Launch + Promote Pattern**
After building: clean up the codebase, push to GitHub with a strong README, generate a sizzle reel, and promote on social. Treats distribution as a first-class step in the build process, not an afterthought.