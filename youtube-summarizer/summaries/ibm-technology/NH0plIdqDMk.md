# What is Agentic Security Runtime? Securing AI Agents

Video ID: `NH0plIdqDMk`

## Summary
This video addresses the challenge of securing AI agents that require external connections, highlighting that engineers building these agents often lack identity expertise. It proposes "agentic runtime security," which involves using dynamic, session- and intent-bound credentials for AI agents to access resources like databases or LLMs, thereby stripping standing privilege. The solution integrates user identity via Identity Providers (IDPs) using OAuth 2.0, with a strong recommendation for OAuth 2.0 CIBA for sensitive operations to prompt users for explicit, out-of-band authorization and protect against threats like jailbreaking.

## Key insights
- AI agents should replace hardcoded, static credentials with dynamic, just-in-time, session-bound, and intent-bound credentials for accessing external resources (databases, LLMs, SaaS), effectively stripping standing privilege.
- User identity is critical, and AI agents should integrate with Identity Providers (IDPs) using standards like OAuth 2.0 (Authorization Code Flow) to understand user context and authorize actions.
- For sensitive operations, OAuth 2.0 CIBA (Client-Initiated Backchannel Authentication) provides an additional layer of security by prompting the user's mobile device for out-of-band approval, acting as a "passkey for agents."
- The security logic, including evaluating user tokens, creating dynamic credentials, and integrating authentication flows, must be implemented directly within the AI agent's code for robust runtime security and protection against threats like jailbreaking and prompt injection.