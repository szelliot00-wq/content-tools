# Python utility package for building Claude Code hooks

Source: https://github.com/RasmusGodske/claude-hook-utils

## Summary
`claude-hook-utils` is a Python utility package by RasmusGodske that reduces boilerplate when building Claude Code hooks. It provides a base `HookHandler` class, typed dataclasses for hook inputs, and a builder pattern for responses, letting developers focus on validation logic rather than JSON parsing and schema formatting. The package supports PreToolUse, PostToolUse, UserPromptSubmit, SessionStart, SubagentStart, and SubagentStop hook types.

## Key takeaways
- **Install with** `pip install claude-hook-utils` — extend `HookHandler`, override the hook methods you need, and call `.run()`
- **Three response decisions** for PreToolUse: `allow`, `deny` (reason shown to Claude so it can adapt), and `ask` (prompts the user for confirmation)
- **Input helpers** like `file_path_matches('**/*.vue')` and convenience properties (`input.file_path`, `input.content`, `input.command`) simplify common checks
- **`with_updated_input()`** lets you modify tool parameters before execution (e.g., auto-correcting file paths)
- **Built-in JSONL logging** via `HookLogger` writes structured logs to `.claude/logs/{namespace}/hooks.jsonl`, with session ID auto-extracted
- **Fail-open error handling**: if your hook crashes, it exits 0 and allows the tool to proceed, so bugs in hooks don't block Claude Code
- **One handler, multiple hook types**: a single Python script can handle both PreToolUse and PostToolUse (or any combination) by overriding multiple methods