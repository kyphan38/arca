# dns

- [] Done content

## What is DNS?

Concept: DNS stands for Domain Name System. It is a decentralized system that acts like a phone book for the internet

Problem: Computers identify each other using numbers called IP addresses (e.g., 142.250.1.1). However, humans prefer friendly names like google.com rather than memorizing long lists of numbers

Solution: Just as a contact list maps a person's name to their phone number, DNS maps a domain name to the server's IP address

## How It Works

Process

- When a client (user) wants to visit a website, they type the domain name
- The DNS system looks up the name and returns the specific IP address to the client
- The client then uses that IP address to send a request directly to the server

Note: If you know a website's IP address (using a command like nslookup), you can type that IP directly into your browser address bar and reach the same website without using the domain name

## Who Controls the System?

Concepts

- ICANN: The system is overseen by a non-profit organization called ICANN (Internet Corporation for Assigned Names and Numbers), which essentially owns all domains in the world
- Registrars: ICANN does not sell domains directly. Instead, they use accredited resellers called Domain Registrars (e.g., Google Domains, GoDaddy, Namecheap)
  - When you buy a domain, you go through a Registrar.
- ISP: Your Internet Service Provider (ISP) is also a crucial component that interacts with these DNS servers to help route your requests

## DNS Records

Concepts

- The record: Registrars host servers that hold DNS Records. These records store the information needed to resolve a request
- A record: The most common type is the A Record (Address Record)
  - This record specifically configures a domain (like neetcode.io) to point to a specific IP address

## Caching (Speeding it Up)

Concepts

- Static IPs: Server IP addresses typically do not change very often (they are static)
- Local storage: Because the IP doesn't change, your computer saves (caches) the IP address on its own disk after looking it up once
- Benefit: You do not have to query the DNS system every single time you visit a site you've visited before, your computer remembers the address

## The Anatomy of a URL

Concepts

- Protocol: The first part, usually http or https
- Subdomain: The part before the main name
  - Example: www is a common convention, or domains in domains.google.com
  - You can create as many subdomains as you want if you own the domain
- Domain name: The primary name you purchased, such as google
- TLD (Top Level Domain): The suffix at the end, such as .com, .io, or country codes like .jp (for Japan)
- Path: The specific resource or file you are accessing after the slash, like /search

## What is a Server? (Recap)

Concepts

- A computer with a Public IP address
- Usually associated with a domain name
- Has a firewall explicitly configured to allow external traffic (unlike your home router, which blocks it)
