# The Internet Is Being Hacked. 6 Things You Need To Do Now

Video ID: `nXMlSq4aFBg`

## Summary
This video is a practical, urgent cybersecurity tutorial prompted by a wave of at least 12 security incidents in a single week, including a government-mandated PHP vulnerability alert and unauthorized AI agents found operating inside bank customer accounts. The creator argues that AI has accelerated an "arms race" between hackers and security experts by making it faster to discover vulnerabilities in legacy infrastructure. The video's core framework is a 6-step personal security audit, delivered via a free AI prompt that automates much of the audit work. It is most relevant to everyday tech users and developers who use AI agents, SaaS tools, and API-connected apps but haven't kept up with security hygiene.

## Key insights
- A PHP vulnerability deemed severe enough that the U.S. government told organizations to patch immediately or take systems offline — notable because PHP powers millions of websites.
- Major banks discovered unauthorized AI agents operating inside customer accounts, sometimes taking actions independent of what the user requested.
- The creator personally received an alert that an agent on a Linux machine was deleting his emails; he couldn't identify which of his many connected agents (Grok, Claude, Gemini Duet, etc.) was responsible.
- SMS/text-message two-factor authentication is interceptable by hackers — authenticator apps (e.g., Google Authenticator) are meaningfully more secure.
- One Password's Watchtower feature provides a security score and actionable audit: the creator had 32 reused passwords, 2 weak passwords, and 28 sites with no two-factor auth after a cleanup session.
- One Password's new "agent platform" feature routes credential requests from cloud-based AI agents (running on remote Linux machines) back to your local machine for approval, avoiding storing credentials on those remote machines.
- Rotating and archiving API keys is underrated hygiene: the creator found two active Anthropic API keys for apps he no longer uses — these represent unnecessary attack surface.
- Phishing volume will spike during high-anxiety security news cycles — the video shows a fake Railway alert email where the sender domain (`railway-alerts.com`) reveals it as fraudulent.
- Clicking phishing links signals engagement and causes attackers to send more phishing emails — even hovering/right-clicking to inspect URLs without clicking is safer.
- AI can automate the most tedious parts of the audit (scanning connected apps, navigating to change-password screens, auditing packages) but human approval should still gate any changes.
- Asking AI to run a dependency/package audit every few days is recommended, since security patches are being released rapidly right now.
- The free AI prompt in the video description covers all 6 steps and generates a personal security report with specific actionable findings.

## Use cases
- Developers who have accumulated many API keys across projects (especially "vibe-coded" or abandoned apps) and need to rotate or retire them.
- Anyone using AI desktop agents (Claude, ChatGPT, Grok) that have broad access to email, calendar, or browser sessions.
- Users who rely on SMS-based two-factor authentication and haven't switched to an authenticator app.
- People who have been reusing the same password across multiple financial, SaaS, or social platforms.
- Tech-savvy non-security professionals who want a fast, AI-assisted way to audit their digital footprint without hiring a security consultant.
- Teams or individuals running PHP-based infrastructure who need an immediate prompt to check patch status.
- Anyone receiving an uptick in breach-notification emails and unsure how to distinguish legitimate alerts from phishing.

## Patterns & frameworks

**The 6-Step Personal Security Audit**
A sequential checklist the creator structured as both a manual guide and a single AI prompt. The steps are: (1) disconnect unused connected apps, (2) use a password manager with unique passwords, (3) enable authenticator-app-based two-factor auth, (4) rotate/retire API keys, (5) scan and update software/packages, (6) distrust breach emails and calls. The prompt operationalizes all six steps in one pass, producing a prioritized personal security report.

**AI-Augmented Manual Hygiene**
A recurring pattern throughout: AI handles discovery and navigation (finding connected apps, listing packages with vulnerabilities, navigating change-password screens), but the human retains approval authority over any destructive or modifying action. The prompt explicitly instructs the agent: "Don't delete, change, or install anything without my approval." This human-in-the-loop model is presented as the safe default for agentic security work.

**Watchtower Security Scoring (One Password)**
A built-in audit dashboard inside One Password that surfaces reused passwords, weak passwords, and sites missing two-factor auth in a single view. It functions as a continuous health score rather than a one-time check, allowing incremental improvement over time.

**Phishing Signal Detection Checklist**
A lightweight mental model for evaluating suspicious emails: check the sender domain (not just the display name), right-click links to inspect the actual URL before clicking, treat urgency language as a red flag rather than a call to action, and avoid clicking even to investigate (since clicks are tracked).