# Show HN: Posthorn, self-hosted mail without the mail server

Source: https://github.com/craigmccaskill/posthorn

## Summary
Posthorn is a self-hosted outbound email gateway that sits between your apps and a transactional mail provider (Postmark, Resend, Mailgun, AWS SES, or SMTP relay). Rather than having each self-hosted app manage its own mail provider credentials and integration, Posthorn provides a single Go binary with a TOML config that accepts mail via three ingress types (HTTP form, HTTP API, SMTP) and forwards it through your chosen provider. It's designed for homelab/self-hosted operators who want centralized outbound mail handling without running a full mail server.

## Key takeaways
- **Three ingress modes:** HTTP form (with honeypot, rate limiting, CSRF), HTTP API (Bearer token auth, idempotency keys), and SMTP listener (for apps like Ghost, Gitea, Mastodon that speak native SMTP).
- **Five transport backends:** Postmark, Resend, Mailgun, AWS SES, and outbound SMTP relay — switching providers is a single TOML edit.
- **Solves a real self-hosting pain point:** cloud providers (DigitalOcean, Lightsail, Linode, Vultr) block outbound SMTP, making SMTP-only apps broken without a workaround.
- **Minimal footprint:** single Go binary, distroless Docker image, only three external dependencies (TOML parser, UUID library, LRU cache).
- **Not a mail server:** no mailbox storage, no IMAP, no DKIM key management — it only handles outbound relay.
- **v1.0 just released** (yesterday), with v2 roadmap including SQLite submission log, retry queue, suppression lists, webhooks, and HTML body support.
- **Production requirements:** needs DNS records (SPF/DKIM/DMARC), a reverse proxy for TLS termination, and proper rate limiting configured before handling real traffic.