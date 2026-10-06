# Resurrecting iChat Audio and Video Conferencing

Source: https://blog.pipetogrep.org/2026/09/11/resurrecting-ichat-audio-and-video-conferencing/

## Summary
Chris Jones documents how they revived iChat AV's audio and video calling on OS X Leopard/Snow Leopard, which had broken because Apple's SNATMAP server (used for NAT traversal and public IP discovery) stopped responding and its configuration endpoint now redirects to HTTPS that old OS X can't handle. After a failed first attempt in 2023, Chris used an LLM in 2026 to reverse-engineer the SNATMAP protocol from network captures, then wrote a Python UDP server implementing it, and set up a full lab environment to test peer-to-peer iChat calls across simulated NAT. The fix is now publicly hosted, requiring only a single `/etc/hosts` entry on both Macs to restore video calling.

## Key takeaways
- Adding `157.230.2.213 configuration.apple.com` to `/etc/hosts` on OS X Leopard or Snow Leopard restores iChat AV audio/video calls using Chris's hosted SNATMAP server.
- iChat's AV calling relies on a SNATMAP server for NAT traversal — it discovers your public IP/port via UDP, then both clients attempt a direct peer-to-peer RTP connection without manual port forwarding.
- The root cause of failure was Apple's configuration endpoint redirecting to HTTPS, which old OS X TLS can't handle, causing iChat to fall back to exchanging private LAN IPs that don't work across the Internet.
- An LLM was used to reverse-engineer the SNATMAP binary protocol from packet captures, enabling the author to write a compatible server without needing to disassemble iChat.
- Self-hosting is possible: run the Python SNATMAP server, serve a `snatmap.txt` config file from a web server at the expected path, and point `configuration.apple.com` at your server.
- A modern Logitech webcam (tested: C920) works fine — an original iSight is not required.
- pfSense/OPNsense users need source port preservation enabled in outbound NAT settings for this to work.