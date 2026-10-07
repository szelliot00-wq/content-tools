# Hackers obtain counterfeit TLS certificates for Google and other large services

Source: https://arstechnica.com/security/2026/10/hackers-obtain-counterfeit-tls-certificates-for-google-and-other-large-services/

## Summary
Attackers hijacked three country-code top-level domains (.gh, .sl, .as) and manipulated their authoritative DNS records to pass automated domain control validation checks. This allowed them to obtain fraudulent TLS certificates for Google and other major organizations. Google responded by updating Chrome to block the identified unauthorized certificates and working with certificate authorities to revoke them.

## Key takeaways
- Attackers compromised three top-level domain registries (.gh Ghana, .sl Sierra Leone, .as American Samoa) to gain DNS control over domains within those namespaces.
- By controlling DNS records, they passed automated domain control validation and obtained counterfeit TLS certificates for "several Google domains" and other major services.
- Unauthorized TLS certificates enable cryptographic impersonation — attackers can pose as legitimate sites to intercept traffic.
- Chrome was updated to block the identified rogue certificates; no action required from end users.
- Google advises domain owners to monitor certificate transparency logs for unexpected issuance and to publish restrictive CAA (Certification Authority Authorization) DNS records as a defensive measure.
- Relying solely on browser-side protections is insufficient — domain owners must take proactive steps to harden their own certificate management.