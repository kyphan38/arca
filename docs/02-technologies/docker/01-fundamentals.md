---
title: "fundamentals"
description: "Docker daemon and runtime, container isolation with namespaces and cgroups, and Alpine images"
sidebar_position: 1
tags: [docker, containers]
---

# fundamentals

## Core Architecture & Containers

### Docker Daemon & Runtime

```mermaid
flowchart TD
  CLI["docker CLI (client)"] -->|REST over Unix socket| D["dockerd (daemon)"]
  D --> CT["containerd"]
  CT --> R["runc"]
  R --> K["Linux kernel: namespaces + cgroups + OverlayFS"]
```

- dockerd: Long-running background process
- containerd: Lower-level runtime
- runc: Executes syscalls

### Container Isolation

```mermaid
flowchart TD
  C["Container<br/>a normal Linux process"]
  subgraph NS["Namespaces - what the process can SEE"]
    pid["pid<br/>Process IDs"]
    mnt["mnt<br/>Mount points"]
    net["net<br/>Network stack"]
    uts["uts<br/>Hostname"]
    ipc["ipc<br/>Shared memory"]
    user["user<br/>UID / GID maps"]
    cg["cgroup<br/>Cgroup view"]
  end
  subgraph CG["Cgroups - what the process can USE"]
    cpu["CPU<br/>Shares, quota"]
    mem["Memory<br/>Cap, swap"]
  end
  C --> NS
  C --> CG
```

## Alpine Linux Images

### Overview & Philosophy

- Alpine image: Built on Alpine Linux instead of heavy distributions like Ubuntu or Debian
- Philosophy: Only includes files strictly necessary to run the process
- Base size: Approximately 5 MB

### Key Features

- BusyBox: Combines common UNIX utilities into a single optimized executable file
- musl libc: Replaces glibc as interface to the Linux kernel
- Characteristics: Lightweight, fast, designed for embedded systems and minimal environments

## Related

- [commands](./03-commands.md) - daily commands, container rules, restart policies
