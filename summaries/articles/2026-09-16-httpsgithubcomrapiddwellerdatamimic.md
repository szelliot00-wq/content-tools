# Datamimic – don't let your coding agent invent its own test world

Source: https://github.com/rapiddweller/datamimic

## Summary
DATAMIMIC is an open-source Python library (Community Edition) and enterprise platform for generating deterministic synthetic test data and pseudonymizing PII-sensitive datasets. The core value proposition is that it produces reproducible, seed-controlled output — unlike tools such as Faker — making it suitable for regulated industries (banking, healthcare) where audit trails and stable CI/CD test fixtures matter. The repo also includes an AI agent interface via CLI and optional MCP adapter, designed to prevent coding agents from inventing arbitrary test data when building data models.

## Key takeaways
- **Deterministic by design**: using a fixed seed produces byte-identical output across every run and machine, which stabilizes regression tests and supports audit re-execution.
- **CE vs Enterprise (EE)**: the free Community Edition handles single-system synthetic generation and manual PII pseudonymization; EE adds automated PII scanning, multi-system execution (Oracle, MongoDB, Kafka), governance/RBAC dashboards, a Rust performance fastpath, and compliance evidence packs (GDPR, HIPAA, PCI DSS, DORA).
- **AI agent integration**: the CLI and optional MCP adapter provide a structured authoring workflow (`datamimic scaffold`, `lint`, `dry-run`) so coding agents query live schema contracts rather than guessing DSL syntax, with `verified=true` as the explicit stopping condition.
- **Domain-aware data**: built-in domain models (healthcare, finance, insurance, demographics, e-commerce) generate contextually consistent data (e.g. age-appropriate medical conditions) rather than random field values.
- **Two pseudonymization modes**: seeded (deterministic, GDPR Art. 4(5) pseudonymization) for stable regression testing, and non-seeded (non-deterministic, stronger privacy posture) for one-time data deliveries.
- **Broad system support in CE**: PostgreSQL, MySQL, Oracle, MS SQL, SQLite, MongoDB, CSV, JSON, XML, XLSX, DbUnit, and fixed-width files are all supported out of the box.
- **Time-series generation**: any pipeline can be turned into a time-series loop with ISO 8601 `start`/`end`/`interval` attributes, covering IoT, financial ticks, log streams, and more.