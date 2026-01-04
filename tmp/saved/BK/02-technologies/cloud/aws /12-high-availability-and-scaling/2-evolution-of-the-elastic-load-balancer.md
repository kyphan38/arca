# evolution of elastic load balancers

## Overview

Concept: ELB refers to entire family of three load balancer types

- Version 1: The older generation (Classic)
- Version 2: The newer generation (Application and network)
- No valid scenarios exist for choosing Version 1 over Version 2

## Version

Concept

- Version 1
  - Introduced 2009; oldest ELB product
  - Handles HTTP, HTTPS, and lower-level protocol
  - Limitations
    - Not a true Layer 7 device; lacks HTTP protocol awareness
    - Lacks advanced functionality of Version 2
    - Significantly higher cost
  - Supports only one SSL certificate per load balancer
- Version 2: Faster performance. Supports Target Groups and Rules for multi-app handling
  - Application Load Balancer (ALB)
    - True Layer 7 (Application Layer) device
    - Supports HTTP, HTTPS, and WebSocket
    - Default choice for web applications using standard web protocols
  - Network Load Balancer (NLB)
    - Supports TCP, TLS (Secure TCP), and UDP
    - Applications not using HTTP/HTTPS
    - Email servers, SSH servers, custom protocol gaming servers
