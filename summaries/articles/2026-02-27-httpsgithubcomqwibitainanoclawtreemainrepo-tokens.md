# Show HN: Badge that shows how well your codebase fits in an LLM's context window

Source: https://github.com/qwibitai/nanoclaw/tree/main/repo-tokens

## Summary
The article introduces "Repo Tokens," a new GitHub Action designed to measure a codebase's size in LLM tokens using `tiktoken`. This action then displays a badge in the repository's README, with colors (green, yellow, red) indicating what percentage of an LLM's context window the codebase fills, defaulting to 200k tokens. The primary goal is to provide a visible metric, similar to bundle size badges, to encourage developers to maintain lean, "agent-friendly" codebases that can be fully contained within an AI coding agent's context.

## Key takeaways
-   **New Advantage for Small Codebases:** With AI coding agents, having a codebase small enough to fit entirely within an LLM's context window offers a significant advantage.
-   **Repo Tokens GitHub Action:** This tool provides a way to quantify codebase size specifically in LLM tokens.
-   **Visual Metric for LLM Context Fit:** A color-coded badge (green <30%, yellow 50-70%, red 70%+) in the README visually indicates how well a codebase fits into a configurable LLM context window (default 200k tokens).
-   **Promotes Lean Codebases:** The action aims to nudge developers towards keeping their codebases smaller and more efficient for AI agent interaction, much like bundle size badges for JavaScript libraries.