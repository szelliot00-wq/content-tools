# The GitHub Repo That Runs Her $100M Startup

Video ID: `qsDX0PMKcaE`

## Summary
JZ (Julie Zhuo), Chief Product Officer at Luro (a $100M AI time platform), walks through how Luro has built a company-wide operating system (OS) hosted in GitHub that systematizes AI workflows across every business function — from customer success to finance to engineering. The core argument is that most organizations have a small "1% AI power user" cohort whose workflows and knowledge remain siloed, and the company OS is the mechanism to democratize that capability across the entire org. JZ also covers how Luro's PMs now ship full front-end and back-end features independently using AI coding agents like Devin, and what the future shape of product teams looks like. The video is most relevant to product managers, CPOs, and team leaders at companies trying to move from ad hoc AI experimentation to structured, org-wide AI adoption.

---

## Key insights

- **The "1% problem":** Most organizations have a small group of highly AI-proficient employees tinkering with workflows, while 90–99% of the org doesn't know what tools to use or when. The company OS is designed to close that gap by encoding the 1%'s best practices into shared, accessible skill files.

- **Luro's GitHub-based company OS:** Every business function (customer success, design, engineering, finance, marketing, sales, legal, etc.) has its own folder in a shared GitHub repo. Each folder contains sub-folders for that function's activities, and each activity has a "skill file" — a codified playbook for how to do that task well.

- **Skills surfaced in Claude:** These skill files are uploaded directly into Claude as organizational skills, so any employee can invoke a specific skill (e.g., `/morning briefing product`) without navigating to a separate tool or remembering which agent to call.

- **Daily briefings via Slack:** Customer-facing team members receive an automated morning briefing in Slack showing their calendar, meetings, check-ins, and onboarding sessions — all pre-loaded with relevant skills so they know exactly how to handle each item with AI assistance.

- **Three-step process to build a company OS:**
  1. **Start small** — identify one tedious, repetitive workflow and automate it (e.g., auto-populating a feature request form in Slack that routes, triages, and tickets automatically).
  2. **Build a playbook** — document an entire function's workflow end-to-end (Luro's are ~50–55 pages, drafted quickly with Claude), then identify which parts require humans vs. which can be automated.
  3. **Create a mega-agent** — rather than forcing employees to remember dozens of individual agents, build a single "go-to-market agent" or function-level agent that routes requests to the appropriate sub-agent automatically.

- **PMs shipping front-end AND back-end features:** At Luro, PMs (some with no CS background) use Devin (an agentic AI engineer) to ship full product features end-to-end, including back-end logic. Example: a PM named Nick shipped "temporary initiatives" — a feature with front-end UI, back-end data handling, and integration with project management systems.

- **The "captain" model:** For any given feature or initiative, the person whose core skill set is most critical becomes the "captain" who owns it end-to-end. Architectural changes → engineering captain. Interaction/UX → design captain. Customer/business context → PM captain. The captain decides when to pull in others.

- **Two-track product review process:**
  - **Fast track:** Small, scoped features (like "temporary initiatives" or empty states) can go through a lightweight review — just a Slack channel review and PR check — and ship in a day or less.
  - **Strategy track:** Larger systemic changes (e.g., overhauling how activities are displayed across the entire product) require a full product strategy review and architectural review.

- **The work ontology:** Luro has mapped every business function to an "ontology" — a color-coded map of all tasks that function performs. Green tasks (what they *should* be doing more of, like feature shipping, QA, customer relationship building) are tracked to increase. Tasks that are being automated away (competitive market analysis, synthesizing feedback, stakeholder emails) are flagged to decrease.

- **"Unreasonable hospitality" systematized:** A core Luro value is unreasonable hospitality toward customers. Rather than leaving it as an abstract cultural statement, they've embedded it into the OS — the system surfaces prompts during customer check-ins, pulling relevant Gong transcript insights and suggesting personalized gestures (e.g., engraved passport holders for a customer's first international trip).

- **Dust vs. Claude for agent building:** Luro historically used Dust as an agent-building layer, but JZ notes the gap between specialized tools (Dust, Glean) and native Claude capabilities is closing rapidly. The direction is to consolidate everything into Claude skill files directly.

- **Information overload warning:** JZ tried building many scheduled Claude automations personally and found it became overwhelming. The lesson: don't automate everything — curate what matters and deliver it in one consolidated daily touchpoint rather than many separate automations.

- **AI Operations as a dedicated function:** Luro has an "AI Ops" team — described as the new "Biz Ops" — staffed with people who are intensely curious, relentless about finding efficiencies, and constantly tinkering. Started with one person (Sasha), whose demonstrated value created demand from every other function for their own dedicated AI Ops person.

- **Four levels of AI proficiency (JZ's interview framework):**
  - **Level 1:** Using AI in chat/search mode (ChatGPT, Claude Q&A)
  - **Level 2:** Automating a single workflow
  - **Level 3:** Building internal apps
  - **Level 4:** Building shared apps or shipping to customers/production

- **Interview method — screen share:** JZ asks every candidate (across all functions, not just product) to screen share and show how they actually use AI day-to-day. This immediately separates claimed proficiency from real-world level. Most people who say they're "AI-first" turn out to be Level 1.

- **The shrinking product org:** JZ went from managing hundreds of people to 5 PMs and 4 designers. She argues that adding headcount adds coordination cost and dilutes individual ownership. The ideal future team is lean but not starved — small teams of highly capable, AI-enabled "orchestrators."

- **PM fundamentals haven't changed:** Despite all the tooling revolution, JZ emphasizes that core PM principles — customer proximity, problem-first thinking, knowing why you're building and for whom — are *more* important than ever. What's changed is the speed of execution and the tools to remove coordination overhead.

- **CEO conviction required for transformation:** Luro's transformation was enabled by CEO Ryan's decision to re-architect the entire product and company to be AI-native. JZ acknowledges this level of top-down conviction is necessary, but encourages leaders at every level to drive AI adoption within their own function even without CEO mandate.

---

## Use cases

- **CPOs and VPs of Product** trying to scale AI adoption org-wide rather than leaving it to individual initiative
- **PMs at traditional companies** who want to start shipping to production without relying entirely on engineering bandwidth
- **Team leads in non-technical functions** (customer success, sales, marketing) who want to bring AI tooling to their teams systematically
- **HR and talent leaders** redesigning interview loops to assess real AI proficiency vs. claimed proficiency
- **Operations leaders** considering standing up a dedicated AI Ops function
- **Founders and executives** at pre-AI-native companies trying to understand how to start the transformation (especially the "start small with one workflow" framing)
- **PMs at large enterprises** (e.g., Adobe-era environments) who feel far from this reality and need a roadmap for where to begin
- **Product educators and coaches** updating PM curricula to reflect the AI-native operating model
- **Customer success managers** looking to systematize hospitality, onboarding, and renewal workflows with AI

---

## Patterns & frameworks

**1. The Company OS (Operating System)**
A GitHub-hosted repository organized by business function → activity → skill file. The OS encodes best practices from top AI users and makes them available to the entire org via Claude skills or agent builders. Delivers through existing channels (Slack, email) to minimize friction. Not a static doc — it's a living set of playbooks and automatable skills.

**2. The Four Levels of AI Proficiency**
A maturity model for assessing individuals or organizations:
- L1: Chat/search mode
- L2: Workflow automation
- L3: App building (internal tools)
- L4: Shared apps / shipping to production customers
Used as an interview and org-assessment rubric.

**3. The Work Ontology (Work Map)**
For each business function, every task is mapped and color-coded: tasks to *increase* (human judgment, relationship-building, feature shipping) vs. tasks to *automate* (synthesis, reporting, scheduling, templated comms). Drives decisions about where to build skill files and agents.

**4. The Captain Model**
Every feature or initiative has one "captain" — the person whose core skill (engineering, design, or product judgment) is most critical to that feature's success. The captain owns the work end-to-end, decides when to pull in others, and is accountable for quality and impact. Replaces the traditional waterfall handoff model.

**5. Two-Track Product Review**
- **Fast track:** Small, well-understood features bypass heavy review; go through lightweight async channels (e.g., Slack PR review). Can ship in hours or a day.
- **Strategy track:** Systemic or high-risk changes trigger a formal product strategy review and architectural review.
The key discipline is explicitly sorting features into the right track upfront.

**6. The Mega-Agent / Router Agent Pattern**
Instead of building many discrete agents that employees must remember to invoke individually, build one "meta-agent" per function (e.g., a GTM agent) that routes any request to the appropriate sub-agent. Dramatically reduces the cognitive load of adoption.

**7. The Playbook-to-Skill-File Pipeline**
Start by writing a full operational playbook for a function (~50 pages, now writable in hours with LLMs). Audit the playbook for human-required vs. automatable steps. Convert automatable steps into skill files or agents. Surface them in the OS. This is the core build loop for expanding the company OS.

**8. AI Ops as the New Biz Ops**
Create a dedicated AI Operations function staffed by people who are curious, tinkering, and efficiency-obsessed. One AI Ops person per function (or shared to start) drives adoption faster than making it "everyone's responsibility" — which effectively makes it no one's responsibility.

**9. The "Orchestrator" PM Profile**
The future PM archetype: big-picture strategic thinker *and* detail-oriented executor who can take features from zero to production independently. The valuable PM is neither purely strategic nor purely technical — they're an end-to-end builder with deep customer understanding and business judgment, augmented by AI agents for everything else.