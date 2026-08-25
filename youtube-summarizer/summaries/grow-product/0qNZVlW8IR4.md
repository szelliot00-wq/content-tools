# The Product Builder Playbook (Full Breakdown) | Srini Raghavan | Product Growth

Video ID: `0qNZVlW8IR4`

## Summary
This episode features Srini Raghavan, CPO of Freshworks (a $2.8B employee experience SaaS company with 70,000+ customers), explaining how his team of 200+ has restructured product development around AI. The central argument is that the traditional linear PM → UX Designer → Engineer handoff is obsolete, and that a new "product builder" role — one person who can research, design, and ship — is replacing all three. Raghavan walks through Freshworks' full AI-powered product development life cycle (AI PDLC), demonstrating it live in Cursor, Figma Make, and Claude with MCP connectors. The video is most relevant to CPOs, PMs, and product leaders at established SaaS companies trying to understand how to modernize teams without sacrificing quality or governance.

---

## Key insights

- **The three traditional roles (PM, UX Designer, Engineer) are converging into a single "product builder" role.** AI enables one person to handle research, prototyping, and shipping — Freshworks is already operating this way in pockets of the org.

- **Freshworks' PM-to-engineer ratio has collapsed dramatically.** 18 months ago it was 1 PM to 10–20 engineers plus a UX designer per 2 PMs. Now some teams run at 1 PM to 1 engineer, sometimes with no dedicated UX designer at all.

- **Release cadence dropped from 6 months to 2 weeks**, with Raghavan predicting it may hit 2 days to 1 week within 6 more months. This compression is a direct result of the AI PDLC.

- **The AI PDLC is a 12-phase governed framework**, not a free-form "vibe coding" approach. It runs inside Cursor and produces structured markdown artifacts (idea brief, requirements, knowledge-gathering, competitor analysis, customer feedback, quantitative metrics, dependency analysis, prototype, QA checklist, etc.) in sequence.

- **The PRD Genie drafts ~80% of the PRD almost instantly**, grounded in real data: it queries Freshworks' Databricks data lake (called "Bel") via SQL, pulls competitor benchmarks, surfaces customer feedback, and runs an internal dependency analysis — all automatically.

- **The AI is explicitly a co-pilot, not autopilot.** Raghavan repeatedly emphasizes that PM judgment still matters: choosing which version of a reference to use, catching when the design system isn't applied correctly, noticing a layout breaks on narrow monitors. The value of the PM shifts from operational work to judgment and prompting quality.

- **Hallucination prevention is handled through the initialization process.** The init step loads specific versioned references into the context so the AI knows exactly which design system, product version, and data source to use. This is the key governance mechanism for a company with 75,000 customers and 300 million end users.

- **Freshworks uses Cursor as its primary IDE for both engineers and non-engineers**, chosen for three reasons: accessible to non-technical users, flexible model selection (not everything needs the most powerful LLM), and native Figma MCP integration that lets it read mockups and generate code from them.

- **Figma Make is used for prototyping** because it embeds the Freshworks design system ("Duo"), is familiar to existing UX/PM staff (reducing adoption friction), and connects to external sources like Cursor. The demo showed it building 8 UI modules from a PRD in one session, with multiple rounds of back-and-forth to fix design system adherence and responsive layout issues.

- **The agent studio product** (built for IT/HR use cases) demonstrates the end-state: domain-specific AI agents deployed in Slack or Teams that handle onboarding tasks like software provisioning, health insurance questions, W4 forms, and employment verification letters — reducing multi-email/multi-person workflows to a single chat interaction.

- **The Claude + Fresh Service MCP integration** shows the enterprise IT use case: a single prompt ("fetch all Windows 11 tickets from the last 60 days and generate a root cause analysis") triggers the MCP to pull live ticket data, cluster incidents, identify root causes (kernel driver regression, patch install hangs), generate recommended actions, draft ticket replies, and bulk-send those replies — all within Claude. Raghavan estimates 12 to 24 hours of IT agent work collapsed to ~5 minutes.

- **Grok (specifically Grok 4.5) is Raghavan's current model of choice** for the AI PDLC demo, primarily for speed — steps that might take minutes completed in 10–15 seconds. He also uses Claude Opus 4/4.6 for other tasks.

- **For hiring, Raghavan looks for curiosity and evidence of self-directed building**, not just credentials. He asks candidates to open Cursor and show what they've built — GitHub repos are reviewed. He explicitly says passion can't be taught; skills and technical knowledge can.

- **Cultural change requires leading by example.** Raghavan picked up software development again after 14+ years away, writes more code now than when he was a working engineer, and demos the work himself. He runs monthly product team demo showcases to surface internal champions (the PRD Genie itself was built by a team member who demoed it at one of these sessions).

- **The product job is now framed as three equal thirds:** launching the product, driving adoption, and monetizing it. Shipping more frequently is only valuable if the feedback loop tightens — the goal is to fail fast or succeed more decisively, not just to ship more.

---

## Use cases

- **CPOs/VPs of Product at established SaaS companies** trying to accelerate release cadence without rebuilding the entire org from scratch.
- **PMs who want to reduce time spent on operational PRD work** (research aggregation, competitive analysis, metrics gathering) and redirect it toward strategy and judgment.
- **Product teams building on top of existing products** (not greenfield) where hallucination risk is high and governance matters — the init/grounding approach addresses this directly.
- **IT/HR teams at enterprises** looking to reduce support ticket burden, accelerate employee onboarding, and deploy internal AI agents in Slack or Teams.
- **UX designers and PMs who want to prototype faster** without waiting on engineering cycles — Figma Make + design system integration makes this accessible to non-engineers.
- **Engineering leaders evaluating AI IDE tooling** (Cursor specifically) for mixed technical/non-technical teams.
- **Product leaders hiring AIPMs or "product builders"** who need a framework for assessing capability beyond traditional case interviews.
- **Enterprise IT agents** who spend most of their day triaging and responding to repetitive support tickets — the MCP-connected Claude workflow is directly applicable.
- **Companies building agentic products** who need to think about designing for AI agents as consumers (CLIs, MCPs) in addition to human users.

---

## Patterns & frameworks

**1. The Product Builder Role**
A single person who replaces PM + UX Designer + Engineer by leveraging AI for all three functions. The role's core skill shifts from execution to judgment: choosing references, prompting well, catching AI errors, and thinking strategically. Not yet the norm at large companies, but Raghavan considers it inevitable.

**2. AI PDLC (AI Product Development Life Cycle)**
A 12-phase governed framework that runs inside Cursor. Phases include: idea briefing → requirements → knowledge gathering → competitive analysis → voice of customer → quantitative metrics (SQL queries against data lake) → dependency mapping → visual prototyping → QA. Each phase produces a versioned markdown artifact. The "Prism" system (knowledge hub + context hub + skills repository) underpins it by providing grounded references so the AI doesn't hallucinate.

**3. Data First vs. AI First**
Raghavan's distinction: don't start by jumping into AI tooling. First build the foundations — design systems, coding standards, repositories, data lakes, governed reference libraries. These foundations are what make the AI first approach fast and accurate. Skipping this step is why many AI-generated PRDs or prototypes feel untrustworthy.

**4. PRD Genie**
An internal Cursor-based agent that automates ~80% of PRD creation. It is grounded in: Databricks data lake queries (quantitative metrics), competitive benchmarks, customer feedback, and internal dependency analysis. It produces a structured markdown PRD with problem statement, goals, scope, user stories, functional/non-functional requirements, rollout plan, and pricing recommendations. Includes an automated "CPO Check" step that reviews for strategic alignment, clarity, and edge cases.

**5. The CPO Check**
An AI review step baked into the PRD Genie that mimics what a CPO would look for when reviewing a PRD: strategic alignment, clarity of requirements, and identification of edge cases. Named after Raghavan by his team and now automated into the process.

**6. Init/Grounding Protocol**
Before any AI-assisted build begins, a structured initialization step loads versioned references (design system version, product scaffold, data lake connection, feature context) into the workspace. This is the primary mechanism for preventing hallucination in a production-grade SaaS environment. The init step also creates the directory scaffolding and artifact files the subsequent 12 phases will populate.

**7. Fresh Service Starter Kit + Duo Design System**
A scaffolding approach for prototyping: instead of starting from a blank canvas, Figma Make loads the actual UI shell that 75,000 customers already see. This ensures prototypes are immediately plausible and design-system-compliant, not generic wireframes.

**8. The One-Third Rule for Product Jobs**
Product work is divided into three equal-effort areas: (1) shipping/launching, (2) driving adoption, (3) monetizing. The implication is that faster shipping only pays off if equal attention is given to adoption loops and revenue capture — otherwise velocity doesn't move metrics.

**9. Internal Champion Showcases**
A monthly demo meeting where team members show what they've built with AI tooling. This is how internal innovations (like the PRD Genie) get discovered, validated, and standardized across the org — bottom-up cultural change amplified by top-down visibility.

**10. Hire-to-Retire Agent Model**
A design pattern for enterprise AI agents that covers the full employee lifecycle (joining → day-to-day needs → offboarding) through a single AI agent accessible via Slack or Teams. The agent is backed by: a knowledge base (URLs, policy docs, solution articles), pre-built workflows (password reset, software provisioning, incident creation), a service catalog, and multi-language support — all configurable by an IT/HR admin without engineering involvement.

**11. MCP as an Enterprise Integration Layer**
Model Context Protocol connectors (specifically the Fresh Service MCP) allow Claude to read and write live enterprise data (tickets, knowledge base articles) without that data leaving the customer's environment. The pattern: natural language prompt → MCP fetches context → Claude reasons over it → MCP writes back results (e.g., bulk ticket replies). This collapses multi-person, multi-hour workflows into single-session interactions.