---
title: "Day 2: Permissions, Users, and Processes"
description: "UID/GID, octal chmod, umask, special permission bits, process lifecycle, zombie vs orphan, and Linux signals"
sidebar_position: 2
tags: [linux, permissions, processes, signals]
---

# Day 2: Permissions, Users, and Processes

> Source - Linux Fundamentals · 2026-11-23

## Problem

- Insecure file permissions expose sensitive credentials or prevent services from accessing required sockets.
- Unhandled process states (zombies, orphaned processes) leak system resources and degrade stability.

## How It Works

- Identity and Permissions:
  - Every file has User (u), Group (g), and Others (o) permissions with Read (4), Write (2), and Execute (1) bits.
  - `umask`: Default permission mask subtracted from 666 (files) or 777 (directories). E.g., `022` results in `644` files.
  - Special bits: SUID (4xxx, runs with file owner UID), SGID (2xxx, inherits group), Sticky bit (1xxx, only file owner can delete, e.g. `/tmp`).
- Process Lifecycle:
  - Created via `fork()` (duplicate parent) followed by `exec()` (load new binary).
  - Orphan process: parent terminates before child; child is adopted by PID 1 (`systemd` / `init`).
  - Zombie process: child terminates, but parent has not read its exit status via `wait()`. Process table entry remains.
- Essential Signals:
  - `SIGTERM` (15): Graceful termination request; process can catch, flush buffers, and clean up.
  - `SIGKILL` (9): Immediate termination handled directly by kernel; cannot be caught or ignored.

## Traps

- Killing a zombie with `kill -9 <PID>` does not work because the zombie is already dead; you must signal the parent process or restart it.
- Granting SUID bit carelessly creates privilege escalation vulnerabilities if the executable can be manipulated.

## Questions

- Q: Why cannot a zombie process be killed with `kill -9`? A: A zombie is already terminated; it only occupies a PID in the process table until its parent reads its exit status with `wait()`.
- Q: When should you use `SIGTERM` (15) instead of `SIGKILL` (9)? A: Always try `SIGTERM` first to allow graceful shutdown and buffer flushing; use `SIGKILL` only when a process hangs unresponsively.
- Q: What does a sticky bit on `/tmp` prevent? A: It prevents users from deleting or renaming files owned by other users, even though everyone has write access to the directory.
