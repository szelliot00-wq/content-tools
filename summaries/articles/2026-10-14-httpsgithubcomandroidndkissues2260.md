# AOSP Source Releases Are So Late Developers Disassemble Libraries to Report Bugs

Source: https://github.com/android/ndk/issues/2260

## Summary
A developer filed a bug against Android's NDK/bionic library reporting that `wcscspn()` and `wcspbrk()` incorrectly treat any wide character >= U+0100 (e.g., emoji, CJK, Cyrillic) as a match when the reject set contains two or more ASCII characters. The bug was discovered by disassembling `libc.so` directly because Android 17's QPR1 source (the September 2026 builds shipping on Pixels) has not been released publicly — only the older June 2026 sources are available. A Google collaborator confirmed the bug exists at tip-of-tree and acknowledged the embarrassing gap in test coverage.

## Key takeaways
- `wcscspn()` and `wcspbrk()` in Android 17 (build CP3A.260905.009) falsely stop at any character >= U+0100 when the reject set is two or more ASCII characters, breaking string scanning for any text containing emoji, CJK, or extended Latin.
- The regression was introduced between June and September 2026; the publicly available AOSP source still reflects the correct June code, so developers had to reverse-engineer the shipped `libc.so` to identify the bug.
- AOSP source releases are significantly lagging behind shipping builds — Android 17 QPR1 has been stable on Pixel devices for over a month with no corresponding source release, forcing developers to disassemble binaries to investigate issues.
- Bionic's existing `wcscspn` test suite only used ASCII inputs, so the bug was never caught; a non-ASCII test case (e.g., `wcscspn(L"aĀb\n", L"x\n")`) would have caught it.
- Real-world impact included Visual Pinball on Android breaking for any table whose VBScript source contained non-ASCII comments, with the workaround being manual replacement of `wcspbrk` calls with plain loops.