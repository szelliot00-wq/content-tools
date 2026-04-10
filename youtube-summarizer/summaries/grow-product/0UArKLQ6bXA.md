# How this PM Used Claude Code to Support 20 People

Video ID: `0UArKLQ6bXA`

## Summary
This video features an interview with Hannah Stalberg, a PM at DoorDash, who details her "Team OS" (Team Operating System) framework for scaling product teams using Claude Code. The core argument is that by creating a structured, shared knowledge repository where the entire cross-functional team (PMs, engineers, designers, analysts, ops) contributes, teams can manage context efficiently and collaborate at a much higher level. The video provides a deep dive into the repository's structure, advanced context management techniques, and a comprehensive planning process for creating high-quality documents. This is most relevant for product managers, engineers, and team leads looking to leverage AI agents for enhanced productivity and cross-functional alignment.

## Key insights
- **The Problem:** PMs now support larger, more cross-functional teams (e.g., 1 PM to 10 engineers), and roles are blending, requiring shared context for everyone to make product decisions.
- **The Solution: Team OS:** A shared knowledge repository in a coding agent like Claude. It's a version-controlled "team brain" that everyone contributes to via pull requests (PRs), including non-technical partners.
- **Lean & Nested `claude.md` Files:** The root `claude.md` file should be minimal, containing only a document index, team member info (for easy Slack integration), and key channels. Each sub-folder should have its own `claude.md` file with a local index, enabling Claude to progressively load only the necessary context for a given query.
- **Theory of Context Management:** The repository is structured to optimize LLM performance. The goal is to minimize the context consumed for any task to maximize the model's "thinking room." This is achieved by having Claude navigate via indexes rather than searching entire folders.
- **Structured for Scale:**
    - **Analytics:** The `analytics` folder should contain not just dashboards but also codified `metrics_playbooks`, SQL `queries`, and table `schemas`. This allows anyone on the team to correctly perform data analysis without being an expert.
    - **Standardization:** Using shared skills (e.g., a skill to summarize all customer calls in a consistent format) makes large-scale synthesis easy and reliable for the AI.
- **The Power of Plan Mode:** For complex tasks like writing a strategy document, basic prompting is ineffective. The "Plan Mode" workflow is superior:
    1.  **Initiate Plan Mode (`Shift+Tab` x2):** This removes the LLM's bias for action.
    2.  **Parallel Research:** Claude researches the topic and your internal repository's context simultaneously.
    3.  **Iterative Q&A:** Claude uses the `ask_user_question` tool to clarify goals and scope.
    4.  **Review the Plan:** The most critical step is for the user to meticulously read, question, and iterate on the generated plan before execution.
    5.  **Invite AI as a Thinking Partner:** Prompt Claude to "push you on your thinking" and "consider other angles" to identify gaps in your reasoning and improve the final output.
    6.  **Advanced Techniques:** For complex plans, specify verification steps, review the prompts Claude will use for sub-agents, and have agents write to temporary files to avoid context overload.
- **GitHub for Everyone:** Non-technical team members can and should contribute to the Team OS. Hannah's strategy partner, who had never used GitHub, now submits PRs daily to check in customer call notes. The process can be done entirely in natural language.
- **Beginner's Mindset is Crucial:** Learning these tools takes time (Hannah has 1500+ hours). Use Claude to teach you by asking it to explain *why* the repository is structured a certain way or how a command works. This is key to being able to iterate and improve your own setup.
- **"Claude Code" is a Misnomer:** The tool is for all knowledge work—writing docs, doing analysis, building prototypes—not just coding.

## Use cases
- **Product Managers:** Creating high-quality PRDs, strategy documents, competitive analyses, and synthesizing customer research at scale.
- **Engineering Teams:** Onboarding new engineers faster, investigating bugs using historical context, and self-serving product metrics without waiting for a PM.
- **Data Analysts & Scientists:** Scaling their impact by codifying metric definitions, queries, and schemas, enabling the entire team to perform accurate analysis.
- **Cross-functional Teams (Design, Ops, Marketing):** Collaborating in a single source of truth, accessing the latest customer insights, and contributing their own context to the shared knowledge base.
- **Team Leads & Managers:** Establishing a robust, scalable system for team knowledge that persists through personnel changes and reduces reliance on individuals.

## Patterns & frameworks
- **Team OS (Team Operating System):** The central framework of the video. It's a shared, version-controlled knowledge repository that acts as a team's collective brain. It's structured with function-specific folders (e.g., `analytics`, `product`, `engineering`) and nested `claude.md` files to be efficiently navigated by an LLM. The entire team contributes to it.
- **Context Management ("Context 101"):** A mental model for structuring information to optimize LLM performance. It involves four concepts: `Context` (info in the session), `Context Window` (how much info can be held), `Compaction` (compression when the window is full, which loses fidelity), and `Thinking Room` (the unused part of the window where the model reasons). The goal of the Team OS structure is to maximize Thinking Room by loading only relevant context.
- **Plan Mode Workflow:** A repeatable process for generating high-quality documents and completing complex tasks. It shifts the LLM from an "action" bias to a "planning" bias. The core steps are: initiating the plan, allowing the AI to do parallel research, engaging in an iterative Q&A, meticulously reviewing and refining the AI's generated plan, and then executing it.
- **Beginner's Mindset for AI Learning:** A learning methodology that involves actively using the AI tool as a tutor. Instead of just using pre-made tools, you ask the AI to explain concepts, justify its structures, and teach you how to improve your setup, fostering a deeper understanding that allows for effective iteration.