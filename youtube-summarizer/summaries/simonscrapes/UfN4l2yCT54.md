# 5 Claude Cowork Scheduled Tasks (For Business Owners With No Time)

Video ID: `UfN4l2yCT54`

## Summary
This video walks business owners through five production-ready Claude scheduled tasks that run autonomously in the cloud, requiring no active participation once configured. The presenter frames all five around a concept called "loop engineering" — defining a clear "done criteria" so Claude keeps working until every item is handled, then notifies you only about exceptions. The tasks cover financial operations, email management, meeting follow-through, and competitive intelligence. It is most relevant to solo founders, small business owners, and operators who are time-constrained and want to delegate repetitive cognitive work to AI without losing quality oversight.

## Key insights
- Claude scheduled tasks now run in the cloud, meaning work continues with the laptop shut and can be monitored or guided from a phone.
- The presenter had over 600 unreconciled transactions at year-end because the manual process was skipped for 6 months — exactly the problem automated reconciliation solves.
- **Task 1 — Invoice & Receipt Reconciliation:** Runs every Friday at 4:00 p.m., pulls unexplained transactions from FreeAgent, hunts three Gmail inboxes for matching receipts, attaches matches, and emails a "gaps list" for manual review. Composio (free tier available) is used as a middleware layer to connect multiple Gmail accounts since Claude's built-in Gmail connector only handles one account at a time.
- **Task 2 — Subscription Creep Audit:** Pulls ~8 months of recurring transactions, flags price increases, duplicates, and unused services, and calculates month-over-month recurring spend delta. In its first real run, it caught a 15% MoM spend increase (driven by Meta ads, not software), four quietly rising subscriptions, and three parallel AI platforms plus separate API costs running simultaneously.
- **Task 3 — Email Voice Profiling + Inbox Drafting:** A one-time task scans the last 90 days of sent mail to extract a personal email voice profile (greetings, tone, sign-offs) and builds reusable templates for recurring email types (refunds, proposals, invoice chases, hiring). These templates feed a scheduled task that continuously drafts inbox replies in the sender's voice. Templates are stored in Notion so cloud-based scheduled tasks can access them (local files are not accessible to cloud tasks).
- **Task 4 — Meeting-to-Task-List:** Runs twice daily (11:30 a.m. and 4:30 p.m., Mon–Fri), pulls action items from Fathom meeting notes via Composio, formats them as Notion tasks with due dates, source timestamps, and recording links, and drops them into the working task list. The presenter notes this can also be done with Claude's built-in meeting summary connector without Composio.
- **Task 5 — Weekly Competitor Watch (presenter's top pick):** Monitors a Notion table of 30–55 competitors weekly, scrapes websites, blogs, socials, and product updates, and produces a digest. In its first run, 14 of 55 competitors showed activity in 7 days. It identified that Site AI bulk-published 12 LLM visibility comparison pages on July 21st, with source links for direct verification. Done criteria: check every competitor in the list and confirm either activity (with proof/links) or no activity before completing.
- Composio acts as a credential vault and multi-account connector — the agent never sees raw API keys or credentials directly.
- Cloud-based scheduled tasks cannot access local files; the fix is to move reference files (voice profiles, templates, contacts) to a Notion shared folder that Claude can reach via its built-in connector.
- The presenter offers these five tasks as downloadable "skills" that interview the user about their own tools and processes, then configure a customized version — not a one-size-fits-all copy.

## Use cases
- **Accountants / bookkeepers / founders** who manually reconcile expenses and receipts periodically and want that handled weekly without intervention.
- **Business owners** who accumulate SaaS subscriptions and lose track of price creep, duplicate tools, or forgotten trials.
- **Anyone who sends high volumes of repetitive emails** (customer support, hiring, proposals, invoice chases) and wants drafts that sound like them without writing from scratch each time.
- **Operators running back-to-back meetings** whose action items live in recording tools (Fathom, Granola) but never make it into their actual task management system (Notion, etc.).
- **Founders or product teams in competitive markets** with 10–50+ competitors who need a weekly aggregated view of competitor activity without manually checking each one.
- **Solo operators with no admin staff** who need the equivalent of an EA running recurring operational tasks in the background.
- **Teams that store operating procedures or brand standards in Notion** and want AI tasks to reference that shared context automatically.

## Patterns & frameworks

**Loop Engineering**
The core mental model of the video. A "loop" is Claude repeating a defined cycle of work until a "done condition" is met, rather than stopping after a single pass. The presenter identifies three trigger types:
- *Turn-based* — user sends a message, Claude works until done (requires the user to be present; generally avoided).
- *Time-based* — runs on a fixed schedule (every Friday, twice daily); covers most of the five tasks.
- *Event-based* — triggered by a real-world event (email received, meeting ended); can be approximated by polling on a time schedule (e.g., check inbox every hour).

**Done Criteria Design**
The skill the video teaches explicitly. Instead of a vague instruction, you give Claude a binary completion condition: "every transaction from the week is either matched or added to the gaps list." The clearer the finish condition, the faster setup is and the more reliably the task runs unattended. Each of the five tasks has its done criteria spelled out.

**Exception-Based Human-in-the-Loop**
Rather than eliminating human review, the pattern routes only unresolvable items back to the human (the "gaps list" in reconciliation, the flagged discrepancies in the subscription audit). The human receives a curated exceptions digest, not raw data, preserving quality without requiring continuous involvement.

**Middleware/Connector Layering (Composio pattern)**
When a built-in connector is insufficient (e.g., single-account Gmail limit, missing API vault), the workaround is to insert Composio as an intermediary MCP layer. Composio stores credentials externally, supports multi-account connections, and exposes them to Claude without the agent ever handling raw keys directly.

**Shared-Context Store (Notion as cloud context)**
Since cloud-based scheduled tasks cannot read local files, the pattern is to migrate reference materials (voice profiles, templates, competitor tables, team contacts) to Notion. Claude's built-in Notion connector can then pull this context at runtime, and it doubles as a permission-controlled team knowledge base.