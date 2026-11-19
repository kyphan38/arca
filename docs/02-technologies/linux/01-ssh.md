---
title: "SSH Protocol"
description: "SSH layers and the handshake step by step - version exchange, KEXINIT, key exchange, host key check and known_hosts"
sidebar_position: 1
tags: [linux, ssh, networking]
---

# SSH Protocol 

## What it is

- Way to login in to another machine securely over an unsafe network
- Client-server architecture: SSH client connects to SSH server, port 22 by default
- Made of 3 layers
  - Transport (RFC 4253): Sets up the encryption, checks the server is real
  - User auth (RFC 4252): Proves who you are
  - Connection (RFC 4254): Shell, port forwarding, multiple channels

## The handshake

Step 1: Say hello

- TCP connects first, no SSH yet
- Both sides send a plain text line with protocol + software version
  - `SSH-2.0-OpenSSH_9.6`
- Not encrypted, anyone watching can read it
- Both lines are saved - used later in the fingerprint of the handshake

Step 2: Agree on algorithms

- Both sides send a `KEXINT` message
- Each lists what it supports, best choice first, for
  - Key exchange
  - Sever host key type
  - Encryption
  - Integrity check (MAC)
  - Compression (normally off)
- Rule: Pick the first item on the client's list that the server also has
- No overlap &rarr; connection fails
- Each direction (client &rarr; server, server &rarr; client) picks its own encryption
- Still plain text

Step 3: Make a shared secret and check the server

- Client
  - Makes a throwaway keypair, just for this one connection
  - Sends the public one
- Server
  - Makes its own throwaway keypair
  - Sends the public one back
- &rarr; In this case
  - Client: Client's private key + server's public key &rarr; secret `K`
  - Server: Server's private key + client's public key &rarr; secret `K`
- Server
  - Builds a fingerprint `H` of the whole handshake so far, covering
    - Both version lines
    - Both `KEXINIT` messages
    - Its own host key
    - Both throwaway public keys
    - The shared secret `K`
    - Signs `H` with its host key
  - Sends back: Host key + Throwaway public key + Signature

```txt
Both version lines
- Client: SSH-2.0-OpenSSH_9.6
- Server: SSH-2.0-OpenSSH_9.6p1 Ubuntu-3ubuntu13

Both KEXINIT messages: A binary bute array containing 16 random bytes and a list of negotiated algorithms
- 14 8a c2 40 ... 00 00 00 13 curve25519-sha256 ...

Host key: /etc/ssh/ssh_host_ed25519_key.pub
- ssh-ed25519
- a4 b1 9f 3c ...

Both throwaway public keys
- Client: d3 77 18 90 2a ... (32 bytes)
- Server: 8c fe 12 09 bb ... (32 bytes)

Shared secret:
- 5e a1 b2 88 cc 41 00 ... (32 bytes)

=> H = 7b 4a f2 19 c0 88 3d ee a1 02 9b ff 44 d3 82 17 09 e1 33 bb 81 fe 04 2a 99 11 cc 8a 31 0f 65 d2

Signature = Ed25519_Sign(Server_Private_Key, H) = 3a 9f 02 c8 1b ... (64 bytes)
```

- Client
  - Builds the same `H` on its side
  - Checks the signature against the server's host key
  - If it matches: Server is genuine, and nothing earlier was tampered with

```txt
Is_Valid = Ed25519_Verify(Server_Public_Key, H, Signature)
```

Trusting the host key

- No CA, no certificates like HTTPS
- First connection: shows a fingerprint, asks you to accept
- Saved in `~/.ssh/known_hosts`
- Later connections compare against it - warns loudly if it changed
- OpenSSH has its own certificate option for large setups, but that's optional
