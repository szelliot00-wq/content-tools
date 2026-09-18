# The scourge of x86 emulation

Source: https://fex-emu.com/Scourge-of-emulation/

## Summary
This technical deep-dive from the FEX (x86-on-ARM) emulator team explains why emulating the x86 Total Store Ordering (TSO) memory model on ARM's weak-ordering architecture is so difficult. The article walks through the cascading performance and correctness challenges — from basic load/store semantics, to unaligned memory accesses, to atomic instructions and split-locks — with benchmark data across multiple ARM platforms (AmpereOne, Cortex-X4, Cortex-X925, Oryon-3, Apple M1). It highlights where hardware vendors have partially or fully solved these problems, and where fundamental gaps remain.

## Key takeaways
- **x86 vs ARM memory models are fundamentally different**: x86-TSO enforces strict coherency by default; ARM is weakly ordered and requires explicit acquire/release instructions to approximate x86 behavior, which is costly.
- **ARMv8.3+ LRCPC instructions help significantly**: The `RCpc` memory model extension was designed with x86 emulation in mind and largely "solves" basic load performance, but still has gaps.
- **Apple Silicon's hardware TSO toggle is the gold standard**: Apple embedded a full TSO hardware mode, making memory emulation nearly free — showing what serious commitment to x86 emulation looks like.
- **Unaligned memory accesses are a major pain point**: x86 applications frequently access memory without alignment, forcing FEX to backpatch instructions with slow memory barriers (`DMB`) at runtime, causing up to ~50% performance penalties on some cores.
- **Atomic split-locks are the hardest problem**: x86 guarantees atomic operations across cacheline boundaries (split-locks); no current ARM hardware fully supports this. Emulating it correctly requires kernel intervention and is extremely slow (~1000x latency increase in worst cases).
- **Qualcomm Oryon-3 partially solves atomics**: Its "coherent cachelines" feature allows unaligned atomics within a 64-byte cacheline without penalty — matching x86 behavior for most cases, though full split-lock support still requires kernel patches.
- **Valve's Steam Frame ships a kernel patch** written by a FEX developer that handles unaligned atomics in-kernel, achieving ~5x better latency than unpatched platforms.
- **ARM's `FEAT_LSE2` extension helps but falls short**: It loosens alignment requirements within 16-byte granules, but x86 applications frequently cross that boundary, so the practical benefit is marginal.
- **Correct split-lock emulation likely requires hardware support**, possibly via ARM's Transactional Memory Extension (TME), as software-only approaches are either incorrect or have intractable performance costs.