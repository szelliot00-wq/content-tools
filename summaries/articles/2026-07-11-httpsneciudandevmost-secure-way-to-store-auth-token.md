# What's the best way to do authentication in modern applications

Source: https://neciudan.dev/most-secure-way-to-store-auth-token

## Summary
This article by Neciu Dan walks through the evolution of authentication patterns in modern web applications, explaining why the common tutorial approach of storing JWTs in localStorage is insecure and progressively building toward more secure alternatives. It covers XSS and CSRF attacks, compares JWTs vs. server-side sessions, explains the OAuth refresh token pattern, and culminates in recommending the Backend for Frontend (BFF) architecture. It also highlights the emerging threat of infostealer malware and the new Device Bound Session Credentials (DBSC) standard as a hardware-level defense.

## Key takeaways
- **Don't store tokens in localStorage.** Any JavaScript on the page — including third-party scripts and XSS payloads — can read it and exfiltrate your token, creating a long-lived skeleton key for attackers.
- **In-memory storage is slightly better but still insufficient.** Variables survive XSS but are wiped on page refresh, forcing a refresh token somewhere persistent — which circles back to the same storage problem.
- **HttpOnly cookies are the right storage primitive.** The `HttpOnly` flag makes a cookie invisible to JavaScript entirely; pair it with `Secure`, `SameSite=Lax`, and the `__Host-` prefix for maximum protection.
- **Cookies introduce CSRF risk — defend in layers.** Use CSRF tokens (double-submit pattern), `SameSite` cookies, and server-side `Sec-Fetch-Site` header checks together; no single defense is sufficient alone.
- **Server-side sessions beat stateless JWTs for single-app backends.** JWTs can't be revoked without rebuilding a server-side store anyway, so a simple opaque session ID in a database is simpler, faster to invalidate, and always reflects the user's current state.
- **JWTs do have a legitimate use case:** service-to-service auth in microservices and as a one-time identity assertion in SSO flows (read once, then start a real session).
- **The OAuth split pattern is the best browser-token tradeoff:** short-lived access token in memory + refresh token in an `httpOnly` cookie scoped to `/api/refresh`, with refresh token rotation and reuse detection to auto-detect theft.
- **The BFF (Backend for Frontend) pattern is the gold standard.** A thin server proxy holds all OAuth tokens server-side; the browser only ever sees a session cookie. This is strongly recommended for sensitive or business applications.
- **Infostealer malware bypasses all of the above.** Native malware reads the browser's cookie database directly from disk — `HttpOnly` only blocks JavaScript. This is a rapidly growing threat (51.7M infostealer log packages in 2025, up 72% YoY).
- **Device Bound Session Credentials (DBSC) is the emerging hardware defense.** Shipped in Chrome 146 on Windows (April 2026), DBSC ties session cookies to a TPM chip so stolen cookies expire within minutes and can't be refreshed without the original hardware.