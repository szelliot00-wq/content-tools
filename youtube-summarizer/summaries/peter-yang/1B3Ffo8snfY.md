# Full Tutorial: Connect Claude Code to Google, Slack, and Reddit in 40 Min (Skills + MCPs)

Video ID: `1B3Ffo8snfY`

## Summary
This video demonstrates how product managers can leverage Claude Code as a centralized AI workspace by connecting it to common work tools using Multi-Contextual Prompts (MCPs) and APIs. Carl, a product lead and creator of a free Claude Code course for PMs, showcases integrations with Google Workspace, Linear, Slack, and Reddit to automate daily tasks, gather information, and streamline workflows. The core argument is that centralizing these operations within Claude Code significantly reduces "busy work" and context switching, making product managers more efficient by enabling AI to assist with everything from meeting preparation and document updates to task management and team communication. This approach is highly relevant for product managers seeking to maximize AI's utility in their daily responsibilities and consolidate their digital workspace.

## Key insights
-   **Claude Code Maximalism**: The presenter advocates for living in Claude Code all day, positioning it as the ultimate centralized hub for product managers to manage tasks, communications, and information across various platforms.
-   **MCPs for Seamless Integration**: Multi-Contextual Prompts (MCPs) are pre-configured integrations that provide Claude with immediate and correct understanding of how to use specific tools like Google Workspace, Linear, or Reddit. This contrasts with general API usage where Claude might need trial and error.
-   **Enhanced MCP Management**: Anthropic recently released a "tool search" feature for Claude, allowing multiple MCPs to be turned on simultaneously without consuming Claude's memory/context until they are actively needed, making it easier to manage many integrations.
-   **Google Workspace Automation**: The Google Workspace MCP allows Claude to access calendar events, local notes, and Google Drive documents. It can prepare for meetings by finding relevant docs, comparing agendas, suggesting additions, and then *actually updating* those Google Docs (e.g., sprint planning doc, stakeholder review doc).
-   **Linear Integration for Task Management**: The Linear MCP (a modern Jira alternative) is "amazingly easy" to set up with a single terminal command. Claude can list all tickets, identify priorities, and perform bulk updates like renaming projects and associated tickets (e.g., "Moltbot" to "OpenClaw"). It can also generate tickets from PRD requirements.
-   **Slack Communication**: While an official Slack MCP exists (with limited company rollout), an unofficial "stealth mode" MCP can be used for personal purposes to send messages to Slack channels as the user, facilitating automated team updates (e.g., project rename status).
-   **Reddit for Industry Monitoring**: A dedicated Reddit MCP allows Claude to bypass Reddit's web fetch blocks, enabling it to pull top discussions, post titles, and even sentiment from subreddits (e.g., r/productmanagement) – useful for market research and trend monitoring.
-   **Ultimate Daily Standup Generation**: Claude Code can combine information from Linear issues, Google Calendar, and meeting notes (local and Google Docs) to generate a comprehensive daily standup summary, including current tasks, meetings, and blockers, all within the Claude Code interface. This can then be sent to Slack.
-   **"Consult the Council" Skill**: A custom skill that leverages APIs to send a product spec or problem to multiple leading LLMs (ChatGPT, Gemini, Groq) simultaneously for review and feedback. This costs only a few cents per run and helps catch nuances or omissions Claude might miss, leading to higher quality outputs.
-   **Image Generation from Context**: A custom skill can integrate image generation tools (e.g., Nano Banana via Gemini API) into Claude Code. This allows Claude to generate architecture diagrams or other visual assets directly from the project's context (e.g., a PRD) within the workspace, improving efficiency over external tools.
-   **Structured Workspace Organization**: Carl recommends a specific folder structure for Claude Code: `context` (stable info), `meetings` (docs), `projects` (new project folders for all related work), `templates` (reusable formats), `to-do`/`current tasks`, `tools` (custom tool definitions/code), `workflows` (multi-step processes), and `_temp` (dynamic, temporary working space).
-   **Workflow Refinement**: Start complex, multi-step processes as simple workflows within files, and once they are refined and prove valuable for reuse, convert them into formal Claude skills or commands.
-   **AI Review is Crucial**: Always review AI-generated output (e.g., Slack messages, documentation) before it is finalized or sent, as AI can make errors or formatting issues.
-   **Free Educational Resources**: Carl offers a free course, "Cloud Code for Product Managers," which teaches Claude Code directly within Claude Code, emphasizing its accessibility and workflow improvements.

## Use cases
-   **Daily meeting preparation**: Automatically gather calendar events, relevant Google Docs, and local notes, compare against agendas, and suggest additions to meeting documents.
-   **Automating meeting note updates**: Update sprint planning documents, stakeholder review docs, and other meeting notes based on Claude's analysis of context.
-   **Streamlining task management**:
    -   Listing and prioritizing Linear tickets.
    -   Bulk-renaming projects and tickets in Linear.
    -   Generating new Linear tickets directly from product requirement documents (PRDs).
    -   Checking progress on tickets without leaving Claude Code.
-   **Team communication**: Draft and send status updates, project changes, or daily standups to Slack channels as the user or a bot.
-   **Industry trend monitoring**: Automatically pull top discussions, sentiment, or specific information from subreddits or other forums relevant to a product or industry.
-   **Planning and specification review**: Use "Consult the Council" to get diverse feedback from multiple LLMs on product specs, implementation plans, or bug fixes, ensuring higher quality.
-   **Visual asset creation**: Generate architecture diagrams, mockups, or other images directly from project context (e.g., PRDs) using integrated image generation tools.
-   **Personal knowledge management**: Organize project-specific context, research, and working documents within dedicated project folders in Claude Code.
-   **Content creation workflows**: Manage multi-step content creation processes, including research, idea generation, and drafting, with AI assistance.

## Patterns & frameworks
-   **Multi-Contextual Prompts (MCPs)**: A framework for pre-packaged integrations that empower Claude Code to interact seamlessly with external applications (e.g., Google Workspace, Linear, Reddit, Slack). MCPs include all necessary tools and documentation, allowing Claude to understand and utilize the integration correctly from the outset.
-   **Tool Search Feature (Anthropic)**: An underlying Claude Code mechanism that intelligently loads MCPs into context only when needed, rather than all at once. This improves performance and memory management, allowing users to have many MCPs available without concern for context limits.
-   **Stealth Mode MCPs**: An unofficial pattern for integrating Claude Code with applications (like Slack) by leveraging local information on the user's computer, bypassing formal API approvals. This is generally for personal use and requires caution regarding company policies.
-   **Claude Code Workspace Organization**: Carl's recommended file and folder structure for maintaining an efficient and personalized Claude Code environment:
    -   `context`: For stable, foundational information Claude should always know (e.g., company goals, product principles).
    -   `meetings`: To store meeting-related documents and notes.
    -   `projects`: A dynamic folder where each new project gets its own subfolder to contain all associated documents, research, and working files, keeping everything contextual.
    -   `templates`: To store reusable formats and rules for Claude's output (e.g., Slack message formats, PRD structures).
    -   `to-do`/`current tasks`: A simple list for Claude to understand the user's immediate priorities.
    -   `tools`: A dedicated folder for custom tools, their underlying code, and documentation (e.g., API keys, scripts for image generation).
    -   `workflows`: For defining multi-step processes or routines that Claude can execute, often comprising several individual files for each step.
    -   `_temp`: A temporary, dynamic workspace for files that are short-lived, for quick drafting, or for Claude to look at briefly before deletion.
-   **Workflow-to-Skill Progression**: A process where users first develop and refine complex, repeatable sequences of actions as "workflows" using files. Once a workflow is stable and valuable, it is converted into a formal Claude "skill" or "command" (often defined in `.cloud` files) for easy invocation, typically pointing to the underlying tools and files.
-   **Consult the Council (Skill/Pattern)**: A custom skill that exemplifies prompt engineering across multiple LLMs. It involves sending a specific query or document to the APIs of several different large language models (e.g., ChatGPT, Gemini, Groq) to solicit diverse feedback, compare perspectives, and identify a more robust solution, enhancing the quality of AI-assisted decision-making and content.
-   **Generate Image (Skill/Pattern)**: A skill that demonstrates integrating third-party generative AI tools (like Nano Banana via Gemini API) directly into Claude Code. This allows Claude to leverage its context understanding to generate visual assets based on document content, improving the user's creative workflow without leaving the terminal.