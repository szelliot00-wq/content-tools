# Rust-lang/rust is adopting an LLM policy

Source: https://blog.rust-lang.org/inside-rust/2026/08/05/rust-langrust-is-adopting-an-llm-policy/

## Summary
Five Rust project teams have adopted a formal policy governing the use of LLMs in contributions to rust-lang/rust. The policy was created in response to a pattern of problematic LLM use — including unannounced AI-generated code and copy-pasted review responses — that degraded review quality and eroded trust between contributors. The policy sets disclosure requirements, holds LLM-assisted PRs to a *higher* standard than human-authored ones, and gives reviewers the right to opt out of reviewing LLM-generated content.

## Key takeaways
- **Disclosure is mandatory:** All LLM-generated content in public docs, PR descriptions, or GitHub comments must be clearly marked; unmarked LLM content is a policy violation.
- **Reviewers can opt out:** No reviewer is required to engage with LLM-generated PRs if they choose not to.
- **Higher bar, not lower:** LLM-assisted PRs must include tests unconditionally and face additional restrictions; they cannot be used for soundness-critical changes unless the author is already a domain expert.
- **LLM reviews don't count:** AI-generated reviews cannot substitute for human review or self-review, and policies must be written for humans first.
- **Copy-pasting LLM responses to review comments is explicitly called out** as a waste of reviewers' time and a breach of trust.
- **The policy is a starting point:** The teams intend to use data gathered under the policy — whether contributors are learning, making repeat contributions, etc. — to refine it over time.