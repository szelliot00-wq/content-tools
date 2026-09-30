# Context is now the product: Product leadership when software can build itself | Karri Saarinen

Video ID: `Zn9NZ-r1-C4`

## Summary
Karri Saarinen, co-founder of Linear, argues that as AI tools commoditize software execution, the true competitive advantage for product organizations shifts to *context* — the accumulated understanding of customers, problems, and product quality that drives good decisions. He warns against organizations becoming "software factories" that optimize for output while losing the learning that comes from hands-on building. The talk is most relevant to product managers, engineering leaders, and founders navigating how to responsibly integrate AI into their product development process without hollowing out their team's judgment and intuition.

## Key insights
- **Watching tools ≠ making better things.** After a summer away from AI news, Saarinen returned to find nothing fundamentally changed about the difficulty of building great products — suggesting the industry's obsession with new models and agents may be misallocated attention.
- **Output is not the product.** Customers don't buy lines of code, experiments, or process efficiency. They buy something they want. Optimizing for output without improving the product experience is a category error.
- **Building produces two things: the product and the learning.** The effort of figuring out what to build — talking to customers, struggling with decisions — creates compounding knowledge. Automating execution without preserving this learning loop risks eroding the team's understanding over time.
- **Great products come from great teams with great context.** A team's accumulated understanding of the customer, the problem space, technology, judgment, and taste is what enables consistently good product decisions. This is harder to replicate than the software itself.
- **Automate the known, preserve the learning.** Linear uses AI to automate repetitive tasks like bug investigation (via a "winner loop" connecting to Sentry and the codebase), freeing engineers — but the freed time should go toward customers and exploration, not more execution.
- **AI as a context-building tool, not just an execution tool.** Linear collects customer feedback from sales calls, support emails, and internal discussions into a centralized system, then uses AI agents to surface relevant signals — e.g., a daily briefing on what customers are saying about AI workflows.
- **Intuition is trained, not innate.** Saarinen explicitly rejects the idea of intuition as a magical quality. It is the accumulated result of listening, learning, and working closely with customers. The more context a person absorbs, the better their intuition — and this compounds at the team level.
- **Siloing with AI is a risk.** As more people work alone with their own agents, cross-team learning diminishes. Intentional shared practices are needed to counter this.
- **Context as the new product work.** In the future, product organization work may shift away from execution toward managing, curating, and learning from shared context — with AI doing more of the building while humans focus on judgment, quality, and customer understanding.

## Use cases
- **Product leaders** deciding how to restructure team rituals and workflows as AI takes over more execution tasks.
- **Engineering managers** figuring out where engineers should redirect saved time when AI handles bug triage or boilerplate work.
- **Founders and execs** evaluating whether their organization is becoming a "software factory" that ships fast but loses product intuition.
- **Growing teams** where new hires don't share the same quality standards or product context as early employees.
- **Anyone building an internal knowledge/context system** to capture customer feedback and make it accessible to both people and AI agents.
- **Teams building or evaluating AI-powered features** who want to learn from customer usage patterns rather than guessing at best practices.
- **Orgs experiencing over-specialization and process bloat** (a pre-AI problem that AI can either solve or worsen, depending on how it's applied).

## Patterns & frameworks

**The Two Outputs of Building**
Every product development effort produces two things: the artifact (feature, fix, design) and the learning (customer understanding, judgment, taste). The risk with heavy automation is retaining the artifact while discarding the learning. Organizations should deliberately design to preserve both.

**Automate Known / Preserve Learning**
A decision heuristic: tasks that are repeatable, well-defined, and low-learning-value (e.g., bug investigation) are good automation candidates. Tasks that build team judgment, customer intuition, or product taste should remain human-led or at minimum human-reviewed.

**Linear's Bug Investigation Loop ("winner loop")**
An AI agent automatically investigates bugs by connecting to Sentry, the data layer, and the codebase, identifies the source, and proposes a fix. Engineers verify and sometimes adjust the output. Execution is automated; judgment is retained.

**Customer Context Pipeline**
Automated collection of customer signals (sales calls, support emails, internal discussions) into a centralized repository. AI agents then "watch" this context and surface relevant briefings — e.g., a daily digest of what customers are saying about AI workflows. Makes staying close to the customer scalable without requiring manual triage.

**Quality Wednesday**
A weekly ritual where every team member finds one quality defect in the product and fixes it — however small (a hover state, a copy error, an animation). The primary value is not the fixes themselves but the shared practice of training everyone's eye for quality. Findings are shared in a meeting so the whole team learns from each other's observations.

**Feature Roast**
An optional open critique session for new features. Anyone in the company can join and give raw, nitpicky feedback on a feature before it ships. The team building the feature hosts and can ask clarifying questions. The lead then synthesizes feedback into actionable issues. Functions as a forcing function for empathy — confusion from internal attendees predicts confusion from real users.

**Context as Compounding Asset**
Borrowed from the Formula 1 steering wheel example: over decades, F1 teams learned the precise requirements of their use case and built a radically optimized artifact. The same compounding applies to product teams — the more context they accumulate and act on, the better their future decisions. The implication is that context (not code) is the durable competitive asset.