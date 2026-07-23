# Prepare for this round before your next AI PM interview...

Video ID: `iBKrijO1PBQ`

## Summary
This video is a masterclass for product managers preparing for AI-focused technical interviews at companies like OpenAI, Anthropic, Google, and Meta. Hosted by Akash and Prasad Ready (former CPO at El Neutra, senior director at Danar, who has coached 150+ PMs), it teaches five core technical concepts that AI PM interviewers test candidates on, with live demos in Google AI Studio, OpenAI Playground, and Google Colab. The central argument is that most PMs can use AI tools but cannot explain how they work under the hood — and that gap is precisely what technical interview rounds are designed to expose. The video is most relevant to product managers actively job searching at AI-first companies or seeking to move into AI PM roles.

---

## Key insights

- **The interview is a freeze filter, not a depth test.** Interviewers aren't checking whether you can derive attention mechanisms — they're checking whether you can sit between two engineers and not freeze when they go one level deeper. A wrong detail you can recover from; a freeze ends the interview.
- **LLMs predict the next token, they don't look things up.** The most common PM misconception is treating an LLM like a database. It predicts the next most probable token from a probability distribution — e.g., given "The capital of France is," the model assigns Paris a 0.92 probability. This is why hallucination is not a prompt-engineering bug; it's the model working as designed.
- **Temperature controls the sampling distribution, not creativity per se.** Temperature = 0 sharpens the distribution (top token dominates, responses are deterministic). Temperature = 1 samples natively. Temperature > 1 flattens the distribution (non-dominant tokens get a chance), producing varied or unexpected outputs. Demonstrated live in Google AI Studio with animal-naming prompts.
- **Context window defines the boundary of what the model can see.** Models have frozen weights post-training. At inference time, everything the model can act on must fit in the context window. Modern models like Opus 4.8 have ~1 million token windows. Overloading it throws an internal error (demonstrated live by pasting War and Peace + Crime and Punishment).
- **The model never runs a tool — it emits a JSON call.** This is what most candidates get backwards. The model outputs a structured request (function name + arguments as JSON). Your application code executes the function. The result is passed back into the conversation. The model then generates the final answer. The intelligence is in deciding *when* to call and *with what* — not in execution.
- **Vague tool descriptions are a real bug, not cosmetic.** The model decides which tool to call based on the description field. An imprecise description causes wrong tool calls. Validated in the OpenAI Playground demo where a vague weather function description caused incorrect behavior.
- **MCP (Model Context Protocol) is the open standard for tool connectivity.** Developed by Anthropic, MCP lets you write one integration that works across hundreds of tools and models — analogous to what APIs were in the SaaS era. Eliminates the need to hand-build separate integrations per tool/model pair.
- **An agent is prompt + tool + skill — not just a prompt.** Most PMs define agents as "a prompt," because they've been trained on custom GPTs. A proper agent definition includes: (1) the system prompt/instruction, (2) the tools it can call (APIs, MCPs), and (3) skills — reusable packages of know-how for an entire class of tasks. Skills don't retrain the model; they're loaded at runtime as structured instructions.
- **Skills dramatically reduce the need for human clarifying input.** A live demo comparing a PRD-drafting agent with vs. without a skill showed: the no-skill version asked clarifying questions; the skill version read the existing context library, found an existing PRD, and produced a launch-readiness PRD with the right stage, go/no-go checklist, rollout plan, and rollback criteria — far closer to something you'd send to colleagues.
- **Orchestration (LangChain) is the conductor, not the musician.** LangChain coordinates when each model/tool/step runs and in what order. It does not make the model smarter. A minimal chain has three components: prompt template → model → output parser. Demonstrated in Google Colab generating a fact about black holes.
- **RAG (Retrieval-Augmented Generation) is the most commonly tested AI product pattern.** Instead of relying on training data, RAG fetches relevant text from a vector store (e.g., FAISS) and injects it into the prompt. Use cases: reducing hallucinations, handling frequently changing data without retraining. Ground truth response matched injected snippets exactly in the live demo.
- **Single SDK calls are often better than using a framework.** For a single LLM call with one tool, a raw SDK is simpler and easier to debug. LangChain/LangGraph earns its place when you have multi-step flows, swappable components, state management, memory, and multiple agents. The abstraction can hide what's breaking — saying this trade-off out loud signals real experience.
- **LangChain split into two products.** LangChain is the core library. LangGraph is the agent layer from the same team. Candidates saying they "build agents in LangChain" are almost certainly using LangGraph. LlamaIndex is retrieval-first (RAG with fewer lines). CrewAI and OpenAI Agents SDK handle multi-agent coordination. Visual no-code options include n8n and Lindy.
- **Routing is the most practical concept almost no PM candidate can explain correctly.** Not every query deserves the same model. A router classifies the query and sends it to the appropriate model: cheap/small models for simple queries, frontier models for complex reasoning. Demonstrated with a 2+2 query routing to GPT-4o-mini (14 tokens) vs. the same query sent to GPT-4o (574 tokens). At millions of calls, the cost delta is enormous.
- **Two routing patterns matter most.** (1) Model routing — classify query complexity and route to cheap vs. large model. (2) Intent routing — classify user intent and send to entirely different agent paths (e.g., billing agent vs. technical support agent, with no overlap).
- **The hybrid system answer wins churn/fraud prediction questions.** For tabular structured data with a binary label (churn yes/no), gradient-boosted trees (XGBoost) are cheaper, faster, and more interpretable than LLMs. LLMs earn their place in the language layer: converting support tickets into features, drafting save emails once a threshold is tripped. The best answer is always "hybrid — trees predict, LLM reads and writes."
- **Measuring hallucination grounding requires two separate checks.** (1) Faithfulness — does the answer trace back to the retrieved text? (2) Retrieval quality — did you pull the right snippet in the first place? These are different failure modes and require different fixes.
- **The "name dropper" vs. "builder" tell for LangChain.** Name dropper: "We used LangChain." Builder: "We used it here, ripped it out there because the abstractions were hiding what broke." Same word, opposite signal.
- **Routing matters more as models improve, not less.** As more capable models proliferate, there are more decisions about which model handles which task. Someone has to own that decision — and at most AI companies, that's the PM.

---

## Use cases

- **PM candidates interviewing at AI-first companies** (OpenAI, Anthropic, Google, Meta, Sierra, NVIDIA, Glean) who need to pass technical interview rounds without an engineering background.
- **PMs who can use ChatGPT/Claude but cannot explain what happens underneath** — the video specifically targets this gap.
- **PMs moving from traditional software roles into AI PM roles** who need to quickly build vocabulary and working mental models.
- **Hiring managers or interviewers** who want a rubric for what good vs. mediocre AI PM technical answers look like.
- **PMs designing AI features** who need to decide between LLMs vs. ML models, single SDK calls vs. orchestration frameworks, or cheap vs. frontier models.
- **PMs in system design interviews** who are asked to walk through an AI product architecture and need to know what layer owns what (app/interaction → orchestration/routing → agent → data/retrieval/memory).

---

## Patterns & frameworks

**Next Token Prediction**
The fundamental mechanism of LLMs. The model assigns probability scores to candidate next tokens and samples from that distribution. Temperature controls how sharply or flatly probabilities are distributed. Not retrieval, not lookup — pure probabilistic sampling. Relevant for: explaining hallucination, explaining why grounding is necessary, explaining why prompts alone don't fix factual errors.

**Tool / Function Calling Loop**
A four-step cycle: (1) hand the model a list of tools with names, descriptions, and JSON schemas; (2) model emits a structured tool call (JSON) when it decides a tool is needed; (3) your code executes the function; (4) result is passed back into the conversation; model writes final answer. Key insight: the model never touches your systems directly. The description field drives tool selection — vague descriptions are bugs.

**Prompt + Tool + Skill = Agent**
Three-layer agent definition framework. Prompt: the one-off instruction in the moment. Tool: lets the agent act on the world or fetch data. Skill: reusable, runtime-loaded package of instructions and routing logic for an entire class of tasks. Skills reduce human input, improve output quality, and do not retrain the model.

**RAG (Retrieval-Augmented Generation)**
Pattern for grounding LLM responses in real data. Instead of relying on training data, fetch relevant text from a vector store (e.g., FAISS, Pinecone) and inject it into the prompt before generation. Reduces hallucinations, handles frequently-changing data without retraining. The most commonly tested system design pattern in AI PM interviews. Two failure modes: faithfulness (does answer trace to retrieved text?) and retrieval quality (did you pull the right snippet?).

**Orchestration Stack (four-layer mental model)**
- Layer 1 — Interaction: app, chat, voice, API (user-facing)
- Layer 2 — Orchestration: routes between agents, manages state; where routers sit
- Layer 3 — Agent layer: named agents with non-overlapping jobs
- Layer 4 — Data & infrastructure: retrieval, vector store, model APIs, memory

**Routing (two patterns)**
- Model routing: classify query complexity → cheap model for simple, frontier model for complex. Optimizes cost at scale.
- Intent routing: classify user intent → send to entirely separate agent with no overlap (billing agent ≠ support agent). A classifier can be a cheap LLM call, embedding similarity, or hardcoded rules.

**Hybrid System Answer**
For prediction problems: use ML models (XGBoost/gradient boosting) for tabular structured data with clear labels — cheaper, faster, interpretable. Use LLMs for the language layer (reading messy input, writing output). The correct interview answer is almost never either/or — it's "hybrid."

**LangChain Minimal Chain**
Three components: prompt template (formats input into a sentence) → model (generates response) → output parser (formats output as string, JSON, etc.). Framework earns its place with multi-step flows, swappable components, memory, and tool coordination. For single calls, use raw SDK. LangChain (core library) vs. LangGraph (agent layer) vs. LlamaIndex (RAG-first) vs. CrewAI/OpenAI Agents SDK (multi-agent) — pick the lightest tool that solves your problem.

**The Name-Dropper vs. Builder Signal**
A one-sentence heuristic interviewers use to distinguish real AI experience from resume padding. Name-droppers stop at the tool name. Builders describe where they used it and where they ripped it out and why. Applies to any AI framework or tool mentioned on a resume.