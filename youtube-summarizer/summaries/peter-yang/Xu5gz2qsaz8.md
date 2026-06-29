# Inside Anthropic’s Bet on Claude Agents that Work While You Sleep | Jess Yan

Video ID: `Xu5gz2qsaz8`

## Summary
This video features Jess Yan, product lead at Anthropic for Claude Managed Agents, in conversation with host Peter Yang. Jess demos the Managed Agents product, explains how it differs from raw prompting loops, and shares how Anthropic employees use agents internally to supercharge their daily work. The core argument is that agents have evolved from simple prompt-response loops into autonomous, long-running actors that can handle complex tasks overnight — and that the bottleneck on productivity is shifting from personal capacity to how much you can effectively delegate. The video is most relevant to product managers, developers, and enterprise teams evaluating how to adopt AI agents in real workflows.

## Key insights
- **Agents have fundamentally evolved**: Early agents were just prompting loops (question → answer in a loop). Modern agents are autonomous, self-discovering, long-running actors with access to third-party systems, internal tooling, and sensitive data — requiring permissioning, observability, and steering mechanisms.
- **The harness is as important as the model**: The "harness" is the scaffolding around the model that enables tool use, memory, human-in-the-loop triggers, and error recovery. Jess argues you cannot achieve maximum model performance without tying the harness and model together — Anthropic tests models against its own harnesses (Claude Code, etc.) rather than just open-source evals.
- **Managed Agents is a pre-built harness + infrastructure**: Rather than forcing developers to wire together a raw prompting loop, Claude Managed Agents ships with out-of-the-box infrastructure, built-in toolsets, file system access, permissions controls, and debugging agents — so the return-on-effort for building an agent is extremely high.
- **Self-recovery is a key differentiator**: Unlike raw prompting loops that break if one step fails, Managed Agents supports agents that detect unexpected outputs, revise their approach, and re-steer themselves — dramatically reducing fragility for long-running tasks.
- **MCP enables safe third-party access**: Model Context Protocol (MCP) provides a standardized, authenticated interface to external databases and services, allowing agents to securely interact with internal systems.
- **Evals are the hardest part of agent development**: Traditional pass/fail evals still work, but more sophisticated patterns are emerging: multi-turn replay testing, A/B testing agent versions against the same interaction strings, and built-in eval loops where the agent grades its own output (ideally in a separate context window to reduce bias). Anthropic uses a mix of binary pass/fail, LLM-as-judge scoring, and trigger-based evals.
- **Vibe testing before formal evals**: Getting an agent into the hands of even a small beta group is more valuable early on than building a rigorous eval suite. Formal evals become necessary once you need to aggregate signals at scale.
- **Outcome-as-structured-output**: As models improve, the paradigm has shifted from "define the exact JSON schema your agent must output" to "describe what a great end result looks like and let the agent self-correct toward it." The outcome itself becomes the structured output.
- **Anthropic uses agents heavily internally**: Jess personally uses agents to track PRs without pinging engineers, fill out customer RFP security checklists, diagnose field issues, prep for customer pitches, and monitor Slack channels for product feedback. She estimates all of this is "10,000 times easier" with internal agents.
- **Scheduled runs + proactive agents**: Jess runs scheduled agents that summarize engineering activity. She sees the future as agents being "always on" — proactively surfacing information like a co-worker would, driven by cron jobs and triggered events, not just reactive ad-hoc queries.
- **Jess talks to Claude more than her co-workers**: She uses Claude as a "therapy" tool to deeply understand thorny concepts before entering team conversations, which uplevels the quality of human-to-human discussions (no more "spin me up" questions — arriving with a real opinion).
- **Claude as a neutral judge in team meetings**: Anthropic tags Claude into API design debates when the team is at an impasse, using it to identify when internal biases are distorting the decision.
- **Real internal use case — waitlist agent**: Jess built an agent to process a 4,000-organization waitlist in a few weeks: cleaning invalid entries, deduplicating, scoring conversion likelihood using internal data, and auto-inviting high-value testers daily. It took ~30 minutes to spin up and was designed to be throwaway once the feature went self-serve.
- **Individual empowerment before enterprise automation**: The highest-ROI starting point for enterprise agent rollout is not automating a 20-team workflow — it's making each individual feel like a one-person startup. Supercharge individuals first, then tackle cross-team mega-processes.
- **Vertical SaaS is becoming hyper-specialized**: As models get broadly capable, the competitive value in AI products is shifting to incredibly narrow, specific use cases (e.g., not "accounting agent" but "accounting agent for solopreneurs"). The shared infrastructure (context patterns, task orchestration) matters more than the domain category.
- **Agents must live where work lives**: The winning distribution model is agents embedded where workflows already happen (Claude Code, chat interfaces) — not requiring users to navigate to a separate website. "Everything is chat now because agents interact best in chat."

## Use cases
- **Product managers**: Tracking engineering PRs autonomously, summarizing Slack feedback channels, personalizing customer pitches, filling out enterprise RFP security questionnaires.
- **Data analysts / PMs doing data work**: Spinning up a data analysis agent that ingests large files, runs Python analysis, and outputs rich HTML reports (product dashboards, shopper heatmaps, predictive churn models) in minutes.
- **Enterprise teams onboarding to agents**: Starting with individual-level automation (one agent per employee use case) before attempting org-wide workflow automation.
- **Developers building on the API**: Using Managed Agents to avoid building custom harness infrastructure from scratch — especially for tasks requiring long-running sessions, error recovery, and third-party integrations via MCP.
- **Individuals / personal use**: Scheduling agents to manage household logistics (e.g., new parent managing infant feeding schedules, fridge monitoring, grocery management agents).
- **Teams stuck in debates**: Using Claude as a neutral third-party judge to surface bias during API design or architectural decisions.
- **Waitlist / CRM triage**: Automatically parsing, deduplicating, scoring, and actioning large web-form datasets that are only relevant for a short operational window.
- **Competitive and customer research**: Running scheduled agents that continuously monitor external signals (customer Slack channels, product feedback) and proactively surface insights.

## Patterns & frameworks

**The Harness + Model pairing**
The model provides intelligence; the harness provides scaffolding (tool execution, memory access, human-in-the-loop triggers, error recovery). They must be developed and evaluated together. As models get more capable, harnesses may get thinner — but they never disappear.

**Prompting loop → Autonomous actor evolution**
A mental model for where agent sophistication sits: (1) basic prompt/response loop → (2) tool-augmented loop → (3) permissioned, observable, long-running autonomous agent with self-recovery. Product and infrastructure complexity scales with each step.

**System prompt vs. initial prompt separation**
Put general behavioral instructions and performance optimizations in the system prompt (reusable across tasks). Put task-specific schema discovery, data context, and step-by-step sequencing in the initial user prompt. This keeps agents general-purpose while still producing predictable, structured outputs per run.

**Built-in eval loop (agent grades its own output)**
Rather than external eval pipelines, embed evaluation inside the agent's session: the agent knows what "good" looks like, grades its own outputs, and iterates until it meets the threshold — ideally in a separate context window to reduce self-serving bias.

**Vibe testing → Formal evals progression**
Start with qualitative vibe testing (small beta group, human judgment). Graduate to formal evals (pass/fail, LLM-as-judge scoring, trigger evals) only when you need to aggregate quality signals at scale. Don't block shipping on evals before you have any real users.

**Individual-first enterprise rollout**
Step 1: Give individual employees agents tailored to their specific tasks — make each person feel like a one-person startup. Step 2: Once individuals are supercharged, tackle cross-team, multi-quarter workflow automation. Trying to start at Step 2 is the most common enterprise mistake.

**Templates + free iteration onboarding**
Reduce writer's block for new agent users by providing starter templates, then give full creative freedom to iterate. Avoids the blank-page problem while preserving user ownership.

**Outcome-as-structured-output (tastemaker prompting)**
Instead of prescribing rigid JSON schemas, describe the desired end state in qualitative terms ("make it rich and interactive," "hit 90% accuracy on this benchmark") and let the agent self-correct toward that outcome. Works best when the agent has enough autonomy and the harness supports mid-task steering.

**Always-on + proactive agent pattern**
Agents shouldn't just respond to queries — they should be triggered by cron jobs and events to continuously refresh context and proactively surface relevant information, mimicking how a good co-worker operates rather than waiting to be asked.