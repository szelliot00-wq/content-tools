# WeWorm: Zero-Click WeChat Worm

Source: https://calif.io/research/weworm

## Summary
Calif Research published details of WeWorm, the first zero-click worm capable of spreading through WeChat voice calls on both iOS and Android. By exploiting a memory corruption bug in WeChat's VoIP stack, an attacker can silently compromise a victim's account while their phone is still ringing — no interaction required — then use that account to call and infect more contacts. The bug was discovered with AI assistance, reported to Tencent in July 2026, and mitigated server-side for all users by August 28 before this public disclosure.

## Key takeaways
- **Zero-click, zero-interaction:** The victim does not need to answer or even touch their phone; declining a call stops one attempt, but the attacker can retry (e.g., while the victim sleeps).
- **Self-propagating worm:** Once a device is compromised, it automatically calls the victim's contacts, spreading the infection chain indefinitely across iOS and Android.
- **Exploits trusted contact model:** WeChat grants friends elevated privileges, so compromising one contact in a network can be used to reach and infect everyone they know.
- **AI dramatically lowered the bar:** The team found the bug and wrote the first RCE exploit in ~2 days using AI; the full worm demo took one more week — work that previously required a large team and months.
- **Tencent has patched it:** Android 8.0.77 and iOS 8.0.76 mitigate the bug; server-side mitigation was confirmed for all users on August 28, 2026.
- **Broader warning:** AI is now putting nation-state-level offensive capabilities into less-skilled hands, raising urgent risk for ordinary users of popular messaging apps worldwide.
- **Coordinated disclosure:** Calif followed responsible disclosure, working with Tencent before publishing, and is withholding full technical details pending a conference presentation.