# Stop Hitting Claude Code Limits (Try These 7 Tips)

Video ID: `4fES92fRhC8`

## Summary
This video provides seven essential tips (plus a bonus) for users of Claude Code to reduce token usage, avoid hitting computational limits, and optimize their subscription costs without sacrificing output quality. The core argument centers on actively managing the AI's context window, streamlining instructions, and strategically choosing models and tool integrations. The advice is highly relevant for developers, product managers, and anyone leveraging Claude Code for coding, ideation, or application building who frequently encounter token limits or wish to maximize efficiency.

## Key insights
-   **Strategic Model Selection:** Use more powerful, expensive models like Opus 4.6 only when absolutely necessary, as they consume tokens faster. Cheaper alternatives like Sonnet 4.6 are often sufficient for most tasks, saving significant costs and limits.
-   **Keep Conversations Short:** The entire conversation history is sent with every message, causing token usage to grow exponentially. Start new conversations for unrelated tasks; for example, two 15-message conversations are cheaper than one 30-message conversation.
-   **Leverage Projects/Folders for Scoping:** Avoid installing MCPs (Modular Chat Prompts) and other tools globally, as this loads them into every session. Instead, create project-specific folders and install only the necessary tools, instructions, and files locally within that folder, drastically reducing unnecessary context bloat.
-   **Monitor MCPs & Prefer CLIs:** Use `/context` or `/mcp` commands to inspect active MCPs. Where possible, choose Command Line Interfaces (CLIs) over MCPs. CLIs only consume tokens when a command is explicitly called, whereas MCPs add token overhead simply by being present in the session. Switching from an MCP to a CLI for "Appify" saved the speaker 40% in token usage.
-   **Optimize `claude.md` Files:** Your `claude.md` file, which sets initial context, should be lean. Remove contradictions, eliminate instructions for tasks Claude already performs well by default (e.g., "write clean code"), and keep the global `claude.md` minimal, moving project-specific rules to local files. Additionally, link to separate `.md` files (e.g., `styleguide.md`) rather than embedding all content directly to only load context when required.
-   **Work in the Correct Folder:** A seemingly simple but crucial tip: ensure you are always working within the appropriate project folder, as each folder holds its own specific `claude.md` and reference files, preventing irrelevant context from being loaded.
-   **Adjust `settings.json`:** Modify specific settings for efficiency:
    -   Set `auto-compact percentage override` to around 75% (default is 83-85%). This triggers context compaction earlier, improving output quality by preventing "context rot" and saving credits.
    -   Set `bash max output length` to 150,000 (default is lower). This prevents silent truncation of output and unnecessary token-consuming reruns of commands.
    -   Add `deny rules` (similar to `.gitignore`) to permissions to prevent Claude from reading irrelevant directories (e.g., `node_modules`, `build` folders, lock files), reducing bloat and stopping annoying access notifications.
-   **Bonus: Utilize Plan Mode:** For large projects, engage Claude's "plan mode" first to conceptualize and refine the approach. This ensures that when tokens are eventually spent on building, it's for the exact, desired outcome, preventing wasteful retries.

## Use cases
-   **Developers and Engineers:** Optimizing development workflows, code generation, and debugging of APIs or applications using Claude Code.
-   **Product Managers:** Efficiently prototyping, ideating, and gathering requirements for new features or products with AI assistance.
-   **AI Application Builders:** Individuals or teams creating software and applications powered by Claude Code, particularly those looking to deploy projects.
-   **Users Managing AI Costs:** Anyone experiencing high subscription bills due to extensive Claude Code usage.
-   **Frequent Token Limit Hitters:** Users who regularly encounter "out of tokens" notifications and seek to extend their session longevity.
-   **Content Creators & Designers:** Streamlining AI-assisted creative tasks such as generating motion graphics, slideshows, or design assets by focusing relevant tools and instructions.
-   **Technical Writers:** Managing and optimizing the context for AI-generated documentation or reports.

## Patterns & frameworks
-   **Global vs. Local Scoping:** A fundamental principle for managing resources (MCPs, `claude.md` instructions, tools, files). Resources should be installed or defined locally within specific project folders where they are needed, rather than globally, to prevent unnecessary context bloat in unrelated sessions.
-   **Active Context Management:** A recurring theme emphasizing the importance of understanding and deliberately controlling the information sent to Claude in each interaction. This includes keeping conversations concise, trimming instructions, and preventing irrelevant files from being read.
-   **CLI Preference:** A specific tool integration pattern advocating for the use of Command Line Interfaces over Modular Chat Prompts (MCPs) where functionality allows, due to their more efficient token consumption model (tokens only used on command execution).
-   **Lean Instruction Design:** A prompt engineering pattern focused on crafting `claude.md` files with concise, non-redundant, and high-impact instructions. This involves removing unnecessary prompts and defaulting to Claude's inherent capabilities to save tokens.
-   **Plan Mode First (Workflow):** A development workflow pattern for larger projects, suggesting an initial conceptualization and planning phase with the AI. This allows for validation and refinement of the approach before committing resources to the actual build, preventing wasted tokens on potentially incorrect or suboptimal implementations.