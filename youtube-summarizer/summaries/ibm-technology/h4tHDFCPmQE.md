# Vibe Coding vs. Agentic Coding: Which Should You Use?

Video ID: `h4tHDFCPmQE`

## Summary
The video distinguishes between vibe coding (prompt-driven, speed-focused AI code generation requiring little human review) and agentic coding (a structured human-AI collaboration loop involving understanding, planning, execution, testing, and validation). It argues neither is universally better — the right approach depends on the task's risk, complexity, and need for human oversight. The video also covers context management, the role of subagents, and the security considerations that grow as agents gain more autonomy.

## Key insights
- **Vibe coding prioritizes speed over understanding**: you prompt, generate, and iterate without necessarily reading the code — ideal for prototypes, demos, and experiments, but risky in production.
- **Agentic coding keeps the developer in the loop**: the workflow is understand → plan → execute → test → validate, with human judgment applied especially at the understanding and validation steps.
- **AI lacks human discernment**: LLMs give you what you asked for, but miss things like spotting architectural problems, understanding a team's intent, or recognizing when a simple fix is being overcomplicated.
- **Context is a finite budget**: more context doesn't always help — large codebases can dilute an agent's focus, making targeted, scoped context more effective than dumping everything in.
- **Subagents solve the focus problem**: narrow, permission-scoped subagents explore specific corners of a codebase and hand back summaries, keeping the main agent focused on orchestration.
- **Agent power requires security controls**: as agents gain the ability to run commands and call external tools, mistakes compound — mitigations include testing, human approval gates for irreversible actions, observability, rollback capability, and guardrails.
- **Match the approach to the task**: vibe coding suits quick bug fixes, variable renames, or design experiments; agentic coding is warranted for new production features, database or payment system changes, and large refactors.
- **The core skill to protect**: regardless of approach, stay the person who can explain the code — over-reliance on AI without understanding erodes that ability over time.