# Build AI Products as Systems of Trust - Alexis Zheng (CPTO, G2)

Video ID: `_FYLoPuPbKc`

## Summary
Alexis Zheng, CPTO at G2, traces the evolution of AI from the data era (2010s) to the compute era (2020s) to what she argues is the next critical frontier: **trust**. Drawing on her experience at Uber and in self-driving cars, she argues that the bottleneck to AI adoption is no longer model capability but the ability to build systems that earn and maintain user trust. She reframes the product manager's role for the AI age: from defining features and flows to designing systems, harnesses, and learning loops at a higher level of abstraction. The talk is most relevant to product managers, AI product builders, and enterprise technology leaders navigating the gap between frontier AI capabilities and real-world adoption.

---

## Key insights

- **The three eras of AI:** Data was the constraint in the 2010s; compute became the bottleneck in the 2020s; now **trust is the last mile** that determines whether AI actually crosses the chasm into everyday enterprise use.
- **The token economy:** Intelligence is the new commodity, tokens are the currency. There are ~4.5 billion prompts/day generating ~300 trillion tokens daily. The entire industry (Nvidia buying Hugging Face, Stripe acquiring a "toll booth," SpaceX buying a coding assistant) is converging on a single token-centric stack.
- **Supply-demand mismatch in AI apps:** New apps on the App Store more than doubled in the first 6 months of 2025, but downloads only grew 2–3% and average ratings declined — supply outpaced trust and demand.
- **Agents have a discovery problem:** Research shows that exposing agents to more skills (110,000+ MCP servers exist) actually *worsens* their performance — agents, like humans, need trust signals to navigate choices effectively.
- **The trust gap is measurable and costly:** 60% of B2B buyers already use AI in their purchase journey, but only 9% trust AI recommendations. 45% of buyers who've adopted agents say expected productivity gains are consumed by oversight and rework.
- **AI products are "iceberg products":** The user experience is just the tip — the system underneath (models, pipelines, evaluation, learning loops) is what actually determines value. Deep learning has "broken the interface," making systems thinking the core PM skill.
- **Abstraction leaking:** As AI takes over more of the interface (users just ask in natural language; agents act on their behalf), the underlying system becomes more important and more visible — PMs can no longer ignore it.
- **Fault tolerance > fixing individual failures:** In self-driving cars, the remaining failure modes become increasingly long-tail and hard to fix one at a time. The same applies to AI agents — the right approach is designing for graceful degradation and system-level reliability, not patching individual bugs.
- **Self-driving car parallels to agents:** Perception stacks identify *vulnerable* objects (caution over completeness); prediction models distributions of outcomes, not single outcomes; epistemic uncertainty causes systems to degrade gracefully (slow down, pull over, call a human); end-to-end latency is a first-class design constraint.
- **Continuous learning loop:** G2/self-driving car model — embed evaluators ("miners") in deployed systems, automatically score every action, trigger model retraining with no humans in the loop, deploy a better version. Enterprise agents can do the same: treat early mistakes like an intern's, convert them into test requirements, and iterate continuously.
- **Verifiability is the bottleneck:** Quoting Andrej Karpathy: "What can be verified can be automated." The real constraint isn't model architecture — it's experience and evaluation at scale.
- **G2's agent evals product:** G2 built simulated companies (with support, sales, legal, finance departments, each with real data/policies/tools) to let buyers evaluate agents before buying. Every agent interaction is captured as a trace and graded against predefined rubrics. Currently live in beta for customer support; sales category is next (harder, because ground truth is more ambiguous and plays out over longer time horizons).
- **Headless agents as a new category:** A new class of agents is emerging that are completely headless and built for the agentic age — the idea being that software itself may eventually be replaced by agents doing the work directly, with no human UI layer.
- **PM market fit:** Just as there is product-market fit, there is "product manager market fit." The PM role is shifting from defining *what* to build (and much of the *how*) toward designing systems, harnesses, and learning loops — operating at a higher level of abstraction.
- **Building at the frontier is the differentiating skill:** No known solutions to model after, high ambiguity, constant prior-updating required. The reward: shipping products that wouldn't otherwise have existed.

---

## Use cases

- **Enterprise AI product managers** deciding how to structure their AI product strategy beyond the model layer
- **AI startup founders** trying to understand why adoption lags despite strong model capabilities
- **B2B SaaS companies** evaluating how to differentiate their AI features from generic cloud/OpenAI experiences
- **Software buyers and procurement teams** trying to evaluate AI agents before committing to them
- **Platform/infrastructure PMs** building evaluation, monitoring, or observability tooling for AI systems
- **Anyone building agentic workflows** who needs to design for reliability, oversight, and graceful failure
- **Product leaders transitioning from web/mobile** who need to rethink their craft for the AI era
- **Engineering leaders** designing feedback and retraining loops for deployed AI systems
- **Marketplace and two-sided platform PMs** who need to think in terms of system-level incentives and emergent behaviors rather than feature-level design

---

## Patterns & frameworks

**1. The Three-Era Trust Model**
*What it is:* A historical lens on AI development — data era (2010s) → compute era (2020s) → trust era (now). Each era had a different bottleneck. Trust is not about blind faith but about defining clear boundaries: knowing when a system works and when humans must step in.
*How to apply:* Use it to diagnose where your AI product is stuck. If adoption is flat despite good model performance, you likely have a trust gap, not a capability gap.

---

**2. The Iceberg Product Model**
*What it is:* AI products have a small visible UX layer (the tip) sitting atop a massive invisible system (data pipelines, models, evaluation, learning loops). "Abstraction leaking" means the system underneath increasingly determines product success.
*How to apply:* PMs must invest in systems thinking and harness design, not just UI/UX. Treat the system as the product.

---

**3. Fault Tolerance Design (from self-driving cars)**
*What it is:* A framework for building reliable probabilistic systems — not by fixing every failure mode, but by designing for graceful degradation. Components: (a) perception with vulnerability prioritization, (b) prediction using outcome distributions not point estimates, (c) epistemic uncertainty signaling (the model knows when it doesn't know), (d) latency-aware reaction design.
*How to apply:* When building AI agents, design each layer to degrade safely, slow down, escalate to humans, or call for help — rather than trying to enumerate and fix every edge case.

---

**4. Continuous Learning Loop**
*What it is:* A system where deployed agents/models automatically score their own outputs (via embedded evaluators/"miners"), collect failures as new training data, generate test suites, retrain, and redeploy — with no humans in the loop.
*How to apply:* Design your AI product's operational architecture to include feedback capture, automatic scoring, and iterative retraining from day one. Early mistakes become structured requirements. The PM's job is designing the loop, not fixing individual errors.

---

**5. Agent Evals / Simulated Environment Testing**
*What it is:* G2's approach — build simulated companies with realistic departments, data, policies, and tools; assign agents real-world tasks derived from enterprise operations data; capture every interaction as a trace; grade against predefined rubrics. Buyers see real agent behavior before purchase.
*How to apply:* For any AI product where trust is a barrier to adoption, build an evaluation environment that surfaces real behavior (policy compliance, task completion, failure modes) in a controlled setting — letting users experience before they commit.

---

**6. "What Can Be Verified Can Be Automated" (Karpathy's principle)**
*What it is:* The claim that the limiting factor in AI system improvement is not model architecture but the quality and scale of your verifiers — the rubrics, evals, and test suites that judge whether outputs are correct.
*How to apply:* Invest PM/engineering effort in building better verifiers and evaluation frameworks. The quality of your learning loop is bounded by the quality of your grading system.