# A 100x faster* alternative to homebrew

Source: https://github.com/zerobrewhq/zerobrew

## Summary
zerobrew is a Rust-based, uv-style package manager client for the Homebrew ecosystem on macOS and Linux. It installs the same Homebrew bottles from the same sources but uses a content-addressed store and parallel extraction to dramatically reduce install times. It is experimental and recommended to run alongside Homebrew rather than as a full replacement.

## Key takeaways
- **Significant speed gains**: zerobrew is 6–16x faster than Homebrew on cold installs and up to 121x faster on warm installs (cached downloads), with 100 packages taking 117s vs Homebrew's 776s cold.
- **Same packages, different install method**: Both tools download the same Homebrew bottles; the speed difference comes from zerobrew's content-addressed store and skipping Ruby formula evaluation, path rewriting, and per-binary re-signing.
- **uv-inspired architecture**: The project brings the same architectural approach that made `uv` fast for Python packages to the Homebrew ecosystem.
- **Compatible CLI**: Supports common workflows — `zb install`, `zb bundle`, `zb upgrade`, `zb outdated`, and running packages without linking via `zbx`.
- **Still experimental**: The project recommends running it alongside Homebrew rather than replacing it outright, especially without understanding the implications.
- **CI-verified parity**: A parity workflow confirms zerobrew-installed and Homebrew-installed prefixes match byte-for-byte; a timing workflow enforces minimum speedup thresholds nightly.