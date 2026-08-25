# Show HN: Screen memory without screenshots, just text to Markdown

Source: https://github.com/dragthelake/ambient-context

## Summary
Ambient Context is an early-stage macOS menu bar app (by dragthelake on GitHub) that captures screen content as text without screenshots. It uses the macOS accessibility tree to read the focused window's text every few seconds and appends it to a daily Markdown file, creating a local, LLM-readable log of your work. The goal is to let tools like Claude Code answer questions about your work history, write standups, or build project memory.

## Key takeaways
- Captures text from the focused window via the macOS accessibility tree — no screenshots, just plain text written to a Markdown file per day.
- Output files are structured with timestamps, app name, and window title as headings, with content deduplicated so each unique block appears only once per day (keeping files small enough to feed whole to an LLM).
- Built with Tauri (Rust + TypeScript/Vite), requires macOS 14+ on Apple Silicon, Node, Rust, and Xcode CLT; currently unsigned so must be self-built.
- Strong privacy design: only reads the active focused window, excludes password managers, private browsing, and secure input fields, pattern-scrubs secrets, and stores everything locally on disk only.
- Capture folder is excluded from its own capture, preventing recursive self-observation.
- Still early/experimental — seeking tester feedback on which apps return rich vs. empty text via the accessibility tree.