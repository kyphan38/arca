---
title: "Day 6: Linux Networking Fundamentals"
description: "TCP/IP stack on Linux, routing tables, DNS resolution flow, socket inspection, and modern CLI tools"
sidebar_position: 6
tags: [linux, networking, tcp-ip, dns, routing]
---

# Day 6: Linux Networking Fundamentals

> Source - Linux Fundamentals · 2026-11-23

## Problem

- Inability to troubleshoot network dropouts, unreachable subnets, or DNS failures across remote Linux hosts.
- Relying on deprecated legacy utilities (`netstat`, `ifconfig`) that report incomplete or slow network statistics.

## How It Works

- The Linux TCP/IP Stack:
  - Link layer: Address Resolution Protocol (ARP) maps IPv4 addresses to hardware MACs (`ip neigh`).
  - Network layer: Kernel routing table evaluates destination CIDR masks to select gateway interfaces (`ip route`).
  - Transport layer: TCP tracks socket connection states (`LISTEN`, `ESTABLISHED`, `TIME_WAIT`).
- Name Resolution Flow:
  1. Local overrides checked first in `/etc/hosts`.
  2. Resolver configuration parsed from `/etc/resolv.conf`.
  3. Query dispatched to upstream DNS servers over UDP/TCP port 53.
- Modern Replacement Tooling:
  - `ip addr`: Interface addressing (replaces `ifconfig`).
  - `ip route`: Routing table viewer (replaces `route`).
  - `ss -tulpn`: Socket statistics showing listening TCP/UDP ports and owning PIDs (replaces `netstat`).
  - `dig +trace`: Recursive DNS query traversal.
  - `curl -v`: End-to-end transport, TLS, and HTTP handshake diagnostic.

## Traps

- Modifying `/etc/resolv.conf` manually on distributions managed by `systemd-resolved` gets reverted upon network restart.
- Leaving sockets in `TIME_WAIT` without connection reuse can exhaust client ephemeral ports during microservice benchmarks.

## Questions

- Q: What modern command inspects which process is listening on TCP port 443? A: `ss -tulpn | grep :443` or `ss -tulpn sport = :443`.
- Q: What configuration determines the order of hostname resolution? A: The `hosts` entry inside `/etc/nsswitch.conf`, usually prioritizing `files` (`/etc/hosts`) before `dns`.
- Q: What is the purpose of the `default` route entry in `ip route`? A: It specifies the next-hop gateway router for packets destined for addresses outside directly-connected local subnets.
