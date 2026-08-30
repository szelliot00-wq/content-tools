# California lawmakers unanimously pass Linux exemption from age-verification law

Source: https://www.tomshardware.com/software/linux/california-lawmakers-unanimously-pass-linux-exemption-from-age-verification-law-software-distributed-under-the-gpl-mit-bsd-and-apache-licenses-are-exempt

## Summary
California's legislature unanimously passed Assembly Bill 1856, exempting open-source operating systems from the state's Digital Age Assurance Act (which takes effect January 1, 2027). The bill redefines "operating system provider" to exclude software distributed under permissive licenses like GPL, MIT, BSD, and Apache, effectively removing Linux distributions, BSD variants, and GrapheneOS from the age-verification requirement. The amendment also addressed several other issues in the original law, including a drafting error that technically classified every device owner as a child.

## Key takeaways
- The bill passed unanimously (39-0 in the Senate) and has been sent to Governor Gavin Newsom for signature.
- Linux distros (Debian, Fedora, Ubuntu, Arch, etc.) and BSD systems are explicitly exempt because they use GPL, MIT, BSD, or Apache licenses.
- Package manager repositories (apt, pacman) are also excluded, as they are not considered "covered application stores."
- Browser extension stores are carved out as well, since they only distribute add-ons that run inside a host application.
- Windows, macOS, iOS, and Android remain fully in scope and must collect age data at account setup starting January 1, 2027.
- SteamOS's status remains ambiguous — its Arch-based components are open source, but Valve bundles it with the proprietary Steam client.
- A new provision prohibits requesting age signals unless legally required, preventing the age API from being repurposed as a general data-collection tool.
- Platforms gain a good-faith safe harbor protecting them from liability when age-gating signals are inaccurate.