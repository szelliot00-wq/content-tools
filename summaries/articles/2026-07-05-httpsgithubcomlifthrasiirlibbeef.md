# Beeg float library, a Rust port of Fabrice Bellard's libbf

Source: https://github.com/lifthrasiir/libbeef

## Summary
`libbeef` is a pure-Rust port of Fabrice Bellard's `libbf`, an arbitrary-precision floating-point library. It implements full IEEE 754 semantics with all five rounding modes, transcendental functions (sin, cos, exp, log, etc.), and decimal floating-point support. The library uses the same algorithms as the C original (NTT-based multiplication, Newton iteration, AGM/binary-splitting), achieving comparable performance with zero external dependencies.

## Key takeaways
- **Pure Rust, zero dependencies**: installs with a single `cargo add`, no C compiler or system libraries required; works on WASM, embedded, and cross-compiled targets.
- **Full IEEE 754 correctness**: signed zeros, NaN, infinities, subnormals, configurable exponent width, all five rounding modes — passes libbf's own verification suite.
- **Transcendental functions included**: exp, log, pow, sin, cos, tan, atan, atan2, asin, acos — all at arbitrary precision.
- **Competitive performance**: mul/div/sqrt are 1.1–2× slower than libbf and 1–4× vs GMP/MPFR; sin is actually faster than libbf. Growth follows the O(n log n) NTT envelope, not quadratic.
- **Small binary footprint**: 482 KiB stripped — smaller than malachite or rug despite including full floating-point and transcendentals.
- **`no_std` compatible**: only requires `alloc`, making it viable for embedded environments.
- **MIT licensed**: more permissive than GMP/MPFR's LGPL, reducing legal friction for license-sensitive projects.
- **When to use something else**: prefer rug/GMP if raw million-bit performance is critical; prefer num-bigint/malachite for integer-only work; the decimal path is functional but not yet performance-optimized.