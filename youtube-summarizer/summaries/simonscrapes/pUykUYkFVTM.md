# The only Claude Code tutorial you’ll ever need (Apr 2026 edition)

Video ID: `pUykUYkFVTM`

## Summary
This video provides a comprehensive guide to using Claude Code, a powerful AI tool that transcends traditional chat interfaces by enabling direct execution of tasks on your computer. The presenter, a seasoned Claude Code user, shares best practices and foundational concepts for building robust business systems, moving beyond simple prompts to creating intelligent, context-aware workflows. It's particularly relevant for business owners, solopreneurs, and even software engineers looking to automate tasks, build applications, or repurpose content efficiently, significantly enhancing productivity and output quality.

## Key insights
-   **Claude Code's Core Advantage:** Unlike browser-based AIs (ChatGPT, Claude, Gemini, Custom GPTs) that only "think, write, and plan," Claude Code can "do" – it writes files, runs commands, creates folders, interacts with apps, and tests results directly on your computer, eliminating manual copy-pasting.
-   **Claude Code vs. Claude Co-work:** Claude Code is currently more powerful, hosting all advanced building blocks like skills, hooks, and planning frameworks first. Learning Claude Code provides a deeper understanding that also unlocks the simpler, visual interface of Claude Co-work.
-   **The Crucial Role of `claude.md`:** This is the most important file per project, loaded at the start of every session, acting as an "extension on Claude Code's brain." It defines the project's purpose, operational rules, brand voice references, "gotchas," and workflows.
-   **Parent Inheritance:** Claude Code reads `claude.md` files by walking up the folder tree. Rules in closer `claude.md` files take priority over conflicting rules from parent folders, allowing for layered, project-specific, or global contexts.
-   **"Don't Dump" Trick for `claude.md`:** Keep `claude.md` concise (under ~200 lines). Instead of pasting large amounts of context (like 50 example posts), point Claude to external reference files (e.g., `/references/brandvoice.md`) which it can load on demand.
-   **Global vs. Local Installation:** Skills, commands, and settings can be installed globally (hidden, loaded everywhere) or locally (visible in project folder, loaded for that project). Installing locally (`--local` flag) is recommended for visibility, easier debugging, and better context control.
-   **Planning Mode for Complex Tasks:** For projects expected to take over 10 minutes, using Plan Mode (Shift+Tab in the terminal) is crucial. Claude will read, think, and ask questions, but not execute. It generates a detailed plan (saved to `spec.md`) that survives context rot, significantly improving output quality.
-   **Slash Commands for Repeatable Manual Tasks:** These are manually invoked (`/command_name arguments`) and live in `.claude/commands/`. They contain a short prompt/SOP for consistent execution of frequent tasks, using `$arguments` for dynamic inputs.
-   **Skills for Automatic, Context-Aware Execution:** Skills (located in `.claude/skills/skill_name/`) are more powerful than commands because Claude automatically invokes them based on their `name` and `description` (YAML front matter in `skill.md`). They can contain entire folders of instructions, reference files, scripts, and assets.
-   **Progressive Disclosure in Skills:** This is critical for managing context and saving tokens.
    1.  **Description (Layer 1):** ~100 words, always loaded. Crucial for Claude to identify the correct skill.
    2.  **`skill.md` Body (Layer 2):** Process steps, <200 lines, loaded only when the skill triggers.
    3.  **Reference Files (Layer 3):** Unlimited, loaded *only when explicitly referenced* within the `skill.md` body and offloaded afterward, preventing context overload.
-   **Finding and Customizing Skills:** Skills can be found on marketplaces like `skills.mpp.com`, but deep customization for your specific brand, voice, and business context is always recommended, as many off-the-shelf skills are poorly built (e.g., large `skill.md` without reference files, vague descriptions). Exercise caution with skills containing `scripts/` folders.

## Use cases
-   **Content Creation & Repurposing:** Transforming long-form content (video transcripts, blog posts, podcast notes) into platform-specific drafts (LinkedIn posts, X threads, newsletters) in a consistent brand voice.
-   **Website Development:** Building personal websites or landing pages from simple prompts (e.g., a landing page in 15 minutes, a full website in 1.5 days).
-   **Application Development:** Building fully functional business applications (e.g., two apps in three weeks for a business).
-   **Business Automation:** Automating backend processes for solopreneurs (contract reviews, payment checks, reporting, lead tracking).
-   **Marketing & Outreach:** Improving LinkedIn content research, automating personalized LinkedIn video messages, generating proposals, creating full company marketing hubs.
-   **Internal Operations:** Building internal dashboards from spreadsheet data, creating content machines in a specific voice, meeting prep and follow-up assistance.
-   **Background Automations:** Running tasks on a schedule while the user is away.
-   **Client-Facing Tools:** Developing tools for clients.
-   **General Productivity:** Drafting follow-up emails, generating status updates, writing proposals.

## Patterns & frameworks
-   **Claude Code's Execution Model:** Describes what you want in plain English, then Claude Code takes action by writing files, running commands, creating folders, interacting with apps, testing results, and showing outputs. It's a fundamental shift from chat-based AI to an interactive agent.
-   **Markdown (`.md`) Format:** A lightweight markup language used for formatting plain text documents. It's easily readable by both humans and AI, allowing for clear structural understanding (headings, bold, lists, links). Used for `claude.md`, `skill.md`, and other planning/output files.
-   **`claude.md` as the Project Brain:** A markdown file (`claude.md`) placed within a project folder that provides essential context and rules for Claude Code sessions within that project. It’s the foundational document that defines the project's parameters and expected behavior.
-   **Parent Inheritance (for `claude.md` and other files):** A hierarchical system where files/rules in a lower-level folder inherit context from `claude.md` files (and potentially other resources like references, skills) in parent folders. The closest `claude.md` to the current working directory takes precedence for conflicting rules. This enables building a "business operating system" with master rules and project-specific overrides.
-   **`settings.json` for Permissions:** A JSON configuration file that defines allowed and denied actions for Claude Code within a project. It allows pre-approving safe operations (like reading/editing local files) while blocking dangerous ones (like package installation or file deletion without permission), striking a balance between autonomy and security.
-   **5 Key Questions Framework (for `claude.md`):** A structured approach to building an effective `claude.md` file by addressing:
    1.  What is this project/folder?
    2.  How do I run things?
    3.  What patterns do I follow?
    4.  What's weird here (gotchas)?
    5.  What's the process?
-   **"Don't Dump" Trick:** A best practice for `claude.md` and `skill.md` to avoid overwhelming Claude's context window. Instead of pasting large bodies of text, reference external markdown files containing that context, which Claude can load only when needed.
-   **Plan Mode:** An inbuilt Claude Code feature (activated via Shift+Tab) that allows Claude to *plan* a project without executing any actions. It reads files, thinks, asks questions, and outputs a detailed plan (e.g., to `spec.md`). This prevents "context rot" for larger tasks (>10 minutes) and ensures higher quality outputs by pre-defining the process.
-   **Context Rot:** A problem where Claude's memory window fills up over time, leading to a decline in output quality as it struggles to recall earlier context. Planning mode and progressive disclosure in skills are solutions to this.
-   **Slash Commands:** Markdown files (`.md`) placed in a `.claude/commands/` folder that define a specific, repeatable prompt/SOP. They are manually invoked by typing `/command_name` in the terminal, followed by any dynamic arguments (e.g., `/repurpose transcript.txt`).
-   **Skills:** Folders containing a `Skill.md` file (and optionally `references/`, `scripts/`, `assets/`). Skills are automatically invoked by Claude based on their YAML front matter (`name`, `description`) when a user's prompt matches the description, providing an instruction manual for specific, complex tasks.
-   **Progressive Disclosure (for Skills):** A method of managing context within skills by layering information. The skill description is always loaded; the `skill.md` body is loaded when the skill triggers; and external reference files are loaded *only* when explicitly needed during a specific step of the skill's execution, minimizing token usage and improving context retention.