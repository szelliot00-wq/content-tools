# How Uv Works Under the Hood

Source: https://noos.blog/posts/uv-how-it-works-under-the-hood/

## Summary
This article provides a technical deep-dive into `uv`, the high-performance Python package manager built in Rust. It explains how `uv` achieves its speed through a combination of massive parallelism for network and CPU tasks, an aggressive global caching system, and a modern dependency resolution algorithm. A key innovation highlighted is the "zero-I/O" installation strategy, which creates virtual environments by linking to cached files instead of copying them, making environment creation nearly instantaneous.

## Key takeaways
- **Performance from Rust and Parallelism:** `uv` is written in Rust for performance and safety, and it heavily parallelizes operations like downloading packages and building wheels, which are often sequential in older tools like `pip`.
- **Aggressive Global Caching:** It maintains a global cache for package distributions, builds, and git checkouts, which drastically speeds up subsequent installations across different projects by avoiding redundant work.
- **"Zero-I/O" Installs:** When possible, `uv` installs packages by creating links (reflinks, hardlinks, or symlinks) from the global cache to the virtual environment, eliminating the time-consuming process of copying files.
- **Modern Dependency Resolution:** `uv` uses a fast, backtracking dependency resolver inspired by PubGrub, which efficiently finds a valid set of packages and provides clear error messages when conflicts arise.