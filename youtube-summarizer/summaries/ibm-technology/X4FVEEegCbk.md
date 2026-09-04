# Skills vs MCP vs RAG vs Memory: What AI Agents Need to Know

Video ID: `X4FVEEegCbk`

## Summary
The video explains four mechanisms for giving AI agents knowledge beyond their training data: Skills, MCP, RAG, and Memory. Using a 500 internal server error as a running example, it shows how each method addresses a different gap in what an agent knows or can do. The core argument is that dumping raw context into a context window is inefficient, and that structured, purpose-fit knowledge delivery is more effective.

## Key insights
- **Skills** are procedural instructions (runbooks + judgment) the agent pulls in on demand via progressive disclosure — they tell the agent *what steps to follow* and *when to escalate*, but can't fetch live data on their own.
- **MCP (Model Context Protocol)** connects the agent to external systems (logs, metrics, dashboards) through a standardized protocol, letting it *act in the world* without bespoke integration code.
- **RAG (Retrieval-Augmented Generation)** pulls relevant chunks from a human-curated document store (manuals, dependency maps) using semantic search — knowledge that *someone wrote down* and stored deliberately in a vector database.
- **Memory** is knowledge the agent *accumulated itself* from past runs — e.g., an undocumented fix discovered the hard way last time — and writes back after each resolved incident, compounding experience over time.
- The key distinction between RAG and Memory is **provenance**: RAG = human-authored documents; Memory = agent-generated experience.
- A practical rule of thumb: written-down knowledge → RAG; learned experience → Memory; repeatable procedure → Skill; live external lookup → MCP.
- Dumping everything into the context window up front is explicitly called out as ineffective — it leads to unfocused, generalized behavior rather than domain-specific reasoning.