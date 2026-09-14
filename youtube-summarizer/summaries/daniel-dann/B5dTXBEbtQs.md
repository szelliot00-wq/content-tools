# Hermes Agent on Cloudways: A Beginner’s Step-by-Step Installation Guide (2026)

Video ID: `B5dTXBEbtQs`

## Summary
This tutorial video, hosted by Daniel and sponsored by Cloudways, walks beginners through deploying the Hermes AI agent on Cloudways' managed hosting platform. The core argument is that Cloudways eliminates the complex server infrastructure setup (Docker, SSL, firewall configuration) that typically precedes running a self-hosted AI agent, letting users focus on using the agent rather than configuring it. Daniel demonstrates the full workflow from deployment through real task testing and Telegram integration. The video is most relevant to non-technical or semi-technical users who want a capable, persistent AI agent without managing a VPS from scratch.

## Key insights
- **Hermes is developed by News Research** and is designed to become more useful over time — it saves reusable "skills" when it finds a reliable method for a difficult task, and retains memory of projects, settings, and preferences across sessions.
- **Hermes is not a stateless chatbot** — it maintains context across sessions and can persist memory even when accessed through different interfaces (e.g., the Cloudways dashboard vs. Telegram).
- **Cloudways offers four instance tiers**: Scout (light development, simple workflows), Operator (more substantial single-agent work), Squad and Swarm (multi-agent setups and heavier workloads). Available resources affect browser automation, sub-agent capability, and parallel execution.
- **Nine server locations** are available, and choosing one geographically close to you is recommended for performance.
- **LLM provider setup requires your own API key** — Daniel selected OpenAI and entered his key during deployment, meaning model costs are separate from Cloudways hosting costs.
- **Three tasks were tested live**: (1) exploring the workspace and listing files — confirming server-level file access; (2) running a terminal command (`df` or similar) to check disk usage — confirming terminal access; (3) a web research task returning structured results with source links — confirming internet browsing capability.
- **Telegram integration works through LLM Channels** — you create a bot via BotFather, get a token, enter it in Cloudways, and set a home channel with `/set_home`. The same Hermes instance with the same memory is then accessible via Telegram.
- **SSH access is still available** through Cloudways, so users retain deep server control if needed — Cloudways reduces setup friction but does not eliminate control.
- **Backup and restore functionality** provides snapshots of configuration, memory, and connected channels — a meaningful operational advantage over a bare VPS install.
- **The key trade-off** is explicit: experienced VPS administrators who want full hands-on control can still do a manual install, but Cloudways is the faster path for those who want Hermes running without infrastructure overhead.
- The video is **sponsored by Cloudways**, which should be factored into how the platform comparison is weighted.

## Use cases
- **Developers or indie makers** who want a persistent AI agent with memory and tool access but lack the time or expertise to configure a server environment manually.
- **Product managers or non-technical professionals** who want to experiment with self-hosted AI agents without a DevOps background.
- **Small teams** exploring multi-agent workflows (Squad/Swarm tiers) without dedicated infrastructure engineers.
- **Anyone wanting an AI agent accessible across multiple surfaces** (web dashboard + messaging apps like Telegram) from a single deployment.
- **Users who need an agent with terminal, file, browser, and code execution access** — i.e., task automation beyond simple Q&A.
- **Those evaluating managed vs. self-hosted AI agent hosting** — the video provides a concrete benchmark for what "managed" actually means in practice.

## Patterns & frameworks

**Managed deployment over manual VPS setup**
The central framework: instead of provisioning a blank server and configuring Docker, SSL, and firewalls yourself, use a platform that handles infrastructure so you can go straight to using the agent. The trade-off is some reduction in raw control in exchange for significantly faster time-to-working-agent.

**Tiered resource sizing (Scout → Operator → Squad → Swarm)**
A named, four-tier scaling model where each tier corresponds to a use case: solo light tasks, solo heavy tasks, small multi-agent teams, large multi-agent workloads. Tier choice directly gates features like browser automation and parallel execution — it's not just about raw compute.

**Skill accumulation over time (Hermes-specific)**
Hermes uses a reusable-skills pattern: when it solves a hard problem reliably, it saves that solution as a callable skill for future sessions. This is a form of agent self-improvement within a persistent memory architecture, distinguishing it from stateless LLM interfaces.

**Multi-channel agent identity (single agent, multiple surfaces)**
The same agent instance — with the same memory and configuration — is accessible through both the Cloudways web UI and Telegram. This "one agent, many channels" pattern means integrations extend reach without duplicating state or setup.

**Verify before claiming success (demo structure)**
Daniel's testing sequence follows a deliberate escalation: file access → terminal command → web research. This pattern of testing progressively more complex capabilities is a useful validation framework when evaluating any new agent deployment.