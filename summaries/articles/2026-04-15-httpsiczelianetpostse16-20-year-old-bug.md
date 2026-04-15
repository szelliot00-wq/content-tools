# Fixing a 20-year-old bug in Enlightenment E16

Source: https://iczelia.net/posts/e16-20-year-old-bug/

## Summary
The article details the discovery and fix of a 20-year-old bug in Enlightenment E16, a window manager from the late 90s that is still actively used and maintained by a small community. The bug caused occasional window "stuckness" or unresponsiveness, which was particularly noticeable when using `fvwm-menu` or other shell commands as menu items. After extensive investigation involving `strace`, `gdb`, and `rr`, the issue was traced to a subtle race condition related to `SIGCHLD` handling and blocking in the `_e_shell_command_do` function, where the signal was being incorrectly blocked or unblocked.

## Key takeaways
- A critical bug causing intermittent window unresponsiveness in Enlightenment E16 persisted for approximately 20 years.
- The bug was a race condition related to `SIGCHLD` signal handling during the execution of child processes (like menu commands), where the signal handler could be incorrectly blocked or unblocked.
- The fix involved adjusting the `sigprocmask` calls in the `_e_shell_command_do` function to ensure `SIGCHLD` was properly blocked before forking and unblocked only after the child process was fully handled.
- The debugging process was complex, requiring advanced tools like `strace`, `gdb`, and `rr` to trace system calls, memory, and execution flow.
- E16, a retro window manager from the late 90s, continues to be maintained and used by a dedicated community, highlighting the longevity and appeal of certain open-source projects.
- The bug fix was relatively small (a few lines of code) but difficult to pinpoint due to its intermittent nature and deep-seated interaction with signal handling.