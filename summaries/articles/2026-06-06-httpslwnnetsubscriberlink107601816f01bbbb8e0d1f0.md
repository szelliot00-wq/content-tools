# Moving beyond fork() + exec()

Source: https://lwn.net/SubscriberLink/1076018/16f01bbbb8e0d1f0/

## Summary
A developer (Li Chen) proposed "spawn templates" to the Linux kernel to optimize the common fork()+exec() pattern, particularly for applications that repeatedly launch the same executable. The proposal was rejected in its current form, but sparked a broader discussion about replacing fork()/exec() with a proper native `posix_spawn()` implementation. Kernel maintainer Christian Brauner suggested building a new API around the existing `pidfd` abstraction — creating an empty process via `pidfd_open()` and configuring it with a new `pidfd_config()` syscall — which Chen agreed was the better direction.

## Key takeaways
- fork()+exec() is wasteful because fork copies all process memory that exec then immediately discards; this problem is worse in large or multithreaded processes
- Chen's spawn templates patch (which caches executable metadata to speed up repeated launches) showed only ~2% improvement and was rejected, with reviewers noting it didn't address the fork() cost itself
- The preferred future direction is a "pristine process" model: create an empty process and configure it step-by-step, rather than copying and discarding an existing one
- Brauner proposed a `pidfd_open()` + `pidfd_config()` API (analogous to `fsconfig()`) as the right kernel primitive, with the goal of enabling a native `posix_spawn()` in userspace
- Some commenters argue the problem is overstated and userspace patterns (persistent subprocesses, zygote forking, moving code into libraries) already solve it adequately
- The community has been going in circles on this for years — proposals gain traction then stall; some advocate proving the concept in userspace first before adding kernel complexity