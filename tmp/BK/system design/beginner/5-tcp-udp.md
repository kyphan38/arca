# tcp udp

- [] Done content

## The Internet Protocol Suite (TCP/IP)

Concepts

- This is often referred to as TCP/IP because TCP runs on top of the Internet Protocol (IP)
- Encapsulation: The TCP packet is actually wrapped (encapsulated) inside the IP packet
- The name TCP/IP can be confusing because the suite also includes other protocols, such as UDP, not just TCP and IP

## TCP (Transmission Control Protocol)

Concepts

- TCP is the most common protocol because it solves the problems inherent in the unreliable nature of the internet
- Ordering data
  - When sending large amounts of data, it is broken into pieces
  - IP sends these packets, but they might arrive at the destination in the wrong order
  - TCP Solution: TCP ensures that when packets arrive, they are reassembled in the exact order they were sent
- Reliability
  - Networks are not reliable, sometimes packets go missing
  - TCP Solution: If a packet is missing, TCP detects it and resends only the missing packet
  - Analogy: It is like sending mail with tracking. If the package doesn't arrive, you know about it and can resend it
- Connection-oriented
  - TCP establishes a two-way connection between the client and the server
  - Three-way handshake: Before sending data, the computers shake hands (synchronize and acknowledge) to establish the connection

The trade-off (Overhead)

- TCP is reliable, but it is slower and expensive for the network
- The guarantees (ordering, re-sending, handshakes) create extra data overhead and latency

Common uses

- Almost everything on the web uses TCP because reliability is critical
- HTTP (web pages), SMTP (email), and WebSockets are all built on top of TCP

## UDP (User Datagram Protocol)

Concepts

- UDP is an alternative to TCP that prioritizes speed over reliability
- No connection:
  - UDP does not establish a connection or perform a handshake
  - The client sends a request, and the server just starts blasting data back
- Unreliable
  - If a packet (called a datagram in UDP) is lost, it is lost forever. It is not resent
  - Data can arrive out of order, and UDP does not fix the order

The benefit (Speed): Because it skips the handshake and doesn't track lost packets, UDP is much faster than TCP

Common uses

- Real-time streaming: Used for live video or calls
  - Why? If a video frame is lost, it is better to skip it and keep up with the live feed than to pause and wait for the old frame to be resent. You want to see what is happening now, not what happened 5 seconds ago
- Online Gaming: Similar to streaming, speed is more important than perfect data
- DNS: The Domain Name System uses UDP

## Summary for Developers

Trade-offs: There is always a trade-off. TCP is for when you need reliability (email, web browsing), UDP is for when you need speed (streaming)

Note: As software engineers, we usually work at the Application Layer (like HTTP) and don't often need to touch the low-level TCP/UDP details
