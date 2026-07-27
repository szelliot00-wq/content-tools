# Token budgets, building at the edge, and the future of product | Dianne Penn

Video ID: `tivaWTTVRhY`

## Summary
Dianne Penn, Head of Product for AI Research and Labs at Anthropic, traces the company's evolution from a five-engineer startup in 2023 to a frontier AI lab shipping models at unprecedented speed. The conversation covers how product management is fundamentally changing in an AI-native environment — from how user feedback is collected, to how requirements are defined, to what skills matter most. It is most relevant to product managers, researchers, and technology leaders trying to understand how to build, evaluate, and operate at the frontier of AI development.

## Key insights

- **Anthropic's early identity was unclear.** When Dianne joined in 2023, nobody associated Claude with coding. The team was fewer than 200 people, with a single engineer owning the entire API business. Finding their identity required experimentation — including quirky showcases like "Golden Gate Claude," a 24-hour experience where Claude obsessively referenced the Golden Gate Bridge, which reached only ~2,000 users but proved the team could ship quickly and authentically.

- **Coding was a smaller training change with outsized competitive impact.** Identifying that users were writing long-form code (not just autocomplete) led to targeted Opus 3 training improvements. It differentiated Claude early and brought in the developer community before anyone considered coding a Claude strength.

- **Opus 3 and Opus 4.5 were the two major inflection points.** Opus 3 (early March 2024) was the company's proof it could build a frontier model. Opus 4.5, roughly a year later (also during winter break), was the moment the model's intelligence combined with a product vehicle — Claude Code — to create real agentic use at scale. The two were inseparable: "Opus 4.5 wouldn't have had that moment without Claude Code, and Claude Code wouldn't have had that adoption without Opus 4.5."

- **Emerging capabilities are discontinuous and hard to predict.** Scaling law papers show a smooth loss curve as compute increases, but capability graphs are discontinuous — models jump from being unable to do 1+1 to being reliable at it. This makes safety harder (capabilities may appear before anyone knows to test for them) and product strategy harder (you can't always predict when a new product becomes possible).

- **There is significant "product overhang" and "user overhang."** Even on current models, there are unexplored use cases. Labs exists partly to pull threads on these discontinuous opportunities before they're obvious to the roadmap.

- **"Evals are the new PRDs."** The core PM artifact at Anthropic is no longer the product requirements document — it's the evaluation set. An eval is a set of prompt/response examples that captures a consistent user pain point, defines what "correct" looks like, and lets researchers measure improvement across model versions. This is described as test-driven development for PMs.

- **The eval creation process is rigorous.** It starts with vague user feedback (e.g., "Claude hallucinated"), then digs into transcripts to find the actual failure pattern (e.g., ~80% of "bad instruction-following" in Claude 2's era was specifically Claude not outputting valid JSON), generates 30–40 representative examples, defines golden answers, and adds the set to a shared repository run against every model version.

- **PRDs are not dead — but their application has changed.** PRDs are still used for: (1) aligning large cross-functional groups (legal, safety, engineering) around a model launch, and (2) exploring ambiguous product bets where user pain points aren't yet well-defined. For well-understood iterative problems, evals are the more actionable artifact.

- **Token spend = experimentation, not the goal itself.** On Gary Tan's "$100k/year in tokens = living in 2028" framing, Dianne reframes it: token spend is the input; experimentation and discovery are the actual outputs. The internally creative people at Anthropic spend heavy time with every research model, but what matters is the insight that emerges, not the spend itself.

- **Experimentation is not an individual sport.** Some of the most valuable discovery happens communally — a Slack channel where the whole company tests early Claude versions, sees each other's use cases, and iterates on them together. Within ~10 requests, novel use cases emerge that no individual would have found alone. Twitter serves a similar function externally.

- **Hands-on building is non-negotiable at every level.** Even senior PMs and managers at Anthropic go through the same onboarding as early-career PMs: reading consented transcripts, talking to users, building things. Dianne carves out time to personally own 1–2 workstreams per model launch to maintain her "theory of mind" about how the models are moving.

- **Claude's alignment and safety work makes it more useful, not less.** The model knowing when to push back, disagree, and add nuance — rather than just agreeing — is what makes it a genuine thinking partner. Dianne uses Claude to pressure-test decisions like Claude's own pricing strategy. Proactivity includes knowing when *not* to do the scheduled thing and instead surfacing a better idea.

- **The "model safeguards package" is becoming a first-class product area.** With models like Fable Mythos triggering export controls and industry-wide safety reviews, Anthropic has built fallback UX systems so users still get useful responses from Opus 4 when a frontier model is restricted. This will evolve further.

- **Forward-compatibility is a product design discipline.** Dianne's standing team question: "If Claude 8 ships, what changes in what users do — and is what we're building today forward-compatible with that?" This grounds ambition in a concrete future state rather than a vague "think bigger" directive.

- **AI writing is intentionally underinvested — for now.** Writing quality and tone/character are acknowledged rough edges. The reason is the "jagged edge" nature of AI: focus went to making models agentic and capable of tool use, and writing became the next rough edge once that improved. Active investment in writing quality is now underway.

- **Judgment, persistence, and proactivity are the most durable human advantages.** These aren't general capabilities — they're behavioral characteristics accumulated through lived experience. Areas like biology and life sciences are still at "the foot of the exponential" where software engineering already is, so domain expertise there remains highly valuable.

- **Anthropic shipped more model series in Q2 of this year than all of 2024.** This pace creates a sustainability challenge solved primarily by team culture: radical ownership, covering for each other during launches, and not siloing knowledge so individuals can take PTO without everything collapsing.

- **For kids (and adults): develop your own inner voice first.** Dianne's parenting philosophy — and her answer to AI brain rot concerns — is the same: form your own point of view before engaging AI. Use Claude as a sparring partner that challenges you, not a validator that agrees with you.

## Use cases

- **Product managers at AI companies** redefining their workflow: when to write PRDs vs. evals, how to translate vague user feedback into actionable research inputs.
- **Research PMs and TPMs** learning how to bridge user pain points and model training loops — how to make feedback "consumable and actionable" for researchers.
- **Labs and innovation team leaders** at larger companies wondering how to structure zero-to-one bets: small pods, bottoms-up culture, strong theme conviction with loose prototype conviction.
- **Mid-career or senior PMs** questioning whether they need to stay hands-on — the answer here is unambiguous: yes, at every level.
- **Engineers and PMs building AI-native products** who want a framework for thinking about product overhang and when emerging model capabilities unlock new product bets.
- **Anyone experiencing AI fatigue or feeling like they "have to" use AI** — the advice is to pair with someone who has genuine enthusiasm, or find one specific problem to go deep on rather than sampling many things shallowly.
- **Hiring managers and founders** building AI product teams who want a profile of what to look for: first-principles thinkers, zero-to-one personality, low ego, hands-on shippers, tinkering spirit.
- **Parents and educators** thinking about what skills to cultivate in children entering an AI-transformed world.
- **Safety and policy teams** thinking about how to design fallback UX systems as frontier models face access restrictions.

## Patterns & frameworks

**Evals as PRDs (Test-Driven Product Development)**
The replacement for the traditional PRD in AI product work. Process: (1) collect vague user feedback, (2) read transcripts to find the specific failure pattern, (3) generate 30–40 representative failure examples with golden answers, (4) add to eval repository, (5) run against every new model version to measure progress. The eval defines the work rather than a spec document. Analogous to writing tests before code.

**"Sweating the tokens, not just the pixels"**
A reframe of the classic UX principle "sweat the pixels." In AI product work, understanding user pain requires studying the full token-level trajectory of a conversation — what was asked, what the model did, where it failed — not just the surface-level UI. Reading transcripts is the new user interview.

**Strong conviction on theme, weak conviction on prototype**
Labs' operating posture for discontinuous bets: hold the area/thesis firmly (e.g., "agentic coding matters") but stay flexible on the exact prototype. If a prototype doesn't work, revisit it one or two model generations later when the model may be capable enough to make it viable. Bets that fail teach you something; don't ship them prematurely just to ship.

**"Claude 8 forward-compatibility test"**
A product design heuristic Dianne uses with her team: imagine a significantly more capable future model exists. What does that change about user behavior? Is the product you're building today still coherent in that world, or does it break? Used to ground ambitious thinking in a concrete future state.

**Communal experimentation / "working in public"**
An internal Anthropic practice where early model versions are tested in shared Slack channels rather than in isolation. When team members share use cases publicly inside the organization, others build on them, and novel applications emerge within ~10 iterations that no individual would have discovered alone. This is the antidote to "experimentation as an individual sport."

**The Labs incubation model**
A structured way to run zero-to-one bets inside a larger organization: (1) small pods, sometimes starting with one engineer, (2) bottoms-up self-direction, (3) explicit charter to explore things not on the core roadmap, (4) willingness to turn off bets that don't work yet and revisit them in future model generations, (5) culture selection — hire people who genuinely want the zero-to-one experience, not people who want org growth.

**Discontinuous capability emergence**
From scaling law papers: model loss decreases smoothly with compute, but capability graphs are discontinuous — the model jumps from "can't do X" to "reliably does X" with no gradual ramp. This means: (a) evals are essential because you may not know a capability appeared, (b) product timelines are hard to predict, (c) adaptability and first-principles reasoning matter more than fixed plans.

**Think first, then use Claude as sparring partner**
Dianne's personal workflow for preserving her own judgment while using AI: form a point of view independently first, then bring it to Claude for challenge and iteration. Contrast this with delegating writing of routine artifacts (monthly business reviews) to Claude fully, with herself as reviewer/verifier. The split depends on where personal judgment is asymmetrically valuable.