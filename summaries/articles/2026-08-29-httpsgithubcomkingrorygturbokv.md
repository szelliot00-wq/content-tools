# TurboKV: Insanely fast Rust key-value store

Source: https://github.com/kingroryg/turbokv

## Summary
TurboKV is an async embedded key-value store written in Rust, built on an LSM-tree architecture with atomic batch writes, ordered range scans, configurable durability modes, compression, and background compaction. It is available as a crate (`turbokv = "0.6"`) and integrates with Tokio. Benchmarks show it significantly outperforms comparable stores like fjall and redb, particularly for batch workloads.

## Key takeaways
- **Three durability presets**: `fast` (no WAL, in-memory only), `durable` (WAL without per-write sync, recommended default), and `paranoid` (full fsync before acknowledgement).
- **High throughput**: In recoverable mode, TurboKV achieves ~1.4M keys/sec sequential fill and ~2.3M keys/sec for large batches — roughly 1.8–4.4× faster than fjall and orders of magnitude faster than redb on macOS.
- **Atomic batch writes**: `WriteBatch` lets you group puts and deletes into a single atomic operation; readers see either the full batch or none of it.
- **Flexible scan API**: Supports range and prefix scans with both eager (`Vec`) and streaming iterator variants; keys are ordered lexicographically.
- **Configurable storage options**: Memtable size, block cache size, and SSTable compression (LZ4, Snappy, Zstd, or None) are all tunable via `DbOptions`.
- **Hardware AES required**: The persisted Bloom filter uses hardware AES instructions; x86 targets need `+aes,+sse2` and ARM targets need `+aes,+neon` RUSTFLAGS.
- **Clean shutdown matters**: Dropping a `Db` handle is not a clean shutdown — always call `close()` or `close_with_status()` explicitly.