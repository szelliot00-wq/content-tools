# Vite 8.0 Is Out

Source: https://vite.dev/blog/announcing-vite8

## Summary
Vite 8.0 has been released, bringing significant performance improvements and a strategic shift towards modern JavaScript module standards. The update delivers faster dev server startup and build times, largely attributed to an upgrade to Rollup 5. Key changes include an ESM-first configuration approach for `vite.config.js` files and the automatic externalization of most dependencies during SSR builds, both representing important steps forward in the build tool's evolution.

## Key takeaways
- **Significant Performance Boost**: Faster dev server startup and build times, primarily due to the upgrade to Rollup 5 and other internal optimizations.
- **ESM-first Configuration**: Vite configuration files (`vite.config.js`) are now treated as ES modules by default, requiring adjustments for CommonJS syntax (a breaking change).
- **SSR Externalization by Default**: `ssr.external` now defaults to `true`, automatically externalizing most dependencies during SSR builds for smaller bundles and faster builds (a breaking change).
- **Upgrade to Rollup 5**: This major internal upgrade underpins many performance gains and brings its own set of improvements and potential breaking changes.
- **Improved Dev Server and Build Features**: Includes refined Hot Module Replacement (HMR), better error overlays, and enhancements to asset handling and dependency optimization.
- **API Adjustments**: Several API changes, including updates to `ConfigEnv` and `ResolvedConfig`, and the removal of `resolve.alias` from Vite's top-level config (now handled via Rollup options).
- **Migration Required**: Users should consult the official migration guide due to several breaking changes and new defaults.