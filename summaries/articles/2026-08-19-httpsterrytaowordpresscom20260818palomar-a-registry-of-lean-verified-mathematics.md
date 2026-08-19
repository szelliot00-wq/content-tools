# Palomar: A registry of Lean verified mathematics

Source: https://terrytao.wordpress.com/2026/08/18/palomar-a-registry-of-lean-verified-mathematics/

## Summary
Terence Tao announces the launch of Palomar, a registry for Lean-verified mathematical proofs, incubated by the Lean FRO and ICARM. The registry addresses the growing challenge of verifying AI-generated proofs by providing a standardized, publicly accessible record of Lean formalizations that have passed both mechanical typechecking and LLM-based semantic review. It functions analogously to a preprint server, accepting snapshots of GitHub repositories that meet defined structural requirements.

## Key takeaways
- Palomar is now open for submissions of Lean-formalized mathematical results, both old and new, whether human- or AI-generated.
- Each submission must include a challenge file (short Lean statement), a solution module (proof), and a `formalization.yaml` file with informal descriptions and metadata.
- Verification has two components: (a) mechanical typechecking via the Lean tool Comparator, and (b) LLM-based semantic matching between informal and formal descriptions.
- Palomar is explicitly **not** a peer-reviewed journal — it does not evaluate novelty, interest, or full correctness beyond the two automated checks.
- Tao personally tested the process by submitting his own formalization of the proof of Sendov's conjecture.
- The registry is named after the Palomar astronomical observatory, fitting its role as a systematic observer of the mathematical proof landscape.
- Discussion and community feedback are hosted on a dedicated Zulip channel.