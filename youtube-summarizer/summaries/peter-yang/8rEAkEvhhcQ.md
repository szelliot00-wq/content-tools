# The 4-Step Agentic Engineering Workflow I Use to Ship Real Apps | Ras Mic

Video ID: `8rEAkEvhhcQ`

## Summary
Michael, a full-stack engineer and YouTube creator with 100K+ subscribers, walks through his personal 4-step agentic engineering workflow that he calls a "software factory" — though he explicitly rejects the common definition of that term. Rather than a fully autonomous pipeline that runs end-to-end without oversight, his system is a structured, human-in-the-loop workflow encoded in an `agents.md` file and a handful of skills. The video is most relevant to developers using AI coding agents (Claude Code, Codex, Cursor) who want a repeatable, verifiable process for shipping real production software without sacrificing code quality or introducing regressions.

## Key insights
- **The core problem with typical "software factories"**: One wrong assumption at the start cascades and destroys the entire run, wasting tokens and producing unusable output. Michael's solution is to inject structure and verification checkpoints rather than letting the agent rip autonomously.
- **The workflow lives in `agents.md` + skills**: The agents.md file doesn't describe the codebase structure — models are good enough to read and infer that themselves. It describes *how Michael wants to work*, encoding his personal engineering workflow as agent instructions.
- **Step 1 — Isolate (New Feature skill)**: Every new feature or bug fix starts by creating a new git work tree branched off main. This enables true parallelism — Michael runs 4–5 Codex agents simultaneously in separate Ghosty terminal tabs, each on an isolated work tree, with no risk of agents stepping on each other. Work trees share resources (dev server ports, databases) but isolate code changes.
- **Step 2 — Build (Code Structure skill)**: Code is written following a service layer architecture with two distinct layers: an orchestration layer (owns business rules, state transitions, service function calls) and a service layer (owns reusable functions, SDK definitions, structured returns). This limits duplicate functions (a common agent failure pattern) and keeps code readable without needing to trace every line.
- **Step 3 — Prove (Evidence-Driven Testing skill)**: The agent must produce *evidence* that its work is correct. For bugs, it records a before video (reproducing the bug) and after video (showing the fix) using FFmpeg — originally built for Linux/Mac, works especially well with Cursor cloud agents. For features or non-screenshotable work, the "before and after" skill (borrowed from Vercel) captures screenshots or performance stats (e.g., navigation time dropped from 850ms to 60ms on one project).
- **Step 4 — Loop (Grepile GP Loop skill)**: After pushing a PR, the Grepile code review agent runs and scores the PR 1–5. If the score is under 5/5, the GP loop fires: it ingests the feedback, writes fixes (following code structure), pushes, and re-triggers Grepile. The loop runs up to 10 iterations until a 5/5 score with zero unresolved comments is achieved. Most state-of-the-art models (Fable, Astra) produce a 4/5 on first PR.
- **Human-in-the-loop is intentional**: Michael personally tests every feature before merging, even in an "automated" workflow. The evidence from steps 3 and 4 is designed to minimize the time spent in manual review, not eliminate it. He calls this "building trust with the agent."
- **Planning style is conversational, not spec-driven**: Michael uses Whisperflow to voice-dictate 5–10 minute "yap sessions" with the agent, iterating back and forth until the feature is defined. The conversation history *is* the spec. For complex setups he wants to revisit, he asks the agent to create a markdown file (e.g., `setup.md`) inside the codebase itself.
- **Model strategy — Astra for finding issues, Fable for writing code**: Astra excels at performance audits (finds caching/prefetch improvements in Next.js/SvelteKit), security audits (caught a critical receipt validation vulnerability in Michael's church payment system), and computer use. Fable writes cleaner, more mergeable code and doesn't redirect to a lesser model during security-related prompts the way Fable 5.1 sometimes does.
- **Don't use state-of-the-art models for everything**: Smaller/cheaper models (GPT-4.5 Soul for routine tasks, Luna for knowledge work and tax number-crunching) handle most work well. Using Astra Ultra on a simple PR causes overthinking, longer runs, and token burn. Model routers are predicted to become important soon.
- **Skills will partially survive better models**: Skills that describe how the codebase works will disappear as models get smarter. Skills that encode *personal workflow preferences and domain knowledge* are more durable — they reflect the developer's taste, not the model's capability gap. Michael tests each new model from scratch (no agents.md, no skills) to see what still needs to be encoded.
- **Cron jobs for production apps**: For a client project involving government-spec compliance, Michael runs a daily scheduled Cursor cloud agent security audit. He considers automated security audits mandatory for any production app, especially those handling money.
- **Skepticism toward lab advice**: Lab engineers have unlimited token budgets and optimize for different constraints than independent developers or consultancies. Michael is philosophically supportive of open-source/open-weight models as a hedge against vendor lock-in and cost escalation.

## Use cases
- **Freelancers/consultants** building production apps for clients who need defensible code quality and verification trails.
- **Solo developers** running multiple parallel feature branches simultaneously without conflicts.
- **Developers with existing production apps** who want to retroactively run performance or security audits (Astra is particularly effective here).
- **Teams introducing AI agents** who want a structured workflow rather than free-form autonomous generation.
- **Developers handling sensitive data or payments** who need evidence that the agent's fixes actually work before merging.
- **People who think out loud** rather than write specs — the conversational planning approach via voice dictation is explicitly called out as a workflow fit.
- **Anyone whose personal "software factory" keeps falling apart** mid-run due to wrong early assumptions — the isolation + verification pattern directly addresses this failure mode.

## Patterns & frameworks

**1. The 4-Step Workflow (Isolate → Build → Prove → Loop)**
The core repeatable process encoded in `agents.md`. Each step maps to a named skill: *New Feature* (isolate), *Code Structure* (build), *Evidence-Driven Testing / Before & After* (prove), *GP Loop* (loop). Skills are called in sequence but the agent is reminded which step it's on rather than running fully autonomously.

**2. Git Work Tree Isolation**
Every task — feature or bug fix — gets its own git work tree branched off main before any code is written. Enables parallel agent execution across a single repo without conflicts. The skill explicitly notes that work trees isolate code but not shared resources (ports, databases).

**3. Service Layer Architecture (Code Structure skill)**
Two-layer code organization: an orchestration layer (business rules, state transitions, "the why and when") and a service layer (reusable functions, SDK wrappers, "the how"). Enforced via a skill to prevent agents from duplicating functions across files. Makes code readable at the function-name level without tracing implementation.

**4. Evidence-Driven Testing**
The agent must produce proof of correctness before a PR is considered done. For bugs: video of reproduction + video of fix (FFmpeg-based). For features: before/after screenshots. For non-visual work: quantitative performance stats. Borrowed/adapted from Vercel's before-and-after skill.

**5. GP Loop (Grepile integration)**
An automated PR quality loop: push → Grepile scores PR → if < 5/5, agent ingests feedback → rewrites code → pushes → re-triggers review → repeat up to 10 iterations. Uses an external code review agent's confidence score as a convergence signal rather than the agent self-assessing.

**6. Conversation-as-Spec planning model**
No formal spec document. Extended voice-dictated back-and-forth with the agent (via Whisperflow) serves as the planning artifact. For anything that needs to persist, a markdown file is created inside the repo itself so both the developer and future agent sessions can reference it.

**7. "Michael Benchmark" for model evaluation**
Personal benchmark for comparing models: run a performance audit, a security audit, and a UI/computer-use task. Whichever model performs best across those three dimensions gets used for that type of work — leading to Astra for auditing/computer use and Fable for code generation.