# AI-Native Product Team Masterclass: Tools, Roles, ADLC, Roadmap

Video ID: `_jBa_YEobGI`

## Summary
This episode features Jes Rajan, who leads a 700-person AI engineering org at Salesforce responsible for Agent Force, discussing how to build a truly AI-native product organization. He presents a four-layer "recipe" for AI-native transformation: tools, roles, the Agent Development Life Cycle (ADLC), and roadmap/planning. The conversation covers how traditional PM/designer/engineer boundaries are blurring, what new skills matter most, and the common mistakes companies make when adopting agentic AI. It is most relevant to product managers, engineering leaders, and executives navigating the shift to AI-native ways of working.

---

## Key insights

- **Tools layer — let best practices emerge organically:** Salesforce started with Cursor, then shifted toward Claude Code as engineers self-selected it. Rather than mandating a single tool, Rajan gives teams access to multiple options, watches adoption data, and lets best practices surface from real usage. The only constraint is that every tool must pass security review first.
- **Slack as the operating system:** 50–60% of work now happens in Slack. It is the primary async interface, holds longitudinal context ("gold dust"), enables serendipitous discovery across public channels, and can orchestrate agents (Slackbot, Slack Code) directly in threads. Customers are brought in via Slack Connect for real-time co-creation.
- **Headless Salesforce / Claude Force:** Salesforce's value was always in its metadata and business logic, not the UI. "Headless" means those APIs are now accessible through Claude, letting customers build bespoke interfaces powered by decades of Salesforce workflows — 70% close-probability sales flows, 80% ticket-resolution flows — without being locked into the original UI.
- **Determinism problem with LLMs:** Moving pipelines into probabilistic tools creates a risk (you can't have two pipeline numbers). The solution at Salesforce is "Agent Script" — a language that transpiles plain-English agent descriptions into structured tool calls, context lookups, and API calls. This massively reduces hallucination by routing deterministic tasks to deterministic APIs rather than generating code on the fly.
- **Eval-first culture is the key cultural shift:** Data science teams are naturally "eval native" — they think probabilistically and tie test cases to outcomes. Engineering teams historically operated in a deterministic world. The biggest internal transformation Rajan is seeing is engineering teams adopting an eval-first mindset: custom scorers (using LLMs and other models), golden datasets, and outcome-tied metrics — not generic tests.
- **Roles are converging, not disappearing:** The PM/designer/engineer triad still exists as a scrum unit, but the tools let each role operate in the others' domains. Engineers can prototype and get customer feedback without a PM middleman; PMs can build prototypes in Slack without waiting for an engineer. Ratios haven't changed much yet, but job descriptions are expanding.
- **The two new must-have PM skills:** (1) AI prototyping — building quick mockups directly in tools like Slack or Claude to get customer feedback before involving designers or engineers. (2) AI evals — defining golden datasets, scoring rubrics (what a 10/10 output looks like vs. a 6/10), and setting the quality bar for agents.
- **What to look for when hiring an AI PM:** Agency (bias toward action without being told what to do), being "agent-native" (default to teaching an agent to do a task rather than doing it yourself), craftsmanship skepticism (not accepting AI slop — attention to detail, putting your name on output), and the ability to translate skepticism into concrete eval test cases.
- **Forward deployed engineers/PMs:** These roles exist because technology is diffusing faster than customers can absorb it. FDEs immerse in customer problems, build custom solutions with them, and feed insights back to the core product team to decide what becomes a universal product feature. It is rapid prototyping at the customer layer.
- **ADLC inner loop vs. outer loop:** The inner loop is idea → build → deploy. The outer loop is everything that happens after an agent goes live: evaluation in production, detecting drift, updating the agent, and eventually self-healing. Salesforce's "Optimization Agent" watches all running Agent Force agents in an org and identifies opportunities to refine prompts or add context.
- **Model substrate instability accelerates the need for ADLC:** Unlike databases (SQL hasn't changed in decades), the model layer is evolving rapidly. Every new Claude version means previously well-tuned agents may need to be re-evaluated and simplified. Without ADLC (test cases, evals, observability), upgrading models is terrifying; with it, you can move fast.
- **Tech debt is still the PM's problem:** Even in an AI-native world, tech debt slows teams down invisibly. Every engineer fixing old problems is not shipping new customer value. Agents can now help with code review and PR quality, but PMs must still track and prioritize paying down debt.
- **Implementation advice — start simple, minimize variables:** The biggest mistake in AI adoption is launching a "full company transformation." Instead: pick your hardest problem, define clear ROI metrics, build one end-to-end success, then expand. Lock down the simplest architecture first (Occam's Razor), then optimize. Example: a European recruiting firm started with text-based pre-screening in 17 languages, got it right, then expanded to voice.

---

## Use cases

- **PMs transitioning to AI PM roles** who need to understand what new skills (prototyping, evals) are actually required and why.
- **Engineering leaders** deciding how to introduce and govern AI coding tools (Cursor, Claude Code, Codex) across their org without over-prescribing.
- **Executives setting AI strategy** who need a layered framework (tools → roles → lifecycle → roadmap) for sequencing their AI-native transformation.
- **Product teams building agents** who need to understand what an ADLC looks like in practice vs. a traditional SDLC.
- **Teams migrating from Microsoft Teams to Slack** trying to understand what the operational unlock actually is and how to set it up.
- **Companies adopting Agent Force or similar platforms** who want to avoid the common mistake of over-scoping their first implementation.
- **Forward deployed engineers and PMs** trying to understand how their role fits into the broader product development cycle and how customer feedback flows back to roadmap.
- **Hiring managers** building AI-native product teams who need concrete interview signals beyond just "knows AI tools."
- **Organizations upgrading LLM model versions** who need to understand why evals are essential before making those swaps in production.

---

## Patterns & frameworks

**The AI-Native Recipe (4-Layer Pyramid)**
A hierarchical model for becoming AI-native. Bottom layer is **Tools** (access, adoption, security governance). Second layer is **Roles** (blurring PM/designer/engineer boundaries, new skill sets). Third layer is **ADLC** (the lifecycle for building and operating agents). Top layer is **Roadmap/Planning** (taste + customer feedback + FDE signals feeding continuous strategy). Each layer must be in place before the one above it is effective.

**ADLC — Agent Development Life Cycle**
An analogue to the SDLC specifically for agentic software. Five stages: (1) Build, (2) Test, (3) Evaluate, (4) Deploy, (5) Observe/self-heal in production. The key difference from SDLC is that the substrate (the model) itself changes rapidly, so eval infrastructure is not optional — it is what allows you to safely upgrade models and catch drift. Includes an **inner loop** (idea → ship) and an **outer loop** (live agent → evaluate → update → optimize).

**Eval-First Mindset**
A cultural and operational pattern borrowed from data science teams. Instead of writing deterministic unit tests, you define outcome-tied test cases, build custom scorers (LLM-based and rule-based), establish golden datasets, and score outputs against expected quality levels. Applied to both agent behavior and code quality. The key insight: systems built on data will drift because data drifts — evals catch that drift before it compounds.

**Agent Script (Salesforce)**
A domain-specific language that transpiles plain-English agent descriptions into structured tool calls, context lookups, and API references. Its purpose is to inject determinism into an otherwise probabilistic LLM system — routing factual, transactional queries to known APIs rather than asking the LLM to generate answers from scratch.

**Inner Loop / Outer Loop (Agent Lifecycle)**
Two distinct development cycles. The **inner loop** is the team-facing cycle: conjure an idea, work with customers to validate, build, deploy. The **outer loop** is the customer-facing cycle post-deployment: monitor live behavior, detect drift, optimize prompts/context, eventually enable self-healing. Most SDLC tooling covers only the inner loop; ADLC tooling is what operationalizes the outer loop.

**Start Simple, Then Scale (Implementation Pattern)**
A sequenced adoption approach: (1) identify your hardest problem, (2) define clear value and ROI metrics upfront, (3) build one complete end-to-end success with minimal architectural variables (Occam's Razor applied to agent design), (4) learn, refine, and then expand wall-to-wall. Contrasted with the failure pattern of launching a broad company-wide transformation simultaneously.

**Democratic Tool Access + Emergent Best Practices**
An organizational pattern for tool governance: provide broad access (subject to security review), observe what the best engineers and PMs naturally gravitate toward, let best practices crystallize from real usage, then codify and promote those practices. Avoids the brittleness of top-down mandates in a rapidly shifting tool landscape. The mental model is "hug the tangent of the slope" — don't just know where you are, anticipate the direction of change.