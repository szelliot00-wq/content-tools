# Agentic AI Systems, Clearly Explained

Video ID: `kwRTUw8pb2c`

## Summary
This video breaks down agentic AI systems into four clearly defined levels — chatbots, AI workflows, agentic workflows, and agentic AI systems — using content repurposing as a consistent example throughout. The core argument is that most people misunderstand "agents" because explanations are either too technical or too shallow, and that the underlying architecture is far simpler than the jargon suggests. The presenter positions the video specifically for non-developers: business owners, knowledge workers, and daily AI users who want to harness these systems without writing code. By the end, the viewer understands not just what each level does, but what it *can't* do — which is arguably the more valuable insight.

---

## Key insights
- **The four levels represent increasing AI autonomy:** Each level gives the AI more capability and wraps it in more sophisticated infrastructure, moving from passive advice-giving to coordinated autonomous operation.
- **Level 1 – Chatbots (e.g., ChatGPT, Claude, Gemini):** Useful but fundamentally passive and context-blind. They don't know your brand, audience, post history, or performance data. Tools like Claude Projects or Gemini Gems allow static context storage, but it remains static — it doesn't adapt automatically.
- **Level 2 – AI Workflows (e.g., N8N, Zapier, Make.com):** Automation pipelines that trigger on events (e.g., a new YouTube video published) and run the same fixed steps every time. The AI fills in gaps but cannot make judgment calls — e.g., it won't recognize that a video topic suits Twitter better than LinkedIn, or that carousels are outperforming text posts this month.
- **Level 3 – Agentic Workflows (e.g., Claude Code, OpenAI Codex, Cursor):** The critical shift here is *who decides the execution path*. At Level 2, you define the steps. At Level 3, the model does. You give it a goal ("turn this week's video into LinkedIn, Twitter, and newsletter content") and it figures out the steps — pulling transcripts, choosing formats based on viral indicators, running content through a style guide, and iterating.
- **The ReAct loop is the engine of Level 3:** The technical name for the agent loop is ReAct (Reason and Act). The model reasons about what to do, acts on it, observes the result, and iterates until the goal is achieved.
- **A "harness" is what separates a chatbot from an agent:** A harness is the infrastructure wrapping the model that makes it reliable, controllable, and deployable. Without a harness, you have a browser chatbot. With one, the model can read files, run commands, call external tools, and check its own work. Claude Code, Codex, and Cursor are all harnesses — different products, same concept.
- **Level 3 has a ceiling:** A single agent, one goal, one terminal session. It doesn't retain memory between sessions, doesn't know which posts performed best last week, and requires re-explaining context for each new task.
- **Level 4 – Agentic AI Systems:** Multiple coordinated "skills" (specialized agents or instruction sets) run in parallel or sequence to handle an entire operation. In the content example: one skill extracts short-form clips, another builds platform-specific carousels, another drafts the newsletter, another generates ad copy from top-performing angles, and everything queues into a scheduling tool — all from one command.
- **"Skills" are just markdown files in folders:** A skill is a file of instructions for a specific task (e.g., "how to write a LinkedIn carousel," "how to draft a newsletter in my voice"). The agent loads only the relevant skill and reference examples when needed, avoiding bloated context and unnecessary token costs.
- **MCPs (Model Context Protocol) connect the system to external tools:** MCP is the standard for plugging external platforms (scheduling tools, analytics dashboards, CRMs) into a Claude Code harness. It's the integration layer.
- **Memory is a core differentiator at Level 4:** The system carries context between sessions — knowing which posts performed best, which newsletter subject lines had the highest open rates, etc. Memory can be as simple as a markdown file the system reads and updates, or as complex as a database connected across multiple LLMs and tools.
- **Human-in-the-loop is a deliberate design principle, not a limitation:** The best real-world systems reviewed by the presenter always include human review at either the input or output stage. In his content system, the AI drafts, checks, and formats everything, but nothing publishes without human approval. He has not encountered a system that reliably clears this bar autonomously.
- **The system gets to ~95% autonomous:** The presenter's framing is that these systems can handle 95% of the work without human intervention — but the remaining 5% of human oversight is intentional and valuable.
- **It's closer to building a Notion workspace than writing code:** The presenter explicitly states that organizing an agentic AI system is more like structuring folders and files than engineering software, making it accessible to non-developers.
- **Tools at Level 4 include agentic operating systems:** Examples given include the presenter's own community-built "Agentic Operating System," Open Claude, and Hermes (described as an open-source personal agent that has "skyrocketed" in 2025). All take the same approach: build a richer file system on top of a base agent to handle real complexity.

---

## Use cases
- **Content creators and YouTubers** who want to automatically repurpose long-form video into LinkedIn posts, Twitter/X threads, newsletters, short-form clips, and ad copy without manually prompting AI each time.
- **Small business owners** who want AI to run operational workflows (marketing, content, customer comms) without hiring additional staff or learning to code.
- **Knowledge workers and solopreneurs** who use ChatGPT or Claude daily but feel limited by its passivity and lack of business context.
- **Marketing teams** that need platform-specific content at scale with consistent brand voice and quality standards.
- **Product managers and operators** evaluating which level of AI tooling is appropriate for their current workflows and where to invest next.
- **Non-technical founders** who want to understand the landscape of AI tooling (chatbots vs. workflows vs. agents vs. systems) before making build/buy decisions.
- **Anyone managing repetitive, multi-step knowledge work** — writing, research, formatting, scheduling — that currently requires significant manual coordination.
- **Teams considering automation tools** like Zapier or N8N who want to understand the ceiling of those tools and when to graduate to agentic systems.

---

## Patterns & frameworks

### The Four Levels of AI Autonomy
A progression framework for understanding AI capability and infrastructure complexity:
| Level | Name | Who Decides Steps | Key Tools | Main Limitation |
|---|---|---|---|---|
| 1 | Chatbots | Human | ChatGPT, Claude, Gemini | Passive, no business context |
| 2 | AI Workflows | Human (pre-defined) | N8N, Zapier, Make.com | Rigid, no adaptive judgment |
| 3 | Agentic Workflows | The Model | Claude Code, Codex, Cursor | Single agent, no memory |
| 4 | Agentic AI Systems | The Model + System | Agentic OS, Hermes, Open Claude | Requires thoughtful design |

---

### ReAct Loop (Reason and Act)
The core loop powering Level 3 and 4 agents. The model:
1. **Reasons** about what to do next given the goal
2. **Acts** on that reasoning (runs a command, reads a file, calls a tool)
3. **Observes** the result
4. **Iterates** until the goal is complete

This is what distinguishes an agent from a workflow — the model is the decision-maker, not a fixed sequence of steps.

---

### The Harness Model
A harness is the infrastructure layer that wraps around an LLM to make it actionable and reliable. It enables the model to:
- Read and write files
- Run terminal commands
- Call external tools and APIs
- Check and revise its own outputs

Without a harness = chatbot. With a harness = agent. Claude Code, Codex, and Cursor are all examples of harnesses.

---

### Skills-Based Architecture
At Level 4, complex operations are broken into discrete "skills" — each a markdown file containing instructions, quality criteria, and output formats for a specific task. The system loads the right skill at the right moment, keeping context lean and costs low. Analogous to a team of specialists rather than one generalist.

---

### Human-in-the-Loop Design Principle
A deliberate design pattern where human review is built into the system at either the **input stage** (reviewing what the system is about to do) or the **output stage** (reviewing what the system produced before it goes live). The presenter frames this not as a workaround for AI failure, but as a quality control layer that reflects the current realistic ceiling of autonomous AI systems (~95% autonomous, 5% human judgment).

---

### Context Loading (Right File, Right Time)
The underlying simplicity behind agentic AI systems: rather than feeding the model all context at once (which bloats the context window and costs tokens), the system is designed to load only the relevant skill file, memory excerpt, or reference example at the moment it's actually needed. This is what makes Level 4 systems scalable and cost-efficient.