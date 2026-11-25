# Taking over US Treasury subdomains for $3 each

Source: https://www.intruder.io/research/taking-over-us-treasury-subdomains-for-3-each

## Summary
Researchers at Intruder demonstrated that dangling DNS records pointing to released AWS Elastic IP addresses (EIPs) can be hijacked by anyone willing to cycle through the EIP pool. For just $3 per successful takeover, they claimed 28 live subdomains within 48 hours — including five belonging to US Treasury — by automating EIP allocation across AWS regions. All findings were responsibly disclosed, but AWS declined to make changes, leaving the vulnerability class open.

## Key takeaways
- **Dangling DNS records are a real, exploitable risk:** When an organization releases an AWS EIP but leaves the DNS A record pointing to it, an attacker can claim that IP and serve arbitrary content under the organization's subdomain.
- **The attack is cheap and scalable:** Cycling through ~450,000 unique IPs cost roughly $3 per valid hit. Using multiple AWS accounts (bans are per-account only), an attacker could sweep the full EIP space in ~5 weeks.
- **Government infrastructure was affected:** Five US Treasury subdomains were among the 28 successfully claimed, highlighting that even high-value targets have this exposure.
- **Impact is severe:** A taken-over subdomain can host phishing pages with valid TLS certificates, steal credentials from legacy automations, and potentially hijack session cookies scoped to parent domains.
- **AWS won't fix it at their end:** Amazon considers this a customer-side DNS misconfiguration, not an AWS issue, and has no plans to change EIP allocation behavior.
- **Action required now:** Audit your DNS records for dangling A records pointing to EIPs you no longer own, and remove or update them immediately.