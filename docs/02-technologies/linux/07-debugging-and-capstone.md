---
title: "Day 7: System Debugging and Capstone Lab"
description: "Process inspection, tracing system calls with strace, open file tracking with lsof, and practical production debugging"
sidebar_position: 7
tags: [linux, debugging, strace, lsof, troubleshooting]
---

# Day 7: System Debugging and Capstone Lab

> Source - Linux Fundamentals · 2026-11-23

## Problem

- Services hang silently without emitting application log entries, obscuring whether the block is disk or network I/O.
- Filesystem mount points cannot be detached because an unknown process holds hidden descriptors open.

## How It Works

- Inspecting Process Internals:
  - `lsof -p <PID>`: Enumerates all open files, sockets, pipes, and mapped memory regions for a process.
  - `lsof -i :<PORT>`: Locates the specific daemon bound to a given network port.
  - `/proc/<PID>/fd/`: Direct filesystem access to active file descriptor symlinks maintained by the kernel.
- Tracing System Calls (`strace`):
  - `strace -p <PID>`: Intercepts active system calls (`openat`, `read`, `write`, `connect`, `epoll_wait`).
  - `strace -c`: Aggregates runtime statistics, tracking call counts, latency, and error codes.
  - `strace -e trace=network,file`: Isolates syscall inspection to specified I/O domains.
- Capstone Investigation Flow:
  1. Profile host resources (`htop`, `vmstat`, `iostat`).
  2. Map listening sockets and holding processes (`ss -tulpn`).
  3. Track open descriptors and lock targets (`lsof`).
  4. Attach syscall tracer to isolate blocking calls (`strace`).

## Traps

- Attaching `strace` introduces substantial execution latency; avoid running broad traces on production databases under peak traffic.
- Deleted files held open by processes remain in `/proc/<PID>/fd/` marked as `(deleted)` and continue claiming disk blocks until closed.

## Questions

- Q: How do you locate processes blocking a filesystem from being unmounted? A: Run `lsof +f -- /mount/path` or `fuser -vm /mount/path` to find all processes holding open handles on that mount point.
- Q: What does `strace -p <PID> -e trace=connect` reveal during debugging? A: It isolates outbound network connection attempts, revealing destination endpoints, connection refused errors, and handshake timeouts.
- Q: How can data from a deleted file still held open by a daemon be salvaged? A: Copy the descriptor data directly from `/proc/<PID>/fd/<FD_NUM>` to a new destination file before stopping the daemon.
