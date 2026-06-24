# "Fix" MacBook Neo Cursor Lag: Record 1 Pixel of the Screen Every 10 Seconds

Source: https://gist.github.com/retroplasma/ec21767d0a8380c7ea9c2fbee1c7d6bf

## Summary
"Unlag Neo" is a workaround for a cursor lag bug affecting MacBook Neo (macOS Tahoe) where the cursor stutters near screen edges or inside Terminal windows. The fix exploits the fact that macOS eliminates the lag when screen recording is active — so the tool starts a minimal ScreenCaptureKit session that records just 1 pixel at 1 frame per 10 seconds, using negligible CPU/GPU/SSD resources. A shell script compiles and packages the solution as a standalone `.app` requiring no Xcode or developer account.

## Key takeaways
- The root cause is a macOS Tahoe bug where cursor lag occurs near screen edges and in Terminal; activating screen recording suppresses it.
- The fix records a 1×1 pixel region every 10 seconds and discards the frames — enough to trigger the OS behavior that removes the lag with virtually no system impact.
- A bash script (`create_unlag_neo_app.sh`) compiles a Swift app using only the system's `swiftc` compiler — no Xcode or Apple Developer account needed.
- The app lives in the menu bar with options to enable/disable, toggle "Pause in Fullscreen" (hides the recording indicator during fullscreen video), and set launch-at-login.
- Requires Screen Recording permission; optionally requires Accessibility permission for the fullscreen-detection feature.
- The screen recording indicator is small and considered an acceptable tradeoff by the author, though it does undermine the usual purpose of that privacy indicator.