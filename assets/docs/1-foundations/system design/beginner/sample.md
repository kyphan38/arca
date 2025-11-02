# sample

## Question

In the context of a large-scale system, what are the primary trade-offs of disk storage, and what is its main role?

## Answer

- Primary Role: The disk provides durable, permanent storage. It's the source of truth where data must survive crashes or reboots
- Trade-offs:
  - Pro: It offers high capacity (terabytes) at a relatively low cost
  - Con: It is extremely slow (access times in milliseconds), making it a major performance bottleneck compared to RAM or CPU cache
- System Design Application:
  - Use for: Storing foundational data that must not be lost (e.g., user databases, transaction logs, object storage)
  - Avoid for: Storing data that requires frequent, low-latency access, like session information or data for real-time computations. High-performance systems are designed to minimize disk I/O by using caching layers in RAM

## Question

What is RAM's function in a server, and what is the key trade-off when designing a system around it?

## Answer

- Primary Role: RAM serves as the high-speed working memory for the CPU. It holds the application code currently being executed and the data it actively manipulates
- Trade-offs:
  - Pro: It is orders of magnitude faster than the disk (microseconds vs. milliseconds), enabling high-performance computation
  - Con: It is volatile (data is lost on power failure) and is significantly more expensive per gigabyte, resulting in smaller capacities than disk
- System Design Application:
  - Use for: Caching layers (e.g., Redis, Memcached), in-memory databases, and holding the active "working set" of data for an application to ensure low-latency responses
  - Key Decision: The main trade-off is cost vs. performance. You must provision enough RAM to prevent frequent, slow disk access. However, relying solely on RAM for storage is risky due to its volatility; critical data must eventually be persisted to disk

## Question

You can't directly control the CPU cache. As a system designer, why must you still understand it?

## Answer

- Primary Role: The CPU cache is an extremely fast but small memory layer that holds copies of the most frequently used data from RAM, preventing the CPU from having to wait for the slower RAM. Access takes mere nanoseconds
- Trade-offs:
  - Pro: It offers the fastest possible data access, dramatically accelerating computation
  - Con: It has a very small capacity (megabytes) and is volatile
- System Design Application:
  - Why it matters: While not directly managed, application performance is heavily influenced by "cache-friendliness."
  - Application: Writing code and choosing data structures that promote locality of reference (accessing memory sequentially or reusing data that's close together) leads to high cache-hit rates. A low cache-hit rate (a "cache miss") forces the CPU to fetch from RAM, which is a significant performance penalty. In high-frequency trading or large-scale data processing, cache-aware programming is critical

## Question

Why is "just getting a bigger server" (vertical scaling) often not a viable long-term strategy for large-scale systems?

## Answer

- The Problem: For decades, Moore's Law meant we could rely on single-CPU performance doubling every two years. This trend has significantly slowed down; CPU speeds are plateauing. The performance gains from a single, more powerful machine are now marginal and come at a very high cost
- The Implication: We cannot assume a single computer will eventually be fast enough for our needs
- System Design Application:
  - Architectural Shift: This physical limitation forces us to move from vertical scaling (one big machine) to horizontal scaling (many smaller machines)
  - Core Principle: Modern system design is built on the principle of distributed systems. The key challenge is to design applications that can be partitioned and have their workloads distributed across a fleet of computers, assuming that any single machine has finite capacity

## Question

Compare vertical and horizontal scaling. In large-scale systems, why is horizontal scaling almost always the preferred strategy?

## Answer

- Vertical Scaling ("Scaling Up"): This means making a single server more powerful by adding more CPU, RAM, or faster disks
  - Pro: It's conceptually simple; the application doesn't need to change
  - Con: It has a hard upper limit; you can't make a single machine infinitely powerful, and it becomes extremely expensive. It also creates a single point of failure
- Horizontal Scaling ("Scaling Out"): This means adding more servers to run copies of the same code
  - Pro: It can scale to handle massive amounts of traffic and provides high availability. If one server fails, the others can take over
  - Con: It introduces complexity, requiring a load balancer to distribute traffic
- Why Horizontal is Preferred: Large-scale services prioritize reliability and massive scalability. Horizontal scaling is the only practical way to move beyond the physical limits of a single machine and build a fault-tolerant system

## Question

What is the primary function of a load balancer, and why is it a non-negotiable component in a horizontally scaled architecture?

## Answer

- Primary Role: A load balancer's job is to receive all incoming user requests and distribute them evenly across multiple servers
- Problem it Solves: It prevents any single server from being overwhelmed with traffic, which would lead to slow responses or failures
- Why it's Essential: Without a load balancer, horizontal scaling is impossible. You could have many servers running, but no coordinated way to send traffic to them. It's the component that enables a group of individual servers to act as a single, cohesive, and highly available system

## Question

Describe the three core components used to monitor a modern application (logging, metrics, alerting) and how they interrelate

## Answer

These tools are essential for developers to understand an application's behavior without interacting with it directly

1. **Logging Service:**
    - What: Captures detailed, event-based records for individual user requests, such as successes or failures
    - Use: For deep-dive debugging. When you know something is wrong with a specific request, logs tell you the "why."
2. **Metrics Service:**
    - What: Collects aggregated numerical data over time, like CPU/RAM usage or request error rates
    - Use: To understand trends and overall system health. A chart showing a rising error rate tells you "what" is happening at a high level
3. **Alerting Service:**
    - What: Automatically notifies developers when a metric crosses a predefined threshold (e.g., success rate drops below 95%)
    - Use: To be proactively informed that a problem exists, often before users are impacted

- How They Work Together: Alerting tells you that a problem is happening now. You then look at Metrics to understand the scope and historical context of the problem. Finally, you dive into Logs to find the specific error and debug the root cause
