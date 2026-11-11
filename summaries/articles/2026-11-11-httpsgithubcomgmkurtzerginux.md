# Greg Kurtzer's Ginux is now a userspace kernel

Source: https://github.com/gmkurtzer/ginux

## Summary
Ginux, created by Greg Kurtzer, has pivoted from an experimental standalone Rust kernel that booted via UEFI to a **userspace kernel** — a trusted host process that sits above the Linux kernel and intercepts syscalls for managed Linux instances. Rather than competing with Linux, Ginux now defines an explicit, versioned, and deliberately restricted contract between workloads and the host kernel. It is also being explored as a containment boundary for AI agents, limiting what system calls and resources an agent's process tree can access.

## Key takeaways
- **Direction change**: The original bootable Rust kernel proved an AI-assisted agent could build a working kernel, but the project pivoted because reimplementing Linux mechanisms doesn't reproduce the Linux ecosystem (ABI stability, community, hardware support).
- **Core design**: Ginux runs as an ordinary Linux process and intercepts managed syscalls with three outcomes — emulate, validate-and-translate, or deny — giving each instance a narrower, versioned kernel contract instead of the full Linux ABI.
- **Intentional ABI breakage**: Unlike Linux (which must never break userspace), Ginux *deliberately* breaks the full Linux ABI guarantee selectively, exposing only what an approved workload requires.
- **AI agent containment**: A key research direction is using Ginux as a sandbox for AI agents, restricting their syscalls, filesystem access, networking, and process authority to only what the task requires, with full audit logging.
- **Development method**: The project uses Human-Directed Agentic Engineering (HDAE) — humans own the architecture and acceptance gates, while AI agents handle implementation and test loops.
- **Not production-ready**: Ginux is explicitly research software — no independent security certification, incomplete Linux compatibility, and limited to tested gates.