# The Creator of Claude Code Shares His Opus 4.7 Setup

Video ID: `JTmhJNzA42A`

## Summary
This video breaks down six workflow tips for getting the most out of Claude's Opus 4.7 model, sourced directly from Boris, the lead engineer who created Claude Code, via a post on X. The core argument is that Opus 4.7 isn't just an incremental upgrade — it represents a shift toward longer, more autonomous, agentic AI coding sessions, but only if users actively adapt their workflows to take advantage of the new capabilities. The presenter, Matt, walks through each of Boris's six hacks in practical detail, explaining both what each feature does and why it matters. The video is most relevant to developers, AI-assisted coders, and product builders using Claude Code who want to reduce friction and dramatically increase output quality.

## Key insights
- **Auto Mode (Hack #1):** Eliminates constant permission prompts during long-running tasks using a model-based classifier that automatically approves safe commands. Activated via Shift+Tab in CLI or a dropdown in desktop/VS Code. Currently limited to Max, Teams, and Enterprise accounts. Enables running multiple parallel agents safely without using the riskier "bypass permissions" workaround.
- **Fewer Permissions Prompt Skill (Hack #2):** A lighter alternative to Auto Mode for users without access or those not yet comfortable with full automation. It scans session history, identifies commands you've already approved multiple times, and suggests adding them to a permanent allow list — reducing friction incrementally.
- **Recaps (Hack #3):** A newly shipped native feature that generates a concise, high-quality summary of everything Claude did in a long session and what it plans to do next. Eliminates the need to scroll through hundreds of messages after stepping away for 30 minutes, an hour, or overnight. Previously had to be manually engineered; now built in.
- **Focus Mode (Hack #4):** Activated by typing `/focus`, this hides all intermediate steps and terminal output, showing only final results or key changes. Reduces noise, speeds up review, and shifts the user's attention to high-level decisions rather than line-by-line log checking. Boris describes it as feeling like working with a capable teammate rather than micromanaging a tool.
- **Adaptive Thinking & Effort Levels (Hack #5):** Opus 4.7 moves away from fixed thinking budgets to adaptive thinking controlled via an `effort` command. Three levels: **Low** (faster responses), **High** (Boris's default — good balance for most tasks), and **Max** (reserved for the hardest problems). Higher effort unlocks significantly more intelligence, especially for complex refactoring or novel feature implementation. Analogous to model selection in tools like Cursor.
- **Self-Verification with the Go Skill (Hack #6 — most important):** Boris identifies this as the biggest improvement. By giving Claude the tools to verify its own work, you can instruct it to start a dev server and test end-to-end (backend), use the Claude Chromium extension to interact via browser (frontend), or leverage computer use tools (Claude Desktop). Ending an instruction with `go` triggers Claude to complete the task, test it thoroughly, run a `simplify` command to clean up, and even create a PR automatically.
- **Ultra Review Skill:** A new dedicated review session within Opus 4.7 that flags bugs and design issues in the way a careful human code reviewer would. Pairs directly with self-verification to further increase output quality and autonomy.
- **Boris's overall framing:** "Opus 4.7 is a significant step up. To get the most out of it, take the time to adjust your workflow to take advantage of Claude running for longer and being more agentic." Using old workflows yields modest improvements; adopting the new workflow represents a significant productivity leap.
- **The shift in relationship with AI:** Boris frames Opus 4.7 as moving Claude from "Claude helps me a little" to "Claude is basically a senior engineer sitting next to me."

## Use cases
- **Developers running long overnight or multi-hour coding sessions** who want to come back to verified, working code rather than just plausible-looking code
- **Solo builders or small teams** who need to stretch their output by running multiple agents in parallel on different tasks simultaneously
- **Engineers doing large-scale refactors** where reviewing every intermediate step is impractical and high-effort adaptive thinking delivers better outcomes
- **Frontend developers** who want Claude to visually interact with and test a UI in a real browser using the Chromium extension
- **Backend developers** who want Claude to spin up a dev server and run true end-to-end tests autonomously
- **Anyone using Claude Code on Max, Teams, or Enterprise plans** looking to eliminate permission prompt friction entirely
- **Users who step away from long sessions** (lunch breaks, overnight runs) and need instant context restoration via the Recaps feature
- **Code reviewers or QA-focused engineers** who want a dedicated AI review pass that catches bugs and design issues like a human reviewer would
- **Product managers or technical founders** (non-expert coders) using AI-assisted development who want cleaner, higher-trust outputs with less manual verification

## Patterns & frameworks

**1. Auto Mode (Model-Based Safe Approval)**
A classifier-driven system that evaluates whether a command is safe to run and approves it automatically, removing the human from repetitive low-stakes permission loops. The pattern: identify repetitive low-risk decisions → automate them with a safety layer → free human attention for high-stakes decisions.

**2. Tiered Effort / Adaptive Thinking**
A three-level effort dial (Low / High / Max) that lets users match computational intensity to task complexity. The pattern: don't apply maximum intelligence to every task — calibrate effort to the problem to balance speed, cost, and quality. Boris's heuristic: default to High, escalate to Max only for the hardest problems.

**3. The Go Skill / Self-Verification Loop**
A repeatable agentic workflow pattern: (1) Give Claude the tools to test its own output (server, browser, computer use), (2) append `go` to the instruction, (3) Claude executes → tests → simplifies → optionally creates a PR. The pattern closes the feedback loop autonomously, shifting the human role from checker to reviewer.

**4. The Trust Ladder (Progressive Autonomy)**
An implicit framework for building trust with the AI progressively: start with Fewer Permissions prompts (incremental trust) → move to Focus Mode (hide noise, trust outputs) → graduate to Auto Mode (full safe autonomy) → add Go Skill (autonomous verification). Each rung reduces micromanagement as confidence in the model grows.

**5. Recap-Driven Context Management**
A session management pattern for long-running or interrupted work: use native Recaps to instantly restore context at the start of each session rather than reconstructing state manually. The pattern: treat AI sessions like async handoffs — always leave/receive a structured brief.

**6. Ultra Review as a Dedicated QA Pass**
A two-phase quality pattern: (1) generate output via self-verification, (2) run a separate Ultra Review session focused solely on finding bugs and design flaws. Mirrors the software engineering best practice of separating the "builder" and "reviewer" roles to catch issues a single pass misses.