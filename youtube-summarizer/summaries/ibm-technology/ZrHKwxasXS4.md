# The Rise of Crypto Agility: How to Secure Systems for the Quantum Era

Video ID: `ZrHKwxasXS4`

## Summary
This video explains the concept of "crypto agility" — the ability to rapidly adapt cryptographic systems in response to new threats or vulnerabilities without disrupting business operations. Using historical examples of broken encryption standards, the presenter demonstrates that no algorithm lasts forever and that organizations must proactively prepare for the quantum computing era. The video outlines a practical framework for achieving crypto agility, from discovering existing cryptographic implementations to remediating weaknesses and building modular, adaptable systems.

## Key insights
- **Change is inevitable in cryptography:** Algorithms like DES (broken 1998, deprecated 2005), RC4 (broken 2001), and Triple DES (broken 2016, deprecated 2018) all had expiration dates, proving no standard lasts forever.
- **The quantum threat is real and imminent:** Quantum computers will be capable of breaking widely used encryption, including current 128-bit AES and RSA, requiring urgent action across industries.
- **AES can be hardened by doubling key size:** Upgrading from 128-bit to 256-bit AES is considered sufficient to withstand foreseeable quantum attacks for symmetric encryption.
- **RSA requires entirely new algorithms:** Unlike AES, asymmetric encryption like RSA cannot simply scale key sizes — it demands post-quantum cryptographic replacements.
- **Hardcoded crypto is a liability:** Embedding cryptographic code directly into applications makes updates slow, costly, and error-prone when algorithms are compromised.
- **Modular design enables crypto agility:** Centralizing cryptographic functions into a single callable library allows organizations to swap algorithms quickly without touching every application individually.
- **Discovery is the critical first step:** Organizations must audit their environments using scanning tools to build a "Cryptographic Bill of Materials" (C-BOM) — a full inventory of all cryptographic instances.
- **Prioritization is essential:** Large organizations may have thousands of cryptographic instances and cannot fix everything at once; risk-based prioritization determines what gets addressed first.
- **Remediation is an opportunity to future-proof:** When updating crypto for the quantum era, organizations should simultaneously build agility into their architecture to make future transitions far easier.