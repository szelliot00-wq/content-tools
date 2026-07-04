# How Top AI Engineers ACTUALLY Use Claude Code

Video ID: `GxHKZybxoRI`

## Summary
This video argues that most people are using AI like an intern—micromanaging every step—while top AI engineers (Boris Journey, Andrew Karpathy, Peter Steinberger) have shifted to a fundamentally different model: giving AI a goal and letting it self-test, self-correct, and loop until done. The core shift is from human-supervised step-by-step prompting to autonomous AI-driven loops enabled by new capabilities like computer use, browser control, and vision models. The presenter demonstrates this "loop engineering" approach through real examples from his own business (an internal dashboard and video editing). He positions this as relevant primarily to technical builders, while noting that most businesses still benefit more from mastering AI fundamentals.

## Key insights
- **The old way vs. the new way:** Previously, users acted as managers of every AI step—give a task, wait, check, correct, repeat every few minutes. Now, AI can act, observe its own output, and correct itself in a loop without constant human intervention.
- **The intern vs. senior executive analogy:** Old AI behavior mirrors a school-leaver who needs to check every action. New AI behavior mirrors a senior executive who understands the goal, makes judgment calls, checks their own work, and reports back only when done—not every five minutes.
- **The harness matters more than the model:** The presenter emphasizes that the Claude Code harness (or similar tools like Codex/Cursor) does more heavy lifting than the underlying model. Computer use, screenshot/vision integration, and browser control via Puppeteer are what enable self-testing loops.
- **Key new capabilities enabling loops:** Computer use (AI controls your computer), vision model integration (AI takes screenshots and sees what's on screen), and browser control via Puppeteer (AI can open browsers, sign in, and interact with live software).
- **Self-testing is the critical unlock:** Nine months to a year ago, AI self-testing was unreliable. Now, with proper harness setup and explicit testing suites/unit tests, AI can reliably verify and correct its own work.
- **Real business example 1 — Internal dashboard:** The presenter built a system where he submits a change request via a UI form, it gets written to a Supabase table, Claude picks it up, makes code changes to the dashboard, runs a testing loop, starts a dev server for human confirmation, then pushes to production. He recently switched from Hermes to Claude for this workflow.
- **Real business example 2 — Video editing:** Using Codex, he feeds in a raw uncut video, prompts it to make engaging edits, then run a verification loop using vision to screenshot video frames and check for errors (text overlap, text size, text over face). Codex autonomously iterated until no major errors were found.
- **The docs/engineering loop folder pattern:** He stores markdown files in a `docs/engineering-loop` folder—including a PRD, testing file, iteration guidelines, loop template, and a runs log. When a new feature is added, AI creates a loop run from the template, executes it, logs results, and marks the feature complete.
- **Loop engineering is not for most businesses:** He's helped 2,800+ businesses apply AI profitably and says most need foundational AI skills first—not advanced loop engineering. Fundamentals (AI as an employee, time-saving processes) provide more practical ROI for typical business owners.
- **Loops apply beyond software:** Content creation, video production, email campaigns, QA/testing, research briefs, social scheduling, and lead generation are all named as valid loop use cases.
- **Lead generation loop example:** Spin up infinite lead magnets, distribute via email, feed performance data (open rates, click-through, purchases) back into the loop, and let AI identify what works and amplify it.

## Use cases
- **Software developers / technical founders** building products who want to reduce manual QA and supervision of AI coding agents
- **Business operators** who want to automate internal tooling (dashboards, CRMs, internal apps) with self-improving workflows
- **Content creators and video editors** who want AI to autonomously edit, review for quality, and iterate on video content
- **Email marketers** who want AI to draft, self-review (style, formatting, quality), and optimize campaigns based on historical performance data
- **Social media managers** who want AI to audit scheduling queues, create missing content, check quality, and post autonomously
- **Researchers / analysts** who want AI to loop across multiple sources, identify conflicting information, and surface reliable conclusions
- **QA engineers** who want AI to autonomously run, test, and fix bugs in software without step-by-step human oversight
- **Lead generation teams** who want to run iterative experiments on lead magnets and use performance feedback to improve automatically

## Patterns & frameworks

**Loop Engineering**
A named pattern (the presenter downplays the label) where AI is given a goal and autonomously cycles through: act → check → fix → repeat until the goal is achieved. Requires explicit success criteria, a checking mechanism (screenshots, unit tests, browser control), and the right tool access. The human steps in only to confirm final output before shipping.

**The Five Elements of a Loop**
For any loop to work reliably, you need:
1. **End goal** — what AI is trying to produce
2. **The why** — reasoning behind the goal, so AI can make judgment calls at edge cases
3. **Success criteria** — what "done well" looks like (features, accessibility, quality thresholds)
4. **Checking method** — how AI verifies its own work (computer use, browser, screenshots, vision model, unit tests)
5. **Right tools/access** — API keys, integrations, permissions AI needs to act autonomously

**Intern → Senior Executive Mental Model**
A progression model for thinking about AI capability: early AI (intern) needed hand-holding and checked in constantly; modern AI with a proper harness (senior executive) understands context, makes decisions, self-verifies, and reports back only when done. The shift is driven more by the harness than by model intelligence alone.

**Docs-as-Prompt Architecture**
Storing structured markdown files (PRD, testing guidelines, iteration rules, loop templates, run logs, feature checklists) in a project folder that gets fed into the LLM as persistent context. This gives AI stable, reusable operating procedures rather than relying on one-off prompts.

**Change Request Pipeline**
A workflow pattern: UI form → database table (Supabase) → AI agent picks up task → makes changes → runs self-test loop → starts dev server for human review → merges to production. Decouples human intent (the request) from AI execution and self-verification.