# How PMs can win with open source - Dan Ciruli (Product Leader, Nutanix)

Video ID: `WTJyUTUTwgk`

## Summary
Dan Ciruli, VP/GM of Cloud Native at Nutanix and a former Google engineer, discusses how product managers can navigate and succeed in open source environments. The video covers why companies open source products, how to commercialize open source work, the unique PM dynamics in open source communities, and the role of AI in open source security. It is most relevant to PMs working in enterprise software, cloud infrastructure, or developer tooling who are considering or already managing open source projects.

## Key insights
- **Open source is not purely crowdsourced from individuals** — a large share of contributions come from engineers paid by companies (e.g., Google, Microsoft, Red Hat, IBM, Amazon) on company time. This is what makes large projects like Kubernetes sustainable.
- **Kubernetes is the canonical example** of open source done right: Google realized that as a third-place cloud vendor they could never define a standard alone, but as a consortium they could — and did. This created a multi-billion dollar industry.
- **The CNCF (Cloud Native Computing Foundation)**, created ~2015–2016 by Craig McLuckie, is the key governance structure. It gave both large enterprises and small startups a "safe place" to contribute and consume open source, with conformance tests and commercialization rights preserved. Over 300,000 developers have contributed in its first decade.
- **Monetization strategies for open source** include: (1) proprietary tooling layered on top of the open core, (2) managed/hosted services (the cloud vendor model — "you don't want to run a database, you want to use a database"), (3) paid enterprise support with guaranteed patch access and engineer escalation.
- **The defensible moat in open source** is not the code itself but the surrounding proprietary tools, managed services, support expertise, or trusted brand — not the raw source code.
- **PM roadmaps in open source are not fully owned by the PM** — they are heavily engineering-driven, and you must triangulate between what your company wants, what the community wants, and what is mutually acceptable. Competitors literally sit on the same steering committees.
- **The PM's core job doesn't change** — even with volunteer contributors from rival companies, the fundamental PM skill of communicating "here's what we want to do and why" is what motivates people regardless of who signs their paychecks.
- **AI and open source security** is an arms race: AI multiplies attacker productivity, but "with many eyes all bugs are shallow" — open source code is more auditable than proprietary code. The US federal government adopted open source partly for this reason.
- **Linus Torvalds recently cautioned** against purely AI-generated bug reports and pull requests: humans must add judgment and value, not just relay AI output. Some open source projects now automatically close purely AI-generated PRs.
- **Open source adds drama** — internal debates, management vs. engineering disagreements, license changes, community forks. Dan explicitly names this as a real cost but argues the value created always outweighs it for participants like Google, Red Hat, and Microsoft.
- **The anti-pattern is the "benevolent dictator for life" model** (Linux/Linus Torvalds). It worked, but Dan argues Linux got lucky and this model is not repeatable — a foundation with multi-stakeholder governance is safer and more scalable.
- **ISTIO anti-pattern (personal lesson):** Dan regrets not pushing harder for an MVP approach on ISTIO. The project was over-engineered early on because the team tried to replicate Google's internal system rather than starting simple.
- **Developer reputation in open source is individual**, not corporate — contributors build public proof-of-work that travels with them, making top contributors attractive hires regardless of which company they work for.
- **AI has dramatically increased developer productivity** but Dan is a "pragmatist optimist" — AI tools should make humans more productive, not replace human judgment in architectural and governance decisions.

## Use cases
- A PM at a startup deciding whether to open source a novel internal tool that isn't a competitive differentiator
- A PM at an enterprise company evaluating whether to build on an open source stack vs. a proprietary vendor solution
- A PM managing a product with open source dependencies whose roadmap is affected by upstream community decisions
- A product leader needing to justify open source investment to a CEO or board ("how do we make money from this?")
- A PM trying to build community momentum around an early-stage open source project
- A PM or engineering leader evaluating AI-assisted code review and vulnerability patching processes
- A product leader working with contributors from competitor companies on a shared standard or protocol
- A PM inheriting stewardship of an open source project and needing to understand governance responsibilities

## Patterns & frameworks

**The Triangulation Model (Open Source Roadmap)**
In open source, PMs cannot dictate the roadmap. Instead, they must constantly triangulate between three forces: (1) what the company wants, (2) what the community wants, and (3) what is mutually acceptable. The output is a negotiated roadmap, not a unilateral one. This requires ongoing stakeholder communication rather than traditional top-down prioritization.

**"Chop Wood, Carry Water" (Open Source Contributor Ladder)**
A meritocratic progression model used in Kubernetes: contributors earn trust by doing unglamorous work first (bug reports, documentation, small fixes), then graduate to maintainer status, then project ownership. Trust is built incrementally and publicly. This ladder is what gives end users confidence that the project is well-governed — and Dan argues it cannot be delegated to AI.

**The Safe-to-Adopt Framework**
For an open source project to gain enterprise adoption, it must provide safety signals on two sides: (1) **contributor safety** — large companies must feel comfortable donating engineering time without losing commercialization rights; (2) **consumer safety** — enterprises must trust the project won't disappear or be abandoned. The CNCF model is the blueprint for achieving both simultaneously.

**The "Why First" PM Principle (applied to open source)**
Before deciding whether to open source, contribute to, or build on open source, the PM must articulate the "why" clearly enough to explain it to a CEO. This includes: how the company will make money, what the community benefits from, and how the decision advances the broader product strategy. The "why" is also the tool for motivating external contributors who have no obligation to follow you.

**Multi-Party Legitimacy Strategy**
When launching a new open source project, find at least one other company — even a competitor — to co-announce or co-contribute. The presence of multiple companies signals "this is a standard, not a vendor play," which dramatically increases adoption confidence. It's not linearly more appealing — it's exponentially more credible.

**"Many Eyes" Security Model**
Open source is inherently more auditable than proprietary code. Bugs in open source are discoverable by anyone (increasingly including AI bots), publicized through standard CVE processes, and patchable by the whole community. Proprietary vulnerabilities can sit undetected indefinitely. This is why government bodies (US federal, UK central digital infrastructure) favor open source for security-critical infrastructure.