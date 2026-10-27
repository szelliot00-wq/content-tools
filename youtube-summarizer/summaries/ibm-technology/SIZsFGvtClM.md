# Agentic Engineering: 5 Terms Every AI Developer Should Know

Video ID: `SIZsFGvtClM`

## Summary
This video introduces five foundational concepts in agentic engineering — the practice of building AI-driven development systems. The presenter walks from basic prompt crafting up to fully automated software factories, emphasizing that these ideas are reinventions of classic computing patterns (graphs, feedback loops, distributed systems) applied to AI agents. The goal is to give developers a practical vocabulary for leveraging AI tooling at any scale, from solo use to large team pipelines.

## Key insights
- **Prompt engineering is about communication, not just syntax** — domain expertise matters more than knowing the "perfect" formula, and even dictating instructions verbally can work well with capable models.
- **Few-shot prompting and chain-of-thought (CoT) examples are critical for smaller/local models** — frontier models need less hand-holding, but edge-deployed models benefit significantly from worked examples in the prompt.
- **Context engineering manages everything the model sees** — system prompts, tools, MCP servers, RAG-retrieved docs, and codebases all compete for context space; quality degrades before the advertised limit is hit.
- **Sub-agents protect the main context window** — smaller, purpose-built agents do isolated research or lookups and return only a summary, keeping the primary context lean.
- **Harness engineering is the runtime layer around the model** — it executes tool calls, manages memory across context resets, sandboxes the model's access to the machine, and feeds back results (e.g. test pass/fail, merge conflicts) so the agent can self-iterate.
- **Loop engineering replaces human prompting with triggers** — cron jobs, PR opens, bug alerts, or any event can kick off an agent loop, with optional human-in-the-loop checkpoints for approval.
- **Graph engineering fans out multiple agents in parallel** — agents run concurrently (e.g. market research + repo analysis) and hand off to a downstream implementation agent, but token costs scale quickly.
- **Software factories automate the full SDLC** — task-specific agents replace one general-purpose agent, each requiring three primitives: **isolation** (containers/sandboxes), **identity** (access controls), and **observability** (full audit trails).
- **You don't need all five concepts** — solo developers can get most of the value from prompt, context, and harness engineering alone; software factories are a team-scale concern.