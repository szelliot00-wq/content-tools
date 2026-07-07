# Building AI products at early stages vs global scale: Jonathan Evens (Google DeepMind)

Video ID: `Uev2xZyGi0Y`

## Summary
Jonathan Evans, AI Product Lead at Google DeepMind, contrasts the challenges of launching AI features at massive scale versus building AI-native products from scratch at an early stage. Drawing on two real examples — personalized suggestions in Google Search's AI Mode and a "digital citizenry" democracy sandbox at the Evans Foundation — he argues that the core discipline in both contexts is the same: match AI's genuine advantages to real user pain points, and invest early in solving the hard evaluation and research problems. The talk is most relevant to product managers working anywhere on the spectrum from scrappy startups to enterprise platforms, particularly those grappling with how to justify, measure, and ship AI features responsibly.

## Key insights
- **Start with pain points, not technology.** Evans frames every AI opportunity by asking which user pain is solvable with AI's specific advantages (automation, personalization, scale, synthesis), not by asking what AI can do in the abstract.
- **Competing with your own product is the hardest part at scale.** The Google Search personalization feature had to prove it added more value than the already high-quality existing experience — standard metrics didn't capture this, requiring a redesigned "helpfulness" metric that accounted for subjectivity.
- **Narrow your target use cases ruthlessly.** For Google Search, the team identified that personalization shines specifically when queries are complex, options are overwhelming, or contextual history matters — leading to two hero use cases: local dining and shopping.
- **LLMs are non-deterministic — build for learning, not perfection.** Because LLMs can't predict every outcome correctly, power users serve as the first "human in the loop." Google launched in Search Labs (opt-in, ~millions of users vs. billions) to safely test hypotheses and gather feedback.
- **Evaluations are essential but don't need to be perfect from day one.** The Evans Foundation measured synthetic citizen responses against real survey data and found ~10% divergence — acceptable given that real humans shift their own answers 5–20% over weeks. An imperfect-but-useful eval is enough to start the feedback flywheel.
- **Privacy creates hard constraints on evals at scale.** Human raters can't access private user activity data at Google, so the team used synthetic users and auto-raters that can process large volumes of private data safely — but building a personalized auto-rater was itself an unsolved AI research problem at the time.
- **Spot the AI research dependency early.** In both projects, the blocking technical challenge (personalized auto-raters at Google; high-fidelity persona models at the Foundation) was identified upfront, enabling the right partners or teams to be engaged before it became a crisis.
- **Early-stage teams can reach MVP with vibe-coding tools.** With no full-time developer, the Evans Foundation used AI coding tools to build good-enough UIs, which was a "game-changer" for getting the product in front of users and generating real feedback.
- **Synthetic citizens are currently caricatures.** When prompted to mimic a persona, LLMs produce less diverse and more extreme responses than real humans. The solution was conditioning prompts with a high-fidelity persona model built on ~2,000 real surveys mapped to 100+ human values, developed with specialized external partners (Cooperative AI Foundation, FAIR Institute, Culture Dynamics).
- **The three criteria for an AI-native opportunity:** (1) time-consuming tasks that can be automated or newly enabled, (2) potential to lower barriers to knowledge or insights, and (3) ability to create a safe "in silico" environment where users can try approaches they couldn't in the real world.
- **Risk profiles are fundamentally different.** At scale, the main risk is breaking user trust by disrupting a familiar mental model. At early stage, the main risk is pursuing the product at all — if the underlying technology doesn't work, there is no product.

## Use cases
- **PMs at large tech companies** launching an AI feature on top of a mature product who need to justify it against existing quality benchmarks and define new metrics for subjective value like "helpfulness."
- **Founders or small teams** building AI-native products from scratch with limited budgets who need a framework for deciding whether an opportunity is genuinely AI-ripe.
- **Search and discovery teams** redesigning recommendation or feed experiences to incorporate natural language and user context (e.g., the Netflix analogy Evans opens with).
- **Civic tech / govtech builders** exploring AI for policy simulation, constituent engagement, or democratic deliberation at scale.
- **AI researchers and product teams** grappling with evaluation design for subjective, personalized, or privacy-constrained AI systems.
- **Early-stage non-technical teams** (nonprofits, foundations, small startups) who need to ship an AI MVP without dedicated engineering resources.
- **Anyone designing human-in-the-loop AI systems** who needs to decide between human raters, synthetic users, and auto-raters based on data sensitivity and scale.

## Patterns & frameworks

**Pain Point → AI Advantage Matching**
Before designing any AI feature, map specific user pain points to concrete AI capabilities (personalization, synthesis, automation). Only build where there is a genuine fit. Used in both case studies as the first step.

**Hero Use Case Narrowing**
When launching an AI feature into a broad product, identify the 2–3 specific contexts where AI's unique differentiators will shine most clearly (e.g., complex queries + overwhelming options + history-dependent intent → local dining and shopping). Avoids spreading the feature too thin and competing poorly everywhere.

**Search Labs / Opt-In Gating**
Constrain early AI feature rollout to a voluntary, bounded user pool (millions, not billions) to safely run experiments, test hypotheses, and collect feedback before full exposure. Reduces blast radius of non-deterministic failures.

**Imperfect-But-Useful Evaluations**
Don't wait for a perfect eval framework. Establish a measurable proxy (e.g., synthetic vs. real survey divergence), validate it's directionally sound, and use it to start the improvement flywheel. Refine evals iteratively as the product matures.

**Auto-Rater Substitution for Privacy-Constrained Evals**
When human raters can't access sensitive data (privacy restrictions) or lack bandwidth to process it at scale, replace them with auto-raters (LLM-based evaluators) that can safely process private data in bulk — while flagging that personalized auto-rating at scale may itself be an open research problem.

**Three-Criteria AI-Native Opportunity Screen**
For early-stage products: (1) Are there time-consuming tasks to automate or newly enable? (2) Can AI lower barriers to knowledge or insight? (3) Can AI create a safe sandbox for experimentation that would be impossible or too risky in the real world? All three criteria together signal a strong AI-native opportunity.

**High-Fidelity Persona Conditioning**
To make LLMs simulate realistic, diverse human behavior (rather than caricatures), condition prompts with persona models grounded in real survey data mapped to human values. Partner with specialized external researchers if in-house capability doesn't exist.

**Scale vs. Early Stage Risk Framing**
Evans closes with a clean two-axis mental model: at scale, you are *evolving* an existing product and the primary risk is trust erosion; at early stage, you are *disrupting* with the technology as the entire foundation and the primary risk is pursuing a product where the tech isn't ready. The mitigation strategy — spotting research dependencies early — is the same in both cases.