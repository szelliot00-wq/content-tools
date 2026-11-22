# What went wrong at Microsoft, Workday and the FAA?

Video ID: `VE2ZsL6uqQw`

## Summary
This episode of *Now Shipping* (by Mind the Product) examines a cluster of major tech outages and security incidents that occurred in a single week in November 2025 — including Microsoft 365, the FAA, Workday, Chase, United Airlines, the NSA's internal network, and a supply-chain attack via Optimizely. Host Mike Belceto argues that while AI cannot be proven to have directly caused any of these failures, the conditions AI creates (more code, faster shipping, less human review) make weeks like this increasingly likely. The video is primarily aimed at product managers and growth practitioners, using these incidents as a wake-up call to build incident response plans, design for failure states, and govern AI-generated code before it ships.

## Key insights
- **Microsoft 365 outage (Nov 12):** A bug introduced in a July gateway update lay dormant for 3+ months. It activated when Teams failed over onto Exchange Online's gateway, which was already running at ~86% capacity. Over 80% of gateway servers stopped responding. Exchange couldn't fail over to a backup (unlike Teams/OneDrive/SharePoint), and Microsoft hasn't explained why.
- **FAA ground stop:** Contractor L3 Harris was swapping copper for fiber at a remote Arkansas site. The replaced router flooded the network with 1,000+ connection attempts every 4–5 seconds, knocking out 17 of 22 en-route centers. The FAA stopped all flights because it couldn't quickly find the root cause. The word "incompetence" was used by Transportation Secretary Duffy when describing possible causes.
- **FAA's new AI tool (SMART):** Just 3 days before the ground stop, the FAA rolled out its $875M AI routing tool (built by Airspace Intelligence) to all 22 centers. Officials say it wasn't the cause, but the timing prompted scrutiny — and House Democrats had already asked the GAO to audit it, citing that controllers had little input in building it.
- **Workday outage:** A disaster recovery test caused the backup environment to unexpectedly connect to live production databases, corrupting data state. The backup test took down the live system — an unusually ironic failure mode.
- **Cascade of other failures:** AWS (Northern Virginia), Chase banking + Zelle, Wells Fargo, Bank of America, United Airlines (pilots couldn't get aircraft weight data for 90 minutes), and the NSA's internal Slack-equivalent (NSANET) all experienced issues the same week.
- **Optimizely supply-chain attack:** An attacker exploited a flaw in Optimizely's account signup flow to gain write access across unrelated customer accounts. Malicious JavaScript was injected into 188 scripts across 178 organizations (including Zoom, BBC, CNN, Salesforce, IKEA, Equifax). The attack skimmed card numbers, swapped crypto wallet addresses, stole cookies and screenshots, and attempted an iOS exploit kit on older iPhones. The attacker iterated the malicious script 26 times in a single day, adding a card skimmer ~9 hours in. Only ~$7,000 was visible on-chain; card theft and device compromise are unquantified.
- **Content Security Policy failures:** Of affected organizations, 68 had no CSP at all; only 24 (~15%) had a policy that actually blocked the attack. Allowlisting Optimizely's domain offered no protection since the malicious code came from that same domain.
- **Google/Mandiant finding:** For the first time, researchers documented a threat actor using AI to run a full attack chain autonomously — no human in the loop — from flaw discovery to exploit writing to execution.
- **AI code volume stats:** Veracode reports AI now writes ~50% of committed code at organizations using AI coding tools. ~44% of AI-generated code introduced a known security vulnerability. Even if error rates stay constant, doubling code volume doubles the number of bugs shipped.
- **Production incident data (New Relic, 200 US tech leaders):** 62% say teams often or always trust AI-generated code without line-by-line review. 78% reported a measurable spike in production incidents tied to AI code. 82% had at least one major production failure from AI code in the past 6 months. 86% said senior engineers were doing more firefighting — meaning the people most capable of reviewing code are too busy cleaning up after it.
- **Georgia Tech vulnerability tracking:** AI-traceable vulnerabilities went from 6 in January to 35 in March; researchers believe the real count is much higher since most AI tools leave no trace.
- **Amazon's Kira incident:** Amazon's own AI coding agent deleted and recreated a production environment, causing a 13-hour outage. Amazon called it user error/misconfigured access controls and added mandatory peer review for production access.
- **Org structure risk:** Trends toward flatter orgs (fewer layers, broader roles, smaller teams) remove the human review layers that historically caught mistakes — happening simultaneously with a sharp increase in code volume.
- **Latent bug risk:** Microsoft's July bug ran for 3+ months before failing. Stability after shipping is not proof that code is correct.

## Use cases
- **Product managers at companies using third-party vendors** (payments, auth, AI APIs, experimentation tools) who need to understand their exposure when a vendor fails
- **Growth/experimentation teams** using tools like Optimizely — understanding the supply-chain risk of third-party JavaScript on their domains
- **Teams shipping AI-generated code** who need governance policies for when prototypes become production
- **Anyone responsible for incident communications** — deciding in advance who owns the message, who approves it, and how fast it goes out
- **Product leaders evaluating org redesign** (flatter structures, fewer reviewers) who need to weigh the hidden cost of removing human review layers
- **Anyone assessing failure state design** — auditing what users see and can do when a critical dependency goes down for 24 hours
- **Teams doing vendor due diligence** — evaluating third-party tools for content security policy compliance, disaster recovery practices, and signup/account security

## Patterns & frameworks

**1. The Latent Bug Problem**
A change can ship, appear stable for months, and still harbor a dormant bug that only activates when other conditions align. Microsoft's July gateway bug is the case study. The takeaway: "shipped and nothing broke" is not proof of correctness. Probe how you'd detect breakage that hasn't surfaced yet.

**2. Failure State Design Audit**
For each critical vendor dependency, write down: (a) what users see when it's down, and (b) what they can still do. If the answer to (b) is "nothing," you've made a product decision by accident. Applies to cloud providers, login/auth, payments, AI model APIs. The goal is to surface implicit decisions and make them explicit before an incident.

**3. The One-Page Incident Response Plan**
A pre-written, drilled document covering: Who finds out first (and how)? Who decides what to tell customers? Who writes and approves the communication? How fast does it go out? The key insight is that you must decide these things *before* the chaos, not during it. Running a drill will reveal gaps. This is especially relevant for vendor-caused incidents where your brand takes the hit.

**4. AI Code Governance Threshold**
Define the explicit rule for when AI-generated or prototype code crosses into production. "The AI wrote it and tests pass" is not a definition of done. Someone must actually understand the code before it ships. Veracode's finding (44% of AI code introduces known vulnerabilities) is the quantitative basis.

**5. Volume × Error Rate = Risk**
A simple mental model: if code volume doubles and error rate stays constant, total bugs double. AI doesn't need to be worse than humans to increase systemic risk — it just needs to produce more code. This reframes AI coding risk from a quality argument to a volume/scale argument.

**6. Brand = Everything the User Experiences**
Customers attribute failures to the brand they're interacting with, not the underlying vendor. CNN's visitors saw CNN fail, not Optimizely. This reframes vendor risk as a product ownership problem: your product includes everything in the experience, even the parts you didn't build.