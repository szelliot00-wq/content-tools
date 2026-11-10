# ClickHouse Acquires Xata

Source: https://xata.io/blog/xata-is-joining-clickhouse

## Summary
Xata, a branch-native Postgres platform, is joining ClickHouse to bring agentic database capabilities to ClickHouse Managed Postgres. The acquisition combines ClickHouse's high-performance, NVMe-backed production Postgres with Xata's technology for instant database provisioning, copy-on-write branching, and scale-to-zero compute. The goal is to build a Postgres platform optimized for modern AI-driven development workflows where every pull request and agent run gets its own isolated database branch.

## Key takeaways
- Xata's core innovation is copy-on-write branching: even a multi-terabyte database can be branched in ~3 seconds without duplicating data, so you only pay for the diff.
- ClickHouse Managed Postgres, built on local NVMe storage, is currently the fastest Postgres service available; Xata's technology complements it by handling large fleets of short-lived, mostly-idle databases cheaply via scale-to-zero.
- The combined platform targets two key agentic use cases: a database branch per pull request (for safe CI/CD testing) and a database branch per AI agent run (for isolated development without touching production).
- AI-native companies are already creating thousands of database branches per week, signaling strong demand for this kind of ephemeral, production-like database infrastructure.
- Xata customers are unaffected in the short term; a migration to ClickHouse Managed Postgres will come later.
- The deal also positions the combined company to deliver a first-class integrated OLTP (Postgres) + OLAP (ClickHouse) platform, something developers have historically had to stitch together manually.