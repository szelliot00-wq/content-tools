# Agentic AI Frameworks Explained: Workflows, Multi-Agent, & Production

Video ID: `ZVPlLaehjLk`

## Summary
The video explains that the explosion of agentic AI frameworks (LangChain, CrewAI, AutoGen, etc.) can be overwhelming, but the right choice depends entirely on what type of system you're building. It categorizes agentic AI projects into five distinct types — linear workflows, autonomous multi-agent, role-based, production orchestration, and rapid prototyping — and maps specific frameworks to each. The core message is that these frameworks aren't competing; they're optimized for different problems.

## Key insights
- **Ask "what am I building?" not "which framework is best?"** — the framework choice flows from the system type, not the other way around.
- **Linear workflows** (predictable, sequential steps) are best served by LangChain or LlamaIndex; use LangGraph for more complex sequential setups.
- **Autonomous multi-agent systems** give AI an open-ended goal and let agents collaborate freely — AutoGen and CrewAI are the primary fits here.
- **Role-based systems** are also multi-agent but with strict role boundaries per agent; CrewAI is the top pick, with AutoGen as a structured alternative. Niche tools like ChatDev target specific domains (e.g., software dev).
- **Production orchestration** requires deep API/database/business workflow integration — LangGraph and the Semantic Kernel + AutoGen combination (Agent Framework) are designed for this.
- **Rapid prototyping tools** (LangFlow, Flowise) offer drag-and-drop canvas UIs to validate ideas quickly before committing to a full architecture.
- **Agentic systems differ fundamentally from chatbots** — they involve planning, acting, and iterating rather than a single question-answer exchange, which is why dedicated frameworks are necessary.