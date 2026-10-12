# Will Linux phones become a viable alternative to the Android/iOS duopoly?

Source: https://amosbbatto.wordpress.com/2026/10/05/linux-phones-alternative/

## Summary
Written by Amos Batto in October 2026, this article examines why Linux phones stagnated after the 2020 excitement around the Librem 5 and PinePhone, and argues that conditions are now improving for a viable niche Linux phone market. The main obstacles — weak SoC hardware, short Android kernel lifespans, immature mobile interfaces, and poor corporate strategy (especially PINE64's) — are each being addressed by new developments. The author believes Linux phones won't threaten Android/iOS dominance but could mirror the small-but-real Linux PC market.

## Key takeaways
- **The RK3588S is the best current option for a "pure Linux" phone**, offering enough CPU/GPU power to handle cameras and video in software, with mainline Linux support maturing — though it runs hot and lags behind modern mobile SoCs in performance and efficiency.
- **Qualcomm's IoT "Dragonwing" SoCs** (especially the QCM6490, supported until 2036) offer a simpler design path with integrated modems, but require more proprietary blobs than Rockchip options.
- **Android kernel longevity is improving**: Google and Samsung now promise 7–8 years of OS/security updates on flagship chips, which is critical since Linux phones take years to develop and need long sales windows to recoup costs.
- **Existing Linux phones on Android kernels face a security crisis**: Devices like the FuriLabs FLX1 and Jolla C2 are stuck on unsupported Linux 5.4 kernels with thousands of unfixed CVEs, raising serious security concerns.
- **Phosh succeeded by piggybacking on GNOME's desktop stack**, achieving 98.7% of its codebase now maintained by external organizations (GNOME, Phosh.mobi, FreeDesktop.org), making it more sustainable than siloed predecessors like Firefox OS or Ubuntu Touch.
- **PINE64's failure was strategic**: It prioritized distro packaging deals over paying developers for kernel/driver work, then alienated key volunteers by favoring Manjaro — leaving the PinePhone Pro, PineNote, and PineTab2 effectively abandoned.
- **Three viable Linux phone paths now exist**: (1) Pure Linux kernel with RK3588S; (2) Linux on Qualcomm IoT SoC with an Android kernel; (3) Linux on a mainstream MediaTek/Qualcomm Android SoC via libhybris — each with different tradeoffs around software freedom, performance, and longevity.
- **The real barrier is corporate**: No major phone manufacturer has committed to investing in a Linux phone, and the tiny companies currently doing so lack the resources to overcome hardware and software challenges simultaneously.