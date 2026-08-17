# 5 Ways to Connect AI Agents to Tools: From APIs to MCP

Video ID: `BHGTA6ZEls4`

## Summary
This video counts down five patterns for connecting AI agents to tools, from simple direct API connections to sophisticated vault-based credential management. Each pattern builds on the previous by addressing specific security gaps, progressing from no user visibility to full authentication, delegation, and short-lived credential handling. The presenter frames these patterns in the context of enterprise agentic systems and practical tools like GitHub, Jira, Slack, and Claude.

## Key insights
- **Pattern 5 (Direct connection):** The simplest approach — agent connects to tool using its own credentials (API keys, service IDs). Easy to implement but the tool has no visibility into who the user is, so it's only safe for public or company-wide data.
- **Pattern 4 (Direct + OAuth):** Adds an identity provider and OAuth flows (e.g., GitHub, Jira, Slack native OAuth) so the tool can authenticate the user. The downside is agent impersonation (the tool sees the user, not the agent) and long-lived tokens that can persist 90+ days, creating a security risk.
- **Pattern 3 (MCP layer):** Inserts Model Context Protocol between the agent and tool, creating an abstraction layer so agents only need to know MCP rather than each tool's specific API. Reduces per-agent complexity and improves interoperability across tools.
- **Pattern 2 (Token exchange + on-behalf-of delegation):** Eliminates pure OAuth impersonation by also authenticating the agent itself. The agent operates explicitly on behalf of the user via token delegation, giving the system full visibility into both identities and what each is authorized to do.
- **Pattern 1 (Vault + short-lived credentials):** The most secure pattern. Long-lived tokens are stored in a locked vault, which issues only short-lived credentials to MCP for each request. If a token is intercepted, it expires quickly and cannot be replayed — the preferred model for production agentic systems.
- **Overarching theme:** Each pattern incrementally closes a specific security gap — lack of user visibility → impersonation → long-lived tokens → agent anonymity — making this a useful maturity model for evaluating your own agent architecture.