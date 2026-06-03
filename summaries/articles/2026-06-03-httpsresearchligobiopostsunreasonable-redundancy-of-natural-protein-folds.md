# The Unreasonable Redundancy of Nature's Protein Folds

Source: https://research.ligo.bio/posts/unreasonable-redundancy-of-natural-protein-folds/

## Summary
This article from Ligo Bio explores a fundamental challenge in scaling protein structure data for training generative enzyme design models: natural protein sequences are vastly more numerous than the distinct folds they encode. The team discovered that despite millions of sequences in databases like MGnify, the structural diversity collapses to roughly 25,000 meaningful fold clusters — far fewer than the 2.3 million suggested by naive Foldseek clustering. They developed a spectral graph-based pipeline to cleanly fragment multi-domain predicted structures, audit clustering artifacts, and sample training data more effectively.

## Key takeaways
- **Sequence diversity ≠ fold diversity.** Proteins with only ~24–28% sequence identity can share the same fold (TM-score > 0.75), meaning scaling sequence databases does not proportionally increase structural novelty.
- **The true structural diversity of MGnify is ~25,000 clusters, not millions.** After proper fragmentation, quality filtering, and two-pass clustering, 1.96M fragments collapse into ~25K structural neighborhoods, with 71.5% of fragments concentrated in just the top 1,000 clusters.
- **Naive Foldseek clustering overestimates novelty.** Foldseek "singletons" are not reliably unique — a spot-check found 37% of 1,000 singletons actually shared folds with each other at TM ≥ 0.8.
- **Predicted structures require surgical cleaning.** Global filters (pLDDT, radius of gyration) are too crude; a spectral bisection approach using the Fiedler vector of residue-contact graphs better separates true domains from disordered linkers.
- **Sampling strategy matters for training.** A balancing exponent γ (around 0.5) between uniform-fragment and uniform-cluster sampling best balances fold diversity against natural abundance when training generative models.
- **Implications for enzyme design:** Simply adding more natural sequences may mostly add redundant scaffold examples. The key question becomes whether models trained on nature's redundant fold distribution can generalize to unexplored backbone space — something only wet-lab validation will answer.