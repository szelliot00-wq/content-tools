# Every Claude Code Workflow Explained (& When to Use Each)

Video ID: `38t5UBCa4OI`

## Summary
This video explains that using Claude Code in a single, linear conversation is inefficient. It introduces a framework of five increasingly complex "agentic patterns" that allow users to manage parallel tasks, delegate work to specialized sub-agents, and even automate workflows entirely. The core argument is that by understanding and applying these patterns—from the manual "Operator" to fully autonomous "Headless" mode—developers can work more like a manager of a team, saving significant time and tackling more complex projects.

## Key insights
- **Claude uses built-in sub-agents automatically:** Even in a basic conversation, Claude Code uses three internal sub-agents behind the scenes to keep the main context window clean. These are:
    - **Explore:** A fast, cheap, read-only "scout" (runs on Haiku) that searches files.
    - **Plan:** A read-only agent used in plan mode (`/plan`) to research the codebase before suggesting a strategy.
    - **General Purpose:** A heavy-lifting agent (runs on Sonnet) with full read/write access for complex, multi-step tasks.
- **Pattern 1 (Sequential Flow) is limited by context rot:** The standard one-task-at-a-time approach causes the context window to fill up, leading to Claude "forgetting" details. While skills and commands like `/clear` or `/compact` can help, this method eventually hits a ceiling.
- **Pattern 2 (The Operator) enables manual parallelization:** The user acts as an orchestrator, opening multiple terminal windows for different, independent tasks. The `claude -w <workspace_name>` command creates isolated "work trees," each with its own Claude instance and clean context, preventing tasks from interfering with each other.
- **Pattern 3 (Split and Merge) automates parallel work:** Within a single session, Claude can analyze a task, break it into independent sub-tasks, and "fan out" the work to multiple sub-agents (up to 10 at once) that run simultaneously. It then merges the results. The key limitation is that sub-agents cannot communicate with each other; they only report back to the main agent (a "hub and spoke" model).
- **Pattern 4 (Agent Teams) allows for agent collaboration:** This is the most advanced and experimental pattern, designed for complex projects where agents need to interact. Agents communicate via a shared task list. This feature must be manually enabled and is very token-intensive, costing 4 to 7 times more than a single session.
- **Pattern 5 (Headless Mode) enables full autonomy:** Using the `-p` flag (`claude -p "<prompt>"`), Claude can execute tasks without any human supervision or an open terminal. This is ideal for automating scheduled tasks (e.g., via cron jobs) and batch processing where the output is easy to verify. Trust is the biggest limitation, so it's best for non-destructive or easily reversible tasks.

## Use cases
- **Building a simple website:** Use **Sequential Flow** to iteratively build a landing page, add a hero image, and then a contact form, with each step building on the last.
- **Working on multiple unrelated bug fixes:** Use **The Operator** pattern to open three separate terminals to simultaneously fix a checkout bug, refactor a user settings page, and implement a new onboarding flow without their contexts mixing.
- **Conducting market research:** Use **Split and Merge** to ask Claude to research five competitors. It will spin up five separate sub-agents, each researching one competitor in parallel, and then synthesize the findings into a single report much faster than doing it sequentially.
- **Developing a complex application:** Use **Agent Teams** to simulate a development team. One agent can act as a front-end developer, another as a back-end developer, and a third as a QA tester, all collaborating and sharing information via a shared task list.
- **Automating daily reports:** Use **Headless Mode** with a scheduled script (cron job) to run a command every morning that has Claude review all of the previous day's code commits and generate a summary report, ready for you when you start work.

## Patterns & frameworks
- **1. Sequential Flow:** The default, single-conversation model. Tasks are executed one after another, building on a continuously growing shared context until the context window is full.
- **2. The Operator:** A manual parallelization pattern where the user orchestrates multiple, independent Claude Code instances in separate terminals. This is ideal for tasks that do not depend on one another.
- **3. Split and Merge:** An automated parallelization pattern where Claude, within a single session, breaks a large task into smaller pieces, delegates them to multiple sub-agents to execute in parallel, and then merges the results back into the main conversation.
- **4. Agent Teams:** A collaborative, multi-agent pattern for complex projects. Agents can communicate and coordinate through a shared task list, allowing for interdependent work. This is an experimental and token-expensive feature.
- **5. Headless Mode:** An autonomous execution pattern where Claude runs a task non-interactively from a command-line prompt (`-p`). This removes the "human in the loop" and is perfect for automation, scheduling, and batch processing.
- **Builder-Validator Chain:** A specific application of the Split and Merge pattern where one sub-agent is tasked with building or writing code, and a second, separate sub-agent is tasked with reviewing or validating that work, creating an automated quality check loop.