# Your users don't behave the way they describe themselves: Tom Charman at ProductTank SF

Video ID: `mQ8gm5dlUtw`

## Summary
Tom Charman, co-founder of Block (a behavioral simulation platform), argues that the core missing layer in modern product development is simulation — the ability to predict how users will actually behave before shipping. He contends that building is getting cheaper while shipping is getting more expensive, the 14–16 week feedback loop is too slow for today's AI-accelerated development pace, and that LLM-generated opinions about products are dangerously misleading because they produce convincing commentary without behavioral signal. The talk introduces a 5-level simulation maturity model and makes the case that behavioral simulation — not synthetic opinions — is the path to adaptive products. It is most relevant to product managers, user researchers, designers, and engineers working at companies where validation is a bottleneck.

## Key insights
- **Building is getting cheaper; shipping is getting more expensive.** The assumption that AI reduces shipping costs is a fallacy — there are fewer PMs and user researchers doing 10x the work with half the resources.
- **The feedback loop is broken.** The current build cycle (research → build → ship → A/B test → iterate) takes 14–16 weeks on average, while engineering tools like Cursor and Claude Code ship in hours. Validation can't keep up.
- **LLMs produce AI slop.** Because LLMs predict the next word (i.e., they regress to the average), using them to design products creates homogeneous experiences. They lack taste and creativity.
- **The new "builder layer."** Roles are converging — user researchers are expected to build prototypes, designers to ship products, PMs to ship code. Without a simulation layer, this democratized building happens blind.
- **LLM opinions vs. behavioral simulation is a critical distinction.** Asking an LLM "what do you think of this onboarding flow?" produces polished, convincing, but useless feedback (e.g., "the progress bar reduces uncertainty"). Behavioral simulation shows *observable actions*: 4.2x more retries on password creation, cautious users abandoning while impatient users skipping security steps entirely.
- **Humans don't behave the way they describe themselves.** In paid user research sessions, participants say nice things to be invited back. Self-reported behavior is systematically misleading — this is the central flaw in traditional user research.
- **Industry simulation analogy.** Every high-stakes industry simulates before committing: pilots use flight simulators, surgeons simulate operations, F1 drivers use driving simulators, architects simulate builds (citing the Millennium Tower in SF which sank after construction). Product is the outlier.
- **Block's 5 Levels of Simulation:**
  1. Commentary — LLM opinions, convincing but not behavioral
  2. Completion — Can agents complete tasks? Good for QA, not behavioral insight
  3. Behavior — How do different personas actually navigate and decide?
  4. Fidelity — Does simulation align with real-world outcomes?
  5. Prediction — Can simulation improve outcomes before shipping?
- **87% behavioral fidelity vs. 30–60% industry baseline.** Across 3,000 experiments in open-ended real-world environments, Block achieves 87% fidelity. Standard synthetic systems achieve 30–60%. Claude Code itself is ~60% accurate. Most product teams accept 80% (4 in 5) as sufficient to act.
- **Small language models (SLMs) over large ones for persona simulation.** LLMs pollute the context window when given too many behavioral constraints — the persona degrades to the model's default within 4–5 steps. SLMs can be fine-tuned to embody specific behavioral traits and maintain persona consistency throughout a simulation.
- **The four pillars of digital twin personas:** emotional data, demographic data, psychographic data, and agent memory (how prior emotional state affects future behavior within the simulation).
- **Backtesting, forward testing, retesting.** Block validates its simulations by rerunning historic A/B experiments against synthetic populations (backtesting), comparing live results to simulated predictions (forward testing), and iterating on simulation accuracy over time (retesting).
- **N-of-1 personalization is theoretically possible but practically problematic.** Managing 10 million unique UIs for 10 million users is operationally intractable. Near-term reality: 5–20 personas per product, each with a distinct UI variant.
- **Agents will automate ~10–15% of internet behavior** — the boring, repetitive tasks. The other 85% will still depend on human behavior. Agent-to-agent pipelines that skip humans should just use APIs, not simulate human behavior.
- **Regulated industries are the sweet spot:** finance, healthcare, education, insurance. Reasons: higher confidence threshold before shipping, less available data than e-commerce, and the ability to simulate rare but critical events (e.g., back-to-school traffic can only happen once a year in the real world).
- **Competitive moat is data, not the model.** The 10th bank using Block benefits more than the 1st because Block learns how humans behave *within* banking contexts — not the customers' proprietary data, but synthetic behavioral patterns across similar environments.
- **The end goal is adaptive products, not better testing.** Simulation is the training ground for adaptive UIs — once fidelity is high enough, products can serve differentiated experiences to different behavioral segments with confidence.

## Use cases
- **Product managers** validating feature ideas before committing engineering resources
- **User researchers** scaling from 15–20 interviews to population-level behavioral insight using simulation to fill the gap
- **Designers** testing whether onboarding flows, messaging, or UI layouts will cause confusion, abandonment, or hesitation in specific persona segments
- **Engineers** using simulation as a QA layer beyond functional testing — does the thing work *and* will users actually complete it?
- **Healthcare product teams** modeling emotionally volatile, irrational patient behavior across many permutations (e.g., 9–13 discharge personas) where direct data is scarce and stakes are high
- **Regulated industry builders** (finance, insurance, education) who need high confidence before shipping due to compliance and impact risk
- **Prompt and agent optimization** — testing what copy or agent output will most effectively guide a human user toward a desired behavior
- **Simulating rare events** like back-to-school surges or product launches where real-world data only exists once per year
- **A/B test design** — using simulation to predict which variant will win before running a live experiment

## Patterns & frameworks

**5 Levels of Simulation**
A maturity model for how deeply a team is simulating user behavior. Level 1 (Commentary) is LLM opinions. Level 2 (Completion) is task success/failure. Level 3 (Behavior) is observable decisions and pathways. Level 4 (Fidelity) is validation against real-world outcomes. Level 5 (Prediction) is pre-ship outcome forecasting. Block positions itself between levels 4 and 5.

**Simulate → Validate → Deploy (replacing Build → Ship → Measure)**
A proposed replacement for the traditional reactive product cycle. Instead of building, shipping, and waiting for A/B results over 14–16 weeks, teams simulate before committing, validate against real or synthetic baselines, then deploy with higher confidence. Compresses the cycle to ~2 weeks.

**Backtesting / Forward Testing / Retesting**
Three validation modes for simulation accuracy. Backtesting reruns historic A/B experiments through synthetic populations to measure delta. Forward testing puts predictions live and compares to real results. Retesting is the ongoing improvement loop that compounds platform accuracy over time — the primary moat for simulation platforms vs. DIY.

**Four-Pillar Persona Construction**
For building behavioral digital twins: (1) emotional data, (2) demographic data, (3) psychographic data, and (4) agent memory (how accumulated emotional state shapes future in-session behavior). Reduces dependence on rich product clickstream data, making it applicable in data-sparse environments like healthcare.

**Commentary vs. Behavior distinction**
A mental model for evaluating AI-generated product feedback. Commentary is what an LLM says it would do (rationalized, convincing, low-signal). Behavior is what an agent actually does when placed in the product — observable hesitations, retry patterns, abandonment points, path divergence by persona segment. The distinction determines whether simulation output is actionable.

**SLMs over LLMs for persona fidelity**
Using small, fine-tuned language models instead of general-purpose LLMs to embody specific behavioral personas. Rationale: LLMs degrade persona consistency within 4–5 prompts due to context window pollution and drift toward the base model's defaults. SLMs trained on specific behavioral traits maintain consistency and are cheaper to run at inference scale.