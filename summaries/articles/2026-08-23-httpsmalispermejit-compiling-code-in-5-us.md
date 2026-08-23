# JIT Compiling Code in 5μs

Source: https://malisper.me/jit-compiling-code-in-5-us/

## Summary
The article demonstrates how to build a fast JIT compiler using a "copy-and-patch" technique (stencils), using a toy regular expression engine as the example. The author shows that by generating ARM64 assembly directly — rather than relying on LLVM or C code generation — compilation takes around 5μs, fast enough to JIT every SQL query in the pgrust database. AI assistance made writing the assembly practical even without prior assembly experience.

## Key takeaways
- **JIT compilation can be ~12-20x faster than interpretation** for the regex engine tested, matching handwritten specialized code.
- **Copy-and-patch (stencils) is the key technique**: pre-written assembly templates with small "holes" (character values, branch offsets, addresses) are filled in at runtime and concatenated, avoiding full compiler infrastructure.
- **5μs compile time is the threshold** that makes it viable to JIT *every* query rather than only hot paths, which is the pgrust strategy.
- **AI lowers the barrier to assembly**: the author credits AI coding assistants with handling the low-level ARM64 instruction encoding details that would otherwise require deep assembly expertise.
- **Existing databases use LLVM or C codegen** precisely because hand-writing assembly was historically too hard — this represents an opportunity for newer databases to leapfrog them.
- **Loading the code requires mmap with execute permissions**; on Apple Silicon, `pthread_jit_write_protect_np` and `sys_icache_invalidate` are needed to safely write then execute the generated instructions.