# How to scale intent, quality, and artistry with Al | Katie Dill (Stripe)

Video ID: `GLvFTMtw4Jk`

## Summary
Katie Dill, Head of Design at Stripe, draws a parallel between the post-WWII building boom (which produced generic, soulless "zombie buildings" by copying modernist style without intentionality) and today's AI building boom, arguing that the same risks apply to software. Her core thesis is that AI makes building fast and cheap, but without a strong point of view, encoded standards, rigorous editing, and creative ambition, teams will produce "zombie UI" — monotonous, generic, and uncared for. She offers four concrete recommendations for using AI to build products with genuine soul and differentiation. The talk is most relevant to product managers, designers, and engineering leaders navigating AI-assisted development at scale.

## Key insights
- **The post-WWII parallel:** Modernism had intentionality (e.g., Villa Savoye, the Bauhaus), but when copied en masse under urgency, it produced generic, context-free buildings. The same pattern threatens software today as AI lowers the barrier to build.
- **Three watch points for the AI building boom:**
  - LLMs optimize for the most *probable* answer — what's popular or has worked before — not what's original or specific to your brand and users. A Korean BBQ website that looks like generic SaaS is the example used.
  - The "burrito dilemma": AI makes things *feel* finished very fast (like a microwaved burrito that satisfies hunger but is nearly inedible). Apparent polish is misleading — it doesn't mean the problem is actually solved or the product differentiated.
  - Work feels disposable because it's so easy and quick to produce, leading teams to ignore long-term considerations like maintenance and ownership.
- **Zombie UI is a real risk:** An environment (literally shown as a building in Turkey) of copy-paste patterns ill-suited to context. Software equivalents are monotonous, vacant, and show no care for users.
- **Care shows in the details:** Examples of soul in products include Grok's bot animation, the calendar app showing today's date in the tab, and the Link agent wallet anticipating troubleshooting needs for AI agents buying online.
- **Stripe's brand value of "optimism"** is embedded into colors, writing style, copy, and product decisions — alignment on this is critical because building is now distributed across many contributors.
- **Quality standard debate:** A cross-functional partner asked "What's the quality standard for something made with AI?" — Dill's answer: it doesn't matter how it was made, only whether the output is good. This led to 17 bullet points of improvements to an ad, coining the internal verb **"Pepsi bubbling"** (meticulous craft, going one level deeper than what the customer can consciously see).
- **Design systems are having a moment** because humans are no longer always in the room. Agentic construction and generative UI require systems that encode intent, not just consistency.
- **Gutenberg analogy:** He didn't just create 52 characters — he created 290 unique glyphs (different widths, abbreviations, ligatures) so fully-justified typesetting would feel as beautiful as handmade. The goal: extensible *and* opinionated enough to feel crafted at machine scale.
- **Stripe's evolution of tooling:** Started with an MCP that ingested design documentation — results were inconsistent (three people, same prompt, three different outputs). Evolved to a **CLI built on their design system** that acts as a harness making AI "more obedient," consumes documentation at the right time/place to avoid context rot, and includes not just components but **full templates and flows** — the system knows how the product is supposed to behave end-to-end.
- **Christopher Alexander quote:** "A system can satisfy every rule and still be dead." Encoded standards are the floor, not the ceiling.
- **The filter is gone:** Previously, quality filtering happened at every stage (idea selection, staffing, iteration). Now 20 ideas can be built in a week, so filtering must happen *post-build* — which is harder. The role of the **editor** becomes critical.
- **Editing requires experiencing like a user:** Does it solve the problem? Is it coherent? Does the full journey hang together, not just individual screens in isolation?
- **What AI can't do well (yet):** Unexpected details that surprise and delight, deeper meaning beneath the surface, and continuous themes that tie a product into a coherent whole. "The cup is green but may as well have been blue" — AI slop signals that details don't matter.
- **Stefan's animation example:** The opening animation for the event went through **56 iterations** using AI assistance. Each pass refined realism, movement, and life. The key insight: AI enabled a more complex scene and more viewpoints than would have been attempted manually — it expanded the possibility space.
- **Stripe's "Built to Grow" cover:** A human marbler created stunning physical iterations; AI was then used to fine-tune colors and lines further — human judgment scaled by machine.
- **Tactics for better AI creative output:** Write specific prompts (brand values, what "good" means, source material); stress outputs by always pushing a step further; use adversarial agents to critique results.
- **The cultural challenge is harder than the tactical one:** Cookie-cutter is safe. Finding something unique that improves the status quo is harder and more impressive. Leaders should give teams room to explore and "protect the strange."
- **Gothic architecture as the countermodel:** John Ruskin (1850) noted no two Gothic columns were alike — each showed the unique hand and mind of its maker. That's the aspiration: software that feels truly cared for.

## Use cases
- **Product leaders** deciding how to govern AI-assisted development across distributed teams without losing brand coherence
- **Design leads** building or modernizing a design system to support agentic and generative UI construction
- **Engineering teams** integrating AI coding tools (MCPs, CLIs) who need guardrails that encode intent, not just components
- **Brand and marketing teams** using AI for creative output (ads, visuals, copy) and struggling to maintain quality standards
- **Startup founders** building fast with small teams who risk shipping generic, undifferentiated products
- **Anyone shipping AI-generated UI** who needs a framework to know when "done" actually means "good"
- **Creative directors and editors** in product organizations whose role is evolving in the age of agentic construction
- **Teams debating quality standards** for AI-generated vs. human-generated work

## Patterns & frameworks

**The Four Recommendations (Dill's framework for building with soul using AI)**
A four-part structure for avoiding zombie UI:
1. *Have a point of view* — define brand values and user needs before prompting; if you don't, AI fills the gap generically
2. *Encode your standards into the machine* — design systems must now capture intent, templates, and flows, not just atomic components
3. *Refuse to confuse done with good* — appoint editors, filter post-build, and experience the product as a user would
4. *Unleash creativity and artistry* — use AI as a creative catalyst, not just a productivity tool; invent new interfaces and aesthetics

**The Burrito Dilemma**
Mental model for the danger of premature "doneness." AI produces something that looks polished in 90 seconds, just as a microwaved burrito goes from frozen to "lunch" in 90 seconds — but apparent completion masks serious quality gaps. Antidote: always push one step further.

**Pepsi Bubbling**
Stripe's internal term (verb) for meticulous craft — going one level deeper than what the customer can consciously perceive. Originated from a design crit on an ad with subtle flaws (soft edges, bubble sizes). The principle: that invisible layer of care surfaces as a felt sense of quality.

**The Gutenberg Standard**
A benchmark for design systems: don't just encode the parts — encode enough opinion and extensibility that machine-made output feels as intentional and beautiful as handmade. Gutenberg's 290 characters (vs. 52 needed) is the reference: over-engineer the system so the output has no ugly gaps.

**The Post-War / Gothic Duality**
A historical framing device contrasting two outcomes: the post-war building boom (speed + copied style - intentionality = zombie buildings) vs. Gothic architecture (distributed craftsmanship + intentionality = unique, cared-for structures). Used as a before/after vision for what the AI building boom could become.

**Adversarial Agent Critique Loop**
A practical workflow: generate output with AI → stress-test it yourself → also deploy an adversarial agent to critique it → iterate. Used to counteract the temptation to accept the first polished-looking result.