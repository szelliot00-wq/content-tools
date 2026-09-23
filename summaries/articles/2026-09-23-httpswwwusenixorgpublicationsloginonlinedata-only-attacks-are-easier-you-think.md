# Data-only attacks are easier than you think (2024)

Source: https://www.usenix.org/publications/loginonline/data-only-attacks-are-easier-you-think

## Summary
Researchers at VUSec (Vrije Universiteit Amsterdam) present Einstein, an automated tool that demonstrates data-only attacks — exploits that corrupt program data rather than hijacking control flow — are far more practical than previously assumed. Unlike traditional exploits that redirect code execution, data-only attacks let the victim program run its intended code but with attacker-manipulated arguments to system calls. Einstein uses dynamic taint analysis to automatically identify and confirm such exploits against popular web and database servers, generating hundreds of working attack primitives while bypassing modern defenses like DEP and CFI.

## Key takeaways
- ~70% of security bugs in major software (Microsoft, Google, Mozilla) are memory safety bugs, making data-only attack vectors widely applicable.
- Data-only attacks avoid the need to hijack control flow, letting programs run normally but with corrupted syscall arguments — making them invisible to control-flow defenses (DEP, CFI, CPI).
- Einstein automates exploit discovery using dynamic taint analysis focused on "identity data flows" — cases where attacker-controlled data flows directly into security-sensitive syscall arguments.
- Against nginx alone, Einstein confirmed 944 working exploit primitives, including code execution, arbitrary file writes, and data exfiltration channels.
- High-coverage mitigations (memory safety, Data Flow Integrity) are too expensive to deploy broadly; low-cost mitigations leave gaps Einstein can trivially exploit — there is currently no easy, complete defense.
- Even with low code coverage (27–49%) during analysis, Einstein uncovered large numbers of exploitable paths, suggesting real-world exposure is likely worse.
- The research calls on vendors to prioritize complete defenses and frames making those defenses more deployable as a critical open research problem.