# We Replaced MMAP with Io_uring in Our Rust Query Engine. It Got Slower

Source: https://www.conviva.ai/resource/we-replaced-mmap-with-io_uring-in-our-rust-query-engine-it-got-slower/

## Summary
Conviva's engineering team replaced mmap-based file reads with io_uring in their Rust/DataFusion query engine, expecting dramatic performance gains by bypassing the kernel page cache. Instead, the initial io_uring implementation ran 60% slower than mmap on cold reads (21.8s vs 13.6s), despite reducing major page faults by 35×. The article documents the root cause of mmap's failures under concurrent load — page cache thrashing, lock contention, and a storm of minor faults — and explains why the first io_uring design failed to capitalize on those insights.

## Key takeaways
- **mmap breaks under concurrency**: The kernel's page cache is shared host-wide across all pods; under heavy concurrent load, p95 latency spiked from ~30s to 150s+, driven by page cache thrashing, 2M+ minor faults/sec, and 2M+ context switches/sec — not actual disk I/O.
- **The hardware ceiling was far out of reach**: mmap delivered only ~3.44 GB/s of the available ~21.7 GB/s NVMe throughput — a 16% utilization rate.
- **io_uring solved the wrong bottleneck first**: Major faults dropped 35×, but a single-threaded "Batch Materialization Layer" doing I/O coordination, Arrow decoding, cache management, and query serving all at once became the new bottleneck.
- **O_DIRECT helped, but modestly**: Enabling O_DIRECT reduced runtime from 21.8s to ~19s — real, but far short of expectations, partly due to an extra memory copy when constructing Arrow buffers.
- **Design before building**: The team notes in hindsight that proper io_uring design requires upfront architectural work; iterating fast without that led to a layered design that was hard to optimize.
- **Part 2 covers the fix**: The resolution — identifying that 40 concurrent SQEs was the actual problem, plus an architectural rethink — is addressed in the follow-up article.