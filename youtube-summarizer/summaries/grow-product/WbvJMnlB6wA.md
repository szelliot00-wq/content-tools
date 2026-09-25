# The Old PM Playbook Just Got Downgraded (Use This)

Video ID: `WbvJMnlB6wA`

## Summary
Wade Foster, CEO and co-founder of Zapier, walks through Zapier's V2 AI fluency rubric (published March 31, 2026) and demonstrates what separates unacceptable, capable, adaptive, and transformative PM work in 2026. The host Akash creates three live PM artifacts — a basic PRD, an improved PRD with a prototype and customer evidence, and a full agentic product factory — and Wade grades each in real time. The core argument is that AI fluency is no longer a differentiator but a baseline expectation, and the real edge comes from combining good product judgment with AI tools, not replacing judgment with AI. The episode is most relevant to product managers, product leaders, and CEOs evaluating or building AI-native workflows.

---

## Key insights

- **AI fluency is now table stakes, not a differentiator.** Using AI for summarization, writing, looking up information, and generating basic PRDs is "capable" at best in 2026 — that bar existed in 2024. Companies like Zapier, Shopify, and many others already grade employees on this.
- **The four-tier rubric: Unacceptable → Capable → Adaptive → Transformative.** Zapier's rubric grades on specific behaviors, not vague impressions. Most of Zapier's PM org operates in the Adaptive range. Transformative is intentionally rare — fewer than 5–10% of PMs, maybe one per team per half.
- **Being 100% transformative is actually counterproductive.** If you are always in transformative mode, you are constantly tweaking systems and not shipping. The goal is to operate mostly at adaptive with occasional transformative experiments.
- **A PRD alone is no longer sufficient.** In 2026, a strong PM artifact includes: (1) a working prototype built with a coding agent, and (2) customer evidence pulled from Gong calls, Zendesk tickets, subreddits, and community forums — ideally synthesized with AI across a large corpus. Both can now be done in hours, not weeks.
- **Prototypes are non-negotiable at the adaptive level.** "Seeing is believing, and a prototype is a picture times ten." A PM who cannot build a prototype because of technical skill is no longer a valid excuse — coding agents close that gap.
- **Customer evidence at scale is a new baseline expectation.** In the live demo, Akash added data from 47 Gong calls (agent tooling came up unprompted in 34 of 47), 312 Zendesk tickets tagged MCP/AI agent, 1,800+ Discord posts mentioning MCP, and 9 design partner interviews. This level of synthesis was previously a multi-week effort; with AI it takes hours.
- **The "slop cannon vs. turbo brain" framework (Dan Hawinmire, Fair).** Good judgment + AI = turbo brain. Poor judgment + AI = slop cannon. Wade endorses this. He adds that the slop cannon is actually harder to manage than someone who uses no AI at all — they generate so much low-quality output that it creates work for everyone around them.
- **You can share AI-assisted work at varying quality levels — but you must be transparent.** Wade describes a workplace etiquette emerging at Zapier: when sharing a doc, signal the review level. "I skimmed it, removed obvious errors, sharing for speed" vs. "I stand behind every sentence." Passing off unreviewed AI output as polished work is the key offense.
- **The accountability rule: "You can delegate the work, but you can't delegate the accountability."** This is Zapier's internal line on AI slop. The human is still responsible for the output, regardless of how much AI generated it.
- **Transformative PMs build product factories, not features.** The third artifact demonstrated a five-layer agent architecture: skills layer (PRD, eval, recall, etc.), orchestration layer (sub-agents for engineering, design, legal, UX, skeptic), tools/MCP layer (Zendesk, Gong, Reddit, Amplitude, Linear, Figma, GitHub), deterministic enforcement layer (rejects memory writes without sourced evidence), and a memory layer. A nightly "triage swarm" deduplicates and clusters customer signals, flags contradictions against existing bets, and auto-generates PRDs, prototypes, evals, and code draft PRs. Human gates are at: (1) do we care about this build chain? and (2) do we merge it? Wade rated this solidly transformative.
- **The PM's job is shifting to auditing the factory, not running each machine.** Wade's factory analogy: when a widget fails, you don't fix individual widgets — you fix the machine. Similarly, PMs running agentic systems are increasingly responsible for auditing when and why the system fails, not doing each task manually.
- **The CEO should be behind the PM on AI fluency in their specific domain.** If a CEO can spot things the PM missed, that's a warning sign. Domain specialists should be further ahead than generalist leaders. Wade rates himself as adaptive, not transformative.
- **Zapier's strategic response to "no code apocalypse": the new no code is code.** Agents write the code; humans never look at it. Zapier's value is providing a deterministic runtime for those agent-generated workflows — reliable, low-token-cost execution vs. the clunkiness of local agent loops.
- **The future of B2B SaaS is headless.** The user of your software is increasingly an agent, not a human. Salesforce is explicitly going headless. If your SaaS cannot be run headless via APIs and MCP servers, you are swimming against the current.
- **Wade's personal agent stack as a CEO:**
  - *Morning brief* (6am): Pulls calendar, inbox, Slack, to-do list — runs deterministically on Zapier, only burns tokens on the summarization step.
  - *Scribe/Daily recap* (5pm): Loops over outstanding emails, Slack saves, and Granola meeting transcripts; drafts follow-up emails and populates to-do list. Cut end-of-day admin from ~2 hours to ~15 minutes.
  - *Exec/board agenda generator*: Loops over weekly meetings, Slack, email, and AI chat sessions; surfaces the most important unresolved topics. Prevents pet agenda items from crowding out genuinely urgent issues.
  - *CEO CRM*: Runs every Saturday night; drafts 10–20 personalized outreach emails to enterprise customers based on renewal signals, usage trends, and relationship recency. Enables CEO-level customer relationships at scale that would otherwise fall to CSMs.
- **Zapier's competitive moat: 9,000+ integrations and deterministic runtime.** No competitor has matched the integration breadth built over 15 years. The differentiation in the agent era is running automations reliably and cheaply — not burning tokens on tasks that can be handled deterministically.

---

## Use cases

- **Individual PMs** who want to understand what "adaptive" vs. "transformative" AI fluency looks like in practice, with concrete artifact examples.
- **Product leaders and managers** who need to evaluate PM performance on AI fluency and want a rubric they can adapt or borrow.
- **PMs preparing performance reviews** or self-assessments at companies that have adopted AI fluency grading.
- **PMs writing PRDs** who want to know what evidence and prototype standards are now expected before bringing an idea to leadership.
- **CEOs and founders** evaluating their own AI fluency relative to their team and learning practical personal agent setups (morning brief, daily recap, CRM outreach).
- **SaaS product teams** deciding whether and how to expose their platform via MCP servers or headless APIs to remain relevant as agents become the primary users.
- **Teams experiencing internal "AI slop"** who need a framework and etiquette for managing low-quality AI-generated output and setting expectations on review levels.
- **PMs at large companies (30+ PMs)** deciding how to distribute the responsibility of building agentic systems — not everyone needs to build the factory; most need to learn to run it.
- **No-code/low-code product builders** reconsidering their architecture in light of the shift toward agent-native, headless platforms.

---

## Patterns & frameworks

**1. The Zapier AI Fluency Rubric (V2, March 2026)**
Four tiers applied per role (PM, engineer, marketer, etc.):
- *Unacceptable*: Below the hiring bar.
- *Capable*: AI used for summarization, writing, basic PRDs, simple lookups. Table stakes in 2026.
- *Adaptive*: Structured approach to spec/prototype generation; using AI to synthesize large customer data sets; generating multiple working solutions rapidly; stretching into adjacent roles (data, marketing, sales) at 80–90% competency.
- *Transformative*: Building agent pipelines that replace manual workflows; systems thinking over feature thinking; operating like a "product factory"; first-of-kind approaches that shift how the whole team works.

**2. Slop Cannon vs. Turbo Brain (Dan Hawinmire, Fair)**
A 2x2 mental model:
- Good judgment + AI = Turbo Brain (multiplicative force)
- Poor judgment + AI = Slop Cannon (generates high volumes of low-quality output, harder to manage than someone not using AI at all)
- Good judgment + no AI = Slow but solid
- Poor judgment + no AI = Quiet underperformer (at least manageable)
Takeaway: AI is a multiplier on judgment, not a substitute for it.

**3. The "Delegate Work, Not Accountability" Rule**
Zapier's internal line on AI slop. Using AI to produce output is fine; failing to own the quality of that output is not. You are still accountable for everything that leaves your name on it.

**4. Transparency Signaling for AI-Assisted Work**
An emerging workplace etiquette pattern at Zapier. When sharing AI-assisted documents, explicitly state the review level:
- "AI-drafted, quick skim only, sharing for speed"
- "AI-drafted, I've reviewed key claims"
- "I stand behind every sentence"
This prevents the most damaging pattern: passing off unreviewed AI output as polished work, which transfers judgment burden to the reader.

**5. The Product Factory Architecture (Five-Layer Agentic Stack)**
A transformative PM system design:
1. *Skills layer*: Reusable agent prompts for recurring PM tasks (PRD, eval, launch checklist, weekly review, etc.)
2. *Orchestration layer*: Sub-agents fanning out in parallel across functions (engineering, design, legal, UX, skeptic)
3. *Tools/MCP layer*: Integrations with Zendesk, Gong, Reddit, Amplitude, Linear, Figma, GitHub
4. *Deterministic enforcement layer*: Rejects memory writes without sourced evidence; flags destructive actions
5. *Memory layer*: Sourced, structured knowledge base accumulating hypotheses, decisions, research, and stakeholder signals

Paired with a nightly triage swarm (cron job) that deduplicates signals, tags observations vs. hypotheses, matches against open bets, and flags contradictions. Human gates at: (1) approve build chain, (2) approve merge.

**6. Deterministic Wrapper Pattern**
Use a reliable runtime (e.g., Zapier) to wrap agentic workflows so they run on a schedule, at low token cost, without keeping a laptop open. Reserve AI inference only for the steps that genuinely require reasoning; handle data fetching, routing, and posting with deterministic code. Gives the reliability of traditional automation with the intelligence of agents where needed.

**7. The "CEO Should Be Behind the PM" Rule of Thumb**
A domain specialist should have deeper AI fluency in their specific role than a generalist leader. If the CEO can spot AI fluency gaps the PM cannot, that is a performance signal. Specialists are expected to be ahead of generalists in their domain.