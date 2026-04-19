# The Claude Code Setup Nobody Shows You (Replaces OpenClaw + Hermes)

Video ID: `c2kJ7j3CgUs`

## Summary
This video argues that popular agentic AI frameworks like Hermes and OpenClaw, while promising automated tasks and delivered results, are often messy, technical, and expensive. The speaker demonstrates how to replicate and improve upon their core functionalities directly within Claude Code using a Pro or Mac subscription, avoiding extra costs and technical overhead. He breaks down five essential features—persistent memory, self-improving skills, rich interaction, scheduled tasks, and business context—showing how to build a robust, custom agentic operating system that delivers high-quality, contextualized outputs for business owners and individuals looking to manage multiple goals efficiently.

## Key insights
-   **Problem with Existing Frameworks:** Hermes and OpenClaw promise simple automation but have messy, technical setups, require extra payment for the best models (not available on Claude subscription), and lack transparency into their "black box" operations.
-   **Claude Code as a Superior Alternative:** Everything these frameworks offer can be built directly inside Claude Code using a Pro/Mac subscription, making it cheaper and providing full visibility and control for business owners.
-   **Five Core Features of an Agentic System:**
    1.  **Persistent Memory:** Memory that learns and maintains long-term searchable history.
    2.  **Skills:** Automated processes that create themselves and improve over time.
    3.  **Interaction Layer:** How users engage, beyond just basic chat interfaces.
    4.  **Scheduled Tasks:** Jobs that run automatically without constant supervision.
    5.  **Business Context:** Injecting relevant business-specific information for contextualized outputs.
-   **Four Memory Layers for Claude Code:**
    1.  `claude.mmd` / `agents.mmd`: Agent's operating instructions (who it is, how it behaves, rules).
    2.  Brand Context Folder: Business-specific details (brand voice, ICP, positioning, client details) shared across all skills for hyper-focused outputs.
    3.  Agent Context Folder: Describes agent's actions (`sold.md`) and user's common actions (`user.md`) for a personalized feel.
    4.  Project Memory: History and plan for each project, allowing Claude to remember past work and pick up where it left off.
-   **Memory Management Learning:** Avoid "context rot" by segmenting context. Keep core instruction files (`claude.md`) concise (not 1000+ lines) and use separate reference files loaded only when needed.
-   **Skill Creation & Improvement:**
    -   Use Anthropic's "skill creator skill" to generate new skills based on descriptions or existing processes.
    -   Keep `skill.md` files refined (less than 200 lines), stripping out surplus information into reference files.
    -   Implement self-learning loops by baking in feedback mechanisms or `learnings.mmd` files (non-negotiable rules) so skills improve with each use.
-   **Advanced Interaction Layer:**
    -   Claude Code's inbuilt channels feature allows phone interaction (Telegram, iMessage, Discord) for quick tasks, similar to Hermes.
    -   For complex business goals and managing multiple agents/projects, a custom UI layer called the "Command Center" is recommended. It features a Kanban-style board for multiple goals, full conversation visibility, sub-chats, and an auto-updating plan next to the chat.
    -   Anthropic's updated Claude desktop for multiple goals is still seen as too technical and GitHub-focused for high-level business planning.
-   **Effective Scheduled Tasks:**
    -   Claude's new "Routines" feature allows scheduled jobs but is limited to built-in connectors. Building your own allows leverage of Mac/Windows functionality without extra infrastructure.
    -   Chain multiple skills together in scheduled workflows (e.g., weekly content digest that pulls videos, analyzes, generates LinkedIn posts, and drops them into a review folder).
    -   Crucially, add a **human checkpoint** for automated workflows. Aim for 80% automation (research, drafting) but always have human supervision before shipping outputs to avoid "AI slop."
-   **The Power of Business Context (The "Business Brain"):**
    -   This is the most critical feature, often overlooked by tool-focused frameworks.
    -   It's the "compounding advantage" that underpins all other pillars.
    -   Create a single shared "brand context folder" containing your brand voice, ICP, positioning, client details, etc., that every skill references. Updating this folder once updates all relevant skills, ensuring consistently high-quality, contextualized outputs.
-   **Building Strategy:** Start with building the "business brain" (solid context foundation) first, as every other feature's effectiveness is multiplied by it.

## Use cases
-   Business owners seeking to automate recurring tasks and processes with AI.
-   Individuals or businesses looking to build custom AI agent systems (instead of relying on third-party frameworks like Hermes or OpenClaw).
-   Teams needing to manage multiple parallel business goals or "departments" run by different AI agents.
-   Content creators wanting to automate content generation (e.g., LinkedIn posts, newsletters, video analysis) while maintaining brand voice and quality.
-   Marketing professionals aiming to automate client research, landing page creation, or campaign generation.
-   Anyone using Claude Pro or Mac subscriptions who wants to leverage its full capabilities for complex, business-specific workflows.
-   Users who want transparency and control over their AI agent's operations, rather than a "black box" solution.
-   Businesses aiming for efficient automation while mitigating the risk of low-quality "AI slop" through a human supervision layer.

## Patterns & frameworks
-   **Four Memory Layers:** A structured approach to organizing an agent's knowledge:
    1.  `claude.mmd` / `agents.mmd`: Core agent instructions and rules.
    2.  Brand Context Folder: Central repository for all business-specific information (voice, ICP, positioning).
    3.  Agent Context Folder: Defines agent personality and common user actions.
    4.  Project Memory: Stores project-specific history and plans.
-   **GSD (Get Done) Frameworks:** Planning methodologies used for structuring and executing complex projects, referenced as an example for project planning within the Project Memory layer.
-   **Context Rot:** A problem where AI output quality degrades when too much irrelevant or poorly organized context is provided, emphasizing the need for segmented and timely context loading.
-   **Skill Creator Skill (Anthropic):** A specific Claude skill (developed by Anthropic) designed to help users generate new AI skills by providing descriptions or process outlines.
-   **Self-Learning Loop (for skills):** A mechanism within skills where the agent requests feedback or adheres to `learnings.mmd` files (non-negotiable rules) to iteratively improve its performance on a given task over time.
-   **Command Center (Custom UI):** A custom-built user interface layer that abstracts away terminal or chat management, providing a Kanban-style dashboard for supervising multiple business goals and AI agents simultaneously, with detailed visibility into conversations and plans.
-   **Human Checkpoint:** A strategic decision in automated workflows to perform 80% of the work automatically but always include a human review/approval step before final output delivery or publication, ensuring quality and mitigating risks.
-   **Business Brain (Conceptual Framework):** The foundational strategy of consolidating all critical business context (brand voice, ICP, positioning, client details) into a single, shared, and well-organized "brand context folder" that all skills and agents can access. This serves as the underlying intelligence that injects relevant context at the right time, making all AI outputs high-quality and business-specific.