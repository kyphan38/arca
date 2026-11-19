---
title: "images"
description: "How Docker images work - manifests, layers, OverlayFS, tags vs digests, disk usage and docker rmi"
sidebar_position: 2
tags: [docker, containers]
---

# images

## Image Structure & Storage

### Image Definition & Build Process

Image definition

- Manifest: JSON document listing configuration and layers
  - Configuration: Environment variables, default `CMD`, exposed ports, default `USER`, etc.
  - Layers: Ordered list of tar archives representing filesystem changes, identified by SHA256 hashes
    - Files: Physical binaries and libraries like `/usr/bin/curl`
    - Deduplication: Unique layers stored once and shared across images

```mermaid
flowchart TD
  T["python:3.12-slim<br/>tag - mutable label"]
  subgraph IMG["Image - OCI artifact, content-addressed"]
    M["Manifest<br/>sha256:9f2a... (digest, immutable)"]
    CFG["Config blob<br/>env, cmd, entrypoint,<br/>user, workdir, ports"]
    subgraph L["Layers"]
      L3["Layer 3 - slim cleanup<br/>sha256:e5f6..."]
      L2["Layer 2 - python runtime<br/>sha256:c3d4..."]
      L1["Layer 1 - debian base<br/>sha256:a1b2..."]
    end
  end
  T --> M
  M --> CFG
  M --> L
```

Image build process

- Step 1: Start container from previous layer state
- Step 2: Execute build command inside container
- Step 3: Diff filesystem changes against starting state
- Step 4: Tar changed files and whiteouts
- Step 5: Generate SHA256 hash of the tarball
- Step 6: Discard throwaway container

Build concepts

- Whiteout: Marker file indicating deletion of a path from lower layers
- Image size: `RUN rm -rf` in a separate layer does not shrink the image
- Practice: Run cleanup in the same `RUN` instruction as the installation

```mermaid
flowchart LR
  S1["FROM alpine:3.20<br/>pull the base"] --> L1["Layer 1 - alpine base<br/>full rootfs (~5 MB)"]
  S2["RUN echo hi > /greeting<br/>writes one file"] --> L2["Layer 2 - diff tar<br/>contents: /greeting"]
  S3["RUN apk add curl<br/>installs a package"] --> L3["Layer 3 - diff tar<br/>contents: curl + libs + deps"]
```

### Layers & OverlayFS

Layer creation

- Instructions creating layers: `RUN`, `COPY`, `ADD`
- Instructions editing config blob: `ENV`, `CMD`, `ENTRYPOINT`, `LABEL`, `WORKDIR`, `USER`, `EXPOSE`

Layer storage

- Registry: Gzipped tarball blobs identified by SHA256 hashes
- Host: `/var/lib/docker/overlay2/<random-id>/diff/`
- Layer sharing: Layers are shared between images sharing the same base

Runtime combination (OverlayFS)

- OverlayFS: Combines multiple directories into a single unified view
- lowerdir: Stacked read-only image layers
- upperdir: Read-write directory created per container for writes
- workdir: Kernel scratch space
- merged: Unified directory mounted as container filesystem
- Copy-on-write: Modifying lower-layer files copies the entire file to `upperdir`
- Volumes: Database or heavy-write workloads belong on volumes, not `upperdir`

```mermaid
flowchart LR
  subgraph HOST["OverlayFS stack on the host"]
    UP["Writable layer (upperdir)<br/>born at docker run, gone at rm<br/>read-write"]
    subgraph LOW["lowerdir - read-only, shared across containers"]
      L3["Layer 3 - curl"]
      L2["Layer 2 - /greeting"]
      L1["Layer 1 - alpine base"]
    end
  end
  MV["/ (merged view)<br/>/bin /etc /lib /usr<br/>/greeting, /usr/bin/curl<br/>+ anything written at runtime"]
  HOST -->|union| MV
```

Multi-container disk usage

- Sharing: Running 50 containers from one image uses only one copy of `lowerdir`
- Isolation: Docker creates 50 unique pairs of `upperdir` and `workdir`

```mermaid
flowchart TD
  subgraph A["Container A"]
    UA["upperdir<br/>A's writes go here"]
    WA["workdir<br/>kernel scratch"]
  end
  subgraph B["Container B"]
    UB["upperdir<br/>B's writes go here"]
    WB["workdir<br/>kernel scratch"]
  end
  subgraph C["Container C"]
    UC["upperdir<br/>C's writes go here"]
    WC["workdir<br/>kernel scratch"]
  end
  subgraph LOW["lowerdir - one copy on disk, shared by every container"]
    L3["Layer 3 - curl + libraries (read-only)"]
    L2["Layer 2 - /greeting (read-only)"]
    L1["Layer 1 - alpine base (read-only)"]
  end
  A --> LOW
  B --> LOW
  C --> LOW
```

Storage cost breakdown

- lowerdir: Paid once regardless of running container count
- upperdir: Paid per container, scales with file writes
- workdir: Paid per container, minimal scratch overhead
- Writable layer lifecycle: Files written to `upperdir` are deleted during `docker rm`
- Data persistence: Databases require volumes to persist data when container is removed

### Tags vs Digests

- Tag: Mutable reference pointing to a manifest digest
- Digest: Immutable SHA256 hash of the manifest, changes only if content changes

```mermaid
flowchart TD
  subgraph MUT["Mutable - the registry retargeted node:20"]
    T1["Day 1: node:20"] -.-> D1["sha256:9f2a...<br/>CI passes"]
    T30["Day 30: node:20"] -.-> D30["sha256:8c1e...<br/>CI fails"]
  end
  subgraph IMM["Immutable - pin to the digest"]
    P["node:20@sha256:9f2a...<br/>readable label + verified hash"] --> DP["sha256:9f2a...<br/>forever this image"]
  end
```

### Disk Usage Measurement

![img](./img/02/05.webp)

- `docker image ls`: Shows virtual size by summing all layers, ignoring sharing
- `docker system df`: Shows actual disk usage, accounting for layer sharing

## Image Removal (docker rmi)

- Rule: `docker rmi` removes the manifest, layers are deleted only when unreferenced

```markdown
python rt     40 MB   → only python used it      → DELETED   (-40 MB)
pip libs      10 MB   → only python used it      → DELETED   (-10 MB)
debian base   30 MB   → node still uses it       → KEPT      ( 0 MB)
                                                  ─────────
                                       Disk freed:    50 MB
```

- Shared layers: Deleting an image only frees disk space for unshared layers

## Image Best Practices

- Pin by digest: Use immutable references like `node:20-slim@sha256:9f2a3b…`
- Disk measurement: Use `docker system df` for actual usage, not `docker image ls`
- Disk cleanup: Use `docker image prune` or `docker system prune` to free space
