---
title: "Day 5: Production-Ready Bash Scripting"
description: "Defensive Bash patterns, set -euo pipefail, trap signal handlers, parameter expansion, and automated backup scripting"
sidebar_position: 5
tags: [linux, bash, scripting, automation, devops]
---

# Day 5: Production-Ready Bash Scripting

> Source - Linux Fundamentals · 2026-11-23

## Problem

- Unchecked Bash scripts continue executing after errors, compounding failures or corrupting state.
- Aborted processes leave orphan lockfiles and uncleaned temporary directories behind.

## How It Works

- Defensive Script Header:
  - `set -e`: Exit immediately if any command exits with a non-zero status.
  - `set -u`: Treat references to unset variables as errors and exit.
  - `set -o pipefail`: Capture failures in upstream pipeline commands rather than returning only the rightmost exit code.
- Signal Trapping and Idempotent Cleanup:
  - `trap cleanup_fn EXIT INT TERM`: Hooks cleanup logic to run on normal exit or interrupt (`SIGINT`, `SIGTERM`).
  - Ensures temporary directories created via `mktemp -d` are pruned reliably.
- Scoping and Parameter Expansion:
  - Enforce function variable encapsulation with `local`.
  - Robust expansions: `${VAR:-default}` (fallback), `${VAR:?error_msg}` (fail if missing).
  - Preserving arguments: `"$@"` maintains individual token bounds; `"$*"` flattens tokens into a single string.
- Verification: Validate scripts with `shellcheck` before production deployment.

## Traps

- Running `rm -rf "$TARGET_DIR/*"` when `$TARGET_DIR` is accidentally empty or unset can evaluate to `rm -rf /*`.
- `set -e` is ignored inside command tests like `if cmd; then` and arithmetic expressions evaluating to zero.

## Questions

- Q: What does `set -euo pipefail` guard against? A: It stops on command errors (`-e`), blocks uninitialized variables (`-u`), and preserves pipeline failure exit codes (`-o pipefail`).
- Q: Why should cleanup routines be bound to the `EXIT` pseudo-signal? A: The `EXIT` hook triggers on both clean script completion and unhandled errors, preventing stale scratch directories.
- Q: What is the difference between `"$@"` and `"$*"`? A: `"$@"` preserves each positional argument as an isolated token, while `"$*"` merges all arguments into one string.
