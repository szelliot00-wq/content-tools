# Cruller: Bun's Zig Runtime, Continued on Zig 0.16

Source: https://ziggit.dev/t/cruller-buns-zig-runtime-continued-on-zig-0-16/16734

## Summary
Cruller is a fork of Bun's Zig-based runtime, ported to vanilla Zig 0.16, created by solenopsys. It strips out development tooling (bundler, package manager, test runner, TypeScript transpiler) to produce a lean runtime focused solely on running pre-built production JavaScript servers. The port required decoupling Bun's build system from its patched Zig integration and adding compatibility shims for API changes since Zig 0.15.

## Key takeaways
- Cruller targets production deployment only — it loads pre-built JavaScript entrypoints and intentionally excludes package management, bundling, and transpilation.
- It retains JavaScriptCore, HTTP/1-3, WebSockets, streams, static serving, and the module resolver from Bun's original runtime.
- The stripped binary is ~73 MiB vs Bun's ~88.5 MiB, an ~18% size reduction, with near-identical JS benchmark performance (within 2% variance).
- The build now uses a vanilla Zig 0.16 build graph with a generated-code embedding module so release builds are self-contained and portable.
- AI was used as an engineering assistant for parts of the migration and debugging, but architecture decisions and verification remained maintainer-directed.
- Current status is work-in-progress; Zig semantic checks, CJS/ESM entrypoints, Node path tests, and basic HTTP smoke tests pass.