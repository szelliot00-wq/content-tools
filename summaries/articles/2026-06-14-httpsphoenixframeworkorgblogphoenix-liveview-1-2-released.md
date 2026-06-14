# Phoenix LiveView 1.2 Released

Source: https://phoenixframework.org/blog/phoenix-liveview-1-2-released

## Summary
Phoenix LiveView 1.2, released June 10th, 2026 by Steffen Deusch, introduces colocated CSS as its headline feature, extending the colocated hooks/JS pattern from 1.1. It leverages the modern CSS `@scope` rule to allow component-scoped styles that don't leak to other elements on the page, achieved by annotating rendered HTML with special attributes at compile time. Scoping is opt-in rather than on by default, since `@scope` browser support is still maturing as of this release.

## Key takeaways
- **Colocated CSS** lets you write `<style :type={MyApp.ColocatedCSS}>` directly inside HEEx templates; styles are extracted at compile time and fed into your normal CSS pipeline (Tailwind/Esbuild).
- **CSS scoping via `@scope`** is supported through HTML annotation (`phx-r` on root elements, unique `phx-css-foo`-style attributes per component), enabling styles that target only the owning component's DOM subtree.
- **Scoping is opt-in**, not default — browser support for `@scope` is still limited. A behaviour/callback is provided for custom scoping strategies instead.
- **HEEx compilation was refactored** — the team split compilation into separate tokenization and parsing steps to support colocated CSS/JS cleanly and reduce code duplication (detailed in a separate deep-dive post).
- **`root_tag_attribute` config** must be set explicitly (`config :phoenix_live_view, root_tag_attribute: "phx-r"`) to enable the scoping annotation.
- **Other 1.2 improvements** include a `TagFormatter` for the HTML formatter, per-module formatter configuration, test warnings, and improved JavaScript client documentation.
- **Upgrading from 1.1** is straightforward: update the version pin to `~> 1.2.0` in `mix.exs` and re-fetch dependencies.