# More Tailscale tricks for your jailbroken Kindle

Source: https://tailscale.com/blog/jailbroken-kindle-proxy-tun-modes

## Summary
This Tailscale blog post (June 12, 2026) covers community-developed improvements for running Tailscale on jailbroken Kindle devices. An updated KUAL plugin by greywolf1499 adds proxy modes (SOCKS5 and HTTP) that work around the limitation of userspace-only Tailscale on Kindles, enabling apps like KOReader to actually route traffic through your tailnet. A separate KOReader-native Tailscale plugin also exists, adding support for Kobo and PocketBook devices beyond just Kindles.

## Key takeaways
- The original Tailscale Kindle implementation only made the device reachable on your tailnet — it couldn't route outgoing traffic to other Tailscale devices due to running in userspace (non-TUN) mode.
- A community update now adds SOCKS5 and HTTP proxy modes to the Kindle KUAL plugin, letting apps like KOReader connect to Tailscale-hosted servers (e.g., Calibre, Wallabag, Audiobookshelf).
- Practical use cases unlocked include syncing books from a self-hosted Calibre server, fetching articles via Wallabag, listening to Audiobookshelf, and even using the Kindle as a thin terminal client via SSH.
- A separate KOReader-native Tailscale plugin exists that handles proxy setup automatically within KOReader, and it supports Kobo and PocketBook devices in addition to Kindle.
- This is all community/unofficial code — patience and some technical comfort with jailbreaking are required; not all Kindle generations are supported equally.