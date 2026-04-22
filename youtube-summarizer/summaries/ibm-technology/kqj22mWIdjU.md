# Building a Team of AI Agents: Roles, Feedback, & Teamwork Explained

Video ID: `kqj22mWIdjU`

## Summary
This video explains how to design teams of AI agents by drawing parallels to human team structures. It outlines the distinct roles that subagents can play within a larger agent system, using a mobile app development scenario as a practical example. The video also covers strategies for optimizing each role's performance and emphasizes that agent teams, like human teams, should start small and scale as complexity grows.

## Key Insights
- **AI agents mirror human teams:** Complex tasks require multiple collaborating subagents, each with a specialized role, just as human projects require diverse team members with distinct responsibilities.
- **Core agent roles include:** Doer (executes individual steps), Planner (breaks problems into smaller tasks), Tool Operator (interacts with APIs and external tools), Learner (retrieves and filters outside information, often via RAG), Critic/Feedback (reviews outputs, checks for hallucinations, or scores competing results), Supervisor (monitors progress and prevents bottlenecks), and Presenter (synthesizes and communicates results to the user).
- **The ReAct pattern is a popular starting framework**, combining a Tool Operator (action), Planner (reasoning), Critic (observation), and Presenter (answer) into a simple but effective agent structure.
- **Four ways to optimize a subagent's performance:** Prompting (clear instructions), Model Selection (matching model size, specialization, and reasoning ability to the role), Model Tuning (fine-tuning with labeled examples, though resource-intensive), and Context Management (providing relevant information without overwhelming the model).
- **Start lean, then scale:** Like a startup, an agent team should begin with a few key roles to reach a working solution quickly, then expand with additional specializations to improve quality, consistency, and reliability over time.
- **Some roles are themselves mini-agents:** The Tool Operator and Learner roles may internally involve multiple LLM calls and tool interactions, blurring the line between a single role and a standalone agent.