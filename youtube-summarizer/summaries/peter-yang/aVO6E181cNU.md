# How I Plan, Build, and Run Loops with Claude Code in 40 Minutes | Thariq Shihipar

Video ID: `aVO6E181cNU`

## Summary
Thariq Shihipar, a member of the Claude Code team at Anthropic, demonstrates how he plans, builds, and runs agentic loops and workflows using Claude Code in a live session with podcaster Peter Yang. The video centers on Thariq's personal video editing workflow as a concrete example of non-technical work automated through Claude, while also covering broader philosophy around planning, context management, and multi-agent orchestration. The core argument is that effective agent use requires iterative exploration to eliminate "unknown unknowns" before committing to implementation, not a single upfront spec. The video is most relevant to product managers, creators, and non-engineers who want to move from one-shot prompting to sustained, autonomous agent loops.

## Key insights
- **Loops come in three forms**: `/loop` (recurring agent execution), `/goal` (prevents early stopping by giving the agent an explicit exit condition), and **workflows** (JS files that spin up sub-agents to parallelize and verify work). Each serves a different use case.
- **`/goal` is for preventing premature stopping**: When you've done enough exploration and want the agent to power through ambiguity rather than pause and ask, `/goal` signals "fill in the gaps and keep going."
- **Workflows are the most powerful form** because they decompose non-deterministic tasks into roughly deterministic ones by separating the worker agent from the verification agent.
- **Self-referential bias is real**: A model verifying its own output is more lenient. Workflows solve this by using a separate agent to verify against a rubric — the agent that created a clip is not the same agent that judges whether it's good.
- **Planning is iterative exploration, not a one-time document**: Thariq describes planning as "getting rid of your unknown unknowns" — it involves learning how tools work (e.g., Whisper's edge cases like silence becoming "Thanks for watching," no speaker recognition), generating mockups, and doing technical research before committing to a build.
- **Prototype in cheap formats first**: Instead of building in React, build the UI concept as an HTML artifact. Only move to the expensive implementation once the spec is proven out. This applies the "smallest step to prove the concept" principle.
- **Implementation notes as living spec**: Thariq asks the agent to keep implementation notes as it goes, capturing unexpected findings. These feed back into the spec iteratively — speccing is not a one-time handoff.
- **Claude Code's system prompt was cut by 80%**: As models get smarter, they need fewer constraints, fewer examples, and less direction. Over-constraining with "never do X" is often worse than explaining *why* you don't want something, which gives the model more flexibility to make good judgment calls.
- **CLAUDE.md files are probably too long**: The same principle applies — shorter, principle-based instructions outperform long example-heavy instructions with the current generation of models.
- **Claude Tag (Slack integration) is taking over background/parallel work**: Thariq now runs one focused Claude Code session locally and routes all background/parallel tasks to Claude Tag in Slack. Multi-agent work happens there because it's where the team already collaborates.
- **Skills can wrap workflows**: A workflow is just a JS file. You can save it into a skill so it becomes reusable. Skills can also be instructions for setting up a workspace rather than doing a task directly.
- **Context window hygiene matters**: Keep MCP usage lean, shorten CLAUDE.md, trim skills. More room in the context = more freedom for the model to perform well.
- **His personal productivity goal**: Be more productive but work *less* — achieved by focusing on one primary project, avoiding lazy multi-tasking prompts that waste compute and time.
- **Becoming "more technical" is about knowing constraints, not syntax**: Understanding trade-offs between backend services, library options, and system limits is what makes you a better agent operator — not learning TypeScript syntax. Claude can teach this if you push it.
- **HTML artifacts are now how the Anthropic team shares plans and status**: PR summaries, incident reports, plans — all generated as HTML artifacts. Currently available on Teams and Enterprise tiers.

## Use cases
- **Video creators** automating transcription, caption overlays, B-roll, and clip generation from raw recordings using Whisper + Remotion.
- **Podcast producers** generating show notes, YouTube thumbnails, clip ideas, and social copy from interview transcripts via chained skills.
- **Non-technical PMs or creators** who want to understand how to move from one-shot prompts to sustained agentic loops without writing orchestration code manually.
- **Teams doing design iteration** who want to generate multiple UI design variations as HTML artifacts before committing to a coded implementation.
- **Anyone managing parallel background tasks** who wants to offload async work (PR babysitting, research, exploration) to Claude Tag while staying focused locally.
- **Engineers or PMs doing research spikes** who need to understand edge cases of a new library or API before building on top of it.
- **Content teams wanting parallel clip generation** — using workflows to spin up one sub-agent per clip with a shared rubric and separate verification, rather than generating clips sequentially.
- **Anyone over-prompting or burning context** who needs a framework for trimming CLAUDE.md and skill instructions to make the model more effective.

## Patterns & frameworks

**The Iterative Planning Loop ("Eliminate Unknown Unknowns")**
Not a one-time spec document. The process cycles: human request → agent technical exploration → mockups/explainers → refine spec → begin implementation → agent surfaces unexpected findings → re-spec if needed → continue. Each pass reduces what you don't know about the problem space before committing expensive compute.

**Prototype-First Cheaply, Then Implement**
Prove out a design concept in a cheap format (HTML artifact) before building the expensive version (React + video re-render). Apply the question: "What is the smallest step to prove out this concept?" Only escalate implementation cost once the spec is validated.

**Worker / Coordinator / Verifier Workflow Pattern**
Three-agent separation in workflows: (1) a **coordinator** agent that breaks work into chunks and orchestrates, (2) **worker** agents that execute each chunk in parallel (e.g., one per video clip), and (3) a **verifier** agent that checks each output against a rubric. This prevents self-referential bias and forces more compute per unit of output.

**Skill + Workflow Packaging**
A workflow (JS file) can be saved inside a skill, making it reusable and callable as a slash command. Skills can also serve as setup instructions for a workspace rather than task executors — building up a persistent repo of scripts the agent can reuse rather than recreating from scratch each session.

**Signal-Based `/goal` Usage**
Use `/goal` when you have a measurable or clearly articulable exit condition (e.g., "rendered video matches transcript," "latency below X ms") and you've already done enough exploration that you're confident telling the agent to fill gaps autonomously. It's an explicit signal to power through rather than stop and ask.

**Principle Over Constraint Prompting**
Instead of "never do X," give the agent the *reason* you don't want X. "Never" is interpreted literally and constrains the model even in edge cases where X would be appropriate. Giving the reasoning lets the model apply judgment. Corollary: examples in system prompts can inadvertently constrain output format — removing them may yield more creative, better-fit results with capable models.

**Reference-Anchored Exploration**
When exploring design or content style, provide a concrete reference (e.g., a URL to a person's blog or website). The agent fetches the HTML and uses real brand signals rather than guessing, producing more relevant variations. Applied here: Peter Yang's website URL → Substack-aligned overlay designs.