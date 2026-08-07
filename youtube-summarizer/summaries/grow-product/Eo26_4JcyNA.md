# These skills give you PM superpowers in Claude Code

Video ID: `Eo26_4JcyNA`

## Summary
This video features Aji Udway, a 25-year product management veteran and former CPO at Typeform, Kalanley, and Parable, demonstrating a library of Claude Code "skills" (reusable prompt-based workflows) that embed PM and business judgment directly into the development environment. The central argument is that developers are accelerating 10x with AI while PMs remain a bottleneck — and that product and business-layer skills running inside Claude Code can close that gap. Udway walks through a live scaffolding skill that takes a raw idea through market research, viability gating, architecture decisions, CI/CD setup, prototyping, and customer discovery planning — all within a single Claude Code session. The video is most relevant to product managers, solo founders, vibe coders, and engineering leads who want to compress the PM/design/dev workflow into one AI-native environment.

---

## Key insights
- **Developers are speeding up; PMs are the new bottleneck.** AI coding tools have accelerated engineering output dramatically, but PM judgment (viability, prioritization, customer discovery) hasn't kept pace. These skills are designed to fix that asymmetry.
- **The "three-layer" model of a tech company.** Successful products require three simultaneous layers: (1) software/hardware, (2) product (customers + business model), and (3) business (resource allocation). Most Claude Code skill repos only address layer 1.
- **The scaffolding skill is an 11-step orchestrator.** It sequentially calls sub-skills: context gathering, project type detection, web search for reference projects, viability gate, market research, product brief, architecture decisions, folder/CLAUDE.md generation, test setup, CI/CD setup, and GitHub first-push readiness.
- **Viability gates actually say no.** Unlike a raw LLM chat that tends to validate ideas, the viability gate uses structured evals across six dimensions — revenue, technical feasibility, differentiation, competitive landscape, target user definition, and problem clarity/urgency — and will recommend abandoning an idea if three or more dimensions score weak. Standup Zero (a Slack standup digest tool) failed: moderate scores on problem clarity, target user definition, and differentiation, with a crowded competitive landscape.
- **Market research gets you ~60–70% of the way.** LLMs can produce Perplexity-quality competitive scans, pricing landscapes, and differentiation maps. The remaining 30–40% requires real sources and human validation. Users must sense-check output: are the competitors mentioned current and relevant? Does the persona match what you know?
- **The tool generates a tailored CLAUDE.md automatically.** Rather than authors spending time crafting CLAUDE.md front matter, the scaffolding skill produces a project-specific CLAUDE.md that defines folder structure, prototype conventions, bug classification patterns, and CI behavior.
- **Vibe coders lack CI/CD and code review habits.** The skill addresses this directly by setting up continuous integration, test folders, secret/gitignore hygiene, and a bug-learning log — giving non-technical builders "the bones of a solid codebase" before writing a single line of product code.
- **Prototyping is built into the skill.** The skill generates multiple self-contained HTML/CSS prototypes to explore interaction models before committing to a direction. In practice, Udway layers 5–6 design sub-skills and combines them in pairs to generate diverse prototype variants quickly.
- **Customer discovery is also a skill.** The "customer discovery week" skill produces a full plan: recruitment criteria, three-step interview protocol (open-ended exploration → targeted questions → survey quantification), synthesis templates, and a hard gate — it refuses to proceed unless you can name at least five real target contacts, treating fewer as a validation signal that you may not have market access.
- **The "vibe memo" skill captures the why.** As decisions are made during development, vibe memo logs the reasoning behind them, not just what was built — solving the "why did we do this?" problem in large or fast-moving codebases.
- **Enterprise rollout pitfall: ungoverned forking.** The biggest mistake in team deployments is letting everyone fork skills independently. The recommended pattern is a centralized, short CLAUDE.md that references a shared skill library; individual learning should feed back into the central repo so everyone benefits.
- **The skills library is open source.** Available at labs.productmind.com and linked GitHub repo. Includes: new project scaffolding, vet-a-feature, sharp problem test, vibe memo, roadmap-from-strategy, listing machine, scope cutter, MVP vs. SLC decision tool, and pricing design skill.
- **Anti-gravity is just VS Code.** The IDE shown is a VS Code fork; the skills work in any Claude Code harness via terminal.

---

## Use cases
- **Solo founders/vibe coders** who build without a PM or designer and need structured validation before writing code
- **PMs at startups** who need to match the new pace of AI-accelerated engineering teams
- **PMs evaluating feature requests** who want a structured way to vet opportunity cost against other backlog items ("vet a feature" skill)
- **Engineering leads onboarding a new project** who want architecture, CI/CD, and folder structure set up automatically with consistent standards
- **Product teams doing market research** who want a fast first draft (~60–70%) of competitive landscape and positioning before deeper primary research
- **Enterprise teams rolling out Claude Code** who need a governance model that prevents knowledge fragmentation across forked configurations
- **Founders deciding between multiple startup ideas** who want an objective kill/proceed signal before investing engineering time
- **Teams lacking a customer discovery process** who need a ready-made interview and survey plan with clear qualification gates
- **Any builder** who ships to GitHub with zero users and wants to reduce the odds of that outcome before starting

---

## Patterns & frameworks

**New Project Scaffolding Skill (11-step orchestrator)**
A master skill that calls sub-skills in sequence: gather context → detect project type → find reference projects → run viability gate → market research → write product brief → make architecture decisions → generate folder structure + CLAUDE.md → set up tests → configure CI/CD → prepare GitHub first push. Designed to take a raw idea description and produce a commit-ready repo skeleton with documented business rationale.

**Viability Gate**
A compressed version of the Sharp Problem Test that scores an idea across six dimensions: revenue potential, technical feasibility, differentiation, competitive landscape, target user definition, and problem clarity/urgency. Three or more weak scores triggers a hard "do not build" recommendation. The gate is intentionally adversarial — unlike a default LLM response, it is designed to say no.

**Sharp Problem Test**
A deeper evaluation framework (from the book *Building Rocket Ships*) that goes beyond market lane analysis to focus on whether the product can generate 3x the value it delivers — i.e., whether there is a defensible revenue case. Used as a sub-skill within the scaffolding orchestrator and also available standalone.

**Vet-a-Feature Skill**
Same logic as the scaffolding viability gate but scoped to a single feature within an existing product. Focuses on opportunity cost relative to other backlog items and anti-patterns, with the Sharp Problem Test baked in more aggressively.

**The Three-Speed Problem**
A mental model describing the historical bottleneck (development) being cut by 10–20x via AI, while the "why to build" (customer-bound discovery) and "access to market" (customer-bound distribution) speeds remain slow. The imbalance means the PM/discovery layer is now the critical path, not engineering.

**Three-Layer Product Stack**
Framework for thinking about what a tech company needs: (1) software/hardware layer, (2) product layer (customer understanding, business model), (3) business layer (resource allocation, strategy). Most AI coding skill repos only address layer 1; these skills address all three.

**Three-Step Customer Discovery Protocol**
A structured interview methodology: Step 1 — open-ended exploration with no leading questions or prototypes (learn what questions to ask); Step 2 — targeted interviews using questions surfaced in Step 1 (validate hypotheses); Step 3 — convert validated questions into a survey to quantify responses at scale.

**Centralized CLAUDE.md Governance Model**
For enterprise rollouts: maintain a short, high-signal central CLAUDE.md that references a shared skill library. Individual project CLAUDE.md files reference the central one rather than duplicating or diverging. Innovations discovered by individuals feed back into the central repo. Prevents knowledge fragmentation while preserving flexibility for local context.

**Vibe Memo Pattern**
A lightweight logging skill that captures decision rationale (the *why*) alongside code changes (the *what*), building an evergreen decision log inside the repo. Addresses the common problem of losing context about architectural choices as a codebase scales or team changes.