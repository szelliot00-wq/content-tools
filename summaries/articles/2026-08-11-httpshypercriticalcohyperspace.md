# Hyperspace

Source: https://hypercritical.co/hyperspace/

## Summary
Hyperspace is a Mac App Store app that reclaims disk space by finding files with identical contents and converting duplicates into APFS space-saving clones — without deleting any files. The app works in three steps: Scan (find duplicates), Review (inspect and selectively include/exclude groups), and Reclaim (replace target files with clones of the source). Because it relies on APFS cloning, all files remain fully independent after reclamation, meaning changes to one clone do not affect others.

## Key takeaways
- **No files are deleted:** Duplicate files are converted into space-saving clones that share one copy of data on disk, but all file entries remain visible and independent.
- **APFS-only:** The cloning feature requires Apple's APFS file system, and clones can only be created within the same volume.
- **Rigorous duplicate detection:** Files are compared by size and three hash algorithms (MD5, SHA-1, SHA-256) applied to both file data and resource forks — every bit must match.
- **Free to scan, paid to reclaim:** Scanning is unlimited and free; unlocking reclamation requires a one-time purchase (1 month, 1 year, or lifetime) or a subscription.
- **Safety-first design:** Hyperspace skips locked, busy, or unowned files; excludes system/library folders by default; and stops reclamation immediately if a file gets "stranded" in an inconsistent state.
- **Configurable scope:** Settings control minimum file size, allowed file types, package scanning, cloud storage access, and Library folder access to broaden or narrow what gets scanned.
- **Best run with other apps closed:** Hyperspace cannot coordinate with other processes, so running it while other apps are idle reduces the risk of file-write conflicts.
- **Shortcuts support:** Basic functions (add sources, scan, review, reclaim) are automatable via macOS Shortcuts.