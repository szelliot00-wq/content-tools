# Debian Becomes Unresponsive after 6.1.0-55 Kernel Update

Source: https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1154101

## Summary
This is a Debian bug report (filed November 15, 2026) documenting a critical regression in the `linux-image-6.1.0-55-amd64` kernel package. Multiple users reported that systems become unresponsive within minutes of booting the new kernel, with a kernel NULL pointer dereference in the `ext4` filesystem driver (`ext4_mb_load_buddy_gfp`). Reverting to the previous kernel (6.1.0-54) resolves the issue. The bug affects both bare-metal servers and Xen virtual machines.

## Key takeaways
- The crash is caused by a NULL pointer dereference in the ext4 kernel module, specifically in `ext4_mb_load_buddy_gfp`, triggered during inode eviction/truncation operations.
- Systems become completely unresponsive (SSH, HTTP, IMAP, SMTP all fail) within a few minutes of booting the affected kernel.
- The bug is reproducible across multiple users and hardware configurations, including ASUS motherboards (Intel i3-10100T) and Xen VMs.
- Workaround: boot into the previous kernel (`6.1.0-54`) via the Grub advanced options menu.
- The bug is tagged `upstream`, suggesting the root cause is in the upstream Linux kernel, not Debian-specific packaging.
- A related patch discussion exists on the kernel mailing list (`lore.kernel.org`) referencing an `ext4/ntfs3 null folio` fix, hinting at the likely upstream cause.