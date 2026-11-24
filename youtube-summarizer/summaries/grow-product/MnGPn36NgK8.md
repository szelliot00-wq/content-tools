# FAANG PM Reveals How to Evaluate AI Agents (and Get Paid $1M+)

Video ID: `MnGPn36NgK8`

## Summary
This episode features Mahesh Yadav, a former AI PM at Google, Amazon, Meta, and Microsoft, who breaks down the most critical skill separating successful AI PMs from the rest: agent evaluation (evals). The core argument is that building AI agents is now trivially easy thanks to harnesses like Claude Code and Microsoft Copilot, but only 15% of agents make it to production because teams cannot reliably evaluate whether agents meet a quality bar. Mahesh presents a three-stage framework — setting HHH (Helpful, Honest, Harmless) criteria, scaling evals from human reviewers to LLM judges, and reducing cost/time with new decision models like TypeSafe Jev. The video is most relevant to mid-to-senior product managers who want to remain valuable and competitive as AI commoditizes traditional PM work, and to anyone building production-grade AI agents.

---

## Key insights

- **Building agents is no longer a differentiator.** Agent harnesses (Claude Code, Microsoft Copilot, OpenAI Codex) now handle context, memory, tools, and guardrails out of the box. Anyone can build a legal risk agent in 10–15 minutes. The moat is in evaluation, not construction.
- **Only 15% of enterprise agents reach production.** Of that remaining 85%, 63% of teams admit they would not put their name on the agent if asked. The gap between "it works in demo" and "it works in production" is entirely an evals problem.
- **Microsoft internal data point:** ~2,000 agents were built internally, but reuse across those agents was under 1%. Agents get tried once, fail, and are abandoned — a direct consequence of skipping rigorous evals.
- **The HHH framework — Helpful, Honest, Harmless** — is the core evaluative lens. Each dimension must be broken down into specific, binary yes/no questions tailored to the agent's domain. For a legal contract risk agent, "helpful" might mean: does the redline stay within the clause boundary? Does it avoid excessive strikethrough? Does it cite the relevant rule from the playbook?
- **Criteria must be set with a floor and a ceiling.** The ceiling comes from public model benchmarks (e.g., Humanities Last Exam measures reasoning capability; best models score ~61%). The floor is competitive benchmarks — what can a competitor or a vanilla Claude prompt do? Internal company launch thresholds add a third constraint. Example: ceiling 70%, competition floor 45%, internal standard 60% → launch criteria set at 65%.
- **If your agent is scoring above your ceiling, your test is too easy.** A 90% score on a legal reasoning eval might mean the task is closer to Q&A (ceiling ~96% per GPQA Diamond) than deep reasoning (ceiling ~61% per Humanities Last Exam).
- **Human evals are the starting point, not the end state.** For the first 10 contracts/samples, a subject matter expert (SME) manually answers each binary eval question. This builds "ground truth" data, which is later used to validate automated evaluators.
- **Scaling evals: LLM-as-judge via Azure AI Foundry.** Azure AI Foundry offers pre-built evaluators for coherence, fluency, groundedness, tool call accuracy, safety, and custom criteria. Cost drops from $0.25/question (human SME) to $0.0025/question — a 100x reduction. 25,000 questions goes from $6,250 to ~$62.50.
- **Validating LLM judges with accuracy/precision.** Before trusting an LLM judge, compare its yes/no outputs against human ground truth. An accuracy rate of 70–80% is the threshold for deploying automated evals. Below that, the judge is unreliable and cannot replace human review.
- **Precision vs. recall for agent outputs:** Precision penalizes false positives (agent flags risks that aren't real risks). Recall penalizes false negatives (agent misses real risks by being too conservative). PMs must decide which matters more for their use case — over-flagging vs. under-flagging — and set evaluation criteria accordingly.
- **Decision models (e.g., TypeSafe Jev) reduce eval cost another 100x.** Unlike LLMs trained with RLHF (which optimize for human-pleasing text generation), decision models use Reinforcement Learning with Common Distribution (RLCD). They require the evaluator to pre-define the answer choices (yes/no, NDA/MSA/DPA), then output a calibrated confidence score. This confidence score is reliable — unlike an LLM's hallucinated confidence — enabling automated routing: if confidence < 70%, escalate to human review.
- **Jev benchmark results from live testing:** 214 seconds to run evals, cost reduced ~100x vs. Azure AI evaluators, matched Azure's accuracy, and produced a trusted confidence score for each answer. Only 2 out of 20 predictions mismatched human ground truth.
- **40–45% of an AI PM's time should be spent on evals.** This includes reviewing 200–1,000 traces manually per week, bucketing failure types, assigning Jira tickets to engineering with specific regression targets, and tracking eval accuracy week-over-week to catch drift.
- **Eval drift is a silent killer.** An LLM judge calibrated at 70–80% accuracy will degrade as new query types emerge. Weekly manual sampling (200–2,000 traces) keeps the judge honest and surfaces new failure modes that the original eval questions don't cover.
- **Compensation for AI PMs at FAANG:** Level 6 = $750K–$1.2M total comp; Level 7 upper band = $1.2M–$2M; Level 8 + stock multipliers = $2.5M–$3M+. For non-US markets, the expectation is 2–4x salary growth within 3–4 years of moving into AI PM roles.
- **The PM's ownership boundary:** PM owns the HHH criteria, the eval questions, the success thresholds, the cost/accuracy targets, and the weekly review of traces. Engineering owns implementation, toolchain, CI/CD for eval pipelines, and continuous improvement. PMs should use Claude Code to prototype evals and show engineering the art of the possible without prescribing implementation.

---

## Use cases

- **Enterprise AI PMs** trying to justify and de-risk shipping an AI agent to production with executive sign-off.
- **Startup founders or solo builders** who need a lightweight eval system before they have dedicated QA or engineering resources.
- **Legal tech teams** building contract review or risk analysis agents (the primary worked example throughout the video).
- **Finance teams** automating AP/AR, reconciliation, and reporting — same HHH framework applies with domain-specific questions.
- **Any PM managing an external vendor selling AI agents** — use evals to objectively compare the vendor's agent against a vanilla Claude prompt to determine if the vendor adds value.
- **Engineering managers** who want to give PMs a structured way to own quality without overloading eng with criteria-setting.
- **Career-switchers or mid-level PMs** looking for a concrete skill roadmap to move into high-compensation AI PM roles (the 10–15–20 day learning plan at the end of the video).
- **Teams using Azure AI Foundry** who want to operationalize evals without building custom tooling from scratch.
- **Teams evaluating whether to adopt TypeSafe Jev or similar decision model APIs** as a cost-reduction strategy in existing eval pipelines.

---

## Patterns & frameworks

**1. The HHH Framework (Helpful, Honest, Harmless)**
The core evaluation lens for any AI agent. Each dimension is decomposed into specific, binary yes/no questions derived from customer interviews and domain expert input. "Helpful" = does it do the job correctly? "Honest" = is the answer grounded in the designated knowledge source (playbook, documents)? "Harmless" = does it follow company guidelines, avoid competitive disparagement, avoid illegal suggestions, protect sensitive data? Scores are calculated as the percentage of responses where all questions in a dimension pass. Teams set launch-gate thresholds per dimension (e.g., 65% helpful, 70% honest, <5% harmful).

**2. The Ceiling/Floor/Internal Standard model for setting eval criteria**
- **Ceiling** = best available model's score on the most relevant public benchmark (e.g., Humanities Last Exam for reasoning tasks, GPQA Diamond for Q&A tasks). You cannot exceed what the model itself can do.
- **Floor** = competitor or baseline (vanilla Claude prompt, internal DIY agent) performance on the same eval.
- **Internal standard** = company-specific never-ship-below threshold.
- Target launch criteria sits between floor and ceiling, above the internal standard.

**3. The Three-Stage Eval Scaling Ladder**
- Stage 1: Manual human evals (SME answers binary questions per response). Establishes ground truth. Cost: ~$0.25/question.
- Stage 2: LLM-as-judge (Azure AI Foundry evaluators or custom). Validated against human ground truth at ≥70–80% accuracy. Cost: ~$0.0025/question (100x reduction).
- Stage 3: Decision models with RLCD (TypeSafe Jev, OpenAI/Azure decision APIs). Provides calibrated confidence scores, enabling automated human-escalation routing. Cost: ~$0.000025/question (another 100x reduction). Total reduction vs. manual: ~10,000x.

**4. Precision and Recall for evaluating agent output quality**
- **Precision** = of everything the agent flagged as a risk, what fraction was actually a real risk? High precision = fewer false alarms.
- **Recall** = of all real risks in the document, what fraction did the agent catch? High recall = fewer missed risks.
- These are in tension: maximizing recall (flag everything) tanks precision (lots of noise). The PM must decide the right trade-off for the product context (e.g., a first-pass screening tool favors recall; a final sign-off tool favors precision).

**5. Ground Truth Accuracy Check for LLM Judges**
Before deploying an LLM-as-judge at scale, run it against human-labeled ground truth on a representative sample. If the judge's yes/no answers match human answers ≥70–80% of the time, it is considered production-ready. Below that, the judge is not trustworthy enough to replace human spot-checking.

**6. The AI PM Value Matrix (mentioned, not fully detailed)**
A 2×2 framework with "cost of error" (low to high) on the Y-axis and "knowledge type" (explicit to tactical) on the X-axis. Used to advise companies on where to fully automate (low error cost, explicit knowledge), where to build a co-pilot, where to build an audit agent, and where to keep humans fully in the loop (high error cost, highly tactical knowledge).

**7. The 10/15/20-Day AI PM Skill Roadmap**
- Days 1–10: Understand agent harnesses (Claude Code, Copilot). Build 1–2 agents. Learn the context/action/eval loop.
- Days 11–25: Build 5 industry case studies using the AI value matrix. Identify where AI should/shouldn't be applied. Publish and get peer review.
- Days 26–45: Set up HHH evals for the case study agents. Run Azure AI Foundry evals. Show iteration history (bad → improved).
- Days 46+: Build GTM/pricing strategy for the same agents, accounting for token-variable cost structures and user segments (heavy/mid/low).