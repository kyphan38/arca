---
title: "Day 3: Bash Mechanics and IO"
description: "Shell command parsing, single vs double quotes, exit codes, subshell vs current shell, standard streams, and redirection"
sidebar_position: 3
tags: [linux, bash, io-redirection, streams]
---

# Day 3: Bash Mechanics and IO

> Source - Linux Fundamentals · 2026-11-23

## Problem

- Unintended word splitting or glob expansion corrupts command arguments and causes critical script failures.
- Inability to route errors separately from normal output leads to silent failures and unhelpful logs.

## How It Works

- Shell Parsing and Quoting:
  - Single quotes (`'...'`): Preserve the literal value of every character; no expansions occur.
  - Double quotes (`"..."`): Preserve literal values except `$`, `` ` ``, `\`, and `!`; protects against word splitting while allowing parameter expansion.
  - Exit code (`$?`): `0` represents success; non-zero (`1`-`255`) represents failure.
- Subshell vs Current Shell:
  - `( cmd )`: Executes in a child subshell; environment changes disappear on exit.
  - `{ cmd; }`: Executes in the current shell context; variables persist.
- Standard Streams and Redirection:
  - File descriptors: `0` = stdin, `1` = stdout, `2` = stderr.
  - Output redirection: `>` (overwrite), `>>` (append), `2>` (stderr only).
  - Combined output: `&>` or `> file 2>&1`.
  - Pipe (`|`): Connects stdout of the left command to stdin of the right command.
  - `tee`: Splices a stream, writing to both files and stdout simultaneously.

## Traps

- Redirection sequence matters: `> file 2>&1` redirects both streams to `file`, but `2>&1 > file` leaves stderr pointing to original terminal stdout.
- Variables modified inside a piped loop vanish in standard Bash because pipelines execute in subshells.

## Questions

- Q: What is the difference between single and double quotes in Bash? A: Single quotes suppress all expansions literally; double quotes allow variable expansion while preventing word splitting and globbing.
- Q: Why does `var="old"; echo "new" | read var; echo $var` not update `$var`? A: Pipelines run commands in subshells, so environment changes inside the pipeline do not propagate back to the parent shell.
- Q: What does `cmd > /dev/null 2>&1` accomplish? A: It silences all program output by routing stdout to `/dev/null` and then pointing stderr to stdout.
