# 5 Rules for Building AI Agents That Work in Production | Nan Yu & Jacob Shumway

Video ID: `4mKtJzfGj0U`

## Summary
This video features Nan Yu and Jacob Shumway from Linear discussing how they built Linear's production AI agent from the ground up. They walk through the full journey from a 2025 internal memo to a shipped product, covering architecture decisions, evaluation strategies, and lessons learned. The core argument is that agents work best when given minimal instructions, dynamic context-loading tools, and clear entry points in real user workflows — not just a chatbot interface. It is most relevant to product managers, engineers, and founders building or evaluating native AI agents for SaaS products.

## Key insights
- **An agent is an LLM running in a loop:** you give it a goal, tools to build its own context, and it calls tools turn-by-turn until the goal is accomplished — no magic beyond that.
- **Start scrappy:** Linear's first version called the LLM directly from the frontend, was flagged internal, and just exposed their existing command menu as tools. No architecture, just experiments.
- **Stealth launch over big reveal:** They silently hooked the agent into their existing Slack integration (where users already mentioned bots) and watched emergent usage patterns appear without directing them.
- **Emergent behavior surprised them:** Users discovered they could just tag `@linear` with an upward-pointing finger emoji and the agent would infer from context what to do — behavior nobody planned for.
- **The biggest problem in applied AI isn't model capability — it's underuse:** The models are smart enough; the gap is not deploying them well enough ("capability overhang").
- **Give it as little instruction as possible:** Over-prompting causes the agent to overfit on irrelevant instructions and overemphasize things that don't matter for the task at hand. Let the model figure it out.
- **Don't inject context — give tools to load context:** Instead of dumping everything into the prompt, give the agent tools to dynamically fetch what it needs. This prevents bloated, misfocused prompts.
- **Skills architecture unlocked scale:** Rather than giving the agent every possible action up front (which caused hallucinations and context issues), they built discrete "skills" (e.g., create issue, write document) that the agent dynamically loads based on the request.
- **Skills encode product opinions:** Each skill includes not just what to do but how Linear thinks it should be done — e.g., how to set priority when writing an issue, how to structure a description.
- **Router pattern for hot paths:** They built a small, cheap model as a router that sends ~80% of requests (mostly "create issue") to a highly optimized subprompt, and routes the rest to the full agent.
- **Start with the biggest model, then optimize down:** Use the most capable model until you've proven it works and built evals, then shrink the model for cost efficiency once you have a benchmark framework.
- **Eval mix: objective + subjective:** Objective evals check deterministic behavior (e.g., "always set status to in-progress when asked"). Subjective evals use LLM-as-judge for things like "did you extract the right title?" — but these are used sparingly because agents legitimately have high variance.
- **Don't over-eval variance:** Consistency isn't always valuable for agents. Too many evals around variable behavior produces false signals and constrains the agent unnecessarily.
- **Feedback loop → evals pipeline:** Thumbs up/down in product → team reviews weird cases → added to eval dataset → ongoing improvement. The "dude" incident (agent refused to respond because the user was informal) is a real example of this.
- **Agent self-reports missing capabilities:** When the agent is asked to do something it has no tool for, it calls a special tool to report that back. Linear auto-ingests these into their issue tracker — constantly streaming a backlog of capability gaps.
- **Ship when hero use cases are rock solid, accept variance elsewhere:** They defined a set of "in warranty" use cases (the ones they demo and market) and ensured those were reliable, while accepting that the long tail would have variance.
- **Every ticket is attributed to a human:** Even when the agent does the work, the issue is assigned to the human who initiated it. This keeps work tracked in the right backlog and prevents things from getting lost in Slack.
- **Native agent vs. MCP tradeoff:** An MCP just gives tools; it lets users go off the rails. A native agent lets Linear embed their product philosophy — what good PM work actually looks like — directly into the agent's behavior.
- **The chatbot is the follow-up, not the entry point:** Real entry points are where users already work — Slack threads, meeting debriefs, project updates. The in-app chat covers the long tail of follow-up tasks.
- **Future roadmap: proactivity + long-running memory:** The next phase is agents that stay aware throughout a project's entire lifecycle (days to a quarter), proactively keeping documents updated and people coordinated.
- **End-to-end demo in 6 minutes:** A real Slack thread with design debate → `@linear create issue` → Linear reasons through the thread, creates the issue, assigns it to Jacob, writes a PR → all in 6 minutes with a click-to-run PR at the end.

## Use cases
- **SaaS companies deciding whether to build a native agent or just publish an MCP server** — the video gives a clear framework for when native agents add unique value (embedding product opinions, controlling defaults, preventing "slop").
- **PMs and engineers building their first agent prototype** — the scrappy front-end-first, stealth-launch approach is a concrete playbook.
- **Teams designing agent evaluation systems** — the objective/subjective split and the "don't over-eval variance" principle are directly applicable.
- **Teams managing complex multi-step workflows** (e.g., sales call notes → bug/feature tickets, meeting debrief → PRD update) where the agent can stitch together context across tools.
- **Customer support workflows** — translating foreign-language tickets and auto-filing issues from Intercom/Zendesk is a concrete example from the video.
- **Engineering teams using Slack as a primary coordination surface** — the Slack-first entry point design is immediately replicable.
- **Interview grading and rubric evaluation** — Nan uses Linear agent + Granola MCP to score candidate interviews against a rubric document automatically.
- **Automation triggers** (e.g., Datadog alarm → bug filed → agent attempts fix → human reviews PR) — covered as an example of near-fully-autonomous loops.

## Patterns & frameworks

**Agent = LLM in a loop**
The foundational mental model: define a goal, provide tools, run question→answer→tool call cycles until the goal is met, then synthesize a final response. Not a magic system — just a loop.

**Skills architecture (dynamic context loading)**
Instead of a monolithic prompt with all instructions and context, define discrete "skills" (e.g., create-issue, write-doc) that carry their own tool sets and opinionated instructions. The agent calls a meta-tool to load whichever skills are relevant to the current request. Prevents context bloat, reduces hallucinations, encodes product opinions per workflow.

**Router pattern**
A small, cheap model sits in front of the main agent and classifies incoming requests. High-frequency, well-defined use cases (e.g., ~80% of requests = create issue) get routed to a lightweight, highly optimized subprompt. Everything else routes to the full generalist agent. Saves cost and improves reliability on hot paths.

**"In warranty" use case model for shipping**
Define a small set of hero use cases — the ones you market and demo. Ensure those are rock solid. Accept that the long tail will have variance. Ship when the warranty set passes, not when everything is perfect.

**Evals: objective + LLM-as-judge, used sparingly**
Objective evals cover deterministic requirements. LLM-as-judge covers subjective quality. Key insight: don't build too many evals around agent variance — agents legitimately vary, and evals around that create false signals. Reserve evals for places where consistency genuinely matters.

**Feedback loop → eval pipeline**
User thumbs down / reported weirdness → human review → added to eval dataset → scored against future runs. Closes the loop between production behavior and model improvement without requiring upfront ground truth data.

**Self-reporting capability gaps**
The agent is given a dedicated tool to report when a user asks for something it can't do. Reports auto-ingest into the issue tracker (deduplication included). Creates a continuously updated product backlog driven entirely by real user needs.

**Entry points vs. chatbot interface**
The chatbot is not the product — it's the fallback for follow-up and edge cases. Real entry points are where users already operate: Slack threads, meeting notes, document editing. Map the actual workflow, identify natural interruption points, and hook the agent there. This answers the "why use your native agent instead of ChatGPT?" question.

**Power law of use cases**
For domain-specific agents, a small number of use cases (e.g., "codify decisions from freeform input") account for the vast majority of usage. Identify that cluster early, optimize for it, and let the model handle the long tail generically.

**AI as the expanding middle**
Humans currently own the first 10% (intent/decision) and last 10% (review/approval) of any workflow; AI handles the middle 80%. The expectation is that middle expands over time toward 99.8%, with humans only providing the initial spark and final sign-off.