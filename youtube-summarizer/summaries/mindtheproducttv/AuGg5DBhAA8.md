# Nobody outside tech is using AI agents

Video ID: `AuGg5DBhAA8`

## Summary
"Now Shipping" host Mike Belceto covers three AI news stories relevant to product managers: Salesforce's integration of AI agents into Slack via MCP, OpenAI's dramatic price cuts on GPT models, and a viral post by Josh Miller (Browser Company co-founder) questioning why AI agents haven't broken through to mainstream consumer adoption. The video's central argument is that AI is rapidly becoming infrastructure — cheap, ubiquitous, and table stakes — while the real unsolved problem is user experience and distribution for non-technical users. It is most relevant to product managers, founders, and builders working on AI-powered products, particularly those targeting enterprise or consumer markets.

## Key insights
- **Salesforce Slack + MCP integration**: Salesforce made Slack a fully functional MCP client, meaning Agentforce agents now operate inside Slack threads rather than requiring users to visit a separate AI tool. A sales rep can pull CRM data, summarize customer interactions, and draft emails all within one Slack thread, orchestrating across 6,000 AppExchange integrations and 2,600 Slack Marketplace apps.
- **Agentforce is generating real revenue**: $1.4B in annual recurring revenue with 114% year-over-year growth, driven largely by large enterprise customers — this is not a pilot-stage product.
- **The "agents where people work" principle**: The interface layer of enterprise AI is shifting to wherever teams already live (Slack, Teams), not a separate dashboard. Products that embed into those layers will have a structural advantage.
- **Enterprise AI adoption is further along than assumed**: Product teams shouldn't assume their large enterprise customers "aren't ready" for AI agents. Some are already in Agentforce contracts with Salesforce. Sales and CS teams should be queried for ground truth on adoption.
- **MCP is becoming table stakes**: Belceto argues that MCP support is no longer a differentiator or pilot program — it's an expectation for how products expose their capabilities to others.
- **OpenAI cut GPT model prices by up to 90%** on July 30th. At $2/million tokens previously, a product making 10,000 calls/day at 5,000 tokens each costs ~$35,000/year. At the new ~$0.20/million rate, that drops to under $4,000/year.
- **Revisit killed features**: Features that were cut because AI inference cost was the blocker may now be economically viable. Teams should explicitly audit their prioritization backlog for cost-killed ideas.
- **The moat is no longer the AI**: If frontier-quality AI is cheap enough to be infrastructure (like cloud storage or compute), competitive advantage comes from proprietary data, distribution, and customer relationships — not the model itself.
- **Pricing pressure on Anthropic and Google is coming**: Similar to what happened with Sonnet 5 pricing, OpenAI's cuts will likely pressure competitors to follow. Good for AI budgets.
- **OpenAI gave ~100,000 researchers free frontier model access through 2027** — a market development move to embed builders deeply into the platform at no cost.
- **Josh Miller's observation**: The co-founder of the Browser Company (Arc, now building Dia) posted that virtually nobody outside of tech is actually using AI agents, despite remarkable model capability and widespread infrastructure.
- **ChatGPT crossed the mainstream threshold; agents have not**: Non-technical users have experienced ChatGPT, but they're using it as "a glorified Google meets Grammarly" — query/response, not goal-delegation.
- **Why agents haven't gone mainstream — UX gap**: ChatGPT went viral because the interface was a blank text box with one input and one output. Agents require articulating a goal, delegating execution, and trusting a multi-step process without watching — a much higher cognitive and trust bar.
- **Why agents haven't gone mainstream — distribution gap**: Enterprise has IT departments, defined workflows, and the ability to mandate adoption. Consumers have to discover agents themselves and self-motivate through the friction. Nobody is forcing your parents to set up an AI agent.
- **Consumer agent breakout is coming, but timing is uncertain**: Belceto believes it will happen; product people building consumer products need to decide whether they make that same bet and plan accordingly.

## Use cases
- **Enterprise product builders**: Deciding whether to build Slack/Teams-native integrations or MCP support rather than standalone AI dashboards.
- **Salesforce/CRM-adjacent product teams**: Understanding how Agentforce + Slack changes the competitive landscape for enterprise productivity tools.
- **PMs doing prioritization reviews**: Auditing the backlog for features killed due to AI inference cost that are now worth revisiting.
- **Founders or PMs setting AI infrastructure strategy**: Deciding where the real moat is now that model quality is commoditizing.
- **Consumer product builders**: Assessing whether to invest in agent-based features now or wait for mainstream UX patterns to emerge.
- **Sales/CS leaders at B2B companies**: Proactively asking reps what they're hearing about enterprise AI adoption among customers, rather than assuming customers aren't ready.
- **AI product designers**: Thinking about how to reduce the UX friction of goal-setting and trust-building that currently blocks agent adoption.
- **Budget owners using AI APIs**: Reassessing cost models and renegotiating or re-architecting around new pricing tiers.

## Patterns & frameworks

**"Agents where people live" principle**
The insight that AI agents only deliver value when they operate in the same environment where people already spend their day. If agents live in a separate tool, adoption suffers regardless of capability. The Slack MCP integration is the applied version: bring the agent to the workflow, not the other way around. Applicable when designing where AI features surface in a product.

**"Revisit the killed-for-cost backlog" process**
A concrete prioritization practice: when AI inference costs drop significantly, systematically re-examine features that were deprioritized because the economics didn't work. Cost was a constraint, not a strategic decision — removing the constraint changes the calculus. Treat pricing shifts as a trigger for backlog review.

**"AI as infrastructure" mental model**
Frames AI capability (model quality, inference) as becoming commodity infrastructure — like cloud compute or storage — rather than a differentiator. The implication: moats must be built on data, distribution, and customer relationships, not on access to capable AI. Useful for competitive positioning and roadmap strategy.

**"Interface barrier to viral adoption" framework**
Drawn from the ChatGPT vs. agents comparison: the simpler and more familiar the interface, the lower the barrier to mainstream adoption. ChatGPT succeeded because it was a single text box. Agents fail to cross over because they require goal articulation, delegation, and trust in autonomous execution — a multi-step cognitive ask. Use this to evaluate whether a product's UX is accessible enough for non-technical users.

**"Enterprise forces adoption; consumers must self-discover" distribution model**
Enterprise adoption is accelerated by IT mandates and defined workflows — friction is overcome by organizational pressure. Consumer adoption requires self-motivated discovery and tolerance for early friction, making distribution the primary challenge. Relevant when deciding whether to target enterprise vs. consumer first for an agent-based product.