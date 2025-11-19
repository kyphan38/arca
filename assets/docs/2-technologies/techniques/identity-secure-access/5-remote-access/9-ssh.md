# ssh

- [x] Done

## What is SSH?

Concepts

- A secure way to send commands and control a computer over the internet
- It uses encryption to encode data so no one else can read it while it travels between devices
- Manage servers from a distance or to transfer files securely
- It supports tunneling (port forwarding), which lets data pass through networks that usually block it
- It replaces older tools like Telnet, which were insecure because they sent commands in plain text that anyone could intercept (like a private call put on speakerphone)

## What does SSH do?

Functions

- Creates secure connections: It connects your device to a remote computer (usually a server) over the internet
- Protects your data: It uses encryption to scramble the information you send. If anyone tries to spy on the connection, they will only see random noise (static) instead of your data
- Tunnels information: It helps move data across networks that might normally block it
- Uses port forwarding: It wraps small chunks of data (called packets) with extra address information to guide them safely from one machine to another

## How does SSH work?

### TCP

Concepts

- SSH runs on TCP/IP
- Prioritizes making sure data arrives intact rather than just sending it quickly

### Public key cryptography

Concepts

- SSH incorporates encryption and authentication via a process called public key cryptography
- It uses a two-key system to provide identity
  - Public key: Like an open padlock that anyone can use
  - Private key: Like the specific key kept secret by the owner to open that padlock

Features

- Create a session key: The public and private keys are just used to say "hello" and verify identity. Once connected, both sides agree on a temporary, identical shared key (symmetric key) to encrypt the actual conversation
- Two-way identification: Unlike visiting a website (HTTPS), where usually only the website proves it is real, SSH requires both your computer and the remote server to prove their identities to each other
- Deep access: While HTTPS just lets you view web pages, SSH gives you access to the server's brain (the command line), which is why firewalls often block it for safety

### User Authentication

Concepts

- Double check: While encryption keys check if the computers are safe, the system still checks if the human is authorized. This usually requires a username and password
- Remote control: Once logged in, you can type commands on the remote computer just as if you were sitting directly in front of it

### Port Forwarding (Tunneling)

Concepts

- The middleman concept: Just like Bob sending a message to Dave through Alice, SSH can send data to one computer to be passed along to another
- Bypassing security barriers: This is useful for reaching hidden servers
  - Example: If a secure server blocks outside internet access, you can connect to a gateway server that is allowed in. That gateway then passes your data to the secure server. To the secure server, the request looks like it is coming from inside the safe network

## Master Flow

Stage 1: TCP Connection

- Your laptop (client) talks to server port 22
- The mechanics: SNYK, SNYK-ACK, ACK
- Status: We have a raw, insecure pipe. No encryption yet

Stage 2: Negotiation

- The versions exchange (plain text):
  - Client sends: `SSH-2.0-OpenSSH_8.1`
  - Server sends: `SSH-2.0-OpenSSH_8.2`
  - Check: Do we both support 2.0? Yes
- The algorithm menu (KEXINIT packet)
  - Client sends: I support: `curve25519-sha256`, `ecdh-sha2`, `diffie-hellman-group14`, etc.
  - Server sends: I support: `curve25519-sha256`, `diffie-hellman-group14`, etc.
  - Selection: They pick the first algorithm that appears on both lists (e.g., `curve25519-sha256`)

Stage 3: Host identification

- Prerequisite: The server generated its host keys ago when it was installed
- Server sends its public host key (e.g, `ssh-ed25519 AAAAC3...`)
- Client calculates the hash and searches in `~/.ssh/known_host` on your laptop
  - If new: Client asks you: Do you trust this fingerprint?
  - If changed: Client shouts: `Warning: Remote host identification changed`
  - If match: Trust is verified. We proceed

Stage 4: The secure tunnel (Key exchange)

- They perform the Diffie-Hellman exchange
- Result: Both sides now possess the exact same session key (symmetric key)
- Status: Encryption is on. From this exact millisecond, every byte sent is scrambled using that session key. Even if a hacker is listening, they see static noise

Stage 5: User authentication

- The server asks for credentials inside the encrypted tunnel
  - If you use a password
    - Input: You type mypassword
    - Process: Server receives it. It finds your user in `/etc/shadow`
    - Hash check: Server takes the salt (a string of random data generated for each specific user when their account is created to avoid 2 different users with the same password hashing) from the file, adds it your input, runs the hash function
    - Compare: Does hash(input + salt) match the stored hash?
      - Yes &rarr; Access granted
  - If you use an SSH key
    - Prerequisite: Your user public key is already inside the server's `~/.ssh/authorized_keys`
    - Challenge: Server generates a random number
    - Sign: Your laptop uses your user private key to mathematically sign the number
    - Verify: Server uses your user public key (from the file) to verify the signature
      - Valid signature? &rarr; Access granted

### Fingerprint

The problem: Public keys are huge

- A public key is a massive block of mathematical gibberish
- If the server sent you its full public key to verify visually, it would look like this on your screen

```txt
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCB007n/ww+ouN4gSLKssMxXnBOvf9LGt4L
5R698+mOzFKe20Spxh6szZ5Y/d+t5... (imagine 500 more characters) ...7+s5
Rv6+q8B5q8B5q8B5q8B5q8B5q8B5q8B5q8B5q8B5q8B5q8B5q8B5q8B5q8B5q8B5q8B5
```

- The issue: If I asked you, "Does this match the key you wrote down last year?", it would take you 10 minutes to compare them character by character. You would make a mistake

The solution: The fingerprint

- A fingerprint is a cryptographic hash of that massive public key
- It takes the huge key and crushes it down into a short, unique string that is easy for humans to read
- Method: Fingerprint = SHA256(Public key)

Example: Key vs. fingerprint

- The actual public key

```txt
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJlX... [lots of characters] ...5r8X
```

- The fingerprint

```txt
SHA256:rZ9zU/2+aB3k9...
```

## What is SSH used for?

Functions

- Remotely managing servers, infrastructure, and employee computers
- Securely transferring files (SSH is more secure than unencrypted protocols like FTP)
- Accessing services in the cloud without exposing a local machine's ports to the Internet
- Connecting remotely to services in a private network
- Bypassing firewall restrictions

## Port

Concepts

- Default port: 22
- Firewall access: Most firewalls (security barriers) intentionally leave Port 22 open so administrators can remotely manage servers
- The loophole: Because Port 22 is usually open, traffic that might normally be blocked can be tunneled through this port to reach other parts of the network

## Security Risks

Concepts

- Too much power: SSH usually grants admin or root access. If an attacker gets in (or an employee makes a mistake), they can delete files, steal data, or install malicious software
- Slipping past guards: Attackers can exploit the fact that Port 22 is left open to sneak into secure networks that are otherwise protected
- The lost key problem
  - No expiration: Unlike passwords that you change often, SSH keys do not expire automatically
  - Permanent access: If an attacker steals a key, they have access for months or years until someone notices and manually cancels it
- Management chaos: Large companies often have millions of keys. It is very difficult to track them all, making it easy for stolen or old keys to go unnoticed

## Common Failures

### Category 1: The Network Layer Failures (Stage 1)

Case 1: `ssh: connect to host 1.2.3.4 port 22: Connection refused`

- The context: Your packet knocked on the door, and someone inside yelled "go away"
- The root cause
  - Service down: The machine is on, but the SSH Server software (`sshd`) is crashed or stopped
  - Wrong port: You are knocking on Port 22, but the admin moved SSH to Port 2222 to hide it
- Remediation
  - Check if the SSH service is running (if you have console access)
  - Try a different port: `ssh -p 2222 user@host`

Case 2: `ssh: connect to host 1.2.3.4 port 22: Operation timed out`

- The context: You knocked on the door, and... silence. You waited 30 seconds, and no one answered
- The root cause
  - The void: The server is turned off or the IP is wrong
  - The wall: A firewall (Security Group) is silently dropping your packets. This is the most common issue in Cloud (AWS/GCP)
  - The VPN: You are trying to reach a private internal server without being connected to the company VPN
- Remediation
  - Check your VPN connection
  - Check the firewall rules (Allow inbound TCP port 22)
  - Ping the server (`ping 1.2.3.4`) to see if it's alive (though firewalls might block ping too)

### The Identity & Security Failures (Stage 3)

Case 1: `Warning: Unprotected private key file`

- The context: SSH refuses to run because your private key is lying on the sidewalk
- Root cause: File permissions
  - Linux/Mac forces you to keep your private key secret. If the file permissions allow anyone else on your laptop to read it (e.g., `0644` or `0777`), SSH triggers a fail-safe and stops
- Remediation: Lock the file so only you can read it
  - `chmod 600 ~/.ssh/id_rsa`

Case 2: `Warning: Remote host identification has changed`

- The context: The fingerprint mismatch
- Root cause
  - Server was reinstalled (host keys changed)
  - Man-in-the-middle attack
- Remediation
  - Verify with the admin that the server was reinstalled
  - Remove the old line: `ssh-keygen -R 1.2.3.4`

### Category 3: The authentication failures

Case 1: `Permission denied (publickey)`

- The context: You offered a key, and the server said no

Root cause:

- Missing key: The public key is not in the server's `~/.ssh/authorized_keys` file
- Wrong key: You are using `id_rsa`, but the server only knows your `id_ed25519` key
- Wrong user: You are trying to log in as `root` but the server config (`sshd_config`) has `PermitRootLogin no`

Remediation

- The test: Use Verbose mode (see below) to see which key you are offering
- The fix: You must get your public key onto that server (ask an admin, or use a password if allowed to add it)

Case 2: `Received disconnect from ...: 2: Too many authentication failures`

- The context: You have too many keys on your keyring
- Root cause
  - You have 7 different keys on your laptop (GitHub, AWS, Personal, Work)
  - SSH tries them one by one
  - The server has a limit (usually 6 tries)
  - By the time SSH tries the correct key (Key #7), the server has already kicked you out for spamming it
- Remediation
  - Tell SSH to use only the specific key for this host: `ssh -i ~/.ssh/my_specific_key -o IdentitiesOnly=yes user@host`

- Tell SSH to use only the specific key for this host: `ssh -i ~/.ssh/my_specific_key -o IdentitiesOnly=yes user@host`

- It prints the internal monologue of the SSH client. It shows you exactly where it fails
  - Connecting to
  - Remote protocol version
  - Server host key
  - Offering public key
- Pro tip: If `-v` isn't enough, use `-vv` or `-vvv` for extreme detail

:::note
`ssh -v user@host`
:::
