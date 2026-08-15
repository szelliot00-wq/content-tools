# "That's not SoC 2 compliant"

Source: https://ampcode.com/notes/thats-not-soc-2-compliant

## Summary
Amp, a small software company, pushes directly to main without pull requests and recently had to defend this practice when pursuing SOC 2 certification. Their auditors confirmed that SOC 2 doesn't mandate pull requests — it requires that changes be authorized, tested, approved, and recorded. Amp designed a deliberate set of controls (access restrictions, verified commit signatures, a full CI/CD validation pipeline, and linked audit trails) that satisfies those requirements without code review or PRs.

## Key takeaways
- SOC 2 does not require pull requests; it requires that you identify and manage your risks through whatever controls fit your process.
- The Trust Services Criteria never mention `git` or PRs — they ask that changes are authorized, tested, approved, and recorded.
- Amp's PR-free controls include: documented access policies, GitHub-enforced commit signature verification, a mandatory CI/CD validation pipeline, and commit-to-Amp-thread audit trails.
- Code review by a second human is not a SOC 2 requirement.
- This approach works for Amp because they are small (20 people, mostly engineers) and high-trust; they acknowledge it doesn't automatically apply to a 2,000-person org.
- The scalable insight is risk calibration: even at large companies, not all code carries equal risk, yet it's often subjected to the same heavyweight process designed for the most critical systems.
- Teams can start small: pick one system, ask what risks your PRs are actually managing, and explore whether those risks could be managed another way.