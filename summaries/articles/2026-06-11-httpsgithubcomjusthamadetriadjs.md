# Validation, Docs, tests, and database schemas from one source of truth

Source: https://github.com/justhamade/triadjs

## Summary
TriadJS is a TypeScript-first API framework built around a single source of truth: one schema definition that automatically generates runtime validation, OpenAPI/AsyncAPI documentation, BDD tests, boundary/fuzz tests, database schemas (via Drizzle), and typed frontend client hooks. The core idea is that API specification, implementation, validation, and tests should never drift apart because they are all derived from the same typed definitions. It is pre-1.0 but feature-complete across 21 packages with adapters for Fastify, Express, Hono, and AWS Lambda.

## Key takeaways
- **One definition, many artifacts**: Write a schema once with the `t.model()` DSL and get validation, OpenAPI 3.1, AsyncAPI 3.0, Gherkin feature files, DB migrations, and typed frontend hooks — no manual syncing.
- **Auto-generated boundary tests**: `scenario.auto()` reads your schema constraints (e.g. `minLength`, `max`, `enum`) and generates missing-field, boundary-value, type-confusion, and fuzz tests automatically.
- **Broad adapter support**: HTTP adapters for Fastify, Express, Hono (edge runtimes including Cloudflare Workers/Deno/Bun), and AWS Lambda; WebSocket support via Fastify.
- **Frontend codegen built-in**: Generates typed TanStack Query, Solid Query, Vue Query, Svelte Query hooks, form validators, and WebSocket clients from the same router definition.
- **AI-friendly by design**: All context (schemas, handlers, tests, docs) lives in one place, making it easier for LLMs and new engineers to reason about an API without cross-referencing multiple files.
- **Claude Code integration**: Ships a marketplace plugin with 10 skills and 8 slash commands (`/triadjs:new`, `/triadjs:endpoint`, `/triadjs:test`, etc.) for AI-assisted scaffolding and iteration.
- **Replaces a multi-library stack**: Consolidates Zod, zod-to-openapi, Cucumber, Schemathesis, hand-written fetch/WS wrappers, and separate Drizzle schema definitions into a single framework.