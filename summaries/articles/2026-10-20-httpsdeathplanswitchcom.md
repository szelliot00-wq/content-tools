# Show HN: Death Plan Switch, a self-hosted dead man's switch for solo devs

Source: https://deathplanswitch.com/

## Summary
Death Plan Switch is a free, self-hosted dead man's switch built by a solo developer in regional New South Wales, Australia. It sends a weekly check-in email; if the developer stops responding, it escalates to next of kin and then to relevant contacts (clients, backup developers, etc.) within 13 days. The project was born from the realization that a one-person web business leaves clients with no way to recover domains, hosting, or credentials if the owner dies or becomes incapacitated.

## Key takeaways
- **How it works:** A weekly email requires the user to actively press a button to check in; link-opens don't count because email scanners can trigger those automatically.
- **Escalation chain:** Non-response escalates first to next of kin, then to designated contacts (e.g., backup developer, clients), all within 13 days of the last check-in.
- **Minimal technical requirements:** Requires PHP 8.1+, no database, installs via browser in minutes; the only manual step is a crontab line that the installer writes for you.
- **Self-hosted and open source:** Free, MIT licensed, designed for developers who want control over their own infrastructure rather than relying on a third-party service.
- **Practical motivation:** Targets solo/independent developers whose clients' sites, domains, and hosting all run through one person with no fallback if that person disappears.
- **False alarm protection:** After the switch fires, a button lets you notify contacts it was a false alarm.