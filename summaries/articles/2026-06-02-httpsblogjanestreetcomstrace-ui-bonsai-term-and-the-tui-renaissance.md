# strace-ui, Bonsai_term, and the TUI renaissance

Source: https://blog.janestreet.com/strace-ui-bonsai-term-and-the-tui-renaissance/

## Summary
Jane Street's blog post describes `strace-ui`, an interactive TUI wrapper around the `strace` debugging tool, and the framework that made it possible: `Bonsai_term`. Originally a web UI framework built in OCaml, Bonsai was extended to the terminal, and its arrival coincided with a broader TUI renaissance driven largely by the success of AI coding agents like Claude Code. The combination of a powerful reactive framework, screenshot-based testing, and AI assistance has sparked a wave of new terminal app development internally at Jane Street.

## Key takeaways
- **`strace-ui`** transforms the raw, hard-to-parse output of `strace` into an interactive terminal UI with features like FD filtering, struct formatting, and hex dump rendering.
- **`Bonsai_term`** is an extension of Jane Street's `Bonsai` web UI framework (OCaml, functional, reactive) adapted for terminal UIs — the same primitives that power their web apps now power TUIs.
- **Claude Code's arrival in early 2025** is credited as a catalyst for the TUI renaissance: terminal apps won out over IDEs for AI-assisted development due to their speed, simplicity, and ubiquity.
- **Screenshot-based expect tests** make Bonsai_term unusually AI-friendly — agents can run tests and read the text output as a literal UI rendering, enabling a tight feedback loop.
- **Jane Street built their own Claude Code-like tool (AIDE)** using Bonsai_term, which in turn accelerated the framework's development by generating reusable UI components.
- **TUIs have practical advantages over web apps** in this context: no JS transpilation issues, full access to native OCaml libraries, keyboard-driven, and fast by default.