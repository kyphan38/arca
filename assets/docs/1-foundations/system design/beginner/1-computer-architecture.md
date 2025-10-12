# computer architecture

Question 1: In the context of a large-scale system, what are the primary trade-offs of disk storage, and what is its main role?

Question 2: What is RAM's function in a server, and what is the key trade-off when designing a system around it?

Question 3: You can't directly control the CPU cache. As a system designer, why must you still understand it?

QUestion 4: Why is "just getting a bigger server" (vertical scaling) often not a viable long-term strategy for large-scale systems?

## Why We Start With Computer Basics

- To understand how large computer systems (called distributed systems) are designed, we first need to know how a single computer works
- From a software point of view, a computer has a few main parts: the disk, memory (RAM), the processor (CPU), and the CPU's cache

![img](./img/1.png)

## The Disk (Storage)

- The disk is also known as storage, a hard disk drive (HDD), or a solid-state drive (SSD)
  - SSDs are generally faster than HDDs
- Its main job is to store data permanently
  - If you save a file to the disk and your computer crashes or restarts, the file will still be there when you turn it back on
- Disks can hold a lot of information (high capacity with a low cost), usually measured in hundreds of gigabytes (GB) or even terabytes
  - A terabyte is a trillion bytes
- It is extremely slow for reading/accessing data compared to RAM or CPU cache
- All data on a computer, like text, games, and videos, is stored as simple zeros and ones called bits
  - Eight bits make up a byte
- Application
  - Use for: Storing data that must not be lost
  - Avoid: Storing data that requires frequent, low-latency access, like session information or data for read-time computations

## Memory (RAM)

- Memory, or RAM is not to store data permanently
  - If your computer crashes, any data only stored in RAM will be lost
- It holds the data for CPU to execute
- RAM usually has less storage space than a disk, often measured in gigabytes (like 8, 16, or 32 GB)
- Advantage
  - RAM is much faster than disk, it's about 10, 100, or even 1000 times faster
    - Reading or writing to RAM takes microseconds (millionths of a second), while doing the same on a disk takes milliseconds (thousands of a second)
- Disadvantage
  - RAM is more expensive than disk, which is why computers have less of it
- Application
  - Use for: Caching layers, in-memory databases, etc.
  - Key decision: The main trade-off is cost vs. performance

## The CPU (The Computer's Brain)

- The Central Processing Unit (CPU) is the brain of the computer. It manages everything the other parts do
- The disk and RAM cannot talk each other directly, they need the CPU to move data between them
- The main jobs are
  - Reading and writing data to both RAM and the disk
  - Performing calculations like addition, subtraction, etc.
  - Running the instructions in our computer programs
- The code we write is turned into simple instructions (zeros and ones) that the CPU can understand and follow
  - The CPU reads this code from RAM to execute it
- The CPU also uses RAM to store the data our code works with, like variables in a program

## CPU Cache

- The CPU has its own small, extra-fast memory called a cache (belongs to the CPU)
- It is much smaller than RAM (measured in megabytes) but is incredibly fast
  - Reading from the cache takes nanoseconds (billionths of a second)
- Like RAM, the cache is not permanent
  - Data will be lost if the computer crashes
- The cache's job is to speed things up by holding copies of data from RAM that the CPU uses very often
- When the CPU needs data, it checks the cache first. If the data is there, it can grab it super quickly instead of going to the slower RAM
  - This makes the whole system run much faster

## Limits of a Single Computer

![img](./img/2.png)

- A single computer is a building block, but it has limits. To solve very big problems, we often need to combine many computers together
- One of the biggest limits is CPU speed
- For a long time, Moore's Law described how CPUs got exponentially faster, doubling in speed roughly every two years
- However, in the last 10 years or so, this trend has slowed down and CPU speeds are starting to level off. We can no longer count on a single CPU getting infinitely faster
c