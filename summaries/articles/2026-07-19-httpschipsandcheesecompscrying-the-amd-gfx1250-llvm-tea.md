# Scrying the AMD GFX1250 LLVM Tea Leaves

Source: https://chipsandcheese.com/p/scrying-the-amd-gfx1250-llvm-tea

## Summary
This Chips and Cheese article by Aurora Nockert analyzes LLVM commits to reverse-engineer architectural details of AMD's upcoming GFX1250 accelerator (MI455X), ahead of AMD's formal MI400 series announcement. The piece compares GFX1250 against RDNA4 consumer GPUs, previous CDNA accelerators, and Nvidia's Blackwell, identifying what's been inherited, what's new, and what's been stripped out. The GFX1250 appears to be a compute-only chip that blends RDNA4's programming model with CDNA4's raw performance capabilities.

## Key takeaways
- **Two new accelerators in LLVM:** GFX1250 (MI455X) targets ML/AI workloads and powers the Helios rack; GFX1251 (MI430X) targets HPC with 200+ TFLOPs of double-precision compute.
- **Wave32-only execution:** GFX1250 drops Wave64 support entirely (unlike RDNA) and supports 20 waves per SIMD (4 more than RDNA4), which will require re-evaluating many existing GPU kernels.
- **Massively expanded register file:** Each wave can now address up to 1024 VGPRs, up from 512 on CDNA (256 VGPR + 256 accumulation) and 256 on RDNA — a significant boost for tensor workloads.
- **Unified WGP cache:** LDS and vector L0 cache are merged into a single 448KB "WGP Cache" structure, matching what Nvidia and Intel have done for years. Addressable LDS per wavefront doubles to 320KB vs. CDNA4.
- **Best-of-both tensor support:** GFX1250 uses WMMA (from RDNA4) but with CDNA4-style K dimensions, and supports all datatypes from both predecessors — including OCP MX-style floating-point scaling — except fp64, which is reserved for GFX1251.
- **Cluster support (AMD's answer to Hopper Thread Block Clusters):** Includes cluster-level barriers, distributed shared memory access across workgroups, and hardware barrier arrival/monitoring intrinsics that go beyond Nvidia's equivalent.
- **New data movement features:** Tensor Memory Accelerator (similar to Nvidia's TMA), explicit vector memory prefetching, and cooperative 128B atomic loads/stores aimed at accelerating collective communications (RCCL).
- **Hardware tanh + transcendental improvements:** Native tanh support (common in neural network activation functions) added, with fp32 transcendental latency reduced from 9 to 8 cycles.
- **Pure compute chip:** Nearly all graphics instructions removed (no export, no parameter interpolation, etc.), going further than even prior CDNA generations.
- **Dynamic VGPR allocation absent:** Despite being touted in RDNA4 and potentially more useful under ML register pressure, the feature is a no-op on GFX1250.