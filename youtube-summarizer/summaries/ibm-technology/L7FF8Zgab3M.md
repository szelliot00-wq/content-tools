# What is OpenClaw? Inside AI Agents, LLMs and the Agentic Loop

Video ID: `L7FF8Zgab3M`

## Summary
This video explains the fundamental difference between traditional AI chatbots and AI agents, using OpenClaw as a real-world example. It covers how AI agents operate through an "agentic loop" — reasoning, acting, and observing in cycles — to autonomously complete tasks rather than just providing information. The video also explores OpenClaw's architecture, its extensibility through skills, and important security considerations for responsible deployment.

## Key insights
- **The gap between "knowing" and "doing":** Traditional LLM chatbots can tell you how to do something, but AI agents can actually execute those tasks autonomously by connecting the LLM to real-world tools.
- **The Agentic Loop (ReAct Pattern):** AI agents continuously cycle through reasoning (deciding what to do), acting (using tools like web search, terminal commands, or APIs), and observing (processing results) until a task is fully completed.
- **OpenClaw's hub-and-spoke architecture:** A central always-on WebSocket gateway handles message routing, session management, and tool usage, while adapters normalize inputs from platforms like Slack, iMessage, Discord, and Teams into a unified format.
- **Skills make OpenClaw extensible:** Skills are simple markdown folders that teach the agent specific workflows (e.g., Google Calendar, Docker, GitHub, Trello). The LLM only loads relevant skills on demand to avoid filling the context window.
- **Local LLMs or hosted APIs:** OpenClaw supports both locally running models and cloud-hosted API models, giving users flexibility over privacy and performance tradeoffs.
- **Security risks are significant:** Misconfigured OpenClaw instances can act as backdoors since the agent has access to the file system and terminal. Thousands of exposed instances already exist online due to misconfigurations.
- **Prompt injection is a key vulnerability:** Malicious instructions embedded in untrusted inputs (emails, web pages) can trick the agent into executing unintended commands, making input validation critical.
- **Best practices for safe deployment:** Run agents in isolated environments, review all skills and code before use, and encrypt credentials before passing them to any LLM.
- **OpenClaw is open source and rapidly growing:** Created in late 2025, it quickly became one of GitHub's most-starred projects, reflecting strong momentum in the AI agent space alongside frameworks like LangGraph.