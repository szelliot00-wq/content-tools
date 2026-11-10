# Spec-Driven Development vs. Waterfall: What's Different for AI Coding?

Video ID: `GpZ5T51jE4U`

## Summary
The video explains Spec-Driven Development (SDD) as a modern approach to AI-assisted coding that superficially resembles the old Waterfall methodology but differs in one critical way: the spec stays alive and evolves throughout development rather than being frozen upfront. The presenter walks through both methodologies, highlights why Waterfall's big-upfront-spec approach failed, and shows how SDD leverages short iterative loops to keep specs connected to the code being built. The video argues that AI agents make specs more valuable than ever because they remove the ambiguity that causes agents to guess incorrectly, wasting time and money.

## Key insights
- **SDD is not Waterfall** — the difference is that the spec is continuously refined in short loops (hours/days per feature) rather than frozen and handed off before development begins.
- **AI agents guess when context is missing** — a good spec provides the context an agent would otherwise have to assume, directly improving output quality on the first attempt.
- **Ambiguity is expensive with AI** — every unclear requirement leads to extra prompt iterations, which costs both time and money; a clear spec reduces the number of cycles needed.
- **Specs stay version-controlled next to the code** — this prevents the "stale requirements doc" problem that plagued Waterfall, since the spec evolves alongside the implementation.
- **A spec serves triple duty** — it guides implementation, defines what "working" means for tests, and provides a checklist for validation, something traditional requirements docs never did.
- **Don't over-spec** — quick bug fixes don't need a spec; reserve SDD for large features touching multiple services or significant modernization efforts.
- **Security and compliance belong in specs** — unlike Waterfall where security showed up late in QA, SDD lets you embed non-functional requirements (auth, logging, secrets) into the spec from the start.
- **The agent can help write and update the spec** — this removes the historically high cost of keeping specs current, which is a key reason the industry abandoned them in the first place.