# SBCL: A Sanely-Bootstrappable Common Lisp (2008) [pdf]

Source: https://research.gold.ac.uk/id/eprint/2336/1/sbcl.pdf

## Summary
The article "SBCL: A Sanely-Bootstrappable Common Lisp" details the robust and transparent bootstrapping process of the Steel Bank Common Lisp (SBCL) compiler. It explains how SBCL constructs itself almost entirely from its own Lisp source code, thereby minimizing reliance on foreign languages or pre-compiled binaries for its core compiler logic. This "sane bootstrapping" involves a multi-stage compilation where the newly built compiler ultimately re-compiles itself to ensure identical output, emphasizing reproducibility and self-validation. This methodology contributes significantly to SBCL's reliability and auditable nature.

## Key takeaways
-   SBCL utilizes a "sane bootstrapping" process, meaning its compiler is predominantly written in Common Lisp and can build itself from source code, minimizing the use of C code for core compiler components.
-   The bootstrapping process is multi-staged, starting with a minimal Lisp system (often an older SBCL or CMUCL) to compile initial core components, and progressively building more complex parts of the compiler.
-   A critical step involves self-compilation, where the newly built compiler then compiles its own source code again; byte-for-byte identical output from this second compilation verifies its correctness, purity, and stability.
-   This approach ensures high reproducibility and auditability, aligning with principles of trustable software by making the entire system verifiable from source.
-   SBCL's method minimizes the "chicken-and-egg" problem by demonstrating that a fully functional and complex Lisp compiler can be built in a self-hosting, Lisp-centric manner.