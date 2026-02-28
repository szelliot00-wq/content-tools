# I Used Claude Code + Analytics to Replace 80% of My PM Work (5 Live Demos)

Video ID: `WK0bZrS8pVs`

## Summary
This video details a "Vibe PMing" workflow demonstrating how product managers can leverage AI tools like Claude Code and Cursor, connected via Amplitude's Model Context Protocol (MCP), to automate up to 80% of their routine work. By servicing product context to AI agents, PMs can move from manual reporting and data analysis to deeper insights, strategic problem-solving, and even direct prototyping. The workflow is highly relevant for product managers and analysts looking to significantly increase efficiency, reduce manual tasks, and focus on higher-leverage activities in their product development process.

## Key insights
-   **Core AI Workflow:** The most powerful AI PM workflow involves managing the entire product process within Claude Code and Cursor, hooked up to product analytics providers like Amplitude's MCP.
-   **MCP Definition:** Model Context Protocol (MCP) is the easiest way to connect AI models with external tools, actions, and data. Amplitude uses it to connect their tools and data to external AI clients like Claude, Cursor, and ChatGPT for complex coding and product workflows.
-   **Context Management:** While context window limitations exist, they are increasingly managed by AI clients (e.g., compaction in Claude Code, dynamic tool calling/RAG in Cursor/Claude) and by refreshing sessions. Useful context includes product roadmaps, specs (as markdown files), PRD templates, and summarized meeting notes.
-   **"Skills" for Automation:** Claude Code's "Skills" feature allows users to define custom prompts, heuristics, and tool configurations for repeatable tasks. For example, a "Analyze Chart" skill can identify anomalies, look for seasonality, and hypothesize drivers in minutes (saving 1-3 hours).
-   **MCP Criticisms & Rebuttals:**
    *   **Overhyped/Unreliable:** MCP is best for connecting external systems, not complex workflows. It has become a native, seamless standard that most AI clients now support with managed connector flows, reducing authentication and setup pain.
    *   **Context Waste:** Newer models and client-side changes (like dynamic tool calling and "Skills") prevent unnecessary tool descriptions from filling the context window by only loading relevant context when a skill is triggered.
    *   **Complexity:** Optimization of tool names, descriptions, and instructions within the MCP server is key to preventing ambiguity and ensuring accurate agent responses.
-   **Amplitude's Agent Platform:** Amplitude is launching a comprehensive agent platform (their "Cursor moment") in February 2024, aiming to make product data navigation and actions accessible via chat for all users. This includes:
    *   **Global Agent:** An embedded agent across the Amplitude platform with access to all data and actions, allowing navigation via chat.
    *   **Sub-Agents:** Specialized, asynchronous agents for specific tasks, e.g., Dashboard Agent (monitors anomalies, automates reporting), Session Replay Agent (analyzes user behavior, bugs), Feedback Agent (unifies qualitative data), Website Optimization Agent (recommends experiments).
    *   **External MCPs:** All Amplitude tools are exposed via MCP, allowing users to build bespoke workflows with other tools like Tableau, GitHub, Figma, etc.
    *   **Slack Integration:** The Amplitude embedded agent is available in Slack for direct queries, analysis, and kicking off actions within the platform.

## Use cases
-   **Deep Chart Analysis:** Investigating anomalies or significant metric changes by dropping a chart link into Claude Code, allowing the agent to analyze segments, group by properties, and hypothesize drivers in minutes (e.g., investigating a spike in tool calls from 8.1 average).
-   **Automated Weekly Reporting/Business Reviews:** Pointing AI dashboard agents to dashboards to automatically synthesize insights, identify urgent issues, and draft reports, pushing them to communication channels like Slack (saving entire Sundays of manual analysis).
-   **Qualitative Customer Feedback Analysis:** Unifying feedback from sources like Zendesk, Intercom, Salesforce, Gong, Slack, G2, App Stores, etc., into an AI feedback product, and then using Claude Code to analyze, cluster, and report urgent issues, bugs, praises, or competitor references.
-   **Converting Insights to Specs/PRDs:** Taking insights from dashboard agents or chart analysis and using Claude Code (with PRD templates and heuristics) to draft detailed product requirements documents, including problem context, solution workflows, design principles, and acceptance criteria.
-   **Prototyping & Task Routing:** Directly prototyping solutions in Claude Code/Cursor based on AI-generated insights, or routing tasks to engineering teams by pushing tickets to tools like Linear via MCP, potentially even messaging engineers directly in Slack with context.
-   **Automating Data Ingestion (e.g., Granola notes):** Hacking Claude Code to create scripts that pull data from tools without native MCPs (e.g., pulling summarized meeting notes from Granola into the product repo).

## Patterns & frameworks
-   **Vibe PMing:** A new philosophy for product management enabled by AI, where PMs automate repetitive tasks to focus on strategic thinking, problem-solving, and creative prototyping, resembling "vibe coding" or "vibe designing."
-   **Model Context Protocol (MCP):** A standardized protocol that enables AI models (like Claude, Cursor) to interact with external tools, data, and actions seamlessly. It involves providing tool names, descriptions, and instructions to the AI agent.
-   **Claude Code "Skills":** User-defined, reusable automations within Claude Code. A skill includes a name, description, a prompt (task definition), heuristics (steps to take), and configured tools (connected via MCP) to accomplish specific objectives, loaded into context only when relevant.
-   **Amplitude Global Agent:** An embedded, platform-wide AI agent that allows users to navigate Amplitude's UI, access any data point, and trigger any action within the product using natural language chat, significantly lowering the barrier for less technical users.
-   **Amplitude Sub-Agents:** Specialized, asynchronous AI agents built for specific PM workflows (e.g., Dashboard Agent, Session Replay Agent, Feedback Agent, Website Optimization Agent), designed to push insights to where users work (e.g., Slack, email).
-   **Git Worktree (in Conductor):** A Git feature used by tools like Conductor to create multiple isolated working copies of a repository. This allows several coding agents to run in parallel on separate branches without conflicting, useful for large-scale agent orchestration workflows.
-   **Context Compaction:** A feature in Claude Code where, if the context window limit is approached, the system summarizes previous turns in the conversation to free up space and allow the conversation to continue without losing the thread entirely.
-   **Dynamic Tool Calling / Retrieval-Augmented Generation (RAG) for Tools:** Advanced techniques implemented in AI clients (like Cursor and Claude) that intelligently select and load only the most relevant MCP tools into the context window for a given query, instead of loading all available tools every time, reducing context waste and improving response quality.
-   **System Prompts:** Robust, predefined instructions given to an AI agent to guide its behavior, decision-making, and output format for specific tasks, especially important for enterprise users who may be less familiar with AI agents.