---
title: "image storage"
description: "Docker tags vs digests, real disk usage of shared layers, what docker rmi deletes, image best practices"
sidebar_position: 3
tags: [docker, containers]
---

# image storage

## Tags vs Digests

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

## Disk Usage Measurement

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

## Related

- [images](./02-images.md) - layers and OverlayFS that this page measures
