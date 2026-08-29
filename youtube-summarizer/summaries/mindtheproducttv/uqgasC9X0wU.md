# Inside Slack Code: what it is, and why Anthropic just became its founding partner

Video ID: `uqgasC9X0wU`

## Summary
This episode of "Now Shipping" (hosted by Mike Belcedo for Mind the Product) does a single deep-dive on the August 24, 2026 launch of Slack Code — a new Salesforce/Slack product that gives teams dedicated AI-agent coding channels inside Slack. The video covers how Slack Code works, why Slack launched it now (competitive and business pressure), the security risks of agentic coding, and the strategic significance of Anthropic being named a founding partner just days after launch. It is most relevant to product managers, engineering leaders, and anyone making tooling or AI strategy decisions at their company.

## Key insights
- **What Slack Code is:** Dedicated channels in Slack where teams tag coding agents (Claude Code, Devin, GitHub Copilot, etc.), which auto-create a project channel with tabs for conversation, agent plan, code diffs, and live preview. Channels archive when done, leaving a searchable audit trail.
- **Human oversight is built in:** Anyone in the channel can pause, redirect, or stop an agent. A human must sign off before anything ships to production — though Cognition's Jeff Wang predicts auto-merge without human approval will happen within a year.
- **Slack's strategic reversal:** In mid-2025, Salesforce actively blocked rival AI companies from Slack data to protect its moat. Slack Code is the opposite move — opening APIs to any developer and courting outside AI partners, betting on becoming "the room where agents want to work."
- **Business context / pressure:** Salesforce stock is down 5% YTD vs. a strong Nasdaq. Slack's CEO was poached by OpenAI in December. The rebuilt Slack bot (running Claude) became the fastest-adopted feature in Salesforce's 27-year history, giving Slack momentum to play offense.
- **The vibe coding market:** Currently a $4.7B market, projected to triple by 2027. 63% of vibe coders self-identify as non-developers (PMs, designers, marketers). Gartner predicts citizen developers will outnumber professional engineers 4:1 by 2028.
- **Productivity numbers:** Cognition reports a 10x increase in merged pull requests over a few months while headcount grew only 40%. Internally at Salesforce, Slack bot has driven 8.1 million annualized productivity hours — up 2x quarter over quarter.
- **The security problem:** Veracode's 2026 security report found ~44% of AI code generation tasks introduced a real, exploitable vulnerability. Average security pass rate across models was 56%. One report tracked monthly security findings going from ~1,000 to over 10,000 in six months — a 10x increase — while code volume exploded.
- **"Illusion of correctness":** A term security researchers use for AI-generated code that looks clean and finished but hides flaws nobody caught because it appeared too polished to double-check.
- **Permissions model:** Every Slack Code agent acts on behalf of the human who invoked it, using only that person's existing access rights. Devin runs in an isolated sandbox with "minimum viable access" and an optional zero-internet mode. Agents produce standard GitHub pull requests, so existing review gates still apply.
- **The Anthropic plot twist (ClaudeForce):** Just 3 days after Slack Code launched as a "neutral multi-agent platform," Salesforce and Anthropic announced an expanded partnership making Claude the default model across the entire Slack/Salesforce stack. Anthropic is named as a founding partner of Slack Code. This includes 37 pre-built "Salesforce and Claude" sales skills that function as an AI chief revenue officer inside Claude.
- **The platform distribution fight:** The competitive question has shifted from "which model do I call from the terminal?" to "which platform owns the shared workspace where my whole team works with agents?" — with Slack, Cursor, GitHub, and the terminal itself all competing for that layer.
- **Engineers vs. Slack as interruption machine:** A noted tension — coding is deep work, Slack is designed for interruptions. Slack's counter-argument is that visibility is a feature: public work deters low-quality output and invites helpful course correction.
- **Stigman's PM workflow as a template:** Slack's VP of Product tags an engineer on her PRs before approval; the engineer gives feedback; the agent takes another pass. The engineer didn't write the code from scratch but still touched the output.

## Use cases
- **Product managers** who want to contribute working prototypes or code without pretending to be engineers — using the "tag an engineer, get feedback, re-run the agent" workflow.
- **Engineering leaders** evaluating which AI coding platform to standardize on before default settings make the decision for them.
- **Security and platform teams** needing to assess whether their agentic coding rollout is paired with a real vulnerability review process (given 44% of AI tasks introduce exploitable flaws).
- **IT/infosec teams** evaluating agent platforms — specifically stress-testing the permissions model: does the agent inherit the invoking user's access, or does it get its own identity that must be managed separately?
- **Tooling decision-makers** at enterprises deciding between Slack Code, Cursor, GitHub Copilot Workspace, and Replit before the platform layer gets locked in.
- **Non-technical contributors** (designers, marketers, PMs) who want to participate in product development using plain-language instructions to coding agents.
- **Teams concerned about "AI slop"** — organizations that need a structured review process to prevent plausible-but-flawed code from shipping at scale.

## Patterns & frameworks

**Multiplayer vs. single-player AI coding**
Slack's core bet is that the current paradigm — one developer, one agent, private terminal — is a temporary phase. Slack Code bets on a multiplayer model where the team shares visibility into agent work. The claim is that visibility itself is a quality and accountability mechanism, not just a collaboration nicety.

**The permissions inheritance model**
A checklist pattern for evaluating any agentic platform: does the agent act as the invoking human (inheriting their existing access, nothing more), or does it get its own persistent identity with permissions that IT must manage? Slack Code uses the former. The video frames this as a required question before adopting any agent platform.

**Tag → feedback → re-run (the Stigman workflow)**
A repeatable PM workflow for contributing real code without deep engineering expertise: (1) use an agent to produce a draft PR, (2) tag an engineer for review, (3) incorporate their feedback and let the agent take another pass. The engineer quality-gates without writing from scratch; the PM ships without overstating their technical role.

**"Protect the moat" → "become the room"**
A strategic pattern observed in Slack's evolution: initially blocking rival AI companies from Slack data to defend competitive position, then fully reversing to open APIs and partner with those same companies — betting that owning the collaboration layer is more durable than owning the data.

**Volume vs. quality divergence (the AI slop problem)**
A named pattern where AI-assisted development drives code volume up dramatically while security pass rates stay flat or decline. The "illusion of correctness" is the specific failure mode: output that reads as clean and finished, discouraging the scrutiny that would catch hidden flaws. The framework implication is that shipping velocity and security review cadence must scale together, not independently.