# I Could've Rickrolled the FIFA World Cup. All I Needed Was My ID

Source: https://bobdahacker.com/blog/fifa-hack

## Summary
A security researcher discovered that registering as a football agent on FIFA's public portal granted access to the same Microsoft Entra (Azure AD) tenant used by all FIFA internal platforms. The backend APIs for FIFA's Football Data Platform performed no server-side authorization checks, meaning any registered agent account — regardless of assigned roles — could access and control live World Cup 2026 streaming infrastructure, match statistics, and broadcast systems. The researcher could have hijacked live camera feeds to push arbitrary video to TV networks worldwide, or manipulated real-time match data shown to commentators and broadcasters. Despite frantic outreach to FIFA, MediaKind, HBS, CISA, and the FBI across a single night, FIFA fixed the vulnerability the next day without ever acknowledging the report.

## Key takeaways
- **Client-side authorization is not authorization.** FIFA's Angular app displayed an "access denied" page based on a JWT flag, but backend APIs accepted requests from any authenticated user regardless of roles.
- **Single-tenant design amplified the blast radius.** Putting public agent registrations in the same Entra tenant as internal systems turned a low-barrier signup into a skeleton key for the entire FIFA platform.
- **The exposure was severe and real.** Live RTMP stream keys, camera feed controls, match score editing, commentator talking points, and internal spreadsheets were all accessible to a zero-privilege account.
- **FIFA had no responsible disclosure channel.** No bug bounty program, no `security.txt`, and no reachable security contact — forcing the researcher to cold-call MediaKind, CISA, and the FBI at 3am to get the issue escalated.
- **Third-party infrastructure partners (MediaKind) were the only ones who responded promptly**, underscoring the importance of vendors having clear, staffed security contacts.
- **Even after the fix, FIFA left the researcher on internal distribution lists**, continuing to send official match documents — suggesting the remediation was incomplete or poorly scoped.