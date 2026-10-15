# Show HN: Flipflop, iroh-powered persistent tunnels for filesharing

Source: https://github.com/andunieee/flipflop

## Summary
Flipflop is an open-source, Rust-based desktop application that uses the Iroh networking library to establish persistent peer-to-peer tunnels between devices for file sharing. Once two devices are paired, either can send files, text, pictures, or apps to the other at any time — even when the recipient is offline (sends are queued and retried). The project is actively developed, recently moved to a GPL-3.0 license, and is available on multiple platforms including Linux (Flatpak), Windows, Android (F-Droid, Zapstore), with 1,232 commits on the master branch.

## Key takeaways
- Built on **Iroh**, a Rust library for peer-to-peer connectivity, enabling direct device-to-device tunnels without a central relay server
- Tunnels are **persistent** — once established, you can send files to the other device anytime, including when it's offline (queued and retried on reconnect)
- Supports sending **files, text, pictures, and apps** through a unified interface
- Cross-platform: desktop (Linux Flatpak, Windows installer), Android (F-Droid and Zapstore), with a browser guest link option for recipients without the app
- Licensed under **GPL-3.0** (recently changed from a prior license due to Slint UI framework requirements)
- Early-stage project (version 0.0.6), actively developed with recent CI, release workflow, and distribution improvements