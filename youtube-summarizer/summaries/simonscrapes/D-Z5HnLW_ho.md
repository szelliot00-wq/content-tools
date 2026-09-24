# Every Jev Concept Explained (use with Claude)

Video ID: `D-Z5HnLW_ho`

## Summary
This video explains Jev, a "judgment model" by TypeSafe, which converts messy unstructured inputs (like customer emails) into calibrated probability scores that software can act on deterministically. Unlike traditional LLMs (Claude, GPT), Jev never writes text — it only returns numbers representing confidence levels, making it 40–1,000x cheaper and 20–400x faster than chat models for bulk classification tasks. The core argument is that Jev doesn't replace Claude but works alongside it: Jev handles fast, high-volume triage and routing decisions while Claude handles reasoning, writing, and conversation. The video is most relevant to developers and product managers building AI-powered workflows involving large-scale data processing, routing, or classification.

---

## Key insights

- **Jev is a "judgment model," not an LLM.** It cannot write, chat, or explain itself. It only returns probabilities, categories, or scores against criteria you define. TypeSafe calls it a "System 1" model (fast gut-call) vs. Claude being "System 2" (slow reasoning).
- **Three output types:**
  - **Null (Yes/No):** Returns a probability 0–1. E.g., "Is this customer angry?" → 0.9 means 90% likely yes. No confidence score returned.
  - **Choice:** Returns a probability for each predefined category. E.g., "Which team handles this — billing, technical, sales?" → billing: 0.85, technical: 0.10, sales: 0.05. Also returns a **confidence** score based on how spread out the probabilities are.
  - **Score:** Ordered scale described in words. E.g., "How angry is this customer?" on a calm → annoyed → furious scale. Returns a position like 2.4/3, meaning mostly annoyed but edging toward furious. Also returns confidence.
- **Calibrated probabilities work like a weather forecast.** When Jev outputs 0.8, it should be correct ~8 times out of 10. This is by design — it's trained for calibration, not to sound convincing like LLMs.
- **Cost and speed:** ~$0.04 per million input tokens, output is nearly free. The demo processed 50 emails in 4.2 seconds (with 8 concurrent workers) for $0.026 — roughly **19,000 emails per dollar**. Running 50 emails daily would cost ~$1/year.
- **Jev never takes actions.** It only returns numbers. Your code (scripts written by Claude) uses those numbers in if-statements to route, rank, or flag.
- **All questions in one request run in parallel ("speculative fan-out").** You send all 5+ questions at once even if some won't apply — irrelevant answers are ignored by the routing logic, and you only pay to read the input text once.
- **Confidence thresholds gate actions by risk.** Low-stakes actions (check balance: 0.6 threshold) allow lower confidence. High-stakes actions (approve a transfer: 0.85–0.95 threshold) require higher confidence before proceeding; below the threshold, the system pauses and asks a human.
- **Jev vs. Claude for the same task:** Asking Claude "does this email look suspicious?" takes 10–15 seconds and returns verbose text. Jev, given predefined criteria upfront, returns a number in ~0.3 seconds for a fraction of the cost.
- **TypeSafe's founder** built the methods behind ChatGPT at OpenAI.
- **TypeSafe ships a Claude Code skill** (two-line install from `docs.typesafe.ai/agent-skill`) that gives Claude a rulebook for structuring Jev requests — question types, specificity rules, batching strategy, and confidence thresholds. You describe the job in plain English; Claude writes the scripts and sends data to Jev.
- **State (input) should be structured, not flat strings.** Each object passed to Jev should have named fields (e.g., customer plan, tenure, email subject, body) so questions can reference specific fields. Irrelevant fields (e.g., thread history) should be excluded to reduce noise.
- **Hard limit of 64,000 tokens per Jev request**, but structured requests are intentionally minimal — you should never be close to this in practice.
- **Post-processing with Jev:** In the demo, after Claude drafts a reply, a second Jev request verifies: "Does this reply actually answer the customer's question?" and "Does it promise a refund or discount?" Only drafts passing both checks are kept.
- **Pre-processing with Jev (guardrails):** Jev screens every incoming message for jailbreaks/harmful content before it reaches Claude, and screens Claude's output before the user sees it.
- **Citation verification example:** An LLM wrote a document with 8 citations; Jev checked each quote against the source. 4 were fine, 1 was non-existent, 1 said the opposite of the source, and 2 were routed to a human.

---

## Use cases

- **Customer support triage:** Automatically sort overnight email queues by anger, severity, and category (billing, technical, feature request), routing to human reps, engineering queues, feature logs, or Claude for drafting replies — ranked by priority.
- **Fraud/suspicious order detection:** Flag orders above a confidence threshold for mismatch between billing and delivery addresses, unusual order patterns, etc.
- **AI guardrails:** Screen LLM inputs for jailbreaks and harmful prompts before they reach Claude; screen outputs before they reach users.
- **LLM output fact-checking:** Verify citations and claims in AI-generated documents against source material.
- **Lead scoring at scale:** Score and rank hundreds or thousands of sales leads in seconds (demo: 700 leads in 40 seconds for ~$0.09).
- **Browser/computer-use agents:** Classify every interactable element on a page and decide action type (click/type/scroll) and target element — with confidence thresholds controlling whether the action fires automatically or pauses for user confirmation.
- **Voice command interpretation:** Classify spoken commands into room, device, and action for smart home control; detect compound commands and hand them to an LLM to split first.
- **Candidate screening:** Score CVs across independent dimensions (Python depth, leadership, system design, learning speed) with weights tuned per role.
- **Inbox/ticket prioritization:** Rank bug reports by severity (cosmetic → annoying → blocking) or support tickets by urgency before a human ever opens them.
- **Intent routing in products:** Sit Jev in front of multiple handlers — deterministic DB lookups, Claude with product docs, human agents — and route each request to the optimal handler instantly.

---

## Patterns & frameworks

**1. Speculative Fan-Out (Ask Everything at Once)**
Send all questions — including ones that may not apply to a given input — in a single parallel request. Jev processes all questions simultaneously; your routing logic simply ignores irrelevant answers. You pay to read the input text only once, and you avoid round-trip latency from sequential questioning. This is the primary source of Jev's speed advantage over iterative LLM calls.

**2. Confidence-Gated Actions (Threshold Per Action)**
Set a distinct confidence threshold for each action based on the cost of being wrong. Low-cost mistakes (e.g., reading a balance) tolerate low confidence (~0.6). High-cost or irreversible actions (e.g., approving a transfer, closing a browser tab) require high confidence (~0.85–0.95); below the threshold the system pauses and asks a human. Confidence is a second number returned on Choice and Score types, derived from how spread out the per-option probabilities are.

**3. Decompose-Then-Weight (Breaking Big Judgments into Scored Dimensions)**
Instead of asking one holistic question ("Is this a good candidate? Score 1–10"), break the judgment into independent, separately scorable dimensions (Python depth, leadership, system design). Score each separately, then combine with role-specific weights in your routing code. This makes the criteria explicit, auditable, and tunable without retraining.

**4. Intent Routing (Classify → Dispatch to Best Handler)**
Place Jev upstream of all downstream handlers as a fast, cheap classifier. Route each input to the optimal handler: deterministic code (DB lookup for "where's my order?"), a specialist LLM (Claude with product docs for a product question), or a human (complex complaint). Inputs that fall below any confidence threshold automatically route to a human as a fallback. Jev is invisible in the latency budget because it resolves before the user notices.

**5. The Five-Question Checklist for Designing Jev Workflows (author's original framework)**
A process for identifying which questions to ask before writing any code:
1. List the actions the software can take.
2. Write each action's trigger as a sentence — that sentence becomes the question, and its form (act/not-act, route, rank) determines the type (null/choice/score).
3. Write down what a human would look at before making that call (defines the state/input).
4. Add edge cases that would change the routing (reveals additional questions needed).
5. Decide what a wrong answer costs to set the confidence threshold for each action.

**6. Two-Pass Architecture (Jev → Claude → Jev)**
For outputs that require Claude to write something, run a second Jev verification pass on the draft before saving it. First pass: Jev classifies and routes. Claude drafts where appropriate. Second pass: Jev verifies the draft against quality criteria (e.g., "Does it answer the question?" "Does it promise a refund?"). Only drafts passing all checks proceed. This catches hallucinations and policy violations without a human reviewer.