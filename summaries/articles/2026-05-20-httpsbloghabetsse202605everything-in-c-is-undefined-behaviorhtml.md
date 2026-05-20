# Everything in C is undefined behavior

Source: https://blog.habets.se/2026/05/Everything-in-C-is-undefined-behavior.html

## Summary
A 30-year C/C++ veteran argues that virtually all nontrivial C/C++ code contains undefined behavior (UB), and that the language's design makes it practically impossible to write fully correct code even for experts. The article catalogs numerous subtle, non-obvious sources of UB beyond the well-known memory safety issues, and concludes that LLMs should now be considered a necessary tool for UB detection. The author frames writing C/C++ in 2026 without LLM supervision as professionally irresponsible.

## Key takeaways
- UB is not just a compiler optimization exploit — it means the compiler can assume certain states "cannot happen," leading to silent, unpredictable behavior regardless of optimization level.
- Common but overlooked sources of UB include: misaligned pointer access, casting a pointer to a misaligned type, passing `char` to `isxdigit()`, float-to-int casts with out-of-range values, objects at address zero, and incorrect variadic argument types (e.g. `%ld` for `uint64_t`).
- Even casting a misaligned pointer is UB before any dereference occurs.
- `memset(..., 0, ...)` does not guarantee null pointers in structs on all platforms — NULL is not required to be address zero.
- Signed integer overflow is UB; unsigned integer promotion rules are subtle enough that even experienced programmers get them wrong at code-skimming speed.
- LLMs can reliably find UB in real-world code (including OpenBSD), and the author argues their use for UB review should be considered mandatory practice in 2026.
- The industry has no scalable solution: fixing UB at scale requires expert review, but experts are scarce and this work has traditionally been delegated to juniors who lack the knowledge to catch it.