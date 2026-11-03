# Context-Aware Coding: Give AI Agents the Right Context

Video ID: `EkdIZXDnRK8`

## Summary
This video explains how to give AI coding agents the right context to produce accurate, codebase-consistent code. The presenter argues that a single-sentence prompt is insufficient when a repo contains years of architectural decisions, and that the quality of agent output depends directly on the quality of context provided. It covers six types of agent inputs and practical techniques for surfacing context when you're not sure what to ask.

## Key insights
- **Context determines correctness**: The same request ("add a login endpoint") should produce different code in different repos — the agent must understand your framework, DB layer, and conventions to match them.
- **Six key agent inputs**: files/existing code, repository structure (a compact repo map), dependency versions (lock files, not just library names), a failing test for feedback loops, documentation/conventions (an `agents.md` file), and your explicit developer intent.
- **Lock files prevent hallucination**: Many "hallucinated" API calls are actually version mismatches — giving the agent the lock file tells it which APIs actually exist.
- **Let the agent interview you**: If you don't know what context to provide, prompt it with "interview me and ask questions until you understand what you need" before writing any code.
- **Have the agent map the repo**: Ask it to explore and explain the codebase in plain language so both you and the agent share a common understanding of its structure.
- **Plan with assumptions visible**: Ask the agent to list its assumptions before coding so you can catch wrong ones early — then write what it learned into `agents.md` for future sessions.
- **More context is not better**: Models attend best to information at the beginning and end of a long input; irrelevant files compete with relevant ones, so filter ruthlessly.
- **Start fresh sessions per task**: Clear out accumulated noise by starting a new session for each task and pointing to only the specific files that matter (e.g., auth module + its tests + conventions, not billing or old build logs).
- **You stay in charge**: The agent does the digging, but the human makes the decisions — the goal is the *right* context, not the most context.