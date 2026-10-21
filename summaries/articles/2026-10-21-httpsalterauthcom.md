# Launch HN: Alter (YC S25) – Access control for multi-user agents

Source: https://alterauth.com/

## Summary
Alter (YC S25) is a privileged access management (PAM) platform built specifically for AI agents. It sits in the request path between agents and external APIs, handling credential storage, policy enforcement, identity management, and audit logging. Rather than sharing over-scoped API keys across agents, Alter gives each agent its own scoped identity and injects credentials per request without exposing them to agent code.

## Key takeaways
- **Credential vault**: Stores API keys and tokens once, injecting them into outbound requests so credentials never appear in prompts, .env files, or agent code.
- **Per-agent identity**: Each agent gets its own identity and least-privilege scopes, replacing the common "one shared admin key for all agents" pattern.
- **Policy engine**: Requests are evaluated against rules on every call, with a default-deny posture — if a policy can't be evaluated, the request is blocked.
- **Human-in-the-loop approvals**: Sensitive or risky calls can be gated on named human approval before proceeding.
- **Tamper-evident audit trail**: Every action is logged with agent identity, the user being acted on behalf of, policy outcome, and approver — exportable to a SIEM.
- **140 integrations**: Covers major SaaS providers (GitHub, Slack, Salesforce, Stripe, etc.) with first-class LangChain, MCP, and AWS support.
- **Enterprise-ready**: SOC 2 in progress, with a public trust center showing live control status and a recent independent penetration test.