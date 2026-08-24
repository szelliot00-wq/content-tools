# How to Build Better AI Evals with Claude Code in 5 Steps | Shreya & Hamel

Video ID: `bdMHQLvtVaQ`

## Summary
This video features Shreya and Hamel, instructors behind a popular AI eval course (4,500+ students), demonstrating a practical 5-step workflow for building better LLMs evals using Claude Code. The core argument is that automated eval tools can catch obvious errors, but human taste and judgment — externalized through deliberate data review — is the irreplaceable differentiator for AI products. The hosts walk through a live demo of Shreya's "error discovery skill" that builds a custom review interface to help humans annotate failure modes at scale, then convert those annotations into rubric-based evals. The video is most relevant to product managers, ML engineers, and developers building AI-powered features who want to move beyond naive automated evals.

## Key insights
- **Top-down vs. bottom-up evals are both required.** Top-down evals come from domain expertise (e.g., "takeaways should use action verbs") and Claude is good at generating these. Bottom-up evals are data-driven — they emerge only after reviewing many real outputs — and Claude cannot generate these for you; only the human can discover them through iteration.
- **Claude is very bad at generating bottom-up evals.** This is a direct quote from Hamel. The failure modes that matter most to product quality require product judgment and taste, which automated tools consistently miss.
- **Fan out evals to sub-agents per criterion.** If you give a long rubric list to a single model call, it will "get lazy" and ignore some criteria. Assigning one sub-agent per criterion (or per group) dramatically improves coverage and accuracy.
- **Use sub-agents to generate a spreadsheet/pivot table of pass/fail results.** This lets the human quickly scan all criteria and exercise judgment about which failures actually matter in context, rather than treating all criteria as equally weighted.
- **The error discovery skill is a 5-step process:** (1) Read the dataset and infer semantic type (article, trace, code, etc.), (2) Design a visual encoding using Gestalt principles (color, spacing, opacity) to surface variance, (3) Build a custom HTML/Python review app, (4) Use an agent to select a diverse sample of records to review (not random), (5) Run an interactive loop where the human annotates in-situ and a monitor agent distills feedback into rubric criteria in the background.
- **The monitor tool enables real-time reflection.** Rather than waiting for all human feedback to be collected, Claude's monitor tool watches annotations as they happen and starts proposing groupings and criteria incrementally, interleaving human think-time with AI processing time.
- **Human annotation + AI scaling = the core loop.** The human provides open-ended qualitative feedback ("I don't like negative contrast in writing"); the agent's job is NOT to invent feedback but to distill it, find all instances across the dataset, and propose annotations — with the human accepting or rejecting in bulk.
- **Automated eval benchmarking findings:** Hamel's blog post found that off-the-shelf automated eval tools (Braintrust Loop, Arize Alex, Langsmith) recover most obvious errors but systematically miss errors requiring product judgment — e.g., a rental sales agent that fails to handle sales objections, or a bot that puts markdown formatting in SMS messages. Coding agents (Claude, Codex) perform at roughly the same level as these specialized tools.
- **Precision on automated eval tools is 80–90% in the best case**, meaning 10–20% of flagged errors are false positives. Human review is needed to validate AI-found errors, not just to find new ones.
- **The competitive moat is taste.** All competitors will run automated evals — that's table stakes. The differentiator is how much human taste and judgment you can inject beyond that baseline.
- **Annotations create a labeled dataset as a side effect.** The records annotated during error analysis can immediately be used as a benchmark to validate the evals you write, solving the cold-start problem of having no ground truth data.
- **The review interface design should inform product interface design.** The structure of how you evaluate outputs (e.g., annotating staccato fragments inline) often reveals what the production UI should look like (e.g., an IDE that flags the same issues to the writer in real time).
- **Writing is called "the final boss for LLMs"** — getting an LLM to write in your voice, to your satisfaction, is among the hardest AI tasks, and requires especially rich bottom-up evals.
- **SaaS is under pressure** from agentic workflows. A custom Claude Code skill can produce a more flexible, domain-specific review interface than any off-the-shelf SaaS product, for free.
- **Overfitting is a real risk with iterative eval addition.** The host notes that adding an eval after a specific episode (e.g., "takeaways must be MECE") can overfit to that episode's context and not generalize. The top-down/bottom-up separation and human judgment on weighting helps mitigate this.

## Use cases
- **Product managers building AI features** who need to move beyond vibe-checking outputs and want a structured, scalable way to externalize quality criteria.
- **ML engineers running eval pipelines** who want to know which automated tools to trust and where to focus manual attention.
- **Developers with personal AI skills/workflows** (e.g., podcast post-production, writing assistants) who want to systematically identify failure modes without manually reviewing hundreds of outputs.
- **Teams with multiple annotators** who need to align on shared quality criteria before writing formal evals.
- **Anyone doing bottom-up error analysis on agent traces** — customer service bots, coding assistants, RAG pipelines — where obvious failures are already caught but subtle product-judgment failures persist.
- **Teams integrating evals into CI/CD** who want a principled rubric to automate against, not just LLM gut-checks.
- **Consultants or indie developers** who can't afford specialized eval SaaS and want a free, flexible alternative built with Claude Code.

## Patterns & frameworks

**Top-Down vs. Bottom-Up Evals**
A two-axis mental model for categorizing eval criteria. Top-down: derived from first principles and domain expertise, independent of data ("what should good output look like in a vacuum?"). Bottom-up: derived from looking at many real outputs and noticing patterns of failure or taste. Claude can help with top-down; bottom-up is exclusively human-driven. Both halves are required for a complete eval suite.

**The Error Discovery Skill (5-Step Process)**
Shreya's open-source Claude Code skill that automates the scaffolding for human-led error analysis:
1. Infer the semantic data type
2. Design a visual encoding (color, spacing, opacity) to highlight variance
3. Build a custom HTML review app (Python backend)
4. Select a diverse, clustered sample for initial human review
5. Run an interactive annotation loop with a background monitor agent that distills open-ended feedback into rubric criteria

**In-Situ Annotation Loop**
A pattern where humans give open-ended, real-time feedback while reading output ("I don't like negative contrast"), and an agent running the monitor tool simultaneously distills that feedback into structured criteria and applies them across the full dataset — interleaving human and AI think-time rather than doing them sequentially.

**Sub-Agent Fan-Out for Eval Criteria**
When a rubric has many criteria, assign each criterion (or logical group) to its own sub-agent call rather than a single call with the full list. Prevents models from deprioritizing or skipping criteria under a long prompt. The results are then aggregated into a spreadsheet/pivot table for human triage.

**Taste Infusion as Competitive Moat**
The strategic framing that automated evals establish a baseline all competitors will reach, but human-externalized taste (via bottom-up evals and error analysis) is the differentiating layer. The framework: use automated tools for recall, use human review to improve precision and catch judgment-requiring failures, then encode the human discoveries into LLM judges for scale.

**Human-in-the-Loop Bulk Annotation**
After the agent proposes annotations across the full dataset based on discovered criteria, the human reviews a representative sample and accepts or rejects in bulk — checking that the agent correctly understood the intent of each criterion (e.g., "yes, it correctly identified what I meant by negative contrast"). This keeps the human in control without requiring per-record review.