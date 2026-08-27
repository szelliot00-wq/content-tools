# Pnpm 12.0

Source: https://pnpm.io/blog/releases/12.0

## Summary
pnpm 12.0, released August 26, 2026, is a full rewrite of pnpm in Rust while maintaining backward compatibility with pnpm 11's commands, flags, settings, and lockfile format. The release introduces several breaking changes around git dependencies, workspace settings validation, and lockfile determinism, alongside new features like project-aware global bins, cross-package-manager provisioning, and a remote side-effects cache proof of concept. It is currently available via the `next-12` npm tag while `latest` still points to pnpm 11.

## Key takeaways
- **Rust rewrite, not a migration**: All pnpm 11 commands, flags, and lockfile formats carry over; behavioral differences are documented separately.
- **Git dependencies normalized**: GitHub/GitLab/Bitbucket specifiers now always resolve via HTTPS regardless of how they're written; SSH URLs are no longer recorded in lockfiles for those hosts.
- **Strict workspace config validation**: Unrecognized keys in `pnpm-workspace.yaml` now error (when a pnpm version pin is satisfied) or warn, with typo suggestions.
- **Deterministic lockfiles for cyclic graphs**: Cyclic dependency resolution is now canonical — repeated installs produce byte-identical lockfiles; peer resolution is 2–3× faster with ~25% less memory usage.
- **Linux hardlink-first**: `packageImportMethod: auto` now tries hardlinks before reflinks on Linux for faster `node_modules` materialization from a warm store.
- **Project-aware global bins**: Globally installed `node`, `deno`, and `bun` automatically use the version the current project pins, with trust prompts for non-stable releases.
- **pnpm can install other package managers**: npm, Yarn, Bun, etc. can be provisioned via pnpm, verified against registry signatures. `pnx` runs them for a single command.
- **Registry revisions**: Registries can serve patched replacement artifacts for published versions without changing version numbers; pnpm records these in the lockfile.
- **`pnpm init` pins latest pnpm**: Scaffolded projects now pin the latest released pnpm rather than the version that ran the command.
- **Global commands block `sudo`**: Commands that modify global state now fail under `sudo` with a clear error, preventing accidental writes to root's home directory.
- **Remote side-effects cache (PoC)**: Build outputs for dependencies can be shared across machines via signed, org-scoped artifacts through `pnpr`, falling back to local builds on failure.
- **Static-analysis entries removed from compatibility DB**: Phantom type-only dependencies (e.g., TypeScript injected under `@typescript-eslint`) are no longer added, fixing ESLint breakage with TypeScript 7.