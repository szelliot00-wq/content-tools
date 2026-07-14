# YouTrackDB is a general-use object-oriented graph database

Source: https://github.com/JetBrains/youtrackdb

## Summary
YouTrackDB is a general-purpose, object-oriented graph database developed and maintained by JetBrains, used internally in production. It combines graph traversal, object-oriented data modeling, ACID transactions, and SQL-like querying into a single database. The project is open source (Apache-2.0), actively developed with 147 contributors, and can be run embedded or as a standalone server via Docker.

## Key takeaways
- **Graph-native storage**: Link traversal runs at O(1) complexity — no runtime JOINs required.
- **Object-oriented data model**: Supports inheritance and polymorphism at the database level, not just the application layer.
- **ACID with snapshot isolation**: All transactions see a stable snapshot from their start time, eliminating dirty reads, non-repeatable reads, and phantom reads.
- **Dual query languages**: Supports Gremlin/TinkerPop out of the box, plus YQL (a SQL-based language with dot-notation graph traversal and pattern matching via MATCH).
- **Flexible schema modes**: Operates in schema-less, schema-mixed, or schema-full mode depending on your needs.
- **Easy deployment**: Runs on any platform without configuration; available as a Maven/Gradle embedded dependency or a Docker image. Requires JDK 21+.
- **Strong security**: Role-based and predicate security policies, plus optional at-rest encryption.
- **Active open-source project**: 209 stars, 147 contributors, 25,000+ commits, primarily written in Java (96%).