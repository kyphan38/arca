# networking basics

- [] Done content

## Communication Basics: IP Addresses

Concepts

- Public IP address: Every machine communicating over the public internet must be assigned a unique Public IP address to identify it and distinguish it from other machines.
- IPv4 (Internet Protocol version 4)
  - It is a 32-bit integer
  - It is written as 12 digits split into four groups separated by dots (e.g., 192.168.1.1)
  - Each group has a maximum value of 256
  - Limitation: This structure allows for about 4 billion unique addresses, which is not enough for all the people and machines on Earth
- IPv6: A newer version that uses 128 bits, allowing for a virtually unlimited number of addresses

## Sending Data: The "Envelope" Analogy

Concepts

- The rules for sending data over the internet are called the Internet Protocol (IP)
- Packets: Data sent over the network is called a packet
- Metadata (The Header)
  - Just like an envelope has "To" and "From" written on the outside, a data packet has a Header
  - This header contains metadata (data about the data), such as the source IP address and the destination IP address
    - The Data: Inside the envelope is the actual information being sent

## Handling Large Data: TCP

Context: If you want to send a large amount of data (like a whole book) using only IP, you would have to rip the pages out and send them in separate envelopes. The problem is the receiver wouldn't know how to put the pages back in order.

- TCP (Transmission Control Protocol): This protocol runs on top of IP to solve the ordering problem
- TCP Header
  - TCP breaks data into multiple packets and adds its own header
  - Crucially, this header includes a Sequence Number
- Reassembly: Because of the sequence number, the server can reassemble the packets in the correct order once they arrive

## The Protocol Layers

Concepts

- Different protocols handle different responsibilities during a single request
- Network Layer (IP): Handles moving data from one machine to another (the address)
- Transport Layer (TCP): Ensures data is transported correctly and reassembled in the right order.
- Application Layer (HTTP): This is where the actual application data lives (e.g., request and response data). As developers, this is the layer we mostly work with

## Types of IP Addresses

Concepts

- Public: A server needs a public IP so clients can find it
- Private: Clients (like your laptop) typically don't need a public IP. They connect to a router, which has the Public IP
- The router creates a Local Area Network (LAN) and assigns your laptop a Private IP address, which is not accessible directly from the public internet
- Static vs. dynamic
  - Static IP: An address that does not change. Servers usually have static IPs so clients can reliably find them
  - Dynamic IP: An address that changes over time. Clients (home internet) usually have dynamic IPs

## Ports

Context: While an IP address helps you find the correct computer, a Port helps you find the specific channel or application on that computer.

Concepts

- A 16-bit value, meaning there are about 65,000 possible ports
- Default ports
  - HTTP: Uses port 80
  - HTTPS: Uses port 443 (e.g., Google.com uses this implicitly)
- Client Ports: When a client receives a response, it comes back on a randomly assigned port (e.g., 7123)
- Localhost
  - Localhost is a nickname for the IP address 127.0.0.1, which points to your own local machine
  - Rule: You can only run one application on a specific port at a time. If port 4200 is in use, you cannot start another app on port 4200
