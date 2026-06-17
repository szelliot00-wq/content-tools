# Kagenti’s Approach to Multi-Agent Security for AI Agents

Video ID: `4vfvvzzwcwI`

## Summary
The video explains the "confused deputy" security vulnerability in multi-agent AI systems, where a legitimate agent is tricked into using its authority on behalf of an unauthorized request — enabling invisible data breaches and credential leakage. It introduces Kagenti, an open-source platform that solves this by adding a security infrastructure layer around existing agents regardless of framework. The core fix is replacing static token-passing with cryptographic workload identities and a full delegation chain that travels with every request, enabling authorization decisions based on the entire call chain rather than just the immediate caller.

## Key insights
- **Confused deputy attacks are uniquely hard in agentic systems** because agents have dynamic, unpredictable execution paths — unlike traditional services where you can statically define and enforce call graphs in your network topology.
- **Tokens passed through agent context chains are a primary attack surface** — a subagent that was never meant to access sensitive data (e.g., patient records) can silently inherit a parent agent's broad access token.
- **SPIFFE gives each agent a short-lived cryptographic workload identity** (an X.509 SVID certificate) tied to a specific workload, namespace, and service account — not a static API key that can be copied or leaked.
- **AuthBridge's delegation chain header is the key fix** — every request carries a cryptographically signed chain recording the full call path (e.g., "Agent D, called by Agent A, on behalf of User X"), so authorization policies can evaluate every actor in the chain, not just the immediate caller.
- **This makes traditional RBAC insufficient for multi-agent systems** — RBAC requires knowing the call path ahead of time, while chain-based authorization works precisely because identity and delegation context travel with the request dynamically.
- **Kagenti's MCP gateway centralizes tool-side enforcement** — routing, rate limiting, and token validation for all tool calls happen in one place, and swapping a tool requires only a single URL change.
- **Istio in ambient mode provides encrypted, mutually authenticated networking** between all agents and tools with zero per-pod configuration overhead.
- **OpenTelemetry + Phoenix + MLflow provide end-to-end observability** — a single trace ID follows the entire request path, so when something goes wrong you can audit exactly what happened and who authorized it.
- **The entire stack is open-source (Apache licensed)** — Kagenti wires together SPIFFE, KeyCloak, Istio, and observability tooling rather than introducing proprietary components.