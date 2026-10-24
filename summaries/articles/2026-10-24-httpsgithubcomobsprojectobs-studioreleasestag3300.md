# OBS Studio 33

Source: https://github.com/obsproject/obs-studio/releases/tag/33.0.0

## Summary
OBS Studio 33.0.0 is a major release of the open-source streaming/recording software, featuring a complete plugin loading overhaul, a significant CEF (Chromium Embedded Framework) update, and numerous UX improvements. The release also delivers a broad set of bug fixes addressing crashes across macOS, Linux, and Windows, along with improvements to capture sources and audio handling.

## Key takeaways
- **CEF updated from 127 to 150** (build 7871), bringing a newer browser engine to OBS's browser source functionality.
- **Plugin loading was completely overhauled**, changing how third-party plugins are discovered and loaded — users with existing plugins should check the knowledge base article for migration guidance.
- **NVENC hardware encoding is now enabled on Arm64**, expanding GPU encoding support to Arm-based Windows devices.
- **Source snapping in the preview was improved**, along with better spinbox behavior for number inputs throughout the UI.
- **Safe Mode no longer starts the WebSocket Server**, reducing potential attack surface when launching in that mode.
- **Multiple crash fixes** were landed: macOS startup crash, Linux USB mic removal, invalid shader cache, profile switching, and more.
- **Game Capture fullscreen detection improved** on Windows, and macOS Screen Capture transparency handling was also refined.
- **Ubuntu 24.04 support was dropped**; the release targets Ubuntu 26.04 for the Linux `.deb` package.
- **For developers**: minimum supported versions of Visual Studio, Windows SDK, and clang-format have been raised; new frontend APIs were added for replay buffer signals, safe mode detection, and canvas video state.