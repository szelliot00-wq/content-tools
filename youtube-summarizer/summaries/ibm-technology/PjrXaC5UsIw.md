# What Is Agentic Coding? How AI Agents Modernize Code

Video ID: `PjrXaC5UsIw`

## Summary
The video explains how agentic coding — AI systems that autonomously navigate, understand, and propose changes to codebases — helps software teams tackle modernization. Using a financial services company adding real-time AI risk scoring to a legacy Java application as a running example, it walks through a 5-step iterative cycle where an AI development partner handles the investigative groundwork so developers can focus on judgment and validation rather than archaeology.

## Key insights
- **60–70% of developer time is spent understanding existing systems**, not writing new code — modernization compounds this because legacy systems accumulate undocumented knowledge over time.
- **The real challenge of legacy code is lost understanding**, not the code itself: why processes run in a specific order, why timing constraints exist, and what hidden dependencies connect seemingly unrelated systems.
- **Three core modernization obstacles**: tangled dependencies (shared state nobody mapped), framework gaps (e.g., Java 8 → Java 17 compatibility issues), and undocumented external connections (credit bureaus, payment networks, compliance APIs with strict formats).
- **The iterative modernization cycle** has five steps: (1) analyze the codebase to build a dependency model, (2) identify safe boundaries for change, (3) generate test coverage including edge cases, (4) developer review and approval, (5) run old and new systems in parallel to catch divergence before it reaches customers or regulators.
- **Developers stay in the loop at every step** — they validate proposals and approve changes rather than being replaced. The AI handles investigation; humans bring judgment.
- **Three non-negotiable safeguards for high-stakes systems**: human approval before any change moves forward, full Git history for traceability and rollback, and no autonomous deployment.
- **The payoff is direct**: time previously lost to navigating legacy code is redirected to actual feature development, enabling the team to deliver the risk scoring feature on schedule.