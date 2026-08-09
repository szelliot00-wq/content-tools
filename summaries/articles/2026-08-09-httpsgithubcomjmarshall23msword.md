# Microsoft Word for Windows 1.1a, Native X64 Port

Source: https://github.com/jmarshall23/msword

## Summary
This is a GitHub repository by jmarshall23 presenting a native x64 port of Microsoft Word for Windows 1.1a (codenamed "Opus"), originally a 16-bit application from the early 1990s. The project compiles the original Word source code and resources into a fully functional 64-bit Windows executable — not an emulator or reimplementation — by replacing only the platform-specific 16-bit assembly and Win16 APIs with modern equivalents. It uses CMake and Visual Studio 2022 as the build system, with a test suite covering runtime, UI, and compatibility with original behavior.

## Key takeaways
- The original C source and resource files are preserved as the authoritative implementation; only platform-bridging code was added or replaced.
- 16-bit x86 assembly entry points were translated to C/C++, segmented memory handles were mapped to x64-safe equivalents, and Win16 APIs were adapted to modern Win32.
- Build requirements are straightforward: 64-bit Windows, Visual Studio 2022, Windows 10/11 SDK, CMake 3.25+, and PowerShell.
- Legacy assembly modules are kept in the repo as an IDE-visible reference but are not compiled into any native build target.
- A comprehensive test suite guards correctness across the ported runtime, original data structures, process startup, and automated UI workflows (typing, formatting, dialogs, saving).
- The project is early-stage with 38 stars, 1 fork, and 13 commits as of the time of this article.