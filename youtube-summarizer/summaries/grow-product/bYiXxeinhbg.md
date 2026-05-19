# How Non-Technical PMs Are Building Products Without Engineers

Video ID: `bYiXxeinhbg`

## Summary
Andre Albuquerque, founder of Europe's largest product builder school (Builders Camp, 4,000+ students), walks non-technical PMs through a four-level progression for building and shipping products using AI coding tools — starting with Lovable and ending with multi-agent Claude Code workflows. His core argument is that non-technical PMs who remain stuck in Jira/Linear/PowerPoint are being left behind, and that AI tools have eliminated the technical barrier to building real products. The episode is most relevant to non-technical PMs, product owners, and early-stage founders who want to move from managing backlogs to actively shipping features.

## Key insights
- **Non-technical PMs are bureaucrats by default**: Most are dependent on engineering teams, stuck writing tickets and decks, and contributing nothing directly to the codebase — a liability in AI-native organizations where even CEOs push to GitHub (e.g. Shopify CEO's fully green GitHub profile).
- **Four levels of progression**: The learning path is Lovable-only → Lovable + Claude Code (via GitHub bridge) → Claude Code + Vercel (inside Cursor IDE) → multi-agent Claude Code with skills, agents, and automation.
- **Level 1 — Lovable**: Start with a personal project (Andre's example: a family vacation home availability manager) to remove risk. Lovable handles auth, databases, and deployment so you never hit unfamiliar infrastructure concepts.
- **Level 2 — Lovable + Claude Code bridge**: Connect both tools to the same GitHub repo. Do coding work in Claude Code desktop app, but use Lovable as a visual QA and infrastructure layer — you can still see product changes and test them without dealing with Vercel or branches. Andre described this as an "accidental jobs-to-be-done" use of Lovable.
- **Level 3 — Claude Code + Vercel (inside Cursor)**: Move off Lovable when you want multiple branches/sessions running in parallel. Vercel provides preview URLs per branch so you can QA before merging to main. Cursor adds a vertical tab UI for sessions (epics) that is easier for non-technical people to parse than the Claude Code desktop app alone. Cursor's free plan also lets you use its agent to debug Claude Code issues.
- **Level 4 — Multi-agent infrastructure (the "machine that builds the machine")**: Build a CLAUDE.md (values/rules), an agents folder, and a skills folder. Andre's agent hierarchy: PM Orchestrator → calls Researcher, Discovery, Designer, Engineer, Implementer agents. The PM orchestrator never writes code itself — it only routes to other agents.
- **CLAUDE.md as team culture**: Every session loads CLAUDE.md automatically. Andre's rule #1: "For every task, call the PM agent." This means he never has to manually invoke it — the architecture does it for him.
- **Agent improvement loop**: When a feature comes out wrong, the correct instinct is NOT to ask Claude to fix it directly. Instead, identify which agent or skill in the pipeline failed, fix that, and re-run the whole pipeline. This prevents recurring errors and continuously upgrades the machine.
- **AI-native team velocity pattern**: Small teams (2–3 people) spend ~50% of time improving the agent infrastructure, not tweaking individual features. Each specialist improves their own domain agent: the engineer improves the engineer agent, the designer improves the designer agent, etc. — creating a compounding acceleration.
- **Shared skills repo**: Andre pushes agent/skill updates to a shared team repository and sends a Slack notification when it updates, so all teammates can pull the latest standards.
- **Avoiding slop — two mechanisms**: (1) Security/infra checks on every PR before it hits production — creates friction without blocking building; (2) Problem-side friction via skills (Jobs-to-Be-Done, Opportunity Solution Tree, MoSCoW prioritization) that force thorough problem discovery before any solution work begins.
- **European PM problem**: The majority of European PMs are non-technical "product owners" — glorified delivery managers who act as translators between strategy and engineering. This disempowers entire teams, siloes design/engineering from discovery and go-to-market, and is the structural reason European product culture lags behind US/Asia.
- **Collaboration should be front-loaded and back-loaded, not in the middle**: Most teams waste collaboration on execution dependencies. The right model: heavy collaboration at ideation/discovery and at delivery/enablement, with individual autonomous execution in between.
- **Monday morning action**: Ask an engineer to add you as a collaborator on a low-risk repository, pick the oldest item on the backlog (something that will never get done), and ask Claude Code to build it as a branch. You won't merge it to production — the goal is to see the magic and internalize the new capability.

## Use cases
- A non-technical PM who wants to prototype and ship features without waiting for engineering sprint capacity
- A product owner in a European company trying to escape the "glorified delivery manager" dynamic
- A solo founder or small startup team (2–3 people) needing to move at AI-native speed with minimal headcount
- A PM who has used Lovable but wants to graduate to Claude Code without losing the visual feedback loop
- A PM or designer who wants to contribute directly to a production repository without deep Git/infrastructure knowledge
- A PM building personal tools (family apps, internal trackers) as a low-risk learning environment
- A product leader who wants to set up a team-wide agent infrastructure with shared standards across engineering, design, and PM
- A company evaluating how to restructure squads around AI-native working patterns (full-stack, autonomous pods)
- A PM preparing to go to their engineer on Monday morning with a concrete starting point for collaboration

## Patterns & frameworks

**The Four-Level Builder Progression**
A staged learning path for non-technical PMs: Level 1 (Lovable only), Level 2 (Lovable + Claude Code via GitHub), Level 3 (Claude Code + Vercel inside Cursor), Level 4 (multi-agent Claude Code with skills/agents). Each level adds infrastructure complexity while the previous level's tools are retained as scaffolding during the transition.

**The Lovable-as-Infrastructure Bridge (Level 2 hack)**
An unintended use of Lovable: bootstrap in Lovable, connect it to GitHub, do all coding in Claude Code desktop app, and use Lovable purely as a visual QA and hosting layer. Merges from Claude Code flow through GitHub into Lovable's preview URL. Eliminates the need to deal with Vercel, branches, or deployment during the learning phase.

**The PM Orchestrator Agent pattern**
A CLAUDE.md rule fires the PM agent on every task. The PM agent never writes code — it only reads requirements and routes to specialist sub-agents (Researcher, Discovery, Designer, Engineer, Implementer). This mirrors a real product squad structure, where the PM owns coordination and delegates execution. Andre's recommendation: model your agents on how your actual team works, not on frameworks you copied from LinkedIn.

**The "Machine that Builds the Machine" principle**
Spend ~50% of build time improving the agent infrastructure (CLAUDE.md, agents, skills), not just shipping features. When output is bad, fix the pipeline stage that failed and re-run, rather than patching the output directly. This creates compounding returns: each infrastructure improvement benefits every future feature.

**Front-loaded / Back-loaded Collaboration model**
Collaboration belongs at discovery (problem framing, decision-making) and at delivery (go-to-market, enablement) — not during execution. Current teams invert this, creating drag through execution-time dependencies. Fixing this unlocks autonomous individual execution in the middle phase and eliminates the slowdown caused by mid-build handoffs.

**Two-Layer Slop Prevention**
Layer 1 (output end): infra/security checks on every pull request before production — acts like a senior engineer reviewing a junior's code. Layer 2 (input end): problem-discovery skills (JTBD, Opportunity Solution Tree, MoSCoW) that generate structured PRD artifacts before any solution work begins, forcing sufficient problem definition upfront.

**The Four Jobs framework (referenced from LinkedIn)**
At the founding/squad level, all successful teams reduce to four roles: Commercial (sales/marketing), Product (builds and ships), Technical (reliability, scalability, architecture), and Security/Infra (protects the production pipeline). With AI tools, the product role no longer requires deep technical skill — the infra role compensates by enforcing quality gates on all incoming code.