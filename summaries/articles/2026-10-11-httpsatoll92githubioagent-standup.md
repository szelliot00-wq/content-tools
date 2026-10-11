# AI agents in a stand-up call

Source: https://atoll92.github.io/agent-standup/

## Summary
Agent Standup is a free, open-source tool that visualizes Claude Code multi-agent sessions as a live "stand-up meeting" with cartoon characters, voices, and screen sharing. It reads session files that Claude Code already writes locally, requiring no configuration and sending no data anywhere. Available as a VS Code extension, desktop app, or CLI command, it works across all major editors and platforms.

## Key takeaways
- **Zero token cost**: reads existing Claude Code session files rather than making any API calls.
- **Cross-platform**: works in VS Code, Cursor, Windsurf, any terminal, or a standalone desktop app on Mac/Windows/Linux.
- **Agent status at a glance**: shows each sub-agent as working, waiting, needs attention (✋), stalled, or done — sorted by urgency.
- **Screen sharing**: agents display their actual terminal output and diffs in the meeting view.
- **Quick install**: `npx @double_geste/agent-standup --open` gets you running in ~30 seconds with no editor required.
- **Whimsical by design**: includes cartoon voices (Animal Crossing/Simlish style), lip-sync, custom pixel-art characters, and optional office sounds.
- **Privacy-first**: nothing is sent externally; visit counting uses only an anonymous 1-pixel GitHub file with no cookies or trackers.
- **Not affiliated with Anthropic**: MIT licensed, unofficial project.