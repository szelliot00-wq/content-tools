# Your PM job just expanded | Tamar Yehoshua (Atlassian CPO)

Video ID: `BtK4kFI1LNo`

## Summary
Tamar Yehoshua, CPO at Atlassian, argues that the PM role hasn't disappeared — it has expanded. Speaking to a room of product leaders, she makes the case that AI tools have shifted *how* PMs work, not what they're fundamentally responsible for (finding product-market fit, building products people love, building sustainable businesses). She walks through three concrete Atlassian case studies showing that whether a PM should be "rowing" (doing hands-on execution) or "steering" (unblocking and directing) depends on product type and phase. The talk is most relevant to PMs and product leaders at mid-to-large companies trying to operationalize AI-native ways of working beyond startup-scale advice.

---

## Key insights
- **The "AI builder" role is real but context-dependent.** Startups are hiring generalist builders instead of dedicated PMs/designers. At large companies (10,000+ people), this manifests differently — roles blur rather than collapse.
- **The PM's core job hasn't changed; the execution has.** Finding product-market fit, building loved products, and driving revenue remain the same. What's changed is speed, tooling, and how PMs spend their time.
- **"Rowing vs. steering" is the central decision framework.** PMs must constantly evaluate whether their highest-leverage activity is hands-on contribution (rowing) or direction-setting and unblocking (steering). The right answer shifts with project phase.
- **Confluence case study — PM checked in 26 PRs in a month.** A PM with zero prior coding experience (never used a terminal) partnered with an engineering manager who built a harness for her. She focused on UX fixes engineers didn't have bandwidth for. Remix launched in 6 weeks, Confluence Slides in 8 weeks — work that would have taken ~6 months pre-AI.
- **Zero-to-one (Roclaw) case study — PM started rowing, then shifted to steering.** PM Josh and designer Kevin vibe-coded a full working alpha before adding engineers. Once engineers joined, Josh noticed they were drifting without clear direction while he was heads-down in code. He stepped back from coding to focus on prioritization and unblocking, and velocity increased. His coding experience made him a better steerer because he deeply understood blockers.
- **Jira case study — PM never touched production code, achieved 3x throughput.** In a 20-year-old enterprise codebase (FedRAMP, isolated cloud, hundreds of thousands of customers), PM coding was too risky. Instead the PM focused on: (1) streamlined prototyping via Loom → auto-generated work items → coding agents, (2) Slack-based feedback triage routed directly to coding agents, (3) Rovo agent processing 900+ pieces of customer feedback from user studies. Shipped 22 user-facing features in 10 weeks.
- **Evals are now a core PM skill.** Atlassian expects PMs to understand and run evals. In the Confluence Slides case, PM ownership of evals drove a 2x throughput improvement.
- **Figma MCP + coding agents automated design bug fixes.** By mapping Figma designs to code, the team fixed ~14 design bugs per hour — a task previously requiring manual engineer effort.
- **Test creation dropped from half a day to 10 minutes** using AI-assisted tooling on the Confluence team.
- **PMs are now consuming information at dramatically higher rates** — deeper customer feedback analysis, faster research synthesis, automated weekly reporting.
- **What PMs no longer do manually:** writing status updates, compiling research by hand, building slides from scratch, manually triaging feedback.
- **"Don't believe everything on X"** — Tamar explicitly warns against chasing AI hype. The signal is what actually works for your customers, not what's trending.
- **The teamwork graph is the enabling layer.** Atlassian's internal context graph ("teamwork graph") is what makes AI tools actually useful at enterprise scale — intelligence without organizational context isn't enough.
- **Measuring AI-driven productivity is unsolved.** Atlassian tracks PRs deployed to production (not written), features delivered, idea-to-delivery cycle time, and OKR attainment. She openly admits no one has cracked this measurement problem yet.

---

## Use cases
- **PMs at large companies** frustrated that startup-centric AI advice doesn't translate to their reality — this talk gives enterprise-specific playbooks.
- **Engineering managers** deciding how to structure contribution models and give PMs safe isolated environments to ship code.
- **Product leaders building AI fluency programs** — the AI Builder Week model and fluency index are directly replicable.
- **PMs on new feature work in existing codebases** — the Confluence model (PM checks in front-end code, engineers own higher-complexity work) applies when there's UX backlog and engineering capacity is constrained.
- **PMs doing zero-to-one product development** — the Roclaw model (vibe-code an alpha, then shift to steering once engineers join) applies when exploring a new product space with high uncertainty.
- **PMs working on large, high-compliance enterprise products** — the Jira model (no production code commits, focus on feedback pipelines and prototype-to-handoff workflows) applies when codebase risk is too high for PM contributions.
- **PMs who are still writing manual status updates, compiling research by hand, or managing feedback in spreadsheets** — immediate automation opportunities.
- **L&D and enablement teams** designing AI training programs for existing (non-AI-native) PM organizations.
- **PMs new to evals** — the talk frames evals as a mandatory skill, not optional, with measurable throughput impact.

---

## Patterns & frameworks

**Rowing vs. Steering**
The central mental model. At any given moment, a PM should ask: is my highest-leverage contribution hands-on execution (rowing) or direction-setting, prioritization, and unblocking (steering)? The answer is not fixed — it should shift based on product phase (zero-to-one vs. mature), codebase risk, team composition, and what's actually bottlenecking progress. The Roclaw PM started rowing (coding the alpha), then deliberately switched to steering when the engineering team started drifting.

**The Ship Metaphor**
Atlassian frames every product initiative as a ship heading toward a destination. The PM's job is to make the ship go faster. "Intelligence + context" (AI model capability × organizational context graph) is the engine. Rowing vs. steering is how the PM chooses their role in accelerating it.

**AI Fluency Index**
A 6-capability, 1–5 scale self-assessment framework Atlassian uses to help PMs identify skill gaps and growth paths — not a performance ladder. Capabilities include: using AI tools, writing with AI, automating data insights, prototyping, and technical literacy. Scale: 1 = Curious, 3 = Capable, 5 = Pioneering. All PMs are expected to reach L3 across all capabilities; L5 should be targeted where it matters most for the team. Importantly, this is decoupled from the performance/promotion ladder, which remains outcome-based.

**AI Builder Weeks**
A quarterly, one-week off-cycle training program for PMs and designers. Structure: external speakers → internal peer training (advanced PMs teaching others) → hands-on project. Each quarter focuses on one skill (prototyping → evals → building agents → checking in code). Over 1,000 participants trained; 120+ new workflows built and adopted. Atlassian has published an "AI Builder Week in a Box" on their website for other companies to replicate.

**Loom → Work Item → Coding Agent Pipeline (Jira prototype workflow)**
A streamlined prototyping-to-handoff loop: PM records a Loom of current UI or Figma designs with narration → Loom auto-generates Jira work items from the recording → PM moves to in-progress → coding agent writes compliant, accessible, design-system-consistent front-end code in the actual repository via managed cloud agent → handoff to engineers is nearly ready-to-ship. Removes local environment setup burden from PMs and ensures output already meets compliance and design standards.

**Feedback Triage Automation**
Routing raw feedback (Slack messages, bug reports, user study videos) through AI agents to automatically categorize, prioritize, and dispatch to coding agents or engineering queues — bypassing manual PM/engineer triage entirely. Applied in two ways in the Jira case: real-time Slack bugs via Jira agent, and batch customer insights (900+ items) via Rovo agent.

**Intelligence + Context = Acceleration**
Tamar's formula for why AI works at enterprise scale: raw model intelligence is only useful when combined with organizational context (who's working on what, what's launching when, what customers need). Atlassian's teamwork graph provides the context layer. Without it, AI tools answer generic questions; with it, they answer organization-specific ones (e.g., the CEO asking Rovo when a feature launches instead of pinging the PM).