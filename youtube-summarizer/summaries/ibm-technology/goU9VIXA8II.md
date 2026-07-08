# MCP vs Skills: Which Is Right for Your AI Agent and LLMs?

Video ID: `goU9VIXA8II`

## Summary
The video explains how MCP (Model Context Protocol) and Skills are two complementary ways to extend an LLM's capabilities beyond its training data. MCP standardizes how AI models connect to external data sources and services, while Skills package reusable prompts and domain knowledge into portable markdown-based files. The presenter frames both as tools for "context engineering" — giving an LLM the right information to produce consistent, accurate outputs — and walks through when to choose one over the other.

## Key insights
- **Context engineering vs. prompt engineering**: Simply asking an LLM a question is prompt engineering; adding structured external data, tool responses, and domain knowledge is context engineering, and it's what makes agents reliable.
- **MCP standardizes external data access**: Rather than copy-pasting API docs and tokens into a prompt, MCP abstracts service APIs into an LLM-ready format, handles authentication, and translates the model's JSON requests into actual HTTP calls.
- **Skills solve the non-determinism problem**: LLMs are non-deterministic by nature, so repeatable tasks (e.g., always formatting CRM data with name, contact info, and favorite cookie) need a structured prompt package — that's what a Skill is.
- **A Skill is a markdown file with metadata**: It includes a title, a description of when to trigger it, and the prompt itself. It can also bundle scripts and resources, and is auto-loaded into the context window only when relevant.
- **MCP = integration layer; Skills = capability layer**: Use MCP when you need real-time, permissioned access to live data (VM status, cluster state, customer records). Use Skills when you need a lightweight, reusable way to teach the model how to do something consistently.
- **Both are open source and broadly supported**: Either can be run locally today and works across major AI tools and models, making them practical starting points rather than aspirational infrastructure.