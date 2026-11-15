# Disk encryption on NetBSD – achieving secrecy

Source: https://netbsd.org/~nia/disk-encrypt/

## Summary
This article walks through setting up partial disk encryption on NetBSD, targeting a practical middle ground between full disk encryption and no encryption. Rather than encrypting everything (which complicates booting), the approach installs NetBSD to a small unencrypted root partition and places sensitive user data on a separate encrypted partition using NetBSD's `cgd` (cryptographic disk driver). The guide covers threat modeling, identifying which directories contain sensitive data, and step-by-step configuration for both disklabel-based and GPT/wedge-based systems.

## Key takeaways
- Full disk encryption is impractical without specialized hardware because the OS needs unencrypted files to boot and prompt for a password.
- The recommended approach uses a small (~4 GB) unencrypted root partition for boot files, with a separate `cgd`-encrypted partition for sensitive user data.
- Not all directories need encryption — `/etc/passwd` stores only password hashes, and many system binaries are identical across all NetBSD installs, making them low-value targets.
- NetBSD's `cgd` driver supports modern key derivation (argon2id) and can use the Adiantum cipher as a software-friendly alternative to AES on CPUs without hardware AES acceleration.
- A disklabel written inside the encrypted partition serves as a password verification mechanism without exposing plaintext data.
- Sensitive directories most worth encrypting include `/home`, `/var`, `/tmp`, and `/usr/pkg` — areas that change during normal system operation and may contain private data.
- The `cgdroot` approach (fully encrypted root via ramdisk pivot) exists but significantly complicates the boot process and rescue options.