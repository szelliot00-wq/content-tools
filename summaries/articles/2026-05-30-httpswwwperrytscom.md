# Perry Compiles TypeScript directly to executables using SWC and LLVM

Source: https://www.perryts.com/

## Summary
Perry is a TypeScript-to-native compiler that uses SWC for parsing and LLVM for code generation, producing standalone executables without any runtime dependency. It targets 10 platforms (macOS, iOS, iPadOS, Android, Linux, Windows, watchOS, tvOS, WASM, and Web) using real native UI frameworks rather than web views or Electron. Binaries are typically 2–5 MB and start in ~1 ms, with benchmarks showing up to 18x faster execution than Node.js.

## Key takeaways
- **No runtime required:** Perry compiles TypeScript directly to native binaries via SWC + LLVM — no Node.js, V8, or Electron needed.
- **Small, fast binaries:** Output is 2–5 MB (vs ~80–90 MB for Node/Bun) with ~1 ms startup time and up to 18x better performance on certain benchmarks.
- **True native UI across 10 platforms:** Uses AppKit, UIKit, GTK4, Win32, SwiftUI, and JNI — not web views — with 25+ native widgets.
- **Familiar TypeScript APIs:** Supports standard Node.js APIs (fs, path, crypto, child_process, etc.) and 30+ popular npm packages reimplemented natively in Rust.
- **Optional V8 runtime:** For npm packages that can't be reimplemented natively, a `--enable-js-runtime` flag enables full npm ecosystem compatibility at the cost of a larger binary (~15–20 MB).
- **Integrated publish pipeline:** `perry compile`, `perry publish`, and `perry verify` handle code signing, App Store submission, and automated cross-platform UI testing end-to-end.
- **Deterministic builds:** Same input always produces the same binary, enabling reproducible CI builds.
- **Generics via monomorphization:** The type system handles generics the same way Rust does, baking specializations into the binary at compile time.