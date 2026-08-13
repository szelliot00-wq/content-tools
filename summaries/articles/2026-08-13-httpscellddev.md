# Celld: Self-hosted, distributed Durable Objects

Source: https://celld.dev/

## Summary
Celld is an open-source, self-hosted alternative to Cloudflare's Durable Objects that lets you run Workers/DO code unchanged on your own infrastructure. It uses an S3-compatible bucket as the coordinator — storing cell ownership leases and SQLite state — with no consensus protocol required. The project targets teams who want the Durable Objects programming model (single-threaded, named, stateful actors) without the cost or vendor lock-in of Cloudflare's managed service.

## Key takeaways
- **Drop-in compatibility**: Existing Workers and Durable Objects code runs unchanged on celld (within its supported API surface).
- **You own your data**: All state is stored as SQLite/LTX segments in a bucket you control, not a vendor-managed datastore.
- **Dramatic cost savings at scale**: At 1,000 resident cells, Cloudflare DO costs ~$4,150/mo vs. celld's ~$49/mo; at 100,000 cells, $415,000/mo vs. ~$1,949/mo.
- **Strong durability guarantees**: RPO=0 (zero acknowledged writes lost on node kill), with ~20s failover after node loss.
- **High density and low overhead**: ~0.47 MB RAM per resident cell, fitting ~2,500 cells per 8 GB node at ~$0.02/cell-month.
- **Bucket-as-coordinator design**: Ownership is claimed via atomic compare-and-swap writes to S3 — no membership protocol, failure detector, or consensus layer needed.
- **Explicit failure domain**: Self-hosting makes failures inspectable (your nodes, your bucket provider) and eliminates noisy-neighbor coupling with other tenants on Cloudflare's shared scheduler.
- **Lightweight install**: Ships as a single 58 MB static binary or Docker container.