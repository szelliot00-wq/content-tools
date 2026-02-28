# How to Make Claude Code Better Every Time You Use It (50 Min Tutorial) | Kieran Klaassen

Video ID: `g6z_4TMDiaE`

## Summary
Kieran Klaassen introduces "Compound Engineering," a philosophy and plugin for Claude Code designed to make AI code generation iteratively smarter. The core idea is a continuous loop of planning, working, assessing, and codifying learnings, allowing Claude Code to learn from feedback and improve with each use. Klaassen demonstrates his setup, showcasing custom slash commands, specialized sub-agents for research and review, and the powerful integration of Playwright for automated end-to-end testing and video creation, advocating for a new paradigm of AI-driven development.

## Key insights
- **Compound Engineering Philosophy:** AI can learn and improve over time. By investing in a feedback loop to capture what works and what doesn't, the AI (Claude Code) becomes more effective and avoids repeating past mistakes, creating a compounding benefit.
- **Four-Step Workflow:** The process includes Planning (using sub-agents for code, best practices, and framework research), Working (executing the plan), Assessing & Reviewing (employing multiple agents for security, architecture, and simplicity perspectives), and Codifying Learnings (capturing insights into documentation or `claude.md` for future reference).
- **Automated E2E Testing with Playwright:** Claude Code leverages Playwright to perform automated, browser-based end-to-end testing without manual script writing. This includes controlling the browser, inspecting console errors, and even recording video demonstrations of features for pull requests.
- **Agent Orchestration and Skills:** The system utilizes sub-agents for parallel, specialized tasks like research or code review, and "skills" to inject just-in-time context or custom functionalities (e.g., image generation) into Claude Code's capabilities.
- **Shift in Engineering Mindset:** Klaassen advocates for trusting AI more, particularly after it has been trained through the compound loop, reducing the need for constant manual code review. This paradigm shifts the developer's role to more of a "tech lead" or "engineering manager" for AI agents.
- **Efficiency Features:** Using "dangerously skip permissions" (in safe environments) streamlines continuous execution. The `&` (ampersand) command allows pushing a Claude Code terminal session to the web app or mobile for seamless workflow continuity.
- **"LFG" Command for Full Automation:** The ultimate goal is demonstrated with an "LFG" (Let's F*ing Go) command, which can automate the entire development cycle from a single prompt, including planning, coding, testing, generating marketing videos, and creating a pull request.