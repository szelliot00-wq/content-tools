# 3‑2‑1 Backup Rule Explained: Protect Your Data from Disaster

Video ID: `WJzsX32qMJY`

## Summary
The video explains the 3-2-1 backup rule as a foundational strategy for protecting organizational data from loss. It breaks down each component of the rule, then extends it to a 3-2-1-1-0 framework covering immutability, air-gapping, and verified recovery. The presenter also ties backup strategy to availability requirements, illustrating the real cost of downtime at various uptime percentages.

## Key insights
- **3 copies**: Keep three copies of your data — one primary (in use) and two backups — so a single backup failure doesn't leave you exposed.
- **2 media types**: Store backups on at least two different storage technologies (e.g., SSD, HDD, NAS, cloud) to avoid a single hardware failure wiping out all copies.
- **1 offsite copy**: At least one backup must be geographically separated from the others — not just across the river, but far enough that a regional disaster (hurricane, power grid failure) can't take both down.
- **1 immutable or air-gapped copy**: At least one backup should be write-once/read-many (immutable) or physically disconnected (air-gapped), so ransomware cannot encrypt or overwrite it. Immutable is generally preferable since air-gapped copies go stale immediately.
- **0 errors**: Backups are worthless if untested. A bank in the video lost all recoverable data because no one had verified the backups actually worked — periodic recovery tests are non-negotiable.
- **Encrypt all backups**: An unencrypted backup is a data breach waiting to happen if someone gets physical or network access to it.
- **Eliminate single points of failure**: Every design decision should be evaluated against whether one event (hardware failure, disaster, attack) can destroy all copies.
- **Downtime has a real cost**: 99% uptime = ~3 days of downtime per year; 99.9% = ~8 hours; 99.99% = ~52 minutes; 99.999% = ~5 minutes. The higher the availability requirement, the more investment in backup and recovery infrastructure is required.