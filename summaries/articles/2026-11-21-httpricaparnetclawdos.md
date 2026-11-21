# ClawDOS – An AI coding agent for DOS

Source: http://ricapar.net/ClawDOS/

## Summary
ClawDOS is an AI coding agent built to run on original IBM PC XT hardware from the 1980s — an 8088 processor at 4.77 MHz with 640K RAM. The harness (`HARNESS.EXE`) runs entirely on DOS and communicates directly with the Claude Messages API, using a separate "bridge" machine only to handle TLS (which the 8088 cannot do). It can write, compile, and run C programs; take CGA screenshots; play music; and persist memories between sessions — all on hardware over 40 years old. The project was built almost entirely by Claude itself, as a creative experiment in pushing AI tooling to extreme legacy constraints.

## Key takeaways
- The entire agent loop runs natively on DOS: HTTP requests, JSON parsing, SSE streaming, and tool execution are all handled by a 176 KB executable on the 8088.
- A separate TLS tunnel on a modern machine bridges plain HTTP from the PC to `api.anthropic.com`, keeping the API key off the PC's disk if desired.
- ClawDOS has 18 tools covering file I/O, running DOS programs, memory/port access, screenshots (encoded as PNG on the 8088), PC speaker music, and persistent notes in `C:\MEMORY`.
- It supports a full development environment on-disk: Turbo C 2.0, two assemblers, GW-BASIC, and a debugger — and knows how to drive each one.
- Prompt caching means after the first request, only new content is uploaded; a typical tool result costs ~500 bytes over the wire, keeping it usable on slow connections.
- Conversations are stored in the API's own message format on disk and survive power loss; any prior chat can be reopened and continued.
- 100% of the repository code (outside the author's personal note) was written by Claude, making it a self-referential demonstration of agentic coding.
- It can run in emulation (86Box) or on real hardware via a PicoMEM card that emulates a hard drive from a microSD card.