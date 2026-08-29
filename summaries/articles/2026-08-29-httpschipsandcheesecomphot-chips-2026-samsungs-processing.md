# Samsung's Processing-in-Memory (PIM)

Source: https://chipsandcheese.com/p/hot-chips-2026-samsungs-processing

## Summary
Samsung presented their LPDDR5X-PIM chip at Hot Chips 2026, which embeds MAC compute units directly inside standard LPDDR5X memory to exploit the chip's internal bandwidth (614 GB/s vs. 76.8 GB/s externally). The design cleverly repurposes standard DDR commands via special row addresses to trigger PIM modes, avoiding the need for a custom memory controller. However, the author argues that while the hardware engineering is impressive, the software challenges around multitasking, caching, and out-of-order execution make practical adoption very difficult without deeper changes to the memory subsystem.

## Key takeaways
- PIM blocks at each of the 16 DRAM banks can access full internal bandwidth (614 GB/s), an 8x improvement over the 76.8 GB/s available through the external interface.
- Per-chip compute throughput is modest (2.4 TOPS at 4-bit weights); useful throughput requires many chips in parallel, which is expensive.
- Samsung uses reserved "magic" row addresses to switch between normal and PIM modes, keeping compatibility with standard LPDDR5X memory controllers — an elegant hardware trick.
- PIM mode changes the meaning of read/write commands globally, so concurrent non-PIM memory accesses from other threads or processes can corrupt PIM state, making multitasking extremely difficult.
- CPU caching, prefetching, and out-of-order execution all break with PIM because reads have side effects and DRAM can generate values the cache hierarchy never sees — requiring uncacheable, non-speculative memory access, which severely hurts CPU performance.
- The author concludes that in-memory compute needs hardware-level support (e.g., OS-visible mode control, cache coherence integration) rather than the current software workaround of isolating memory regions and blocking threads.