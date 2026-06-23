# The new HTTP QUERY method explained

Source: https://kreya.app/blog/new-http-query-method-explained/

## Summary
RFC 10008 introduces a new HTTP QUERY method to address a longstanding gap: the need to perform complex search/filter operations with a request body. GET requests are semantically correct for queries but don't support bodies reliably, and using POST as a workaround breaks idempotency and caching semantics. QUERY is designed to be safe and idempotent like GET, but accepts a request body like POST, making it purpose-built for complex search queries.

## Key takeaways
- GET with query parameters breaks down for complex queries due to URL length limits, encoding issues, and readability problems.
- Using GET with a request body is technically not forbidden but behaves inconsistently across browsers, proxies, and firewalls — making it unreliable in practice.
- POST is the common workaround but is semantically wrong: it's non-idempotent, not safe, and prevents middleware from automatically caching or retrying requests.
- The new QUERY method (RFC 10008) is essentially GET with a request body — safe, idempotent, and cacheable (with the request body included in the cache key).
- Adoption requires caution: not all clients, proxies, and servers support QUERY yet, so switching existing endpoints immediately may cause compatibility issues.