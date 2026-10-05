# Head of ChatGPT on Dots, ambient AI, and why most actions on the internet will soon be taken by AI

Video ID: `MM-C3JqCXBk`

## Summary
This is an interview with Thibault (Head of ChatGPT at OpenAI), recorded live at DevDay, covering OpenAI's new product "Dots" (a persistent ambient AI agent), the agentic future of the internet, and what builders are underestimating about where AI is heading. The core argument is that AI is transitioning from a tool you actively prompt to a persistent intelligence that runs 24/7, knows your goals, and takes actions on your behalf across all your devices. Most relevant to product managers, founders, engineers, and anyone building software products or thinking about their career in an AI-native world.

## Key insights
- **Most internet actions will be taken by agents.** Thibault considers this one of the most underpriced facts in tech: the majority of traffic and actions on the internet will soon originate from AI agents, not humans — with major implications for how products need to be architected and scaled.
- **Dots is OpenAI's bet on ambient AI.** Dots is a persistent AI agent (currently one per user, with multi-dot support coming soon) that runs 24/7, learns your preferences, connects to your apps and devices, and proactively reaches out when relevant — e.g., it pinged Thibault 5 minutes before a live demo when production went down.
- **Agent team size oscillates with model capability.** As models improve, a single larger agent can handle what previously required a team of parallel agents, causing a recurring cycle: expand agent teams → model breakthrough → shrink back to one powerful agent → expand again.
- **Loops and graphs are the wrong abstraction.** Manually configuring agentic loops is a transitional pattern people got excited about but won't be the long-term paradigm. The goal is a system that learns what you want without you having to think about routing or orchestration.
- **Dots will eventually merge with ChatGPT.** The Chat/Work split is being collapsed. All Dots capabilities will eventually roll into the main ChatGPT product for 1.2 billion users. Dots has no model picker — intentionally zero configuration.
- **The ecosystem/plugin platform is the sleeper hit.** OpenAI signed 16 partners for Sign-in with ChatGPT and is opening plugin distribution to potentially 1.2 billion users, with revenue share for popular plugins. Discovery is driven by retention metrics, not SEO-style keyword optimization.
- **Specialist Dots run on dedicated hardware with guardrails.** Some run on Mac Minis. The key architectural difference: the harness runs off-device (not on your machine), and one Dot can connect to and control multiple devices simultaneously — described as "a little bit like an octopus."
- **Safety investment is substantial and growing.** A significant and increasing portion of compute goes to secondary monitoring systems that watch the primary agent for high-risk actions or prompt injection, not just to the agent doing work. OpenAI deliberately held back a more capable model (six-one Astra) rather than release it.
- **Skills trending up: taste, builder mentality, user empathy.** Skills trending down: typing fast. Over 120 ex-YC founders work at OpenAI. PMs are well-positioned because "where should we build, help build it, is this great?" is the core loop of the current era.
- **New grads have a structural advantage.** Younger workers haven't built entrenched habits, can go all-in on AI workflows, and absorb new tools faster. Ahmed Ibrahim (joined as new grad, now heads OpenAI's compute fleet and applied work) is cited as the exemplar.
- **Voice was an underestimated modality.** Thibault did not anticipate how much he'd shift to voice/dictation for interacting with AI. The "flow state" he lost from hands-on coding has returned via ultra-fast voice-driven AI interaction.
- **Configuration fatigue is a real product problem.** Even Thibault finds model pickers, reasoning effort sliders, and multi-agent toggles exhausting. The goal is to make the interface "almost completely disappear."
- **Loneliness and context-switching fatigue are real side effects.** Engineers are spending more time talking to agents than humans. The long-term fix is ambient AI embedded in physical space (projected on walls, voice-native, collaborative with other humans in the room) rather than screen-bound solo sessions.
- **Models progressed faster than expected.** Thibault expected today's capability level (Astra-class) to arrive 1–2 years later than it actually did, forcing a revision of planning priors.
- **OpenAI culture is highly bottoms-up.** The Decisions API, for example, started as four people hacking on a Slack channel over a weekend. Launches are held back when quality isn't ready — several DevDay features were pulled at the last minute to ship later.

## Use cases
- **Founders and PMs building SaaS products:** Must start designing for agent-first traffic patterns, not just human users — especially around scale, MCP integrations, and API economics.
- **Plugin/extension developers:** Understanding that retention (not SEO or marketing) drives plugin discovery and recommendation within ChatGPT.
- **Engineering leaders evaluating AI tooling:** Deciding whether to invest in agentic workflows vs. waiting for single-model capability improvements to make multi-agent orchestration unnecessary.
- **Career-changers or new grads:** Identifying which skills to build (taste, builder mindset, cross-discipline fluency) vs. deprioritize (narrow specialization in one role like "only design" or "only code").
- **Product teams thinking about AI UX:** Reducing configuration complexity, model pickers, and cognitive load for end users — designing toward "the interface disappears."
- **Anyone managing their own productivity with AI:** Building personal agent stacks (multiple Dots with specific roles, like one for Twitter monitoring) and thinking about how to avoid context-switching fatigue and loneliness.
- **Enterprise builders:** Understanding how Sign-in with ChatGPT and plugin economics work for distribution to 1.2B users with revenue share.

## Patterns & frameworks

**The Agent Team Expansion-Shrinkage Cycle**
When models improve dramatically, a single agent can hold more context and do more work, making a team of parallel agents redundant — so the team shrinks. As demands push past that new agent's limits, the team expands again. This cycle repeats with each model generation. Implication: don't over-invest in complex multi-agent orchestration infrastructure; it may collapse into a simpler pattern with the next breakthrough.

**Dots as the "Primary Dot + Specialist Dots" Model**
One primary Dot learns your deepest preferences and handles general work; additional specialist Dots are configured for high-volume, focused tasks (e.g., Twitter monitoring) with their own guardrails and potentially dedicated hardware. This is OpenAI's model for building a "virtual team" without manual orchestration.

**Retention-Driven Plugin Discovery**
Plugin/extension ranking inside ChatGPT is determined by user retention metrics and quality signals — not keyword optimization or marketing. Build something genuinely useful that users return to; the platform surfaces it. Stop using it → it stops being recommended.

**The Ambient AI Vision ("Star Trek Computer")**
The long-term UX paradigm: AI is present in physical space, voice-native, observable (can see a whiteboard sketch), collaborative with humans in the room, available when needed and invisible when not. No screen glue, no prompt engineering, no model selection. Referenced anchors: Star Trek, Neuromancer, the film *Her*.

**Pacing the Frontier = Hardening, Not Slowing**
"Pacing" at OpenAI doesn't mean slowing capability development; it means investing disproportionately in alignment, safety, and monitoring infrastructure — specifically secondary compute layers that watch the primary agent for risky behavior or prompt injection in real time — before releasing the next capability tier.

**The Bottoms-Up Shipping Loop (OpenAI internal)**
Idea surfaces in a Slack channel → small team hacks on it over a weekend → internal dogfood → excitement builds → others contribute → quality bar review → ship or hold. No formal approval chain. Autonomy is total; accountability is personal ("you own up to it").