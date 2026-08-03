# Jolli Memory AI Review (2026) Keep Your Coding Context Without Rescanning the Repo

Video ID: `2EsO4elMc7Y`

## Summary
This video reviews Jolli Memory, a VS Code/IntelliJ extension that gives AI coding agents persistent, local-first memory tied to a Git repository. The core argument is that AI agents lose their reasoning context between sessions and waste time and tokens re-scanning the same files repeatedly; Jolli solves this by attaching structured memory entries to every commit, capturing not just what changed but why. The video walks through a real TypeScript isometric snake game repo with 94 Jolli-documented commits, demonstrating recall, AI commit messages, and PR generation. It is most relevant to individual developers and small teams who frequently return to the same codebase and work with AI coding agents.

## Key insights
- AI coding agents rebuild context from scratch every session, costing both time and tokens — Jolli eliminates this by persisting reasoning across sessions.
- Jolli is free to download and works with VS Code, IntelliJ IDEA, and any Open VSX-compatible editor.
- Memory is stored locally and linked to the Git repository rather than locked inside a specific AI agent, making it portable across supported tools.
- The extension introduces the concept of **episodic memory** — a timeline of what happened in the codebase and why, not just a record of file diffs.
- Each commit gets a structured memory entry containing: commit hash, author, changed file count, a natural-language explanation of what was updated, and the reasoning behind decisions.
- Commits can be browsed two ways: chronologically or grouped by branch/feature, which is useful for understanding how a feature evolved over multiple commits.
- The demo repo has 11 bots each with different strategies, an "iron snake" mode with irregular grid shapes, separate leaderboards per mode, and 94 Jolli-documented commits — a realistic complexity level for the demo.
- The **recall command** lets you specify a branch and instantly surface the relevant history into the current session — summarizing dozens of commits in seconds.
- Example recalled context includes architectural decisions like why the main game logic stayed in one class instead of being split into modules, and why the reset control works from any game state.
- Jolli includes an **AI commit message generator** that reads only the staged diff (not the full agent conversation), keeping it focused and efficient.
- The **Create PR** feature builds a pull request description from branch memory, covering motivation, key decisions, changes, and potential risks — giving reviewers context beyond a raw diff.
- A **"Push to Jolli"** step publishes the structured commit record via a shareable link so teammates can review both the change and the reasoning behind it.
- Jolli does not replace Git history, documentation, or code review — it fills the gap of preserved reasoning that none of those tools currently capture.

## Use cases
- Developers who regularly return to the same codebase after days or weeks away and need to re-orient quickly.
- Small teams where not every reviewer followed the project from the beginning and needs context on why changes were made.
- Workflows involving multiple AI coding agents, where you want memory to follow you when switching between tools.
- Complex or long-running features developed across many commits, where a single commit message cannot capture the full story.
- Code review preparation — generating PR descriptions that explain motivation and risk, not just diffs.
- Onboarding situations where someone needs to understand past architectural decisions without reading every commit and file.
- Any project where important reasoning lives outside the code itself (in tickets, chats, or rejected-approach discussions) and would otherwise be lost.

## Patterns & frameworks

**Episodic Memory**
A timeline-based memory model that records what happened in the codebase and why, commit by commit. Unlike Git history (which records what changed), episodic memory captures the decision-making context. When a new session starts, the agent recalls this timeline instead of starting cold.

**Commit-Linked Structured Records**
Every commit gets a structured entry generated after the commit is created and linked to it. The record includes technical metadata plus a natural-language explanation of the reasoning. This separates the "what" (Git) from the "why" (Jolli).

**Branch/Feature Grouping**
Commits are organized not just chronologically but also by branch and feature. This lets you trace how a specific feature evolved — which problems appeared, why direction changed, and how small updates accumulated into the final result. Framed in the video as making history feel like "a notebook rather than a list of isolated changes."

**Recall → Commit → PR → Push workflow**
A four-step repeatable process: (1) use the recall command to bring relevant branch history into the current session, (2) generate an AI commit message from the staged diff only, (3) generate a PR description from branch memory including motivation/risks, (4) push to Jolli to publish the structured record as a shareable link for teammates.

**Local-First, Agent-Agnostic Memory**
The memory is tied to the repository, not to any single AI agent or editor session. This means the same context can be reused when switching between supported coding agents, avoiding vendor lock-in for institutional knowledge.