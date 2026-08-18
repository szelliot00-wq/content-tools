# What Is RAD? Why It Matters in the Age of AI Coding

Video ID: `J0zbWsutyA8`

## Summary
The video draws a direct parallel between James Martin's 1991 Rapid Application Development (RAD) methodology and modern AI-assisted ("vibe") coding. It argues that RAD's four phases — lightweight requirements planning, user-driven prototyping, iterative construction, and cutover — map naturally onto how teams build software with agentic AI tools today. The key lesson is that AI-generated prototypes are valuable but insufficient on their own; they must be paired with spec-driven development to catch security gaps and business logic errors before production deployment.

## Key insights
- RAD was designed around the assumption that users can't articulate what they want until they see something working — a premise that fits AI prototyping perfectly, since a working app can now be generated from a plain-language prompt in minutes.
- The prompt has effectively replaced the requirements document: describing the problem, users, rules, and constraints to an AI agent mirrors exactly the lightweight planning RAD called for in phase one.
- AI-generated prototypes function as RAD's "keeper" prototype — the starting point that gets refined through user feedback rather than thrown away.
- Studies find roughly 45% of AI-generated code samples contain some type of security issue, making blind deployment of AI-built prototypes genuinely risky.
- Spec-driven development fills the gap: discoveries from prototyping get written into a formal spec (business rules, acceptance criteria, security requirements), which then becomes a test suite the generated code must pass.
- Users clicking through a prototype can't catch rules that were never written — a security reviewer reading a spec can. The spec surfaces invisible logic gaps that UI testing alone will miss.
- The role of programmers hasn't disappeared; it has shifted toward writing precise specs and verifying AI output rather than writing every line of code directly.