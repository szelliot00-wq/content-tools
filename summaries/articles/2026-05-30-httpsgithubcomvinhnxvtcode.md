# Show HN: VT Code – open-source terminal coding agent in Rust

Source: https://github.com/vinhnx/VTCode

## Summary
VT Code is an open-source terminal coding agent written in Rust (94.5% of the codebase) by Vinh Nguyen. It provides LLM-native code understanding with support for multiple AI providers, a rich TUI interface, and a defense-in-depth security model. The project has gained 622 stars and 51 forks, with 383 releases and active development (version 0.115.0 released recently).

## Key takeaways
- **Multi-provider AI support**: Works with OpenAI, Anthropic, Google Gemini, DeepSeek, GitHub Copilot, OpenRouter, Ollama, LM Studio, and custom OpenAI-compatible providers
- **Security-first design**: Multi-layered security with tree-sitter-bash command validation, OS-native sandboxing (macOS Seatbelt, Linux Landlock + seccomp), workspace isolation, and configurable tool policies
- **Agent protocol support**: Implements A2A (Agent2Agent), ACP (Agent Client Protocol), Anthropic API compatibility, and the Open Responses specification for broad interoperability
- **Skills system**: Supports the open Agent Skills standard for extending functionality via discoverable, multi-location skill loading
- **Editor integration**: Native VS Code extension plus Zed IDE integration via ACP; also available on Open VSX for Cursor/Windsurf
- **Installation flexibility**: Available via native installer, `cargo install`, Homebrew, and cross-platform (macOS, Linux, best-effort Windows)
- **ATIF trajectory export**: Standardized session export for debugging, SFT, and RL pipelines, compatible with Claude Code, OpenHands, and Gemini CLI trajectories
- **Subagent/background agent support**: Can delegate work to foreground subagents or run configured background subprocesses