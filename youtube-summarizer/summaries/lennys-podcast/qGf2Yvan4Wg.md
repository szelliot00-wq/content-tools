# Why PMs are suddenly valuable again | Tulsee Doshi (Head of Product, Gemini)

Video ID: `qGf2Yvan4Wg`

## Summary
This episode of Lenny's Podcast features Tulsee Doshi, Head of Product for Google's frontier models (including Gemini, generative media models, Gemma, and audio models), discussing what it means to be a PM for AI models in 2025. Doshi argues that PMs are becoming more valuable again precisely because the ease of building with AI has created a need for taste, signal-from-noise judgment, and cross-functional alignment. She shares frameworks for how to build products against rapidly evolving models, how to evaluate model quality, and how to develop AI intuition. The episode is most relevant to PMs, AI builders, and product leaders navigating the shift from traditional software development to model-centric product work.

---

## Key insights

- **Models are grown, not built.** Training a model is more like Snape's potions class than traditional engineering — you shape inputs intentionally, but the outputs are partially unpredictable. A PM's job is not just to specify what goes in, but to identify where unexpected "magic" emerges and shape that into a great product.

- **"Vibes" are a legitimate PM skill.** Understanding the personality, tone, behavior, and feel of a model is a form of UX evaluation. Doshi's team has a dedicated model behavior team that translates user and customer feedback into behavioral specs, rubrics, training data, and reward modeling.

- **PM ascendance is real.** The phase of "we don't need PMs" has passed. Because anyone can build anything now, building something *great* is the differentiator. Taste, focus, and the ability to turn chaos into clarity are uniquely human PM skills that AI amplifies rather than replaces.

- **The 60/20/20 rule for building against AI.** Build such that 60% of features work reliably today, 20% work well enough and will improve soon, and 20% show glimmers of future possibility. This avoids both over-building for a future that hasn't arrived and under-building by limiting yourself to what's reliable now.

- **Evals don't have to be large to be valuable.** Start with just 5–20 prompts that stress-test a capability. Even a small, manual eval where you rate responses yourself can reveal signal between models and give you clarity on what "good" looks like before you try to scale it.

- **The model's UX is the model itself.** How transparent it is, what questions it asks back, how it communicates — these are all UX decisions that happen during model development, not just in the product wrapper around it.

- **The harness is the wrapper, not the model.** A harness = system prompt + tools + context + skills the model has access to. It defines the environment in which the model operates. Teams should periodically strip away harness components to test whether the base model has gotten good enough to handle tasks natively — over-engineering the harness can actually hamper what newer, better models can do.

- **Skin tone eval reform (Monk scale).** Doshi led work replacing the Fitzpatrick scale (6 skin tones, designed for healthcare, skewed light) with the Monk scale (10 skin tones derived from sociological/anthropological research with Prof. Ellis Monk at Harvard), improving representation in Pixel camera and image generation products.

- **Google's strategy is full-stack, not just frontier.** From TPU hardware to end-user products serving 14 billion-user apps, Google's goal is to serve the full cost-quality curve — not just win the "smartest model" race, though Doshi says Google does want to compete at the frontier (citing Gemini 4 Argon as their current push).

- **Flash teams → agent swarms.** Doshi's Stanford research with Prof. Michael Bernstein on "flash teams" (rapidly assembled/disassembled crowdsourced worker groups optimized for task completion) maps directly onto modern multi-agent AI systems. The same design principles around role specialization and coordination now apply to sub-agent architectures.

- **PM skills trending up: vibes + evals + adaptability.** When hiring, Doshi looks for PMs who play with models daily, have personal use cases to benchmark quality, can roll up their sleeves and look at data/traces, and treat roadmaps as living documents to be rewritten every two months.

- **AI reduces grunt-work burnout.** Burnout comes from chaos and from meaningless work, not from long hours alone. AI tools that eliminate repetitive tasks can actually reduce burnout by freeing PMs to do more creative, high-judgment work they find meaningful.

- **The AI-slop doc problem.** Doshi's heuristic: AI should provide the *data*, PMs should provide the *insight*. AI-generated status/metrics docs are great; AI-generated strategic thinking is not. Teams should build skills/workflows to structure data artifacts so humans can focus on creative and analytical synthesis.

- **New PM habit: "Can AI do this for me?"** Inserting a pause between stimulus (a task appears) and response (starting the task) to ask whether a model can handle it is the most impactful habit shift. One successful delegation experience is enough to rewire the reflex.

- **Upskilling approach: shared skill repositories + protected time.** Doshi's team is building a shared repo of PM-built AI skills/workflows, running cross-team workshops, and planning a 2-day offsite to give PMs dedicated time to explore tools without day-job pressure.

---

## Use cases

- **PMs evaluating AI models** — use the vibes framework and start-small eval approach to build intuition about where a model shines without needing to build a large benchmark first.
- **Product builders using third-party LLM APIs** — apply the 60/20/20 rule when deciding which features to ship now vs. prototype for near-future model improvements.
- **Teams over-engineering AI harnesses** — periodically strip the harness and retest base model capability; the model may have already surpassed the scaffolding you built around it.
- **PM hiring managers** — prioritize candidates who play with models daily, have personal eval rubrics, can read data traces, and treat roadmaps as dynamic rather than fixed.
- **Leaders fighting AI-induced burnout** — identify which parts of the team's work are grunt work vs. creative judgment, and use AI to systematically eliminate the former.
- **Teams dealing with AI-written doc proliferation** — establish a norm: AI generates data-layer content, humans write insight-layer content.
- **Product orgs struggling with alignment amid fast-paced AI development** — the PM's value is now in driving consensus and turning velocity-induced chaos into structured direction.
- **ML/AI teams designing evals** — think end-to-end: judge model quality, judge quality, serving configuration, and mitigations all affect what end users actually experience.

---

## Patterns & frameworks

**The 60/20/20 Rule (Tulsee Doshi)**
Build today such that 60% of your product works reliably now, 20% works well enough with near-term model improvement in sight, and 20% represents a "glimmer of light" — not yet working but defining a future magical experience. This replaces the traditional "build an MVP that works" mantra with a portfolio approach calibrated to model trajectory rather than fixed timelines.

**Start-Small Eval Method**
Begin with 5–20 prompts that stress-test a specific capability. Rate outputs yourself as the initial judge. The goal is to get self-clarity on what "good" looks like before scaling. Once you can articulate good, you can build rubrics, then automate. Scales from personal intuition → small batch eval → large-scale benchmark.

**Vibes-First Model Assessment**
Before structured evals, stress-test models on tasks *you personally care about* — writing, financial analysis, code, creative work. Because you have a strong intuition for quality in your own domain, you can detect meaningful differences between models and notice "magic" that generic benchmarks miss.

**Model Behavior Spec Pipeline**
User/customer feedback → behavioral direction for Gemini → behavioral spec → rubrics → eval data → reward modeling. This is how qualitative PM input ("the model should feel more like this") gets translated into measurable training signal.

**AI-Assisted Doc Structure Norm**
AI provides: data, metrics, synthesis, status updates, Twitter/Reddit sentiment. Humans provide: insight, strategic interpretation, creative direction. Keeping these roles separate prevents AI slop while still capturing efficiency gains from AI-assisted content creation.

**Flash Teams → Sub-Agent Architecture Principle**
From Doshi's Stanford research: effective teams are assembled intentionally around complementary skill sets, can be spun up and down rapidly, and are structured so each member's role is clear. The same applies to multi-agent AI systems — intentional role assignment and coordination structure determines team effectiveness.

**Stimulus → Pause → Delegation Habit**
Insert a deliberate question — "Can AI do this for me?" — between receiving a task and starting it. Build this as a reflexive habit. One successful delegation experience is the trigger that reinforces the loop. Over time this compounds into a library of personal workflows and automations.