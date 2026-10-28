# Spinning Up Is Easy. Shipping What's Right Is Awesome | Kathy Pham   at MTP Chicago 2026

Video ID: `VDLlkExLsec`

## Summary
Kathy Pham's talk at Mind the Product Chicago 2026 argues that while AI has made it trivially easy to spin up prototypes, PRDs, and products, the harder and more important challenge is shipping what's *right* — for users, society, and populations who may never directly use the product. Drawing on 20+ years across consumer tech, government, and healthcare (including her current role leading AI at Revive Health), she presents four principles for product managers navigating the AI era. The talk is most relevant to PMs, product leaders, and anyone building AI-native or AI-assisted products who want to ground fast-moving development in responsibility and judgment.

---

## Key insights
- **"How much privacy will people give up for convenience?"** — A question raised at a large tech company 20+ years ago still defines the core tension: just because users will give up everything (privacy, security, data) to use a product doesn't mean we should take it.
- **AI makes building the wrong thing cheaper too.** The same tools that let you generate a PRD or prototype in minutes also let you skip trust, safety, and ethics checks — accelerating mistakes at the same speed as breakthroughs.
- **Synthetic users are not real users.** AI-generated test populations reflect AI's training biases and gaps; they can't substitute for real, diverse human populations, especially underrepresented ones.
- **Capability is not the same as judgment.** Each technology era (internet → PC → mobile → social → cloud → AI/agents) expanded capability but didn't automatically expand ethical judgment. PMs are the ones who bring judgment to the room.
- **Technology paradigm shifts reframe "what's right."** The Yahoo link-farm → Google one-box → LLM natural language shift illustrates how each era changes not just UX but our ethical obligations (e.g., voice assistants collecting enormous personal data).
- **Alert fatigue in healthcare is a cautionary tale.** Electronic health record alerts — designed as safety features — became so noisy that clinicians ignored them entirely. Layering AI on broken, unused features makes things worse, not better.
- **Evals are the new acceptance criteria.** Traditional acceptance criteria (did the button work? did the form submit?) don't apply to probabilistic AI outputs. You need domain-expert-informed evaluations to determine if an output is actually *right*.
- **The UN launched an Independent AI Evaluation Committee** (referenced as Ramon Chaudhary's initiative), signaling that evals are now a global governance concern, not just an internal engineering practice.
- **No product is an island.** Systems thinking (Don Norman reference) means every product intersects with legal, policy, governance, culture, and marginalized communities — PMs must map that whole landscape, not just their feature.
- **"Should we?" is asked far too rarely.** Especially under IPO pressure or speed mandates, teams skip "is this right for the right communities?" — the most important question in the room.
- **Unintended use is inevitable.** Every product will be used in ways you didn't design for (the rubber duck analogy). Planning for misuse and failure is just as important as planning for success — more so with AI's unpredictability.
- **LLMs compress diversity into stereotypes.** Language models normalize and flatten toward the average; PMs need to actively seek out edge cases, cultural nuances, and marginalized perspectives that models won't surface.
- **Cloud-to-on-premise reversal is a trend to watch.** AI products moving to local/on-premise models is a significant architectural and privacy shift happening right now.

---

## Use cases
- **AI product teams** moving fast with LLM-based features who need a framework for slowing down at the right checkpoints (trust, evals, community impact).
- **Healthcare product managers** navigating clinician workflows, EHR integration, and high-stakes AI outputs where wrong answers have serious consequences.
- **PMs at pre-IPO startups** under speed/growth pressure who risk skipping ethics and responsibility reviews.
- **Product leaders building "connected productivity" tools** that aggregate email, contacts, social media, and personal data — facing the privacy-vs-convenience tradeoff directly.
- **Enterprise PMs adopting AI in internal tooling** (performance reviews, HR, legal) where bias and trust are critical and failure modes are hard to see.
- **Anyone doing AI evals** who needs a mental model for what evaluation means beyond traditional QA and acceptance criteria.
- **PMs in regulated industries** (healthcare, finance, government) where policy, legal, and compliance are inseparable from product decisions.
- **Product educators and coaches** looking for a structured, historically grounded framework to teach responsible AI product development.

---

## Patterns & frameworks

**1. The Four Pillars of Responsible Product Development**
Kathy's core framework for the AI era:
- *Solve the right problem* — Not just "will people use it?" but "is it right for them, for society, and for those who never use it?"
- *Evals as acceptance criteria* — Replace binary pass/fail testing with domain-expert-informed evaluations of whether AI outputs are actually correct and safe.
- *Trust as a feature* — Build trustworthiness into the product explicitly, not as an afterthought; a trustworthy product solves problems without creating new ones.
- *Orchestrate the shift* — Use the PM's unique "manage without authority" muscle to drive responsible AI adoption across the entire org (engineering, marketing, legal, etc.).

**2. The Technology Era Capability Curve**
Each era (Internet → PC → Mobile → Social → Cloud → AI/Agents) expands capability but also expands harm potential at the same rate. The lesson: capability gains always require a corresponding judgment upgrade, and PMs are responsible for supplying that judgment.

**3. "Phone-a-Friend" Network Model**
Borrowed from *Who Wants to Be a Millionaire?*: build a deliberate network of domain experts (anthropologists, lawyers, clinicians, policy experts, critical race/gender scholars, data scientists) you can call on when a product decision exceeds your team's expertise. Be that resource for others too. This is an alternative to relying solely on LLMs for answers outside your domain.

**4. Look Backwards to Go Forward (Anti-Replication Pattern)**
Before adding AI to existing workflows, audit which features people *don't actually use* (e.g., EHR alerts with fatigue-induced ignore rates). Making a broken, unused feature faster or smarter with AI just accelerates the wrong thing. Deliberately identify these before layering AI on top.

**5. "You Are Not the Only Voice of the User" (Tricia Wang)**
PMs often over-identify as the sole proxy for users. The framework: actively recruit external voices — customer advisory boards, domain experts, affected communities — rather than speaking *for* users from inside the product team's bubble. This is especially critical when LLMs collapse diverse user needs into normalized averages.