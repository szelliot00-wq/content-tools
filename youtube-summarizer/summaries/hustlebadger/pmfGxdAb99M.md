# Getting ROI on your AI roll out

Video ID: `pmfGxdAb99M`

## Summary
Gabe, a former food-delivery CEO turned AI implementation consultant, presents a practical framework for achieving ROI from AI adoption rather than joining the 95% of AI pilots that fail (per an MIT study). His core argument is that AI rollout is 70% change management and 30% technology, and that most organizations fail because they chase complex, exciting use cases before solving embarrassingly simple, high-value manual processes hiding "below the surface." The talk is most relevant to business leaders, product managers, and AI champions in mid-to-large organizations who are early in their AI journey and need a structured way to identify, prioritize, and pilot AI use cases.

## Key insights
- **95% of AI pilots are abandoned** without producing ROI, primarily because they are poorly defined or too ambitious from the start.
- **AI adoption is 70% change management, 30% technology.** Building the right system means nothing if people don't use it or use it poorly.
- **The "water level" metaphor:** AI capabilities are a rising tide. Many problems your organization faces are already solved by existing AI — you don't need to chase the latest models. The question is whether your org is even covering proven, well-documented use cases.
- **The hammer problem:** Organizations that get excited about AI try to solve everything with it, leading to disillusionment. The real value sits in the overlap between what AI is genuinely good at and what actually has business value.
- **The most valuable use cases are often "embarrassing" ones** — manual, unglamorous processes that nobody even thinks to flag. Example: a top salesperson spending 3–4 hours every Friday copying Excel cells into a Word template, costing ~£10,000/year alone. When surfaced, similar problems often cascade across the org.
- **Finance departments are universally underautomated.** Every client Gabe has worked with had meaningful automation opportunities in finance, even those with full SAP/ERP setups — because there is always heavy manual copy-pasting around those systems.
- **AI is genuinely bad at:** precise financial calculations (LLMs are language models, not math engines), high-accuracy deterministic tasks (AI is non-deterministic by architecture — the same prompt gives different answers each time), and analyzing complex existing Excel files.
- **AI is genuinely good at:** text and image manipulation, document extraction and matching, categorization, summarization, generating process maps, and handling unstructured inputs.
- **Not everything needs AI** — many processes can be automated with deterministic rule-based code. The goal is business value, not AI for its own sake.
- **Start at the "assistant" level**, not the "agent" level. The progression is: Assistant → Co-pilot → Autopilot → Agent. Most orgs try to build agents before they've even documented the process, which is a recipe for failure.
- **ROI thresholds to use as filters:**
  - Personal productivity: minimum ~£10,000/year saved
  - Team/department level: ~£50,000–£100,000/year
  - Organizational transformation: £1,000,000+/year
  - Gabe won't take on a project with less than a **3x return on investment.**
- **AI costs scale with usage** (token-based pricing), unlike traditional software where adding users barely moves infrastructure costs. This makes ROI math critical upfront.
- **"Phantom savings" problem:** Saving people time only translates to business value if leadership agrees in advance what those people will do with the reclaimed time. Otherwise the saving evaporates.
- **Change management requires addressing fear directly.** In AI training sessions, detractors should be invited to voice concerns rather than ignored. Suppressing fear causes people to "live in their own heads" and block initiatives.
- **Track adoption metrics**, not just deployment. For tools like Copilot, monitor weekly/daily active users and how many people are creating agents or custom GPTs — individual-level dashboards are available on higher tiers.
- **Hallucinations are manageable** through "evals" (evaluation frameworks): define test cases *before* building the solution, run AI-graded or human-graded tests continuously, and don't promote to pilot/production until the solution passes. Bad hallucinations usually stem from bad design, not just inherent model limitations.
- **Data security options** range from contractual zero-data-retention agreements with cloud providers, to EU-sovereign processing, to running local models on ~£4,000 on-premise machines that never touch the internet — sufficient for many use cases that don't require frontier models.
- **Upper management in the US spends a net ~3 months per year** on reporting and communicating reports — tasks that are highly automatable.

## Use cases
- **Insurance/underwriting teams:** Automating manual review of cyber security findings and underwriting documents.
- **Finance and procurement departments:** Eliminating manual copy-paste workflows around ERP/SAP systems, invoice processing, purchase order matching, bank reconciliation, and intercompany charges.
- **HR teams:** Automated CV/resume parsing and categorization (not hiring decisions), onboarding document generation, standard contract generation.
- **Sales operations:** Automating repetitive data transfer tasks (e.g., Excel-to-Word report generation for key accounts).
- **Broker/client communication teams:** Triaging and partially automating responses to high-volume inbound queries from brokers or customers.
- **Customer feedback analysis:** Identifying trends across large volumes of unstructured customer feedback.
- **Compliance and legal teams:** Searching 6,000+ contracts for specific clause wording without manual review.
- **Warehouse/operations:** Digitizing and OCR-processing legacy scanned documents; mapping undocumented processes by recording verbal descriptions and generating process maps via AI.
- **Recruiting:** Processing 100+ daily email job applications (varied formats: PDFs, Word docs, images) into structured, assessable tables with automated pass/fail emails.
- **Any organization in a regulated industry** needing internal document search without sending data to external providers — solvable with vector databases and locally-run models.

## Patterns & frameworks

**The Water Level Model**
A metaphor for AI capability versus organizational adoption. AI capabilities are a rising water level — many business problems are already "submerged" (solved). The model has four layers below the surface: (1) Coordination/personal productivity (obvious, easiest), (2) Manual operations (the richest vein — unglamorous, often hidden, "embarrassing"), (3) Silo-breaking and handover automation (more complex), (4) Organizational transformation. Most organizations focus on the top layers or jump to the bottom, skipping the most valuable middle layer.

**The Overlap Framework (Value × AI Capability)**
A two-axis filter: things AI can do vs. things that actually create business value. The real opportunities live only in the intersection. Fun AI use cases (e.g., generating images) with low business value are traps. High-value processes that AI can't reliably handle (e.g., precise financial modeling) are also out of scope.

**Pain Point Definition Template**
A structured one-pager for each candidate use case: (1) Define the pain point in plain language, (2) Identify what AI capability it likely uses (extraction, matching, summarization, etc.), (3) Describe how AI is expected to solve it. Requires zero technical knowledge and can filter good ideas from bad ones quickly.

**The Three-Bucket Prioritization System**
Categorize all generated use case ideas into three buckets by scale of impact: Personal Productivity (target: £10K+/year), Team/Department (£50K–£100K+/year), and Organizational Transformation (£1M+/year). Helps leadership align on thresholds and prevents vanity projects from consuming resources.

**ROI Calculator Formula**
Annual salary ÷ 250 working days = daily rate → daily rate ÷ hours worked = hourly rate → multiply by hours saved per week × number of people affected × 52 weeks. Gabe requires a minimum 3x return before taking on a project.

**The Automation Maturity Ladder**
Four stages for deploying AI solutions, always entered from the bottom: (1) Assistant — a custom GPT/project prompt, no integration needed, testable in 10 minutes; (2) Co-pilot — AI used alongside work; (3) Autopilot — integrated into a process, handles most cases; (4) Agent — autonomous problem-solving with edge-case handling. Starting at the agent level is the single most common mistake.

**Atomic Use Case Scorecard**
A structured scoring tool for each candidate use case with fields: solution name, problem dimension, expected value, solution type, and data sources used. Plotting feasibility vs. impact on a coordinate system reveals which use cases to tackle first — prioritize high-feasibility, moderate-impact projects for early wins over high-impact but complex ones.

**Eval (Evaluation) Framework for Hallucination Control**
Before building: define specific test cases and failure criteria. During build: continuously test the solution against those cases. Gate on results: solution cannot proceed to pilot or production until it passes all predefined evals. Some evals can themselves be AI-graded (one model grades another's output).