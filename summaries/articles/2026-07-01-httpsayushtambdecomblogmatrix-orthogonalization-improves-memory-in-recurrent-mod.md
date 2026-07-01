# Matrix Orthogonalization Improves Memory in Recurrent Models

Source: https://ayushtambde.com/blog/matrix-orthogonalization-improves-memory-in-recurrent-models/

## Summary
This article from Paradigm (published June 30, 2026) investigates why recurrent neural networks (RNNs) struggle to match transformers on associative recall (AR) tasks, where attention gives transformers direct token-to-token access. The research evaluates approaches using the mLSTM architecture and benchmarks including MQAR and MAD's noisy AR task suite. A central finding is that matrix orthogonalization — specifically via the Muon optimizer — significantly improves associative memory in recurrent models, outperforming the standard Adam optimizer on tail-end associative memory learning.

## Key takeaways
- Transformers have a structural advantage in associative recall due to attention, which RNNs have historically struggled to replicate.
- Matrix orthogonalization is proposed as a technique to close this gap in recurrent models.
- The Muon optimizer (which applies orthogonalization to weight updates) outperforms Adam specifically on tail-end associative memory learning — the hardest part of the AR task distribution.
- The mLSTM architecture is used as the recurrent backbone for evaluation.
- Results are validated on established benchmarks including MQAR and MAD's noisy associative recall task suite.