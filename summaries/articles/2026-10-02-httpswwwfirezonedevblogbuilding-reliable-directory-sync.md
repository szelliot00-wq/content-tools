# Building reliable (and fast) directory sync

Source: https://www.firezone.dev/blog/building-reliable-directory-sync

## Summary
This article by Jamil Bou Kheir from Firezone explains the challenges of directory sync — keeping user and group data from identity providers (Okta, Entra, Google, JumpCloud) in sync with your application. It walks through the data model for users, groups, and nested memberships, examines the SCIM standard and its real-world shortcomings, and explains why Firezone ultimately built a pull-based hybrid sync engine instead.

## Key takeaways
- **Directory sync is distinct from SSO**: It's the mechanism for importing users and groups into your app, not authenticating them.
- **Flattening nested groups** simplifies access lookups from recursive queries to single-row lookups.
- **SCIM standardizes the wire format but not behavior**: Each identity provider implements SCIM differently, leading to provider-specific shims that negate much of the standard's value.
- **SCIM is push-based**, meaning your app must be available at all times or risk missing critical updates (like employee terminations) with no way to trigger a re-sync.
- **Pull-based sync** gives your app control: poll the provider's API on a schedule, checkpoint writes per page to survive restarts, and reconcile by removing records older than the sync epoch.
- **Delta syncs are appealing but complex**: Nested group flattening, short token expiry windows (e.g., 7 days for Entra), and edge cases make incremental sync fragile.
- **Firezone's hybrid approach** combines periodic full syncs (for correctness) with real-time provider-triggered updates (for low latency on critical changes like offboarding), reducing API quota usage while minimizing lag.