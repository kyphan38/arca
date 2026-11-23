---
title: "Day 1: Linux Filesystem and Inode"
description: "FHS structure, everything is a file principle, Inode mechanism, hard vs soft links, and debugging disk space"
sidebar_position: 1
tags: [linux, filesystem, inode, storage]
---

# Day 1: Linux Filesystem and Inode

> Source - Linux Fundamentals · 2026-11-23

## Problem

- Disk shows "No space left on device" even though `df -h` shows plenty of free gigabytes.
- Misunderstanding how files are linked leads to accidental data loss or inability to reclaim disk space after deletion.

## How It Works

- Filesystem Hierarchy Standard (FHS):
  - `/proc` and `/sys`: Virtual pseudo-filesystems exposing kernel internals and hardware states.
  - `/etc`: Host-specific system configuration files.
  - `/var`: Variable data such as logs (`/var/log`), caches, and spool files.
  - `/dev`: Device nodes representing physical or virtual hardware.
- "Everything is a file" philosophy - devices, sockets, pipes, and processes are exposed through file descriptors.
- Inode (Index Node):
  - Stores metadata: owner (UID/GID), file type, permissions, timestamps (atime, mtime, ctime), size, and block pointers.
  - Does NOT store the filename or the actual file content (filenames live in directory data blocks).
- Hard link vs Soft link:
  - Hard link: points directly to the target inode; shares the same inode number; cannot cross filesystems or link directories.
  - Soft (symbolic) link: independent file with its own inode storing the target file path string.

## Traps

- Exhausting inodes: creating millions of tiny files fills the inode table before disk capacity runs out (`df -i` vs `df -h`).
- Deleting an open file: `rm` unlinks the directory entry, but blocks are not freed until every process holding the open file descriptor closes it.

## Questions

- Q: Why does a filesystem report "No space left on device" when `df -h` shows 50GB free? A: The filesystem has run out of available inodes; check with `df -i`.
- Q: If you delete a large log file with `rm` but disk usage does not decrease, what causes this? A: A running process still holds an open file descriptor to the file; truncate the file (`> file.log`) or restart the process.
- Q: What happens to a hard link when the original file is removed? A: The data remains intact and accessible because the inode link count only decreases by one, and data persists while link count > 0.
