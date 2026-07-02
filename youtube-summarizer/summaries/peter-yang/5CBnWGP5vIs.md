# Claude Fable 5 Is Finally Back: 5 Must-Try Use Cases Before July 7

Video ID: `5CBnWGP5vIs`

## Summary
The video is a practical walkthrough by a creator/developer who demonstrates five high-value use cases for Claude Fable 5, framed around the model's return after an 18-day government ban and its limited availability through July 7th on Claude subscriptions. The core argument is that Fable's strength lies in synthesizing large amounts of context — code, business data, personal files — to extract insights and produce detailed plans, making it worth reserving for high-leverage "deep thinking" tasks rather than routine work. The presenter uses his own live projects (a fitness app, a personal OS skill system, a creator business) as real demos throughout. The video is most relevant to indie hackers, solopreneurs, and developer-creators who use Claude heavily and want to maximize a scarce, premium model allocation.

## Key insights
- Fable 5 is available on Claude subscriptions only until July 7th, and only until you hit 50% of your weekly usage limit — after that, it's pay-as-you-go API only, making token conservation critical.
- The presenter recommends sticking to "high effort" mode rather than "Ultra Code" to avoid burning through limits too quickly.
- Fable can self-direct by scanning your memory and projects to suggest what tasks it's best suited for — essentially finding "Fable-worthy work" for you.
- For business/life advice, the presenter uses a structured plan document with sections for: annual goal, decision-making principles, business positioning, competitor landscape, energy audit, and financial context.
- Connecting Fable to live APIs and MCPs (Mercury for bank data, Substack for newsletter stats, YouTube analytics, Vercel for web analytics, Google Workspace) dramatically improves the quality of business advice by grounding it in real data.
- The presenter built a custom "advisor skill" that escalates to a "council skill" — three AI personas (target customer, skeptic, execution-minded operator) that debate each other to surface additional insights.
- On a vibe-coded fitness app (built primarily with Codex and GPT-5.5), Fable spun up five parallel agents, ran all unit tests, and found 12+ major bugs — including a cross-user data leak on involuntary sign-out — that GPT-5.5 and Opus missed.
- For feature planning, Fable used web search to find a free USDA FDC food nutrition API, generated a full HTML plan including a proposed UI design, architecture decisions, data model, risk flags, and open questions.
- The HTML plan can be annotated like a Google Doc using an open-source tool called "Lavish Editor" (a free GitHub repo), allowing inline comments that get fed back to Fable.
- For codebase refactoring, the presenter references Stripe using Fable to refactor 50 million lines of Ruby code in one day — a task estimated to take a human team two months.
- Fable audited 40+ personal AI skills across the presenter's personal OS, spinning five agents and finding 13 improvement opportunities including dead code blocks, ambiguous instructions, stale temporary files, and missing evaluation logic.
- Cheaper models (Opus, GPT) should be used for prep work — hooking up APIs, drafting initial documents — before handing off to Fable.

## Use cases
- **Solopreneurs and creators** who want strategic business advice grounded in their actual revenue, subscriber, and content data via live API connections.
- **Indie developers** with "vibe coded" projects who need a rigorous pre-launch bug audit beyond what standard testing catches.
- **Anyone with a large personal knowledge system** (skills, prompts, documents) that has accumulated technical debt and needs consolidation.
- **Product managers and developers** who want a detailed feature plan — including UI mockups, architecture decisions, risk flags, and acceptance criteria — that a cheaper model can then execute.
- **Creators with large content archives** who want to mine past work for repurposing opportunities, theme analysis, or content roadmap generation.
- **Teams considering large-scale refactors or migrations** where Fable's multi-agent code analysis can compress weeks of human effort into hours.
- **Power Claude users** who want to self-audit what tasks are actually worth using a premium model on, rather than guessing.

## Patterns & frameworks

**The "Fable-worthy work" discovery prompt**
Ask Fable to scan your memory and existing projects and return the top 5 tasks it thinks require deep thinking. This turns the model into a meta-advisor that surfaces high-leverage uses you may not have considered, rather than you having to guess.

**The Plan Document framework (for business/life advice)**
A structured context document with six sections: (1) annual goal, (2) decision principles, (3) business positioning and competitors, (4) energy audit (what energizes vs. drains), (5) financial context, (6) additional life context. This is paired with live API/MCP connections so Fable can pull real-time data to supplement the static document.

**Advisor → Council escalation pattern**
A two-tier skill system: a personal "advisor" skill handles most queries, but escalates to a "council" skill when stuck. The council runs three personas simultaneously — the target customer, a skeptic, and an execution-minded operator — who debate the problem to generate diverse perspectives and surface blind spots.

**Plan with Fable, execute with a cheaper model**
Use Fable's deep reasoning to produce a highly detailed plan (HTML or Markdown) including architecture, UI design, data models, risks, and open questions. Then hand the plan to a cheaper/faster model (Opus, GPT) for step-by-step implementation. This preserves Fable's token allocation for strategic work.

**Prep with cheaper models first**
Before engaging Fable, use Opus or GPT to handle all the grunt work: hooking up APIs and MCPs, drafting initial documents, and structuring context. Fable should enter a conversation that is already fully prepped, not one that requires setup.

**Token conservation discipline**
Use "high effort" mode rather than "Ultra Code" to extend available usage. Babysit Fable's agentic runs to catch looping or rabbit-holing behavior early. Avoid assigning Fable tasks that consume a full context window in one shot (e.g., mining a 3-year content archive) when the token budget is constrained.