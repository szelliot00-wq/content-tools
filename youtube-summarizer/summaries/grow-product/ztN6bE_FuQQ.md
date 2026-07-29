# How to Build Frontier-Lab Quality AI Evals | Ex-Google, Meta PM

Video ID: `ztN6bE_FuQQ`

## Summary
This episode features Daniel McKinnon, a former PM on Meta's Llama models and founder of Gamoff Labs, explaining how to build AI evaluations (evals) that meet frontier-lab standards. The core argument is that evals have replaced the PRD as the primary way to define and communicate what an AI product should do — because examples and scoring are more precise than written specs for generative AI. The video walks through a live demo of building an agentic eval for clinical genomics, showing the full process from easy to hard prompts. It is most relevant to product managers building AI features, especially those new to agentic systems, and to anyone trying to understand how evaluation methodology has evolved from Q&A benchmarks to agentic task benchmarks.

## Key insights
- **Evals replace most of the PRD.** In Gen AI products, the traditional PRD (which describes how a product behaves in words) is inadequate because these systems do too many things. Evals — sets of prompts plus expected answers plus a scoring method — communicate what "good" looks like more precisely than prose specs.
- **Offline evals vs. online evals are fundamentally different.** An offline eval is a pre-baked set of ~100 prompts run during development as a proxy for real user traffic. An online eval is measuring real user satisfaction after shipping. The hypothesis is that offline performance predicts online satisfaction — this often holds, but not always.
- **The shift from Q&A to agentic tasks is the most important change in evals.** Two years ago, evals were simple question-answer benchmarks (MMLU, HumanEval, etc.). Today, frontier models have saturated those. Anthropic's Opus 4.8 is benchmarked on agentic coding, agentic terminal work, computer use, and financial analysis — tasks requiring multi-step reasoning, tool calls, and long time horizons.
- **The Goldilocks scoring principle:** A good eval should score roughly 25–50% at the start. Too easy (100%) gives no room to improve; too hard (0%) doesn't tell you if the problem is even solvable. Over months, scores climb toward 100%, at which point you retire the eval and build a harder one.
- **Domain expertise is the hardest part of eval construction.** The tooling is trivial — it's literally a spreadsheet of (phenotype/prompt, gene/expected answer, scoring method). The hard part is knowing the domain well enough to pick prompts that are meaningful, appropriately difficult, and representative. This is why labs hire investment bankers, lawyers, and accountants for vertical teams.
- **Start easy, then find the ceiling.** The first step is confirming the task is even possible for a model. Daniel used cystic fibrosis (a well-known single-gene disease) as his easy case. His hard case — a digenic congenital heart disease requiring two heterozygous variants across two genes — stumped most models without a specialized harness.
- **Haiku failed even the easy case.** Claude Haiku couldn't identify the canonical cystic fibrosis CFTR deletion, while GPT-5.3 and GPT-5.5 succeeded. This validated the use of multiple models to calibrate eval difficulty — the same task can be easy for one model and a real ceiling for another.
- **Agentic evals are harder to score than Q&A evals.** Long time-horizon tasks produce many intermediate steps; some steps can be wrong but still reach the right answer, and vice versa. Automated scoring (via another LLM judge comparing outputs to a scorecard) is increasingly necessary because human rating at scale is impractical.
- **Sampling matters less than it used to.** In the MMLU era, Google's Gemini Ultra used 32 shots (samples) vs. GPT-4's 5 shots, inflating benchmark scores. Today, Daniel finds that running the same prompt multiple times rarely changes the outcome — model capability is the binding constraint, not sampling variance. Still worth testing per use case.
- **Meta vs. Google culture:** Meta is founder-led, product-led, aggressive, and high-conviction — empowering when Mark Zuckerberg champions a project, brutal when he doesn't (the entire Llama team was dispersed after Llama 4's disappointing reception). Google is more engineering-led and consensus-driven, with a weaker PM function historically. Both have changed significantly since Daniel was there.
- **Evals are also the right tool for deciding what NOT to ship.** If a model scores below a threshold on certain prompt types, a PM can add guardrails to restrict the product to only the categories where it performs well (e.g., 80%+), and hand the hard cases to the research team as a backlog.
- **AI is used to build the evals themselves.** Daniel used Codex to synthetically generate variant files (fake patient genomes with known mutations) and used LLMs as judges to score model outputs against the answer key — AI evaluating AI.

## Use cases
- A PM starting a new AI feature from scratch who needs to define "what does success look like" before writing any spec
- A team building an image generation feature (e.g., at Pinterest) who needs to move beyond vague PRD language like "beautiful kitchens" to concrete, scored examples
- A product team evaluating which model (GPT-5.5, Claude Haiku, etc.) is appropriate for their use case and cost/performance requirements
- A startup or enterprise team building a vertical AI product in a specialized domain (genomics, law, finance) who needs domain-specific benchmarks
- An engineering team that needs a clear, measurable definition of done for an AI feature — the eval replaces the acceptance criteria in the PRD
- Any PM shipping an agentic product who needs to understand when it's safe to move from offline eval to production
- A team deciding whether to add guardrails to a product based on which categories of queries the model can and cannot handle reliably

## Patterns & frameworks

**The Eval-as-PRD Framework**
The central model of the video. Instead of writing prose specs describing desired behavior, define the product through: (1) a set of representative prompts, (2) expected correct responses, and (3) a scoring method. This triple — prompt, response, scorer — is the atomic unit of an agentic eval. The eval communicates product requirements more precisely than prose for Gen AI systems because it forces explicit, testable definitions of "good."

**The Goldilocks Eval Construction Process**
A repeatable five-step pattern for building any eval:
1. Define the problem deeply (requires domain expertise)
2. Start with an easy prompt to confirm feasibility
3. Find the ceiling with a hard prompt to confirm the task is not already solved
4. Binary-search the middle to assemble ~100 prompts spanning the difficulty range
5. Score each prompt (human, LLM judge, or automated) and establish a baseline

**Floor-and-Ceiling Calibration**
Before assembling a full eval set, bracket the difficulty space: run the easiest possible version of the task (establish the floor — can the model do this at all?) and the hardest known version (establish the ceiling — is this already solved or is it truly out of reach?). The useful eval lives in between, targeting a 25–50% initial pass rate.

**Offline → Online Eval Pipeline**
A two-phase quality gate: (1) run offline evals during development to reach a target score threshold, then (2) ship to production and measure real user behavior as an online eval. The offline score is a hypothesis about online satisfaction — track whether that hypothesis holds over time to calibrate how much to trust future offline scores.

**LLM-as-Judge Scoring**
For agentic outputs that are too complex or numerous for human review, use a separate LLM to compare the model's response against the answer key and return a pass/fail verdict. This enables automated scoring at scale and is the dominant scoring method for long-horizon agentic tasks.

**Multi-Model Calibration**
Run the same eval prompts across multiple models simultaneously (e.g., Haiku, GPT-5.3 Spark, GPT-5.5 Extra High) to understand the difficulty profile of each prompt relative to model capability. This helps PMs decide which model is appropriate for which product tier and price point, and surfaces prompts that are unexpectedly hard or easy.