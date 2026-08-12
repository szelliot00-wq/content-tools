# CVE-2026-53361 AF_Unix GC vs. MSG_PEEK use-after-free container escape

Source: https://github.com/sgkdev/bad_garbage

## Summary

CVE-2026-53361 is an unprivileged, container-escapable use-after-free vulnerability in the Linux kernel's AF_UNIX socket garbage collector. The bug arises from a race condition between the GC's collection of in-flight sockets and a concurrent `MSG_PEEK` operation: the peek takes a reference the GC never counts, allowing the collector to free a socket that is still live and leave a dangling `sk_buff`. The linked GitHub repository (`sgkdev/bad_garbage`) contains a proof-of-concept exploit targeting the single MSG_PEEK vector, affecting several major Linux distributions on kernel 6.12 and later.

## Key takeaways

- **Root cause:** The `gc_in_progress` flag can read `false` mid-collection, so a `MSG_PEEK` slips through the guard, creating a use-after-free on an in-flight AF_UNIX socket.
- **Impact:** Exploitable without privileges and capable of container escape.
- **Patch history:** The same GC vs. MSG_PEEK interaction has been fixed three separate times in the kernel's history, indicating the race is subtle and easy to reintroduce.
- **Affected targets:** Stable kernel 6.12 (patched at 6.12.95), Ubuntu 24.04 HWE (6.17, unpatched as of disclosure), RHEL 10 (unpatched), and Debian trixie (patched via DSA-6381-1).
- **Exploit scope:** The PoC targets systems with 2–7 CPUs and uses the MSG_PEEK vector only; a separate non-PEEK vector exists for Ubuntu 24.04 GA (6.8) but is not included here.
- **Mitigation:** Upgrade to kernel 6.12.95+ on stable, or apply the relevant distro security advisory (e.g., DSA-6381-1 for Debian trixie).