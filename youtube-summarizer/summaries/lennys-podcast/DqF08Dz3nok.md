# How to build products on a moving frontier | Dan Shipper (Every)

Video ID: `DqF08Dz3nok`

## Summary
Dan Shipper, co-founder and CEO of Every, argues that product teams face a fundamental tension during AI technology revolutions: they must simultaneously exploit existing roadmaps and explore rapidly shifting capabilities, two activities that pull in opposite directions. His solution is to structurally separate these concerns by creating a "labs team" — a small, dedicated exploration unit distinct from the main product team. The talk covers why labs teams work, how to run them effectively, and how to pipeline discoveries back into the main product. It is most relevant to product leaders, startup founders, and engineering managers building software products during a period of rapid AI model advancement.

## Key insights
- **The core tension**: Exploration (divergent, experimental, throws things away) and exploitation (convergent, focused, executes roadmaps) are opposing modes — forcing everyone to do both simultaneously kills productivity on both fronts.
- **Early adopters inside your org are both assets and liabilities**: Some team members are already running new models on weekends and living in the future. Harnessing them without distracting the rest of the team is the central organizational challenge.
- **Labs teams can be a team of one**: Because AI dramatically amplifies individual productivity, a single person can serve as an entire labs function — spinning up demos, testing new models, and reporting findings without requiring significant headcount investment.
- **Composition matters — "pirates and architects"**: The optimal two-person labs team pairs a pirate (high-volume, messy experimenter obsessed with finding value) with an architect (someone who takes a chaotic prototype and shapes it into something extensible and production-ready).
- **Two Pizza → Two Slice**: Jeff Bezos's "two pizza team" (~8–10 people) is too large for labs work in the AI era. Shipper advocates for one or two people max to minimize coordination overhead and vision conflicts.
- **90/10 disposal ratio**: Labs teams should expect to throw away 90% of what they build. Product teams should expect to adopt only ~10% of labs output. Setting this expectation explicitly reduces pressure and allows genuine exploration.
- **Dogfooding as the tightest feedback loop**: Building things you actually use yourself is the fastest way to know if something is good vs. merely novel. The distinction between "useful" and "just new" is critical and only time-and-usage reveals it.
- **Run competing experiments in parallel**: When the frontier is unknown, having multiple people tackle the same problem from different angles maps the solution space better than a single focused effort — even if it looks incoherent.
- **Make the 90% ROI-positive**: Discarded experiments shouldn't be pure waste. Every turns failed experiments into external content (readers love "here's what we tried and what didn't work"), feeds them into an early adopter customer program, or uses them to brief the product team on capability shifts.
- **The Kate bench example**: Shipper spent ~2 years trying to automate editorial copy-editing to extend his editor-in-chief Kate's impact. He downloaded 3 years of her edits, fine-tuned a model on them, and gradually moved it from personal experiment → internal team tool → tracked dashboard (12% reduction in Kate's post-edit workload) → candidate for customer release.
- **Decision criteria for pipeline progression**: Two key filters — (1) Are people using it and coming back? (2) Is it 10x better than what exists a month later, not just on first impression? Affordability at scale is a third gate.
- **Codex as the archetypal labs success**: OpenAI ran multiple parallel internal experiments on the future of coding (IDE? CLI? desktop?). Codex's desktop app launched February 2026, grew so fast it was merged into ChatGPT and became its foundation — a small labs team effectively taking over an 800M DAU product.
- **The success signal**: You know the labs structure is working when new model drops feel exciting rather than threatening.

## Use cases
- A product leader at a B2B SaaS company trying to figure out whether/how to integrate new AI capabilities without derailing the existing roadmap.
- A startup founder who needs to stay at the frontier but can't afford to hire a large dedicated research team.
- An engineering manager whose best engineers are distracted by shiny new models and want to channel that energy productively.
- A company with a high-volume content or editorial workflow looking to extend expert taste through AI without losing quality.
- Any team that keeps feeling blindsided or destabilized each time a new frontier model is released.
- Product orgs that want to practice "self-disruption" — building the next version of their product before a competitor does.
- Companies with early-adopter customers who want deeper access and a more collaborative relationship.

## Patterns & frameworks

**Explore vs. Exploit Separation**
The core framework: explicitly split your org into a team that explores (labs) and a team that exploits (product). Labs is divergent and disposable; product is convergent and delivery-focused. They run in parallel with a defined handoff process rather than asking the same people to context-switch between modes.

**The Research Pipeline**
A left-to-right progression: Lab-only experiment → internal team adoption → early customer testing → product team evaluation → scaled release. Ideas move through stages only when they clear defined criteria. Most never make it; that's expected and by design.

**Pirates and Architects**
A two-person team composition pattern. The pirate generates high-volume, messy experiments rapidly, optimizing for finding signal. The architect receives promising messy prototypes and refactors them into robust, compounding systems. Each role is ineffective without the other.

**10x Filter (Time-Adjusted)**
A decision gate for moving experiments forward: is this genuinely 10x better than the status quo — not on day one, but after a month of real use? This filters out novelty bias and forces honest assessment of durable value.

**Make the 90% ROI-Positive**
A principle for minimizing waste from the labs' high disposal rate: convert failed experiments into external content, early adopter program value, or internal capability briefings so that even discarded work generates organizational return.

**Two Slice Team**
A scaling heuristic updating the "two pizza team" norm. In the AI era, one to two people with AI tooling can accomplish what previously required 8–10, so labs teams should be kept at this size to avoid coordination drag and vision fragmentation.