# Anthropic Just Solved Claude Cowork’s Biggest Limitation (Goodbye MCP)

Video ID: `9QSumbWubZ4`

## Summary
This video demonstrates Claude Co-Work's new "Recorder Skill" feature, which allows users to teach Claude to automate tasks on any software by recording a screen walkthrough — no API or MCP connection required. The presenter shows a live demo of automating a ManyChat Instagram DM lead magnet setup that previously had to be done manually after every YouTube upload. The core argument is that this feature eliminates the bottleneck of needing developer-built integrations, opening automation to any UI-based software. It is most relevant to content creators, marketers, and business operators who rely on tools without public APIs.

## Key insights
- The Recorder Skill feature captures screen activity, clicks, keystrokes, and voice narration simultaneously, then converts the recording into a reusable, repeatable skill stored as a `skill.md` file.
- No API or MCP connection is required — if you can click it on screen, Claude can learn it. This is the key differentiator from all prior AI automation approaches.
- Verbal context during recording is critical: the presenter explains the "why" and business logic aloud while clicking, giving Claude embedded domain knowledge that a silent screen recording would miss.
- The demo workflow involved: reading a Notion video transcripts table → identifying the latest "not started" video → duplicating a ManyChat automation → renaming it with the video's keyword → selecting the correct Instagram reel → updating the YouTube link → setting the automation live → marking the Notion row as "live."
- ManyChat has no public API, making it previously inaccessible to any AI tool — this feature directly solves that gap.
- Claude caught mistakes the presenter made during recording (e.g., downloading a video and thumbnail that weren't actually needed in the ManyChat steps), demonstrating active comprehension rather than blind replay.
- Claude also proactively suggested updating the Notion row's DM automation status to "live" after completion — a step the presenter had forgotten to include.
- In the live test run, Claude correctly identified the right video (stop using Fable 5), used the new keyword `Fable_123` (not the one from the recording), and completed the full workflow without manual intervention, proving it generalizes rather than just replaying the demo.
- The feature requires Claude Desktop (Mac only at time of recording), the Co-Work folder, and the Claude in Chrome extension for browser-based automation.
- Skills can be converted into scheduled tasks — e.g., a daily check for new YouTube videos that auto-triggers the ManyChat setup, removing the human from the loop entirely.
- The workflow processed 61 steps captured over 240 seconds of recording.
- Token cost is noted as significant, but framed as a worthwhile trade-off for the time saved.

## Use cases
- Content creators who run lead magnet comment automations on Instagram and need to update them per upload.
- Marketers using tools like ManyChat, Klaviyo, or other platforms with no public API.
- Teams operating legacy enterprise software or internal admin portals with no integration options.
- Anyone with repetitive, multi-step UI workflows in proprietary SaaS tools (CRMs, scheduling platforms, reporting dashboards).
- Small business operators who lack engineering resources to build custom API integrations.
- Operations teams managing scheduled publishing workflows across multiple platforms.
- Anyone who currently acts as the manual "glue" between tools that don't talk to each other.

## Patterns & frameworks

**Recorder Skill Pattern**
Record yourself doing a task once, narrating context aloud as you go. Claude converts the recording (clicks + voice + screen) into a `skill.md` file with step-by-step instructions it can follow autonomously. The verbal layer is what distinguishes this from a simple macro recorder — it embeds business logic and decision rules.

**Teach Once, Run Forever**
The underlying mental model: treat your own manual process as the training data. You are the subject matter expert; the recording session is how you transfer that expertise to Claude. After one session, you are no longer the bottleneck.

**Skill → Scheduled Task Pipeline**
Skills created via recording can be promoted into scheduled cloud agents (e.g., "every day, check Notion for a new video; if found, run the ManyChat automation"). This converts a one-off automation into a fully autonomous recurring workflow.

**"Not Started" Status Gate**
A lightweight workflow governance pattern used in the demo: a Notion column (`DM Automation`) acts as a state machine (`not started` → `live`). Claude checks this before acting and updates it after, preventing duplicate runs and providing visibility into automation status.

**UI-First Automation Targeting**
A prioritization heuristic offered by the presenter: identify tools in your stack that have no MCP or API, especially custom portals and old enterprise software — these are the highest-value targets for Recorder Skills since no other automation path exists for them.