# The Exact AI Skills This Solo Founder Uses to Build 5 Apps at Once | Josh Pigford

Video ID: `GdxLaeyu33c`

## Summary
Josh Pigford, a serial entrepreneur who sold Baremetrics for $4M, shares how he builds and ships multiple AI-powered products simultaneously as a solo founder using a structured, AI-assisted development workflow. The video centers on his "build skill" system — a multi-phase, worktree-based development process using Claude Opus, GPT for adversarial review, and a collection of open-source Claude Code skills. It is most relevant to solo founders, indie hackers, and technical builders who want to maximize output with AI tooling and are willing to launch fast and iterate based on real user feedback.

## Key insights
- **Josh runs 5+ products in parallel**: Proxy User (synthetic browser QA), Rumored (LLM hallucination monitoring for brands), Reply Social (social mention aggregator), a medical document tracker built for his mother's stage 4 pancreatic cancer diagnosis, and Clearly (an open-source markdown editor).
- **His ADHD is a feature, not a bug**: He explicitly frames his context-switching brain as naturally suited to running multiple products. He finds more fulfillment in breadth than in the seven years he spent focused solely on Baremetrics.
- **His core build workflow has three stages**: (1) Research — generates a high-level research document by analyzing existing codebases, APIs, pros/cons, and competitor approaches; (2) Implementation planning — breaks work into 3–4+ phases, each as a separate Git branch/PR; (3) Phase execution — each phase gets deep web research, doc search (via Context7), and a UI design pass before code is written.
- **Worktrees are used as save points, not just for context management**: Each phase lives in a separate Git worktree, making rollback easy if a phase breaks things. It also prevents context rot and reduces hallucination by keeping each session fresh.
- **He uses a multi-model review chain**: Claude Opus does all planning and first-pass implementation. GPT (he says "GPT 3.5" and "GPT 5.5" at different points — likely GPT-4-class) does an adversarial review pass that consistently finds 3–5 bugs Opus missed. This mirrors the human code review process on engineering teams.
- **"But for Real" skill**: An open-source Claude Code skill that adversarially prompts the LLM to assume it made mistakes and go back over its own work. Finds an additional 3–5 bugs beyond the GPT review pass. He iterated on the prompt using Chops (his own Mac app for managing skill files) to make it "meaner."
- **"Learnings" skill closes the feedback loop**: After each phase ships, he runs a learnings skill that reviews the session history — including back-and-forth corrections — and distills new rules into the project's CLAUDE.md file automatically. The CLAUDE.md continuously improves over time.
- **CLAUDE.md is auto-generated per project from a template**: It includes product context, user personas, marketing tone, monorepo structure, custom commands, testing instructions, and framework-specific best practices (Rails + Inertia + Postgres is his standard stack).
- **Design is done manually before touching code**: Logo and brand work is done in Adobe Illustrator (fonts, colors, textures). He hasn't found a good AI shortcut for this. Marketing copy is generated *after* the app is built, because building clarifies what the product actually does.
- **He launches within 24 hours when possible**: He views pre-launch landing pages and email collection as a psychological delay tactic, not a real demand signal. His philosophy: build it, ship it, and get real feedback from real users as fast as possible.
- **Monetization threshold is simple**: If a product doesn't cover its infrastructure costs, it gets shut down. He refunds recent paying customers when shutting down. He avoids very low price points because they generate disproportionate support overhead.
- **Support is managed via a self-built in-app chat skill**: An open-source skill that generates an Intercom-like in-app chat system, giving him account context alongside support conversations and allowing him to batch support by product.
- **25 years of pre-AI experience is a real edge**: He can quickly assess whether a technical approach will cause problems in 2 months, identify the right shape of a solution, and move to a shippable state faster than someone without that pattern recognition.
- **His tools are almost entirely open source**: Build skill, learnings skill, but-for-real skill, Chops (skill manager), and others are all on GitHub.
- **Conductor is his orchestration layer**: It handles automated worktree management, unique ports per worktree (allowing 10 parallel sessions in separate browsers), environment variable copying, and model switching between Opus and GPT.

## Use cases
- **Solo founders** building multiple products who want a repeatable, structured AI development process without a team.
- **Indie hackers** who want to reduce hallucination and bugs in AI-generated code through adversarial review workflows.
- **Builders with ADHD or multi-project tendencies** who want a system that accommodates context-switching rather than fighting it.
- **Technical PMs or engineers** who want to use AI to go from feature request → research → implementation spec → phased PRs with minimal manual overhead.
- **Anyone managing family medical complexity** — the health tracker use case is immediately applicable for families dealing with chronic or serious illness and needing shared, AI-queryable medical records.
- **Founders worried about demand validation** — the video directly challenges the "build a landing page first" orthodoxy and offers a counter-framework: build fast, ship fast, learn from real users.
- **Teams trying to replicate peer code review** without reviewers, using multi-model adversarial prompting as a substitute.
- **Brand or marketing teams** tracking LLM hallucinations about their company (Rumored use case).

## Patterns & frameworks

**Build Skill (3-phase pipeline)**
An open-source Claude Code skill structured as: Research → Implementation Planning → Phase Execution. Research produces a high-level technical doc. Implementation planning breaks work into 3–30+ phases (each designed to be user-testable). Each phase executes with deep web search, competitor analysis, doc lookup (Context7), and a UI design pass before writing code. All phases produce a progress file that future phases reference.

**Worktree-as-PR pattern**
Each implementation phase gets its own Git worktree and becomes a discrete pull request. Worktrees serve as both context isolation (preventing hallucination from long context) and rollback checkpoints (save points). Conductor automates worktree setup including unique ports, env vars, and process initialization.

**Multi-model adversarial review chain**
Opus → GPT review → "But for Real" skill. Three sequential passes designed to catch different categories of bugs. The logic mirrors human code review: a second set of eyes (different model, different biases) catches what the first missed. The "But for Real" skill uses adversarial prompting to force the LLM to assume its own output is flawed.

**"But for Real" skill**
A standalone Claude Code skill with an intentionally aggressive prompt that tells the LLM it almost certainly made mistakes and demands a thorough re-review. Iterated via Chops with prompts like "be meaner." Consistently surfaces 3–5 additional bugs per pass.

**Auto-evolving CLAUDE.md via Learnings skill**
After each phase ships, a learnings skill reviews the full session history (including user corrections and failed attempts) and extracts new rules to append to the project's CLAUDE.md. Over time, the file accumulates project-specific institutional knowledge, reducing repeated mistakes.

**Design-before-code brand workflow**
Manual brand work (Illustrator, fonts, colors, textures) → color palette + SVG logo → hand off to AI for code and marketing copy. Marketing copy is generated *last*, after the product is built and its feature set is fully understood.

**Cost-as-market-fit threshold**
A simple, unsentimental business rule: if a product doesn't generate enough revenue to cover its infrastructure costs, it gets shut down. No vanity metrics, no months-long runway burning. Replaces complex product-market fit analysis with a concrete financial floor.

**Launch-first, validate-second**
Explicit rejection of the "collect emails on a landing page" model. Josh ships within 24 hours when possible, treating early real users as the only valid source of product feedback. The framework: assumptions about user problems are always incomplete; real users reveal adjacent use cases you can't anticipate alone.