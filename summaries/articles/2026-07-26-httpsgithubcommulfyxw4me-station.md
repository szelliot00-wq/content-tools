# W4ME Station – a WASM-4 runtime for Java ME phones

Source: https://github.com/mulfyx/w4me-station

## Summary
W4ME Station is an open-source WASM-4 game runtime for Java ME (CLDC 1.1 / MIDP 2.0) feature phones, enabling unmodified WebAssembly game cartridges to run on mid-2000s devices like the Nokia E71. Version 1.0.0 ships with 13 bundled games in a 275 KB JAR, requires no JIT compiler, and supports cartridge loading via HTTP(S), RMS, URLs, or the optional JSR-75 file browser. The project is MIT-licensed and targets the retro/J2ME ecosystem with a full development toolchain containerized via Podman and Distrobox.

## Key takeaways
- Runs unmodified WASM-4 `.wasm` cartridges on legacy Java ME phones (CLDC 1.1 / MIDP 2.0) with no JIT — pure interpreter-based execution.
- Ships 13 bundled games (Sokoban, Chess, Tetris-like Watris, etc.) in a package under 300 KB; additional cartridges can be sideloaded from HTTP(S) or local storage.
- Two release variants: a full build with optional JSR-75 file browsing, and a base build for devices lacking that API.
- Implements the full WASM-4 host API surface: graphics, input, audio (MMAPI/MIDI), disk storage, text, and tracing.
- Supports phone keys, keyboard, pointer input, and an on-screen touch pad that stays outside the 160×160 framebuffer on larger screens.
- Per-cartridge save state is persisted via checksummed RMS generations; sound settings also persist across MIDlet restarts.
- Development stack requires Linux with `just`, Podman, and Distrobox; Java sources are pinned to Java 1.3 for maximum device compatibility.