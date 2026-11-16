# AI Model Debugging: Find the First Divergence Across AI Accelerators

Video ID: `K6ffYKrlPdU`

## Summary
This video explains a systematic methodology for debugging AI model failures that occur when migrating to a new hardware accelerator. The core challenge is that a model may compile and run successfully on new hardware but produce incorrect outputs, with no crash or error message to indicate where things went wrong. The presenter introduces a "first observed divergence" technique: running the same inputs through both a reference machine and the target accelerator, comparing intermediate outputs at checkpoints to narrow down where results first diverge.

## Key insights
- **The full software stack is the suspect, not just hardware.** When porting a model, the compiler, runtime, and accelerator backend all change — the bug could originate at any layer (lowering/fusion, scheduling, precision, tensor layout, etc.).
- **Localize before diagnosing.** Attempting to explain a bug before narrowing its location wastes effort. First find the smallest region of the model where divergence begins, then investigate why.
- **Checkpoint comparison is the core technique.** Run identical inputs on both machines, save intermediate tensors at meaningful boundaries (e.g., after embedding, attention, normalization), and compare them. The gap between the last matching checkpoint and the first failing one is your target region.
- **Floating-point differences aren't always bugs.** Different hardware may reorder operations or use different precision, producing expected numerical variation. Use appropriate tolerances (max absolute error, relative error, cosine similarity) rather than requiring bit-identical outputs.
- **First observed divergence ≠ root cause.** The failing checkpoint identifies *where to start looking*, not what's broken. The actual cause may be in the operation itself, its inputs, or how the compiler translated it.
- **Reproduce with a minimal test, then regression-test it.** Once you isolate the failing operation, build the smallest possible reproducer. Keeping it as a regression test in CI/CD means future compiler or runtime changes that reintroduce the bug get caught early.
- **Always rerun the full model after a fix** to confirm the divergence disappears and hasn't simply moved to a different checkpoint.