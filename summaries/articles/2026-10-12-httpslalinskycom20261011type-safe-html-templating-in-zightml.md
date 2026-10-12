# Type-safe HTML templating in Zig

Source: https://lalinsky.com/2026/10/11/type-safe-html-templating-in-zig.html

## Summary
Lukáš Lalinský introduces **zt**, a type-safe HTML templating library for Zig that adapts Go's Templ approach to the Zig ecosystem. Templates are parsed and transpiled to Zig code at compile time, enabling full type checking, automatic HTML escaping, and zero-allocation rendering. The library integrates with the author's web framework Dusty and supports htmx/Datastar for building SPAs without JavaScript.

## Key takeaways
- **Compile-time transpilation**: Templates are converted to Zig code during `comptime`, so template errors surface as ordinary Zig compiler errors with source locations pointing back to the original template file.
- **Full type safety**: Template parameters are fully typed — passing the wrong type or misspelling a field name is caught at compile time, not runtime.
- **XSS protection by default**: All dynamic values are HTML-escaped automatically; raw HTML output requires an explicit opt-in, making dangerous patterns easy to spot in code review.
- **Zero allocations**: Generated template code compiles down to a sequence of writes with no heap allocations, making it suitable for low-level/high-performance use cases.
- **Composable components**: Supports reusable components, layout inheritance via `@children`, and standard Zig control flow (`if`, `for`, `while`) directly in templates.
- **One known syntax limitation**: Lines starting with `if`, `for`, or `while` are parsed as code, which means bare text starting with those words requires wrapping — the author is considering `@if`/`@for`/`@while` prefixes to resolve the ambiguity.