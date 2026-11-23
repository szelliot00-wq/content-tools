# Yes, 17M lines of Lean is a lot

Source: https://micjm.com/blog/yes-17m-lines-of-lean-is-a-lot/

## Summary
The article investigates whether 17 million lines of Lean code — the reported size of a recent Riemann hypothesis proof — is actually as large as it sounds. The author compares it against two datasets: 259 famous theorems from Mathlib (all human-generated, maxing out around 1.2M lines) and 938 packages on the Lean package index Reservoir. The conclusion is yes, 17M lines is genuinely enormous, though a small handful of AI-assisted proofs do exceed it.

## Key takeaways
- Human-generated Lean proofs of famous theorems typically fall between 100K and 1.2M lines — far below the 17M claimed for the Riemann proof.
- All of Mathlib, the main Lean math library, is only ~2.4M lines, making 17M roughly 7x larger.
- Only three packages on Reservoir exceed 17M lines: an in-progress AI proof at 88M, a database-linking project at 36M (mostly auto-generated), and Anthropic's AI-assisted Fermat's Last Theorem proof at 27M.
- The 17M line figure is at the very top of what currently exists in the Lean ecosystem, and is unprecedented for a proof of a single theorem.
- AI-assisted proofs are driving a new scale of Lean code that dwarfs anything produced by humans alone.