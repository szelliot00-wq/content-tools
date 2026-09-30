# Anthropic CPO’s: Nobody knows what the right product looks like (yet)

Video ID: `sEXdyK6woKU`

## Summary
This panel discussion features Anthropic's Chief Product Officers (Amy and Mike) in conversation with a moderator at what appears to be a product management conference. They explore how the PM role is evolving in the age of rapidly advancing AI, how Anthropic approaches building AI-native products, and what it means to navigate a technology landscape that changes every two months. The video is most relevant to product managers, startup founders, and engineering leaders trying to understand how to build effectively in an era of AI agents and malleable software.

## Key insights

- **The PM role is not going away — it's becoming more critical.** Mike described a real moment where he resisted adding a PM to a shipping project ("Claude's got it"), was overruled, and a week later texted the PM lead to say she was 100% right. The PM provided essential connective tissue: looping in safeguards, enabling the customer success team, keeping stakeholders aligned, and freeing engineers to stay heads-down.

- **The core job of product hasn't changed; the technology underneath it has.** The PM's role is still to bridge real human problems with available technology. What's changed is that the technology now shifts every two months instead of every five to ten years, requiring constant re-evaluation of what you know and how you work.

- **Skills that took decades to build can become obsolete overnight.** Amy described spending years developing deep expertise in user mental models — knowing exactly where a user's thumb goes on their phone, what situation they're in when they pull it out of their pocket. That skill is now largely irrelevant because it's faster to just build three versions and test them. She used this as a metaphor for the "innovator's dilemma at the personal level."

- **Adaptability, judgment, and relentlessness are the new core PM skills.** Rather than deep expertise in a specific technology paradigm, the most valuable traits are: tolerance for ambiguity, willingness to throw away what you know about yourself in the role, and relentless follow-through despite constant forking paths.

- **"Framing the chaos" is a leadership responsibility.** Amy discussed how, during periods of uncertainty, people are tempted to over-map the future to feel in control. Instead, leaders should make ambiguity feel safe and explorable — explicitly naming that everyone is figuring things out in the dark and that parallel exploration is intentional, not a sign of dysfunction.

- **Agent-native architecture means: everything a human can do, an agent should be able to do.** Mike described the evolution from "AI in a sidebar" → "AI-powered features" → "agent-native products." The key primitive is shared plumbing: a single infrastructure layer that both human-facing UIs and agent/API calls flow through, so agents can access the same capabilities without bolted-on integrations.

- **Malleable software is becoming real.** Mike described Anthropic using Claude to build and maintain the project management UI for a complex 4-stream initiative in real time — the UI itself is generated and updated by Claude, and teams can change it on the fly. He sees this as "one of the biggest shifts in how we've worked in the last year."

- **Shared primitives prevent fragmentation across parallel experiments.** Six months prior, Claude.ai chat and co-work had separate memory systems, separate MCP implementations, and separate file storage. That made every new experiment feel disconnected from the start. A dedicated foundations team now ensures shared memory, shared MCP, and shared storage across all product surfaces.

- **Park projects instead of killing them — and build evals.** Anthropic built an early computer use product in 2024 that was unusable. Rather than abandoning it, they ran it continuously in an eval harness against every new model. They discovered Claude 3.7 was a capability leap specifically because the eval suddenly showed it succeeding more often than failing. The lesson: if your project proves the models aren't ready yet and you can externalize that as an eval, that's a win.

- **"Capability blindness" is a real risk.** If you try something once with an older model and never revisit it, you risk concluding the models "can never do this" right before a new model makes it trivially easy. Amy called this out explicitly — Sonnet 4.5 users may have completely different conclusions than current-model users.

- **There's a strong power law in tab/feature usage.** Drawing from Instagram experience, Mike noted that the main feed was ~80% of usage; Explore went from 10% to maybe 15% no matter how much it improved. The product leadership question is always: what is your "main tab" — the dominant experience — and how do you make that great, while not prematurely killing experiments that could eventually be folded in.

- **Claude as a "convenor" is not yet real, but is coming.** Mike described a future where Claude schedules meetings between people it thinks should talk. That hasn't happened yet — not because it's technically impossible, but because the organizational permission/setting hasn't been turned on.

- **The gap between model capability and actual usage is the biggest unsolved problem.** Mike framed the core product challenge for the next year as closing the gap between what models can do and what most people are actually using them for — not for "Claude-pilled" power users with multi-agent setups, but for the researcher, the small business owner, the person managing complex long-horizon work.

## Use cases

- **PMs deciding whether to add a PM to an AI-heavy team** — Mike's "do we even need a PM?" story is directly applicable; the answer is yes, especially for cross-functional connective tissue.
- **Product leaders managing parallel experiments without demoralizing teams** — Amy and Mike's frameworks for parallel bets, shared infrastructure, and explicit communication apply directly.
- **SaaS companies deciding how to add AI/agent capabilities** — Mike's primitive-first architecture advice is a practical guide for companies that don't want to "bolt on" AI.
- **PMs at companies where model capabilities are changing faster than product cycles** — the "park and eval" strategy is directly actionable.
- **Engineering leads or founders acting as de facto PMs** — Mike's personal story of resisting PM involvement is a cautionary tale for technical founders.
- **Product leaders managing the personal/identity challenge of rapid skill deprecation** — Amy's discussion of the "innovator's dilemma at the personal level" is directly relevant.
- **Organizations trying to consolidate multiple AI products into a coherent UX** — the primitives/foundations team model and the tab power-law framework apply.
- **Leaders communicating strategy during periods of high ambiguity** — the "frame the chaos" mental model is immediately applicable in all-hands or team settings.

## Patterns & frameworks

**The PM Bridge (unchanged core, changing tools)**
The PM's job is always to bridge real human problems with available technology. What changes is the technology side, not the human-problem side. The implication: stay obsessed with user problems, but treat your knowledge of how to solve them as disposable and up for renewal every two months.

**The Innovator's Dilemma at the Personal Level**
Just as companies over-invest in existing competencies and miss the next wave, individual PMs do the same with their own skills. Amy applied Clayton Christensen's company-level framework to individuals: your expertise in one paradigm can actively prevent you from developing expertise in the next one.

**Frame the Chaos (psychological safety for ambiguity)**
Rather than trying to eliminate uncertainty by over-planning, leaders should make uncertainty feel safe and navigable. Tactics: name it out loud, acknowledge the emotional difficulty, emphasize that everyone is in the same situation, and position ambiguity as where the productivity and magic actually lives.

**Park + Eval (capability-gated project management)**
When a project fails because models aren't ready, don't kill it — park it and encode what "success looks like" as an eval that runs against every new model automatically. This lets you detect capability leaps as they happen (as Anthropic did with computer use and Claude 3.7) and re-activate the project at the right moment.

**Shared Primitives First (agent-native architecture)**
Before building agent-facing features, build shared infrastructure that all surfaces — human UI, agent calls, REST API — flow through equally. Memory, file storage, and MCP should be unified across products. This is the precondition for experiments feeling complementary rather than fragmented, and for agents to do "everything a human can do."

**DRI / Bet Lead Model**
In high-ambiguity environments, pair exploratory freedom with clear decision authority. Every parallel "bet" needs a single person (the bet lead or DRI) who owns the go/no-go call, resource allocation, and escalation. This prevents the "lost together with no compass" failure mode.

**Power Law Tab Strategy**
Drawn from Instagram: usage of product surfaces follows a strong power law (main surface ~80%, secondary surfaces ~10–15% regardless of investment). The practical framework: identify your "main tab" and protect it; run experiments in secondary surfaces without prematurely killing them; fold proven experiments back into the main surface rather than perpetuating tab proliferation.