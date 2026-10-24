# How close can pure functional programming get to C?

Source: https://rtfeldman.com/fp-vs-c

## Summary
The article benchmarks `roc-deflate`, a DEFLATE compression library written in Roc (a pure functional language), against `libdeflate`, a hand-tuned C library using architecture-specific SIMD instructions. Despite Roc being a memory-safe, garbage-collected functional language with mandatory bounds checks, `roc-deflate` came within a median of 2.6% (M1 Mac) to 8.9% (AMD Ryzen) of libdeflate's throughput across 144 benchmarks. The author argues this narrow gap, combined with Roc's strong safety guarantees, makes pure functional code a genuinely competitive option for performance-critical work.

## Key takeaways
- `roc-deflate` (pure Roc) ran only 2.6–8.9% slower than `libdeflate` (highly optimized C with SIMD), a result the author describes as previously unknown to be achievable.
- Roc already outperformed Rust's `miniz_oxide` in a prior benchmark, making libdeflate the last remaining performance target.
- C's performance ceiling is still higher — Roc's mandatory bounds checks, automatic reference counting, and memory safety impose a hard cap that C/Zig/Rust can exceed.
- On certain inputs, `roc-deflate` was actually ~18% *faster* than libdeflate, though this is due to algorithmic differences, not a Roc-specific advantage.
- Key optimization techniques used: avoiding unnecessary data sharing (enabling in-place mutation), hoisting bounds checks, building lookup tables at compile time, and using wrapping arithmetic to eliminate overflow checks.
- The safety trade-off is framed as compelling: guaranteed memory safety, no side effects, cross-target determinism, and no exploitable build scripts — all for a single-digit average performance cost.
- Roc is pre-1.0 (v0.1.0 imminent) and its package ecosystem has had almost no optimization work yet, so these results may improve further.