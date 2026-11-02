# What Is torch.compile? Dynamo, PyTorch & Faster AI Models Explained

Video ID: `QUZ4KEDxhCM`

## Summary
This video explains how `torch.compile` works under the hood by walking through its three pipeline stages: Dynamo, AOT Autograd, and Inductor. It covers how PyTorch traces, prepares, and compiles model code into optimized hardware kernels, and why compilation helps some models more than others. The video also addresses common pitfalls like graph breaks, recompilation from changing input shapes, and the mistake of measuring compilation time instead of steady-state execution time.

## Key insights
- **Compilation is lazy and specialized:** PyTorch doesn't compile on the `torch.compile` call itself — it traces and compiles on the first forward pass, using that call's tensor shapes, dtypes, and devices to specialize the generated code.
- **Dynamo captures an FX graph with guards:** Dynamo records not just operations but the assumptions (guards) under which the captured code is valid. On subsequent calls, those guards are checked before reusing compiled code.
- **AOT Autograd prepares the graph for the backend:** It decomposes higher-level ops into lower-level ones and, for training, captures both forward and backward graphs so the compiler can optimize both passes.
- **Inductor generates hardware-specific code:** The default backend fuses compatible operations (e.g., bias add + activation into one kernel), generates Triton kernels for GPUs and C++ for CPUs, and calls optimized libraries (e.g., for matmul) when appropriate.
- **Graph breaks limit optimization opportunities:** When Dynamo hits code it can't capture (e.g., a Python branch on a tensor value, or `.item()`), it splits the graph, reducing fusion opportunities and adding boundary overhead. Use `fullgraph=True` to surface these as errors.
- **Recompilation has a cost:** If input shapes or other guarded assumptions change between calls, PyTorch recompiles. Dynamic shape support reduces this but doesn't eliminate it.
- **Measure steady-state, not compilation time:** The first call pays the compilation cost; performance benchmarks must separate that from subsequent calls. GPU measurements also require proper synchronization.
- **Compilation is an opportunity, not a guarantee:** Whether a speed-up materializes depends on how much of the model can be captured, how fusion-friendly the ops are, and whether the workload is compute-bound enough to benefit.