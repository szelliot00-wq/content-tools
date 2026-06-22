# The eng lead behind Claude Code and Cowork on the new way to ship software | Fiona Fung

Video ID: `Ybrl4FYM57c`

## Summary
This episode of Lenny's Podcast features Fiona Fung, VP of Engineering at Anthropic overseeing Claude Code and Cowork, in a deep conversation about how AI is transforming software engineering teams. Fiona draws on 25+ years of engineering experience — from IBM and Microsoft (Visual Studio, TypeScript) to Meta (Marketplace, AR/VR) — to argue that coding is no longer the bottleneck, and the new challenges are verification, quality, team culture, and role-blurring. The episode is most relevant to engineering managers, PMs, and product leaders trying to understand what high-functioning AI-native teams actually look like in 2025–2026.

## Key insights
- **8x code output**: Anthropic engineers ship 8x as much code per quarter compared to 2021–2025, with a hockey-stick inflection visible in the data. This isn't just engineers — PMs, designers, and managers are all committing code.
- **Coding is no longer the bottleneck; verification is**: The constraint has shifted from writing code to ensuring that the massive volume of AI-generated code is correct, safe, and aligned with product goals. Quality and monitoring infrastructure become more critical than ever.
- **The two hiring profiles that matter now**: (1) Creative builders with product sense — "dreamers" who own a product end-to-end, iterate on feedback, and polish the experience; (2) Deep systems experts for the hard parts — e.g., distributed systems, mobile — where trust-but-verify still requires human expertise.
- **Specs in the repo as a verification framework**: Fiona's approach to automated code review is to check in specs ("what good looks like") directly into the repository, then have Claude Code validate that new code matches those specs. This is the evolution of test-driven development — instead of writing tests first, you write the standard first.
- **Routines as the next abstraction layer**: Fiona describes moving from synchronous prompting → async agent-spawning → routines (scheduled agents that generate their own prompts and kick off sub-agents automatically). Her morning routine now generates PR summaries, bug themes, and polish fixes before she wakes up.
- **Management via Claude**: She maintains a persistent Claude Code remote session enlisted across all repos with access to Slack channels and metrics. She uses it to run monthly retrospectives with her team — "what shipped, how did it do, what bugs did we cause?" — replacing manual bullet-list reviews.
- **Bad vs. Sad framework**: Each team defines what constitutes a "bad" experience (irrecoverable, e.g., crash) vs. a "sad" experience (recoverable but painful, e.g., flickering). Stacked "sads" can become a "bad." This gives a cross-surface quality vocabulary without requiring uniform dashboards.
- **High agency + high accountability**: The Claude Code team values individual agency highly, but pairs it explicitly with accountability. Engineers are expected to own the hypothesis for what they're solving, not just ship code.
- **Pairwise programming lunches**: As agents became the primary collaborator, engineers started feeling lonely. The team introduced pair-programming lunch sessions not to write code together, but to watch each other work — discovering that everyone uses Claude Code differently and learns from observing others.
- **Player-coach manager onboarding**: New managers are required to start as ICs before taking on people responsibilities. This builds rapport with the team, grounds them in the product, and avoids the trap of immediately reaching for "manager-y things."
- **Latent demand as a discovery engine**: Anthropic found the Cowork opportunity by noticing that non-coders were already using Claude Code. The pattern: watch for people jumping through hoops to make something work, then build a smoother experience around that behavior.
- **JIT planning (Just-in-Time)**: The team dropped 6-month roadmaps in favor of a lightweight monthly spreadsheet of priorities, with a weekly check-in to confirm they're still relevant. Even this is being evaluated for further automation.
- **Explicit permission to kill processes**: A stated team value — teams are encouraged to identify processes that are "expensive, noisy, or no longer serving their purpose" and kill them. The 6-month roadmap was one Fiona herself introduced and then killed.
- **Swear-word dashboard**: An engineer built a dashboard tracking profanity in user sessions as a proxy for user frustration — a creative, qualitative signal for UX quality.
- **Metrics can become traps**: Fiona's Marketplace example: early expansion gating on "number of sellers" failed to account for power sellers. The metric was wrong for the reality. Her principle: always ask if the metric is still serving the intended outcome, especially as the landscape shifts.
- **Don't confuse motion for progress**: Measuring token usage or lines of code is like the old lines-of-code metric — it captures activity, not outcomes. Focus on whether the output is driving the actual desired result.
- **Context-switching load is increasing**: Running many async agents creates a new cognitive burden — you have to catch up on parallel workstreams. Fiona now blocks dedicated "focus time" not for coding but for reviewing async agent outputs.
- **Fear → lean in**: For engineers resisting AI, Fiona's advice is to identify what is within your control and take one action in that direction. Fear paired with a sense of helplessness creates frustration; agency reduces it.
- **The loneliness problem**: Working with agents is increasingly a solo experience. Intentional team rituals (pair programming lunches, hackathons) are needed to preserve the human collaboration layer.
- **Role blurring**: Engineering, PM, design are converging. PMs ship features when engineers are unavailable. Engineers own product quality end-to-end. The "role" may come to mean simply: the average of what you spend your time doing.
- **Skilling concern for new engineers**: Fiona is genuinely uncertain how the next generation learns foundational engineering skills (the "double-click" on dependencies) if they never have to write code. She speculates fellowship/apprenticeship models may be needed.
- **Model improvements unlock previously failed automations**: Engineers who tried to automate something and found the model wasn't ready should revisit those experiments with newer models — capabilities compound quickly.

## Use cases
- **Engineering managers** wanting to stay on top of high-velocity shipping without reading every PR manually
- **Team leads** designing code review processes that scale beyond human bandwidth
- **PMs and designers** considering how to contribute code and take on broader product ownership
- **Small business owners** looking for practical AI use cases (expense management, menu pricing analysis, document organization)
- **Hiring managers** rethinking what profiles to recruit for in an AI-assisted engineering world
- **Organizations rolling out AI tooling** trying to measure ROI and productivity without falling into vanity metrics
- **Engineering leaders onboarding** to a new team or codebase and wanting a faster ramp-up approach
- **Anyone struggling with AI adoption resistance** on their team, looking for a framework to help people lean in
- **Leaders scaling a team rapidly** and worried about cultural drift
- **Engineers feeling lonely or displaced** by agent-based workflows looking for ways to restore team collaboration

## Patterns & frameworks

**Bad vs. Sad Quality Framework**
Each team defines: "bad" = an irrecoverable error (e.g., crash, data loss) and "sad" = a recoverable pain point (e.g., flickering UI). Teams self-assign what constitutes each in their surface area. This creates a shared quality vocabulary across diverse product surfaces without forcing uniform metrics. Accumulated "sads" are treated as a leading indicator of potential "bads."

**Specs-in-Repo as Automated Review Standard**
Write the definition of "what good looks like" (content design specs, behavior specs, etc.) directly into the repository and keep them in sync with the code. Claude Code review then validates new code against those specs. This extends test-driven development from "write tests first" to "write the standard first."

**Routines (Async Agent Orchestration)**
A progression: synchronous prompting → asynchronous agent spawning → scheduled routines that autonomously generate prompts and spawn sub-agents. Fiona's morning routine scans feedback channels, identifies themes, and produces PRs for review before she starts her day. The abstraction level keeps rising — you're no longer prompting, you're authoring agents that prompt.

**Trust But Verify**
Used for both people and models. High agency is granted, but paired with accountability structures (hypothesis-setting, outcome tracking). For AI-generated code, the same principle applies: let the model do the work, but maintain deep expertise in the areas where verification still requires human judgment.

**JIT Planning (Just-in-Time Planning)**
Monthly cadence replacing 6-month roadmaps. A lightweight shared spreadsheet of the month's priorities, reviewed weekly to confirm relevance. Themes for 6-month horizons are discussed at all-hands-style team gatherings, but detailed planning stays short-horizon given how fast the landscape shifts.

**Latent Demand Discovery**
Watch for users adopting a product in unintended ways or jumping through hoops to accomplish something the product doesn't natively support well. Treat this as a product signal: if people are forcing a behavior, there's likely a smoother experience waiting to be built. Applied at Anthropic to find the Cowork opportunity from non-coder Claude Code usage.

**Player-Coach Manager Onboarding**
New managers join as ICs first, spending initial weeks/months in the code/product before taking on people responsibilities. Builds technical credibility, product intuition, and team rapport before the cognitive load of management is added. Reduces the instinct to immediately deploy "manager-y" behaviors before understanding the team's reality.

**Growth Mindset + Fear → Control Mapping**
When fear or frustration appears, map it: what is within my control? What is one action I can take? Reframe from "this is happening to me" to "what can I do about it?" Used both as personal advice and as a leadership framework for helping resistant team members adopt AI tooling.

**High Agency + High Accountability**
Paired explicitly as two sides of the same coin. Engineers are given broad latitude to identify problems and propose solutions. In exchange, they own the hypothesis ("what are we trying to solve?"), the outcome, and the post-ship accountability. Not just "go build stuff" — "go build stuff and own whether it worked."