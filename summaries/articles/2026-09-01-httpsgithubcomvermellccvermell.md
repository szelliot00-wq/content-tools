# Vermell – Minimal, dependency-free C++ web framework using epoll

Source: https://github.com/vermellcc/vermell

## Summary
Vermell is a minimal, zero-dependency C++ web framework targeting Linux environments, built around a non-blocking epoll event loop with a worker thread pool for handling HTTP requests. It requires only a single header include and static library link, compiles with one `g++ -std=c++20` command, and supports x86_64, ARM, WSL, Raspberry Pi, and Android via Termux. The framework ships with built-in hardening (timeouts, connection limits, a file render jail), an in-tree JSON DOM, static file serving, HTML templating, and environment variable management — all without pulling in any external dependencies.

## Key takeaways
- **Truly zero dependencies** — relies only on base Linux APIs (sockets, epoll, pthreads, fork/exec); no runtime, no garbage collector, no vendored libraries.
- **Single-command build** — `g++ -std=c++20 server.cpp -o exe -lvermell` is all it takes; CMake, Docker, npx scaffold, and APT packages are also available.
- **Linux-only by design** — epoll is the core I/O mechanism, so macOS and Windows are not supported targets; ARM, WSL, and Termux are.
- **Event-driven architecture** — a non-blocking epoll loop reads requests and hands work to a configurable worker thread pool, keeping slow clients from blocking workers.
- **Hardened by default** — request/read/write timeouts, max request size, connection caps, and a file render jail are all on out of the box with sane defaults.
- **Full HTTP verb support** — GET, POST, PUT, DELETE (`deleteX`), PATCH, HEAD, OPTIONS, LINK, UNLINK, PURGE; static routes dispatch in O(1) via a hash map.
- **Templating built in** — `compose()` assembles pages from HTML modules; `render()` fills `[[placeholder]]` variables; both are sandboxed with a configurable root jail.
- **Runtime configurability** — most server knobs (threads, timeouts, queue size) can be changed on a running server without restart; network-side settings (port, backlog) require a restart.