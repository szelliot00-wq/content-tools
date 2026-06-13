# On CPU Physics and CPU Cycles

Source: https://6it.dev/blog/on-cpu-physics-and-cpu-cycles-80730

## Summary
This is a draft chapter from an upcoming book "Efficient C++ Programming for Modern 64-bit CPUs" covering CPU architecture and memory hierarchy from a performance perspective. It walks through the latency costs at each level of the memory/storage stack — from CPU registers and caches through RAM, SSDs, HDDs, and network connections — explaining the physics behind why distance increases latency. The chapter also covers branch misprediction, TLBs, and how C++ storage durations (stack, heap, static, thread-local) map to cache behavior.

## Key takeaways
- **Distance = latency**: Signal speed is governed by parasitic capacitances proportional to wire length, not the speed of light — this is why on-chip access is so much faster than off-chip.
- **Memory hierarchy costs (approximate CPU cycles)**: R-R operation ~1, L1 cache ~3, L2 ~10–15, L3 ~30–70, main RAM ~200–300, NVMe SSD ~30,000–45,000, SATA SSD ~240,000–300,000, HDD ~30,000,000–45,000,000.
- **Branch misprediction costs 15–25 cycles**: Modern CPUs use dynamic branch prediction based on runtime history, so `[[likely]]`/`[[unlikely]]` hints have limited value and should only be used when you're extremely confident (e.g., error handling paths).
- **Superscalar CPUs can retire multiple instructions per cycle**: Achieving even 4 RIPC is challenging in practice; non-integer benchmark results (e.g., 0.75 cycles/op) reflect statistical averaging across parallel execution units.
- **TLBs rarely matter for typical C++ apps**: Using linear data structures (e.g., `std::vector`) minimizes DTLB pressure; huge pages are the fix when TLB misses do become a bottleneck (typically only in databases or JVM workloads).
- **Heap data should be treated as uncached** unless you recently accessed nearby memory; stack is almost-guaranteed cached due to frequent access; static/global variables are cached "reasonably well."
- **Network latencies dwarf local storage**: LAN is ~100,000–500,000 cycles; Wi-Fi ~3–30M cycles; intercontinental round-trips can reach 750M+ cycles. Network worst-case latency is effectively unbounded.
- **`fsync()` latency varies enormously**: From ~120,000 cycles for enterprise RAID with battery-backed cache to 50–200M cycles for HDDs — critical for database design decisions.