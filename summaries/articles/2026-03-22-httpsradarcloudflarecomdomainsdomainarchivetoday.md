# Cloudflare flags archive.today as "C&C/Botnet"; no longer resolves via 1.1.1.2

Source: https://radar.cloudflare.com/domains/domain/archive.today

## Summary
Cloudflare has classified the web archiving service `archive.today` (along with its mirror domains like `archive.ph` and `archive.is`) as "C&C/Botnet." Consequently, Cloudflare's 1.1.1.2 DNS resolver, which filters out malware and botnet activity, will no longer resolve these domains for its users. This means that individuals relying on Cloudflare's security-focused DNS service will be blocked from accessing the archiving site. The decision has generated significant discussion and attention within the tech community, as evidenced by its Hacker News engagement.

## Key takeaways
- Cloudflare has flagged `archive.today` and its mirror domains as "C&C/Botnet," a severe classification indicating suspected malicious command-and-control or botnet activity.
- Users relying on Cloudflare's 1.1.1.2 DNS resolver, which is designed to block malware and botnets, will no longer be able to access `archive.today`.
- The classification of a prominent web archiving service as a botnet component is an unexpected and notable development, prompting questions about the specific detected threats or misuse of its infrastructure.
- The action has generated considerable discussion and interest within the tech community, highlighted by its activity on Hacker News (113 points, 54 comments).