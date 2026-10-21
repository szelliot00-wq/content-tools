# I Got an Ex-ElevenLabs Growth Lead to Give Away His Growth OS

Video ID: `FTbkpiKWLKw`

## Summary
This episode features James McAulay — who helped ElevenLabs scale from $100M to $200M ARR in 9 months — walking through his "Agentic Growth Operating System" (Growth OS), a GitHub-hosted Claude Code configuration designed for growth practitioners. The core argument is that AI has unlocked a new kind of "full-stack growth" role where a single person can run rigorous, data-connected growth experiments without needing engineers. James demonstrates live how skills, tools, scheduling, and goal-alignment machinery work together to keep a growth person focused and accountable. The video is most relevant to solo growth leads, first growth hires, product managers doing growth work, and non-technical founders who want to run disciplined growth experiments using Claude Code.

---

## Key insights

- **Autonomous agents are overhyped in their current form.** Most "autonomous growth agents" people claim on LinkedIn are either wasting tokens on summarization tasks or are simple scheduled skills. True 24/7 self-directing agents don't yet exist reliably — the real value is in directing agents at focused tasks for 1–2 hours at a time.
- **The biggest risk with AI for growth is distraction, not capability.** Because you can build almost anything in a day, staying focused on what actually moves the needle is the core challenge. The Growth OS is explicitly engineered to counter this.
- **Goal-alignment at every cadence is the system's backbone.** James runs: a Mission file (annual), Quarterly OKRs, a Monthly retro (Claude pulls data from Stripe, PostHog, Attio, Zero), a Weekly retro (~1 hour, using WhisperFlow voice input), and a Daily standup skill. Each layer ties back to the one above.
- **Session hooks keep the agent goal-aligned.** Every time Claude Code starts, a hook fires that reminds the agent of the current mission and OKRs, and Claude is instructed to push back if the user starts working on something off-track.
- **Weekly retros have the highest ROI of all cadence skills.** James has done ~15 consecutive weekly retros. The key value: Claude spots behavioral patterns (e.g., over-building/refactoring instead of marketing) by cross-referencing the to-do list (Todoist) and GitHub commit history.
- **Multi-agent adversarial review surfaces blind spots a single agent misses.** James spawns 4–5 sub-agents with different lenses (feasibility, missing items, alignment, technical correctness) to critique PRDs, OKRs, or strategy docs. This "panel of critics" reliably finds issues that the primary agent overlooks.
- **Use Sonnet (not Opus/Fable) for sub-agents.** James accidentally spun up 20 Opus sub-agents and immediately hit token limits. Sub-agent tasks should use Sonnet for speed and cost efficiency.
- **The PRD skill uses a "5 Whys" interrogation before building.** Claude challenges the user to justify why they want to build something, ties it to a specific metric, checks the data (e.g., SEO keyword volume), and sometimes tries to talk them out of building it if the numbers don't support it.
- **PRDs serve as persistent agent checkpoints.** The PRD has checkboxes Claude ticks off as it works. If the session hits a context limit or is killed, the agent reads the PRD on restart and picks up exactly where it left off.
- **Growth experiment discipline is built into the system.** Every experiment requires: hypothesis, key result it ties to, baseline metric, primary metrics, confounders, and a stop condition. Weekly retros scan for stale or unclosed experiments and force documentation of learnings.
- **Data for SEO + Firecrawl replaces $100/month Ahrefs/SEMrush.** Data for SEO is a cheap API (cents per query) for keyword research. Firecrawl converts any website to Markdown for Claude to analyze. Paired with the Lighthouse CLI (for page speed), this combination handles full SEO audits automatically.
- **SEO audits now run on a Sunday schedule.** James has a Claude Code cron job that tests his entire site every Sunday and emails him if any Lighthouse score has regressed after a deploy.
- **PostHog is the #1 recommended analytics tool.** Very generous free tier, strong MCP/API/CLI, and a "PostHog wizard" that Claude can use to set up dashboards and experiments entirely without touching the UI. James has never manually created a dashboard — all done via Claude + the API.
- **Require PostHog events in CI to prevent tracking gaps.** James wrote a test that blocks merging any PR unless it includes PostHog event tracking — preventing the common mistake of shipping features without analytics.
- **Well-annotated event definitions prevent misinterpretation.** James documented all ~350 events with descriptions of when they fire, where, and what they should be used for — a task completed in ~2 hours that would have been impractical pre-AI.
- **Connecting every tool to Claude Code is the multiplier.** His stack includes: Stripe, PostHog, Attio (CRM), Zero (email), Kit (mailing list), Apollo (enrichment), Sentry (errors), Cubic (AI code review), Playwright (testing), VidIQ, Firecrawl, Data for SEO, Eleven Labs, Epidemic, Mistral. A single prompt combining Kit + Apollo + Attio + Slack produced a daily enriched non-buyer lead alert — something that would have previously required an engineer.
- **AI enables self-improving agents.** The most underused capability: pointing Claude at its own system prompt or CLAUDE.md and asking how to improve it based on recent interactions. Most users haven't realized this is possible because Claude Chat can't edit its own config files — only file-based agents like Claude Code can.
- **ElevenLabs was using custom GPTs in 2025, not Claude Code skills.** Skills as a formalized concept weren't widely adopted until autumn 2025. The current state (file-based agents with skills, tools, and CLIs) represents a major evolution in just 12 months.
- **James scaled his own company to $100K MRR in 95 days** with no full-time employees, by pivoting from growth consulting into cohort-based AI training, using a referral/affiliate program (Rewardful) to drive word-of-mouth, and running private enterprise workshops.

---

## Use cases

- **Solo founder or first growth hire** who needs to run rigorous growth experiments without a team
- **Product manager** responsible for growth metrics who wants structured experiment documentation and a weekly review process
- **Non-technical growth lead** who wants to connect analytics, CRM, email, and SEO tools to Claude Code and perform tasks that previously required engineering support
- **Content-led growth** practitioners who want to run iterative LinkedIn/YouTube experiments with automated performance tracking
- **SEO auditing** without a $100+/month subscription — especially for personal brands, newsletters, or lean startups
- **Startup exec or growth consultant** onboarding to a new company who needs to quickly understand goal alignment, funnel data, and experiment history
- **Growth teams at AI-native companies** transitioning from custom GPTs and chat-based workflows to file-based agentic workflows
- **Anyone prone to overbuild or get distracted** by shiny objects who needs an external accountability layer baked into their tooling
- **Coaches, trainers, or educators** who want to productize their expertise into a cohort-based business and use AI to operate it lean

---

## Patterns & frameworks

**Growth OS (Agentic Growth Operating System)**
A GitHub-installable Claude Code configuration consisting of: a Mission file, Quarterly OKRs, skills (daily standup, weekly retro, monthly retro, SEO audit, PRD, multi-agent refine), a curated tool stack with CLIs/APIs, and session/cron hooks. It installs by running a few commands, interviews the user about their goals, and customizes CLAUDE.md to enforce goal alignment throughout every session.

**Hierarchical Goal Cadence**
Mission → Quarterly OKRs → Monthly Retro → Weekly Retro → Daily Standup. Each level checks progress against the one above. Data is pulled automatically from connected tools (Stripe, PostHog, Attio) rather than relying on subjective self-assessment.

**Multi-Agent Adversarial Review**
Spawns 3–10 sub-agents, each with a distinct critical lens (feasibility, missing elements, alignment, technical correctness, Euro-skeptical critic, etc.). The master agent synthesizes findings and returns a prioritized list of P0/P1/P2 issues. Optionally runs autonomous improvements or checks in with the user. Best applied during the planning phase — after auditing but before handing off to a build agent.

**5 Whys PRD Interrogation**
Before writing a PRD, Claude challenges the user with repeated "why" questions until the feature is tied to a specific measurable outcome. If the data doesn't support the hypothesis (e.g., low keyword volume), Claude attempts to talk the user out of building. Once approved, the PRD uses checkboxes as a restart-safe progress tracker.

**Experiment Discipline Template**
Every growth experiment is documented with: hypothesis, tied key result, baseline metric, primary success metrics, known confounders, and stop condition. Retro skills scan for experiments that are overdue or undocumented and force closure and learning documentation. Goal: every experiment informs the next one.

**Self-Improving Agent Loop**
Point Claude at its own CLAUDE.md, skill files, or system prompt and ask: "Based on our recent interactions and the Anthropic docs, how would you improve this?" Claude edits its own configuration files. Only possible in file-based agents (Claude Code/Codex), not in Claude Chat. Used to refine skills iteratively rather than starting from scratch.

**Full-Stack Tool Connectivity Pattern**
Connect every tool in the growth stack (analytics, CRM, email, SEO, payments, enrichment, error tracking) via MCP, CLI, or API key. The more connected, the more complex tasks can be completed in a single prompt without engineering involvement. Treat API key access as the minimum viable integration.

**Content Experiment Loop (Akash's variant)**
A scheduled skill that pulls performance data from the previous day's content (LinkedIn post metrics), evaluates experiment results (e.g., 1 post vs. 2 posts per day), updates its own model of what works, and generates a recommended posting plan for the next day — without requiring manual review of the platform UI.