# Stop Building AI Agents. Build AI Employees Instead (Live Demo) | Pedro Franceschi

Video ID: `LE0LNULrsEM`

## Summary
Pedro Franceschi, co-founder and CEO of Brex, argues that companies should build "virtual employees" — narrow, persona-driven AI agents with defined roles — rather than open-ended general-purpose agents. He demonstrates this philosophy through Jim (an AI recruiter), Crab Trap (an open-source agent security proxy), Magpie (an internal AI cost analytics tool), and his personal "Autopilot" system. The video covers how Brex has restructured its PM function, how it secures and monitors agentic systems in production, and how token spend will increasingly replace headcount as a major company cost. It is most relevant to founders, PMs, engineering leaders, and anyone building or deploying AI agents inside an organization.

---

## Key insights

- **"Virtual employees" over open-ended agents:** The key design principle is building AI that looks, feels, and behaves like a real person with a specific role — not a general assistant. This makes the agent more trustworthy, measurable, and useful to non-technical teams.
- **Jim, the AI recruiter, does three things:** (1) sources candidates from LinkedIn, GitHub, Twitter, and other data sources, (2) filters all inbound applicants by scoring them against role-specific criteria, and (3) acts as an analytics layer so recruiters can query hiring data conversationally in Slack instead of navigating Greenhouse.
- **Jim has a self-improvement loop:** It identifies steps in the recruiting process that could be further automated and surfaces them as suggestions, which a human can then approve and implement.
- **Agreement rate monitoring:** Brex tracks where Jim and human recruiters disagree — e.g., candidates Jim flagged as standouts that recruiters ignored, or candidates Jim rejected that recruiters passed — as a quality signal for both the agent and the humans.
- **Crab Trap secures agents at the network boundary:** Rather than trying to constrain agents via prompt engineering or tool restrictions alone, Brex built an HTTP proxy (open source) that intercepts all network traffic from an agent. It applies a mix of static allow/block rules and LLM-as-judge reasoning on every request to enforce a policy.
- **Policy auto-generation from traffic replay:** Crab Trap can observe an agent's historical HTTP traffic and use an LLM to auto-generate a security policy — e.g., "Jim can read GitHub profiles but cannot push to repos or delete anything." This removes the burden of writing policies from scratch.
- **Magpie tracks token spend with three pillars:** Corporate AI (internal productivity tools), Operational AI (customer-facing automation), and Product AI (AI features in the Brex product). Each can be drilled into by caller, model, use case, cost per call, and cost per customer.
- **Token costs are surfacing surprising variance:** Example given — transaction tagging costs ~10 cents/call while dispute handling costs ~$2/call, a 240x difference. Without granular analytics, this is invisible.
- **Reconciling token usage to actual bank spend:** Because Brex is both the card and the financial rail, they can tie token consumption data directly to dollars leaving a company's account — a uniquely grounded view of AI ROI that they plan to productize for Brex customers.
- **PM role at Brex is more GTM bridge than product designer:** PMs spend less time on product craft and more time synthesizing signals from sales, Gong calls, RFPs, and customer conversations to identify which problems are worth solving. AI helps make sense of large volumes of unstructured data (e.g., six months of Gong calls) to surface insights quickly.
- **Two review types at Brex:** Problem alignment (is this the right problem?) and solution alignment (is this the right solution?). The company maintains a shared repo of PM skills/prompts that pre-processes submissions before they reach a human reviewer.
- **"Manage the work, not the people":** Pedro's management philosophy. Reviews focus on the artifact, not the person. He estimates he spends ~50% of his time reviewing work directly, which he sees as how quality standards propagate through a company ("case law" system).
- **Engineering interviews now test AI proficiency:** Brex's interview loop requires candidates to build something. If a candidate can't use AI tools to move fast, they fail — because the tasks are too large to complete manually without AI.
- **Open source contributions are a positive signal but not a requirement:** Absence of open source work is not a negative signal in Brex's hiring process.
- **Pedro's "Autopilot" personal system:** An OpenAI Codex harness that reads Slack, email, and meeting notes; maps signals to named "people" and "programs" (markdown files); and auto-generates tasks, draft replies, and status summaries. Everything is stored as markdown committed to a repo with a thin UI layer on top.
- **Token budgets: go deep first, optimize later:** Brex gave engineers essentially unlimited token budgets early on to drive adoption, then built analytics tools to optimize later. Pedro argues trying to control costs before understanding usage patterns is premature and counterproductive.
- **The SaaS business model is shifting:** The new model is selling the *work* (outcomes), not the software. AI products are fundamentally an agentic loop plus a set of tools — the differentiator is how well you define and solve the problem, not the software wrapper.
- **World adoption is still extremely early:** Pedro references a visualization of 2,500 boxes (each = 3.2M people) where almost all boxes are red (never used AI), a tiny orange slice pays for AI subscriptions, and an even tinier sliver uses agents effectively. Most companies have not yet gone through the transformation.

---

## Use cases

- **Recruiting teams** wanting to reduce time in ATS UIs like Greenhouse and get conversational access to candidate pipeline data.
- **Founders and small teams** evaluating whether to hire headcount vs. build an AI agent for a recurring operational role.
- **Engineering and platform teams** deploying AI agents in production who need a security and cost governance layer.
- **Product managers** looking to modernize how they ingest customer signals (Gong calls, RFPs, support tickets) and prioritize work.
- **Finance and ops teams** at companies with significant AI spend who need visibility into where tokens are being consumed and why costs are drifting.
- **Executives** who want a personal system to aggregate signals from Slack, email, and meetings into a single action-item and status view.
- **Companies evaluating multi-model strategies** who need a vendor-neutral layer to track spend across Anthropic, OpenAI, Bedrock, Cursor, Codex, etc.
- **Anyone building AI products** who wants a framework for pricing — moving from per-seat SaaS to outcome/token-based models.

---

## Patterns & frameworks

**Virtual Employee Pattern**
Build AI agents as named, persona-driven entities with a specific job description rather than general-purpose tools. Give them a Slack presence, a profile, and a defined set of 2–4 responsibilities. This makes adoption easier for non-technical teams and creates clearer accountability and measurement surfaces.

**Three-Stage Agent Pipeline (Jim)**
1. Sync external systems (e.g., ATS, LinkedIn, GitHub) to build a rich candidate profile.
2. Evaluate every record against role-specific, configurable criteria using an LLM judge.
3. Surface results conversationally (Slack) and analytically (web UI with filtering, scoring, and metrics).

**Network-Boundary Agent Security (Crab Trap)**
Rather than constraining agent behavior at the prompt or tool level, place an HTTP proxy between the agent and the internet. Apply static rules for clearly allowed/blocked actions, and route ambiguous requests through an LLM judge evaluated against a plain-language policy. Auto-generate the initial policy by replaying the agent's observed traffic.

**Three-Pillar Token Analytics (Magpie)**
Segment AI spend into: (1) Corporate AI (internal productivity), (2) Operational AI (customer-serving automation), (3) Product AI (shipped features). Drill down by caller, model, cost per call, and cost per customer to identify drift and optimization opportunities. Ground usage data in actual financial transactions for a reconciled view of ROI.

**Problem Alignment / Solution Alignment Reviews**
Two-stage review process: first align on whether the problem is worth solving (problem alignment), then review the proposed solution (solution alignment). Maintain a shared skills/prompt repo that auto-processes submissions before human review, so reviewers spend time on idiosyncratic judgment rather than repeatable checks.

**Signal → Program → Action (Autopilot)**
Personal productivity system: define a set of "programs" (strategic initiatives) and "people" (key collaborators) as markdown files. Run a continuous signal collector across Slack, email, and meeting notes. Map signals to programs/people, auto-update status files, generate draft action items and replies. Everything stored as plain markdown in a git repo.

**Adopt First, Optimize Later (Token Budget Philosophy)**
Grant broad/unlimited AI access early to drive adoption and build intuition about usage patterns. Only after establishing a baseline and analytics layer should you introduce targeted cost controls — surgical cuts informed by data rather than blanket restrictions that suppress productivity.