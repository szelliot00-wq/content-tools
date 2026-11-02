# F/OSS Comics #13: BSD Unix, Part 3 – The Beginning of BSD Unix

Source: https://fosscomics.com/posts/13.%20BSD%20Unix%20Part%203%20-%20The%20Beginning%20of%20BSD%20Unix/

## Summary
This is episode 13 of a webcomic series chronicling the history of BSD Unix. It covers the period from 1977 to 1979, tracing how Bill Joy and Chuck Haley began the Berkeley Software Distribution after Ken Thompson returned to Bell Labs, through the release of 3BSD and DARPA's growing interest in Unix. The comic format walks through the first two BSD releases, Joy's hands-on distribution work, and the addition of virtual memory support for the VAX that culminated in 3BSD.

## Key takeaways
- In early 1977, Bill Joy created the first BSD by bundling a Pascal system with the `ex` line editor — it was not a standalone OS, just a software collection requiring an existing Unix installation.
- Early BSD required an AT&T Unix source license; Berkeley charged only for the tape and shipping, a philosophy influenced by Berkeley's culture of academic openness and 1960s counterculture values.
- The second release (2BSD) added `vi`, the C shell, and other tools; Joy personally handled all distribution requests, copied tapes, and mailed them himself.
- When a VAX arrived at Berkeley in 1978, graduate student Ozalp Babaoglu and Joy worked together to add virtual memory support (which the stock 32/V Unix lacked), enabling programs to use more address space than physical RAM.
- These efforts produced 3BSD in December 1979, which bundled ported 2BSD tools with the virtual-memory kernel — catching DARPA's attention due to its successful distribution across research institutions.