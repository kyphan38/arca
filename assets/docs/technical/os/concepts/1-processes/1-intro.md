# intro

## The Computer System

- What does a computer system contain?
  - User software: User applications (browser, email client, games, application servers, databases, AI/ML algorithms, etc.)
  - System software: Operating System (OS), etc.
  - System hardware: CPU, memory, I/O devices, etc.

## OS

### Definition

- Middleware/sits between user software and system hardware
  - Examples: Linux, Windows, MacOS
- Manages computer hardware: CPU, main memory, I/O devices (hard disk, network card, mouse, keyboard etc.)
  - User applications do not have to worry about the details of low-level hardware
  - Instead of having the application talk directly to the hardware (which is extremely complicated and dangreous), the OS system provides a set of standardized API called System Calls
- Analogy: Ordering food at a restaurant
  - You &rarr; The waiter &rarr; The kitchen

### Goals

- Abstracts the hardware by hiding the complex, low-level details of how physical components work underthehood
- Optimizes the use of the CPU, memory, and other resources by deciding which process gets to use which resources, and for how long
- Ensures separation between multiple processes. It means that one program should not crash/impact another program or the entire system

## Program

### Definition

- Consist of code (CPU instructions) and data for a specific task
  - Icon (.app) &rarr; Contents folder (executable file) and Resources (data)
- Processes
  - A running program has one or more separate processes to handle each seprate tasks

## What Happens When You Run a Program?

Stage 1: Preparation

- A compiler translates high-level code into an executable file containing machine code (the 1s and 0s) and data
- The executable file (e.g., “a.out”) is created and stored on the hard disk

Stage 2: OS

- Creates a process and a record (Process Control Block) to keep track of its status
- Allocates a private virtual address space for the process in the main memory (RAM) where the process resides in
- Tells the loader (OS'service) to read the content of executable file (from the hard disk) and copy it into the newly allocated address space in RAM
- Intializes the CPU context
  - Set the PC to point the memory address of the very first instruction
  - Initializes other registers

&rarr; Then, the OS hands control over the CPU

Stage 3: CPU

- Fetches the instruction pointed by the PC from memory
- Increments the PC to point to the next instruction
- Decodes the instruction to figure out what operation needs to be done
- Loads the data from memory into registers, if needed
- Executes the instruction
- Stores results back into a register or a memory location

![img](./img/1.png)

![img](./img/2.png)

![img](./img/3.png)

## Concepts

### CPU Virtualization

Previously, one computer could only run one process at a time, which creates a poor, slow user experience. For example, you couldn't listen to music while surfing the web

In order to solve this problem, we should make one computer to run multiple processes simultaneously. The OS achieves multitasking through a concept called CPU Virtualization. This is done using two key components

- The OS scheduler is the component responsible for deciding which process to run next and for how long
- The OS performs a context switch - switches between different processes very quickly to swap processes on the CPU

This process happens so quickly that the OS creates the illusion that each process has its own dedicated CPU

How a context switching is performed

- The OS runs Process A for a short time
- It then pauses Process A and saves its execution context (the current state of its CPU registers, including the PC)
- The OS loads the saved context of another process, Process B
- It runs Process B for a short time before switching again

![img](./img/4.png)

### Memory Virtualization

Without memory virtualization, every process would use the memory directly on the physical RAM, which leads to 2 major issues

- A bug or crash in one process can overwrite and corrupt the memory of another process, or even the OS itself, causing the entire computer to crash
- One process can read or modify another process's data, creating a massive security vulnerability

Memory image: From a process's perspective, it has a large, clean, contiguous block of memory, which starts at address 0, including

- Code: The program's instructions
- Data: Global and static variables
- Heap: For dynamically allocated memory that can grow
- Stack: For function calls and local variables, which grows and shrinks

Mapping

- The OS maintains a page table for each process that translates the virtual addresses into the real physical addresses in RAM
- This guarantees each process is completely isolated

![img](./img/5.png)

### User Mode and Kernel Mode

Imagine a system with only one mode, every process has a full and unrestricted access to all of the hardware and memory. This will create a chaotic and unreliable environment

- (Same to memory virtualization)

Privilege levels: CPUs have different modes of operation. The two most important are

- User mode (Unprivileged): Where user applications run. In this mode, the CPU is not allowed to execute certain "privileged" instructions that could harm the system, like directly accessing hardware or modifying critical OS data
- Kernel mode (Privileged): Where the OS runs. In this mode, the CPU can execute all instructions, giving the OS full control over the hardware and memory

Transitions to Kernel Mode: A process can't just switch to kernel mode whenever it wants. It is controlled and happens only in three specific situations

- System salls: When a user program needs to request a service from the OS (e.g., "read a file" or "send data over the network"). The program executes a special instruction that safely transfers control to the OS, which performs the task in kernel mode and then returns control to the user program
- Interrupts: When a hardware device (like a keyboard, mouse, or network card) needs the OS's attention. The hardware sends an interrupt signal to the CPU, which pauses the current user process, saves its state, and jumps to an OS interrupt handler in kernel mode to service the device
- Faults (Exceptions): When a user program makes an error, such as dividing by zero or trying to access invalid memory. The CPU traps this error and transfers control to the OS in kernel mode to handle it, which often involves terminating the faulty program.

### Managing I/O Devices

To mange the I/O devices, there are two components

- Device controllers: Each physical device is managed by a hardware chip called a device controller. This controller understands the low-level signals needed to operate the device
- Device drivers: To communicate with the device controller, the OS uses a piece of software called a device driver. Each driver is specific to a piece of hardware and knows exactly which commands to send to the controller to perform I/O operations (e.g., "read block 500 from the hard disk"). The driver is also responsible for handling interrupts from the device when an operation is complete.

This hardware/software pairing allows the OS to abstract the details of I/O, presenting a simple, consistent interface for applications to use (e.g., readFile()), regardless of the underlying hardware

## Isolation and Privilege Levels

- Protecting concurrent processes
  - Can one process interfere with another's code or data?
  - How does the OS ensure safe sharing during virtualization?
- CPU mechanisms for isolation
  - Privileged instructions: Access sensitive information or perform sensitive actions
  - Unprivileged instructions: Regular operations (e.g., add)
- CPUs have multiple modes (e.g., Intel x86 CPUs use 4 rings)
  - Low privilege (e.g., ring 3): Only unprivileged instructions
  - High privilege (e.g., ring 0): Both privileged and unprivileged instructions

## User Mode and Kernel Mode

- User programs run in user mode (unprivileged)
  - The CPU executes only unprivileged instructions
- OS runs in kernel mode (privileged)
  - The CPU can execute both privileged and unprivileged instructions
- Mode transitions
  - The CPU shifts to kernel mode to execute OS code during
    - System calls: User requests for OS services
    - Interrupts: External events requiring OS attention
    - Program faults: Errors needing OS intervention
  - After completing kernel-mode tasks, the OS returns to user mode

## System Calls

- A system call is made when a user program requires an OS service (e.g., reading from a hard disk)
  - Why? User processes cannot execute privileged instructions to access hardware, ensuring one user cannot harm another
  - The CPU jumps to OS code to handle the system call and returns to user code afterward
- User programs typically use library functions (e.g., `printf` in C), which invoke (cause) system calls (e.g., to write to the screen)

## Interrupts

- The CPU handles external events (e.g., mouse clicks, keyboard input) via interrupts
- An interrupt is an external signal from an I/O device requesting CPU attention
- Example: A program requests disk data, and the disk raises an interrupt when the data is ready (avoiding program waiting)

## Interrupt Handling

- Process - How are interrupts handled?
  - The CPU is running process P when an interrupt arrives
  - The CPU saves P's context, switches to kernel mode, and runs OS interrupt-handling code (e.g., reading a keyboard character)
  - The CPU restores P's context and resumes P in user mode
- Interrupt-handling code is part of the OS
- The CPU executes the OS interrupt handler and returns to user code

![img](./img/6.png)

## I/O Devices

- The CPU and memory are connected via a high-speed system (memory) bus
- I/O devices connect to the CPU and memory via separate buses
  - I/O devices interface with the external world
  - Store user data persistently
- The OS manages I/O devices on behalf of users

![img](./img/7.png)

## Device Controller and Device Driver

- Each I/O device is managed by a device controller (a microcontroller communicating with the CPU/memory over a bus)
- Device driver: Special OS software with device-specific knowledge to handle I/O operations
- Functions of the kernel device driver
  - Initialize I/O devices
  - Start I/O operations and issue commands to the device (e.g., read data from a hard disk)
  - Handle interrupts from the device (e.g., when data is ready)

![img](./img/8.png)

## Advice

### Why Study Operating Systems?

- Knowledge of hardware (architecture) and system software (OS), and how user programs interact with these lower layers, is essential for writing high-performance, reliable user programs
- Key questions addressed by studying OS
  - What happens when you run a user program?
  - How can you make your program run faster and more efficiently?
  - How can you make your programs more secure, reliable, and tolerant to failures?
  - Why is your program running slowly, and how can you fix it?
  - How much CPU/memory is your program consuming, and why?
- OS expertise is one of the most critical skills for building high-performance, robust, and complex real-world systems

### Beyond OS to Real Systems and Future Courses

- Architecture + OS: Provides the foundation for understanding how a user program runs on a single machine
- Networking: Explores how programs communicate across machines
- Databases and data storage: Covers how applications store data efficiently and reliably across one or more machines
- Performance engineering: Focuses on making programs run faster
- Distributed systems: Examines how multiple applications across multiple machines work together to perform tasks reliably
- Other topics: Virtualization, cloud computing, security, etc.

## Questions

- What does a computer system contain?
