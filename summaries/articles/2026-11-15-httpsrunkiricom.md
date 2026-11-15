# Kiri – The Modern Container Runtime

Source: https://runkiri.com/

## Summary
Kiri is a modern container runtime (currently in beta) for Mac, Windows, and Linux that claims to be 8× faster than Docker Desktop by routing container creation through a single daemon that calls the kernel directly, bypassing the multi-hop architecture used by Docker Desktop, OrbStack, and Colima. It maintains full compatibility with existing Docker tooling — the `docker` CLI, Compose, and the Docker Engine API all work unchanged. Beyond containers, Kiri includes Kubernetes support, Linux VMs, image builds with scanning, and a "Share" feature that exposes any running container publicly over HTTPS. It is written in Rust and ships as a native app (AppKit on Mac, Win32 on Windows) rather than an Electron wrapper.

## Key takeaways
- **Dramatically faster startup**: `docker run` takes 22 ms on Kiri vs. 178 ms on Docker Desktop and 279 ms on OrbStack, measured on 2 CPUs / 8 GB.
- **Lower resource usage**: With 10 containers running, Kiri uses 0.4% CPU and 420 MB RAM, compared to 6.0% CPU and 2.5 GB for Docker Desktop.
- **Simpler architecture**: One daemon handles everything via `clone3` directly — no containerd, no shim, no per-container resident process — reducing a 5-hop chain to 3 hops.
- **Full Docker compatibility**: Existing `docker`, `docker compose`, `docker buildx`, Dockerfiles, Docker Hub, and OCI images all work without changes.
- **Kiri Share**: One-click public HTTPS tunneling to any running container via `runkiri.cloud`, useful for demos, webhooks, and mobile testing.
- **Cross-platform native app**: Uses Apple Virtualization.framework on Mac, WSL2 on Windows, and no VM at all on Linux.
- **Free and in beta**: Available now on Mac, Windows, and Linux; UI is localized into 15 languages.