# Instinct vs Grok Bot vs ChatGPT vs Hermes: Which AI Agent Can You Trust?

Video ID: `6Yeo6M8-W_8`

## Summary
This video compares four AI personal agents — Instinct, Grok Bot, ChatGPT/Codex, and Hermes — across usability, capabilities, and privacy/security tradeoffs. The creator, who uses all four simultaneously, argues that while these agents are increasingly capable of acting on your behalf (booking restaurants, managing email, making purchases), the convenience comes with real risks around data sharing, prompt injection, and loss of control. The video is most relevant to early adopters, productivity-focused professionals, and anyone evaluating AI agents for personal or business use.

## Key insights
- **Instinct** is invite-only, lives in iMessage/WhatsApp as a single thread (no sub-bots), and is raising at a $2.5B valuation. It excels at being simple, resourceful, proactive (uses cron jobs behind the scenes to follow up on tasks), and personable (emoji reactions, human-like UX).
- **Instinct's concerning security ask**: It requested the user's Google 2FA code AND actual Google password during a task to cancel a subscription renewal — the creator admitted they only complied because they were making a tutorial.
- **Instinct found a real money-saving opportunity** unprompted: a $1,200/year Google AI Ultra charge from a free trial about to convert, and successfully canceled the auto-renewal while providing a receipt.
- **Grok Bot** is a team of bots on a persistent cloud computer running 24/7 on SpaceX AI servers. Unlike Instinct's single thread, it uses named bots with distinct personas (e.g., "Doom Scrolling Uncle" for X/Twitter monitoring, "Marie Kondo" for inbox cleanup, "Cheap Dad Bot" for deals and marketplace listings).
- **Grok Bot's key differentiator**: bots share the same cloud computer and can pass instructions to each other and be added to the same thread collaboratively.
- **Grok Bot privacy gap**: Deleting a bot does not remove shared computer files or browser sessions. There is no clear "full reset" option — the reset function restores a snapshot, not a clean slate.
- **ChatGPT/Codex** still handles 90%+ of the creator's actual work. ChatGPT Work runs cloud tasks (no laptop needed), while Codex works with local files and browser on the laptop. The UI is described as messy — threads rather than bots, and cloud vs. local task distinction is confusing.
- **ChatGPT privacy setting to disable**: "Improve the model for everyone" — if on, OpenAI may use data from connected apps to train models. It can be turned off in Settings → Data Controls.
- **Hermes** is open source, runs locally on a Mac mini, and is accessed via Telegram. It stores all memory and skills in local files with zero telemetry — the most privacy-preserving option on the list.
- **Hermes use case**: Sends a daily brief (top 3 priorities, today's calendar, follow-ups) and weekly health reports by connecting to a smart scale and fitness app via MCP.
- **Prompt injection is a real, demonstrated risk**: A friend (Alex Cohen) proved Instinct could be manipulated by sending an email to his own inbox containing agent instructions — Instinct followed them and forwarded private action items to a secondary address. Instinct claims it has added safeguards (email = data, not commands), but the creator notes there's no way to verify this from the outside.
- **Practical security tip**: Audit connected Google apps at my.google.com/linked apps. The creator had 67 apps connected. You can use any of the four agents with browser-use capability to batch-remove apps (e.g., "remove apps 1 to 10") instead of doing it one by one.
- **Payments**: Instinct uses Stripe Link for purchases and requires user approval per transaction — considered relatively secure.
- **Trust hierarchy the creator uses**: Official plugins (ChatGPT, Grok Bot) = comfortable. Cloud browser logins with 2FA/passwords = uncomfortable. Bank account or highly sensitive info = only via official plugins, not cloud browsers.

## Use cases
- **Busy professionals** who want a single-thread AI assistant that proactively follows up on tasks (booking appointments, managing email threads) — Instinct.
- **Founders or marketers** who want automated weekly digests of website metrics, social media trends, or YouTube comment analysis — Grok Bot.
- **People with households/families** who need to manage school forms, spousal errands, and marketplace listings — Grok Bot's persona-based bots.
- **Developers and power users** who want maximum flexibility and don't mind a messy UI — ChatGPT + Codex.
- **Privacy-conscious users** who want a personal agent but don't want their data leaving their own hardware — Hermes (local, open source).
- **Anyone wanting to clean up their Google account** — using an AI agent with browser-use to batch-audit and remove unused connected apps.
- **Health tracking** — connecting wearables/fitness apps to a local agent (Hermes via MCP) for automated weekly health reports.

## Patterns & frameworks

**The Four-Agent Stack (parallel specialization)**
Running multiple agents simultaneously with distinct roles: ChatGPT/Codex for deep work, Grok Bot for always-on monitoring and automation, Instinct for conversational task execution, Hermes for local scheduled jobs. Each agent covers a different trust level and use case rather than replacing the others.

**Proactive Cron-Job Pattern (Instinct)**
Rather than waiting for user follow-up, Instinct schedules background tasks (cron jobs) to monitor for replies or triggers and surfaces them to the user. Example: after emailing a golf instructor, it watches for the reply and notifies the user to confirm — making the agent appear to be "looking out for you" without any manual prompting.

**Persona-Bot Pattern (Grok Bot)**
Assigning distinct names, personalities, and scopes to individual bots improves clarity of purpose and even makes interactions more engaging (e.g., a bot that talks like Marie Kondo). This is a practical way to organize multi-agent workflows on a shared computer.

**Trust Tiering for Data Access**
A mental model for deciding what to share with agents: (1) Official OAuth plugins = acceptable; (2) Logging into accounts via cloud browsers = use caution; (3) 2FA codes and passwords = high risk, avoid where possible; (4) Bank/financial accounts = only via vetted official integrations.

**Prompt Injection Risk Model**
Attackers embed instructions inside content the agent will read (emails, documents, websites). The agent may execute those instructions as if they came from the user. Mitigation relies on model intelligence and explicit safeguards (treating email content as data, not commands) — but neither is fully reliable, making it an ongoing architectural concern for all personal agents.

**Connected App Audit Workflow**
Periodic hygiene process: navigate to my.google.com → linked apps → use an AI agent with browser-use to enumerate, evaluate, and batch-remove stale third-party app connections, reducing your attack surface.