# Ransomware Detection: Why Storage Finds the Attack First

Video ID: `7jUcTG1eeTM`

## Summary
This video explains why storage systems are uniquely positioned to detect ransomware attacks early, before widespread damage occurs. It covers foundational backup strategies, specific technical signals that indicate an active ransomware attack, and how to integrate storage alerts into broader security tooling for coordinated response and recovery.

## Key insights
- **Ransomware is pervasive**: 44% of data breaches involve ransomware, 73% of organizations have experienced at least one attack, and attacks occur roughly 15 times per day across industries.
- **Storage is the most reliable witness**: Because all data ultimately lives on storage, anomalies from encryption become visible at the storage layer faster than at the application layer — making it the last line of defense.
- **Good backups are non-negotiable**: Effective backups must satisfy four properties — Recent, Redundant, Recoverable, and Immutable (read-only). Immutability is critical so ransomware can't corrupt the backups themselves.
- **Entropy and compressibility are early warning signals**: Encrypted data is highly random (high Shannon entropy) and compresses poorly. A sudden drop in compression ratios (e.g., 100TB → 98TB instead of 20TB) is a strong indicator of encryption activity.
- **Other detectable signals include**: Mass overwrite bursts (sudden IO spikes), mass file renames, and collapsed deduplication ratios — especially when multiple signals appear together against a known baseline.
- **Machine learning improves detection accuracy**: Combining multiple anomaly signals against a behavioral baseline reduces false positives and can catch partial encryption attacks where only portions of files are altered to evade simpler detection.
- **Response must be pre-planned and automated**: When an attack is confirmed, the response needs to be fast, coordinated, and automated as much as possible — including isolating affected systems and identifying a clean recovery point just before the point of infection.
- **Integrate storage into SIEM and SOAR**: Feeding storage alerts into a Security Information and Event Management system contextualizes them, while a Security Orchestration, Automation and Response tool can automate mitigation steps like lockdown, isolation, and data restoration.