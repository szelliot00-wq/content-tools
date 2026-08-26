# AI Model vs Agentic Harness: What Actually Drives AI

Video ID: `ZELPNFXJ4_o`

## Summary
This video explains why two AI products using the same underlying model can perform so differently. The key distinction is between the **AI model** (the neural network itself) and the **agentic harness** (the surrounding infrastructure that gives the model tools, memory, and a loop to act in the world). Together, these two components form what we call an AI agent, and most recent capability gains in AI have come from harness improvements, not just model improvements.

## Key insights
- **The model alone is a "brain in a jar"** — capable but isolated, unable to read files, run code, or browse the web without external scaffolding.
- **Benchmark gaps between top models have narrowed**, so when one AI product clearly outperforms another, the harness is usually the differentiating factor, not the model.
- **The agentic harness has three core components**: tools (file access, code execution, web browsing, computer use), memory (instruction files, context compaction, targeted search), and the agentic loop (plan → act → observe → repeat).
- **MCP (Model Context Protocol)** is a standard that lets tools plug into any compatible harness without being rebuilt, enabling modular integration with external services.
- **Continuous verification** — running tests, taking screenshots, or spawning a separate reviewer model — keeps long-running agents from going off the rails.
- **The boundary between model and harness is fluid**: capabilities like long-horizon planning are being trained into models, while behaviors like task consistency are increasingly shaped by harness conventions.
- **The right question isn't "is AI good at X?" but rather "which model *and* which harness?"** — a brilliant model can get stuck in a poor harness, and vice versa.