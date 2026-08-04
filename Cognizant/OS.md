# 🖥️ Operating System (OS) Notes for Cognizant

> **Target:** Cognizant GenC / GenC Next, TCS, Infosys, Accenture, Capgemini, Wipro

---

# 1. What is an Operating System?

An Operating System (OS) is system software that acts as an interface between the user and computer hardware. It manages resources and provides services for programs.

### Examples
- Windows
- Linux
- macOS
- Android
- iOS

---

# 2. Functions of an Operating System ⭐⭐⭐⭐⭐

- Process Management
- Memory Management
- File Management
- Device Management
- Security
- Resource Allocation
- CPU Scheduling
- User Interface

---

# 3. Types of Operating Systems

- Batch OS
- Multiprogramming OS
- Multitasking OS
- Multiprocessing OS
- Real-Time OS (RTOS)
- Distributed OS
- Network OS
- Mobile OS

---

# 4. Process ⭐⭐⭐⭐⭐

A **Process** is a program that is currently being executed.

Example:
- Running Chrome
- Running VS Code
- Running Spotify

### Process States

- New
- Ready
- Running
- Waiting (Blocked)
- Terminated

---

# 5. Thread ⭐⭐⭐⭐⭐

A **Thread** is the smallest unit of CPU execution inside a process.

Example:
- One thread plays music.
- Another thread downloads songs.

---

# Process vs Thread ⭐⭐⭐⭐⭐

| Process | Thread |
|----------|---------|
| Heavyweight | Lightweight |
| Own memory | Shared memory |
| Slow creation | Fast creation |
| Communication is slower | Communication is faster |
| More resources | Fewer resources |

---

# 6. Process Control Block (PCB)

PCB stores information about a process.

Contains:
- Process ID (PID)
- Process State
- Program Counter
- CPU Registers
- Scheduling Information
- Memory Information

---

# 7. Context Switching ⭐⭐⭐⭐

Context Switching is the process of saving the current process state and loading another process's state so the CPU can switch between them.

### Causes
- Time slice expired
- I/O request
- Interrupt
- Higher-priority process

---

# 8. CPU Scheduling ⭐⭐⭐⭐⭐

CPU Scheduling decides which process gets the CPU next.

---

## FCFS (First Come First Serve)

- Executes processes in arrival order.
- Non-preemptive.

**Advantages**
- Simple
- Easy to implement

**Disadvantages**
- Convoy effect
- High waiting time

---

## SJF (Shortest Job First)

Executes the process with the smallest burst time.

**Advantages**
- Minimum average waiting time

**Disadvantages**
- Starvation of long jobs

---

## Priority Scheduling

CPU is allocated to the highest-priority process.

**Problem**
- Starvation

**Solution**
- Aging

---

## Round Robin (RR)

Each process gets a fixed **Time Quantum**.

Used in:
- Time-sharing systems

---

## Multilevel Queue Scheduling

Processes are divided into different queues.

---

# Scheduling Algorithms Comparison

| Algorithm | Preemptive | Starvation |
|------------|------------|------------|
| FCFS | No | No |
| SJF | Both | Yes |
| Priority | Both | Yes |
| Round Robin | Yes | No |

---

# 9. Deadlock ⭐⭐⭐⭐⭐

A Deadlock occurs when two or more processes wait indefinitely for resources held by each other.

### Four Necessary Conditions

1. Mutual Exclusion
2. Hold and Wait
3. No Preemption
4. Circular Wait

---

## Deadlock Handling

- Prevention
- Avoidance
- Detection
- Recovery

---

# 10. Starvation

A low-priority process never gets CPU time because higher-priority processes keep executing.

### Solution

Aging (gradually increasing the priority of waiting processes).

---

# 11. Race Condition ⭐⭐⭐⭐

Occurs when multiple threads/processes access shared data simultaneously, causing unpredictable results.

### Solution

- Mutex
- Semaphore
- Synchronization

---

# 12. Critical Section ⭐⭐⭐⭐

The part of a program where shared resources are accessed.

Requirements:
- Mutual Exclusion
- Progress
- Bounded Waiting

---

# 13. Mutex ⭐⭐⭐⭐⭐

Mutex (Mutual Exclusion) is a locking mechanism that allows **only one thread** to access a critical section at a time.

---

# 14. Semaphore ⭐⭐⭐⭐⭐

Semaphore is a signaling mechanism used to control access to shared resources.

### Types

- Binary Semaphore
- Counting Semaphore

---

## Mutex vs Semaphore ⭐⭐⭐⭐⭐

| Mutex | Semaphore |
|--------|-----------|
| Locking mechanism | Signaling mechanism |
| Only one thread | Multiple threads |
| Ownership required | No ownership |
| Binary | Binary or Counting |

---

# 15. Memory Management ⭐⭐⭐⭐⭐

Memory management is the process of allocating and deallocating memory efficiently.

---

# 16. Paging ⭐⭐⭐⭐⭐

Memory is divided into:
- Fixed-size Pages
- Fixed-size Frames

Advantages:
- No external fragmentation

Disadvantage:
- Internal fragmentation

---

# 17. Segmentation

Memory is divided into logical segments such as:
- Code
- Stack
- Heap
- Data

Advantages:
- Easy logical organization

Disadvantages:
- External fragmentation

---

# Paging vs Segmentation

| Paging | Segmentation |
|----------|--------------|
| Fixed size | Variable size |
| No external fragmentation | External fragmentation |
| Physical division | Logical division |

---

# 18. Fragmentation

### Internal Fragmentation

Unused space inside allocated memory.

### External Fragmentation

Free memory exists but is not contiguous.

---

# 19. Virtual Memory ⭐⭐⭐⭐⭐

Virtual Memory allows programs larger than physical RAM to execute using disk space.

Advantages:
- Better multitasking
- Efficient memory utilization

---

# 20. Thrashing

Occurs when the system spends more time swapping pages than executing processes.

Cause:
- Insufficient RAM
- Excessive paging

---

# 21. Demand Paging

Pages are loaded into memory only when required.

Advantages:
- Faster startup
- Reduced memory usage

---

# 22. Cache Memory

A small, high-speed memory between CPU and RAM.

Purpose:
- Faster data access

Levels:
- L1
- L2
- L3

---

# 23. File System

Responsible for storing and organizing files on storage devices.

Examples:
- NTFS
- FAT32
- ext4

---

# 24. Interrupt

An interrupt is a signal that temporarily stops the CPU's current task to handle an important event.

Types:
- Hardware Interrupt
- Software Interrupt

---

# 25. System Call

A system call allows a user program to request services from the operating system.

Examples:
- open()
- read()
- write()
- fork()
- exec()

---

# 26. Kernel

The kernel is the core component of the operating system that manages hardware and system resources.

Responsibilities:
- Memory Management
- Process Scheduling
- Device Management
- File System Management

---

# 27. Kernel Types

- Monolithic Kernel
- Microkernel
- Hybrid Kernel

Examples:
- Linux → Monolithic
- Windows → Hybrid
- macOS → Hybrid

---

# Frequently Asked Interview Questions

### Q1. What is an Operating System?

An Operating System is system software that manages hardware resources and provides services to applications.

---

### Q2. Difference between Process and Thread?

A **process** is an independent executing program with its own memory, whereas a **thread** is a lightweight execution unit within a process that shares the process's memory.

---

### Q3. What is Context Switching?

Context Switching is the process of saving one process's state and restoring another's so the CPU can switch execution.

---

### Q4. What is Deadlock?

A deadlock is a situation where processes wait indefinitely for resources held by each other.

---

### Q5. What are the four conditions of Deadlock?

- Mutual Exclusion
- Hold and Wait
- No Preemption
- Circular Wait

---

### Q6. Difference between Mutex and Semaphore?

A **mutex** allows only one thread to access a critical section at a time, while a **semaphore** can allow multiple threads depending on its count.

---

### Q7. What is Paging?

Paging divides memory into fixed-size pages and frames, eliminating external fragmentation.

---

### Q8. What is Virtual Memory?

Virtual Memory uses disk storage to extend RAM, allowing larger programs to run.

---

### Q9. What is Thrashing?

Thrashing occurs when excessive page swapping leaves little CPU time for actual execution.

---

### Q10. Which scheduling algorithm is used in time-sharing systems?

**Round Robin Scheduling**.

---

# ⭐ Most Important Topics for Cognizant

- Operating System Basics
- Process vs Thread
- PCB
- Process States
- Context Switching
- CPU Scheduling Algorithms (FCFS, SJF, Priority, Round Robin)
- Deadlock
- Starvation & Aging
- Critical Section
- Mutex vs Semaphore
- Race Condition
- Paging vs Segmentation
- Fragmentation
- Virtual Memory
- Thrashing
- Cache Memory
- System Calls
- Interrupts
- Kernel & Kernel Types
- File System
```