# Any window from your Mac, on your iPhone and iPad

Source: https://github.com/Saffsanity/sill

## Summary
Sill is an open-source Mac app (with a companion iPhone/iPad app) that streams any Mac window or the full desktop to your iOS device over a local network, USB cable, Direct Wireless Connection, or a VPN like Tailscale. It uses HEVC video encoding and supports full two-way interaction via touch, trackpad, keyboard, and Apple Pencil — with no account or server required. The project is free, Apache-2.0 licensed, and built entirely in Swift using Apple frameworks.

## Key takeaways
- **No account or server**: all connections are peer-to-peer (local network, USB, Direct Wireless, or your own VPN), with end-to-end encryption and device pairing
- **Full input support**: touch, on-screen trackpad, physical keyboard/mouse, Apple Pencil, and even three-finger Mac trackpad gestures all work from the device
- **Clipboard sync**: text copies transfer both directions (up to 256 KB), but password manager concealed entries stay on the Mac
- **Menu bar integration**: Mac app menus are accessible from the iPad's own menu bar (iPadOS 26+) or Sill's toolbar
- **Free with no subscription**: optional GitHub Sponsors tip, but every feature is unlocked for everyone
- **Limitations**: no audio streaming, text-only clipboard, Mac must be awake with Sill running, and only one window (or desktop) at a time
- **Install options**: free notarized download from getsill.app, Homebrew cask, or build from source with Xcode 27