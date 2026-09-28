# We Built Grok Bot. Here Are Our 14 Best Bots | Peng Zheng & Lauren Tan

Video ID: `xZ5TEaleUdg`

## Summary

This video features Peng Zheng (designer/design staff) and Lauren Tan (technical staff) from the Grokbot team at xAI, walking through their personal and professional Grokbot setups. The conversation covers how they use persistent, named AI bots to automate complex multi-step workflows across work and life, from buying 3D printing filament to booking international flights to orchestrating massive engineering agent swarms. The core argument is that Grokbot's model — persistent, named agents with their own memory, tools, and identities — represents a paradigm shift from "prompting AI" toward "designing systems of agents," and trust-building is the critical bottleneck to unlocking that value. Most relevant to product managers, engineers, and designers who want to move beyond one-shot AI prompting into durable, autonomous agentic workflows.

---

## Key insights

- **Chief of Staff bot as a universal router:** Both Peng and Lauren use a "chief of staff" bot as the default inbox — if you don't know which bot should handle a task, send it there and it delegates.
- **Chaining tasks in a single prompt is a superpower:** Peng demonstrated selling a DJI mic on Facebook Marketplace by giving one prompt that included: check official pricing, find local competitor prices, review past listing writing style (by consulting the writer bot), post the listing, and then automatically reduce the price by $5 weekly if no interest.
- **Bots can consult other bots mid-task:** When the chief of staff bot needed to write a marketplace listing, it automatically messaged Peng's writer bot to learn his past writing style — cross-bot context sharing without human intervention.
- **Group chats with multiple bots for ideation:** Peng creates group chats with PM, design, and engineering bots to debate and ideate on a concept (e.g., "build a cat meow translator app") — each bot contributes from its own perspective, and you can @mention a specific bot to get a targeted reply.
- **Bot identity is persistent across projects:** The same designer bot works across multiple separate project chats, maintains context in all of them simultaneously, and its "work status" is visible in its own DM — it's the same entity, not a copy.
- **Peng's design workflow: do 5%, delegate 95%:** Rather than drawing everything in Figma, Peng builds the system, creates one key frame, then asks the designer bot (connected via Figma MCP) to scale it into a full end-to-end flow using correct design tokens, colors, and typography.
- **Lauren's engineering setup is a hierarchical agent swarm:** Chief of staff → engineer lead (whose explicit rule is "never do work yourself, only delegate") → three engineer bots → cloud agents (Claude agents or Cursor agents). This structure lets Lauren orchestrate massive parallel workstreams from a single high-level instruction.
- **Auto-merge PRs without review:** Lauren has made the Grokbot codebase sufficiently "agent-friendly" that she sometimes doesn't look at a PR until after it has already landed and merged, relying on the agent swarm's eval and review pipeline.
- **Dr. Eggbot — a bot that designs and audits other bots:** Lauren has a meta-bot that reviews all her other bots' transcripts, proposes improvements (new skills, new bots, routine changes), and audits routine frequency to prevent excessive token usage from over-eager wakeup schedules.
- **Lauren booked a complex multi-leg international trip entirely through Suki (her personal assistant bot):** OC → Denver → London → Amsterdam → home, including hotels near the venue, using the corporate Navan travel tool — all from a single Slack message link with conference details.
- **Bots can have their own phone numbers:** Lauren gave Suki a third-party phone number so the bot could text her (not just ping in-app), which solved her habit of missing notifications when in Do Not Disturb mode — used for lunch reminders and DoorDash orders.
- **Social bots as an "outer loop":** Lauren's Potato bot checks X mentions every 30 minutes, aggregates bug reports from users, and feeds them into her inner engineering loop — she can say "go talk to Potato and figure it out" to her engineer lead bot, with no copy-pasting required.
- **Skills are the trust-building mechanism:** The recommended path to bot autonomy is: observe the bot doing the task interactively → course-correct → convert the refined workflow into a reusable skill → trigger it with a slash command → set up a routine once one-shot reliability is confirmed.
- **Plugins can bundle MCPs, skills, and tools together:** PAC (Lauren's open-source plugin stack) installs on both Grokbot and Cursor and shares the same skills across both environments. The X plugin similarly bundles an MCP server plus a skill.
- **Peng's check-in pipeline as a creative use case:** Photo of a location → Grokbot generates day/light mode images with background removed → auto-posts to his personal website, replacing the need for a CMS or manual upload backend.
- **Memory is bot-local, capabilities are shared:** Tools, connectors, and skills are shared/reusable across bots, but memory and preferences are specific to each individual bot — enabling both reuse and personalization simultaneously.

---

## Use cases

- **Personal life admin:** Buying consumables (filament, toilet paper) on Amazon, updating inventory databases, selling items on Facebook Marketplace with automated price-drop logic.
- **Calendar and email management:** Adding/modifying calendar events from screenshots, identifying action items in inbox, paying friends via Venmo/Zelle when prompted.
- **Travel booking:** Complex multi-leg international flights and hotel booking via corporate tools (Navan), including proximity-to-event filtering, with human approval before final purchase.
- **Content creation pipeline:** Converting articles to audio podcasts for commute listening; generating location check-in posts with AI-generated images for a personal website.
- **Design work:** Brainstorming and iterating design options via a Figma MCP-connected bot; generating full-screen flows from a single key frame; reviewing and modifying design tokens.
- **Engineering / software development:** Running evals on skill changes before merging, orchestrating multi-agent PR pipelines with auto-merge, managing a Linux VM (Omachi) via a bot for environment setup and testing, disk space cleanup.
- **Community/social monitoring:** Aggregating X mentions, identifying repeated bug reports, feeding insights into an engineering loop without manual copy-pasting.
- **Bot fleet management:** Auditing existing bots for redundancy or over-broad context, optimizing routine frequency to reduce token costs, designing new bots from scratch with consistent engineering rigor.
- **Multi-perspective ideation:** Running a "group chat" with PM, design, and engineering bots to stress-test a product idea from multiple angles before committing to it.
- **Writing and communication polish:** Non-native English speakers using a writer bot to refine emails and Slack messages inline before sending, with a draft widget visible in the chat.

---

## Patterns & frameworks

**Chief of Staff Pattern**
A single catch-all bot that acts as the default inbox and router. When you don't know which specialist bot should handle a task, you send it to the chief of staff and it delegates. Functions as the human-facing interface for a larger bot fleet.

**Hierarchical Agent Swarm**
Chief of staff → domain lead (instruction: "never do work yourself, only break down and delegate") → specialist bots → cloud agents (Claude/Cursor). Each layer adds decomposition and supervision without doing terminal work itself. Lets one human orchestrate large parallel workstreams via a single top-level message.

**Bot-as-Named-Persistent-Agent Mental Model**
Rather than sessions or model instances, bots are personified, named entities with persistent memory, their own tools, and a stable identity across multiple concurrent projects. Matches how people relate to human colleagues or service providers (you know who to call, not how the system works internally).

**The Trust Ladder (Observe → Skill → Routine)**
1. Manually run a task with the bot present, watching and course-correcting.
2. After iteration, encode the refined workflow as a reusable skill (slash command).
3. Once the skill reliably one-shots the task, promote it to an automated routine.
At each rung, autonomy increases and babysitting decreases. Skip rungs and trust breaks down.

**5% Human / 95% Bot Design Workflow**
Human sets the system, creates one key frame or anchor artifact, then delegates scaling to the bot. Bot fills in the complete end-to-end flow using established design tokens and patterns. Human reviews and adjusts at the end rather than at every step.

**Outer Loop / Inner Loop via Social Bots**
Social monitoring bots (checking X mentions, aggregating bug reports) form an "outer loop" that feeds signals into the "inner loop" of engineering bots. Context passes between them by bot-to-bot conversation rather than human copy-pasting, keeping the human in a strategic rather than operational role.

**Michelin Kitchen (Quality at Scale)**
Lauren's framing for the aspirational state of an agentic engineering setup: not a "factory" (implying low quality at volume) but a Michelin-starred kitchen — high craft and quality, but at restaurant scale. The goal is to design the system, guardrails, and bot collaboration so that the output maintains quality even as throughput increases.

**Three Tiers of Work Evolution**
1. **Manual:** Human does everything directly (draws in Figma, types in Notion, messages in Slack).
2. **Prompted:** Human prompts AI to do those things on their behalf.
3. **Agentic/System design:** Human designs the system, guardrails, and bot relationships; bots execute autonomously and long-runningly, with humans providing high-level strategic input.