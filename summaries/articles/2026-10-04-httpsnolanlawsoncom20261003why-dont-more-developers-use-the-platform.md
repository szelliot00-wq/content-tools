# Why don't more developers "use the platform"?

Source: https://nolanlawson.com/2026/10/03/why-dont-more-developers-use-the-platform/

## Summary
Nolan Lawson explores why developers resist "using the platform" — leveraging built-in browser/system APIs instead of third-party libraries. He traces the resistance through historical browser fragmentation, ecosystem habits, documentation gaps, and the genuine joy of building things from scratch. The post ultimately argues that "not using the platform" often stems from ignorance of the underlying system, but that this ignorance is itself how many developers learn — a tension worth understanding rather than dismissing.

## Key takeaways
- **Historical inertia**: Browsers lagged behind libraries for decades (e.g., jQuery filling gaps before native APIs caught up), conditioning developers to reach for npm packages by default.
- **Familiarity bias**: Developers embedded in a framework ecosystem (e.g., React/npm) often don't think to check whether the platform already solves their problem natively.
- **Documentation disparity**: Third-party libraries often had better-marketed, more accessible docs than official platform references, making them the path of least resistance.
- **Building is how developers learn**: Many current "use the platform" advocates were once library authors themselves — the process of reinventing the wheel builds deep expertise.
- **Platform ignorance is universal**: The same pattern appears outside the web (e.g., manually compressing ClickHouse data when it auto-compresses) — developers build workarounds for problems that don't exist when they don't fully understand the underlying system.
- **The senior engineer effect**: Experience typically moves developers toward smaller, simpler contributions that leverage platform capabilities rather than fighting them.
- **AI coding is a wildcard**: AI may either accelerate platform-native solutions (optimistic) or proliferate poorly-understood custom code with new layers of complexity (pessimistic).