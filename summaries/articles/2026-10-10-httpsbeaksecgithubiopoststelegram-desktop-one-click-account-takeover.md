# Telegram Desktop vulnerability allowed any user's file to be stolen

Source: https://beaksec.github.io/posts/telegram-desktop-one-click-account-takeover/

## Summary
A security researcher (BeakSec) discovered a two-flaw chain in Telegram Desktop (through version 7.2.8) that allows one-click account takeover. The first flaw is an unescaped semicolon separator in Telegram's single-instance IPC socket, enabling command injection via a crafted `tg://` link. The second is an internal `interpret:` URI scheme that reads arbitrary local files and sends them to a chat with no authorization check. Chaining these two flaws lets an attacker exfiltrate a victim's Telegram session files — and take over their account — from a single clicked link.

## Key takeaways
- **CVE-2026-107181, CVSS 8.1 High**: Affects Telegram Desktop through 7.2.8; fixed in 7.2.9 (commit `db3405699f`, released Sept 17, 2026).
- **IPC injection**: Telegram's single-instance socket uses semicolons as command separators but never escapes semicolons within URL values, so a crafted link like `tg://x?a=1;CMD:quit` injects additional commands into the running instance.
- **Unguarded `interpret:` scheme**: An internal URI used for Telegram's own release automation reads any file from disk and posts it to a chat — no confirmation prompt, no check on who triggered it.
- **Predictable file paths**: Auto-downloaded group attachments land at a known path (`%APPDATA%\Telegram Desktop` relative), so an attacker can pre-plant instruction files without knowing the victim's username.
- **Account takeover without a passcode**: If no local passcode is set (the default), stealing `tdata/key_datas` is sufficient to decrypt the session authorization and fully replay the victim's account on a fresh install.
- **Delivery vector**: `tg://` links clicked inside Telegram are handled in-process (no injection possible), so the attacker sends an `https` link that redirects to the crafted `tg://` URL via their own server.
- **Mitigation**: Upgrade to Telegram Desktop 7.2.9 or later; optionally set a local passcode to add a layer of protection even if session files are stolen.