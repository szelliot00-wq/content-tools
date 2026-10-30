# What Is Quantization? How AI Models Get Smaller & Faster

Video ID: `mmns33BsBcY`

## Summary
This video explains quantization as a technique for compressing AI model weights to lower numerical precision, reducing memory footprint and inference cost with minimal accuracy loss. It walks through the mechanics of how floating-point values are scaled and rounded to fit smaller bit formats (FP8, INT8, INT4), using a 70B parameter model as a concrete example. It also covers the two main approaches — post-training quantization (PTQ) and quantization-aware training (QAT) — and the tradeoffs between them.

## Key insights
- **Models are massive by default**: A 70B parameter model stored in FP16 requires ~140 GB — more than most single GPUs can hold — making compression essential for practical deployment.
- **Quantization works by range-mapping**: Each layer's full value range is scaled down to fit a smaller set of representable values, then rounded to the nearest one. Precision of that mapping determines how much accuracy is preserved.
- **Standard target formats**: FP16 (2 bytes) → FP8/INT8 (1 byte) → INT4 (0.5 bytes). The 70B model shrinks from 140 GB → 70 GB → 35 GB respectively.
- **Accuracy loss is real but bounded**: INT8 is largely lossless in practice. INT4 carries more risk, but with careful rounding, accuracy typically stays above 90% of the original — losses are usually in the tenths-of-a-percent range.
- **PTQ vs. QAT**: Post-training quantization (PTQ) is faster and more common; quantization-aware training (QAT) simulates low precision during training, costing more compute but tolerating aggressive quantization levels like INT4 better.
- **Naming conventions encode precision**: Model names often embed parameter count and bit-width (e.g., "8B-FP8"), and mixed formats exist where weights are INT8 but activations remain FP16.
- **Ubiquitous in production**: Quantization is used across the stack — from on-device phone models to large inference clusters — making it one of the most practically important model optimization techniques.