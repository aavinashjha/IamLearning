Processes are abstraction of running programs
- Binary Image
- Virualized Memory
- Various Kernel Resources
- An associated security context
- Processes are running binaries

Threads are unit of execution in a process
- Virtualized Processor
- Stack
- Program State
- Threads are smallest unit of execution schedulable by an operating system's process scheduler

- A process contains one or more threads
- In single-threaded processes, the process contains one thread. Thread is the process - one thing going on.
- In multi-threaded processes, the process contains more than one thread - more than one thing going on.

Major virtualized abstractions:
- Virtualized Memory: Gives processes a unique view of memory that seamlessly maps back to physical RAM or on-disk storage(swap disk)
- Virtualized Processor: Lets processes act as if they alone run on processor, where multiple processes are multitasking across multiple processors

- Virtualized Memory is associated with the process and not the thread
- Thus, threads share one memory address space.
- Conversely, a distinct virtualized processor is associated with each thread.
  Each thread is an independent schedulable entity.

Benefits of multithreading:
--------------------------
- Programming Abstraction: 
  > Dividing up work and assigning each division to a unit of execution (thread) is a natural approach to many problems.
  > Programming patterns that utilize this approach: reactor, thread-per-connection, thread pool
  > Thread are also viewed as antipatterns - Threads are for people who can't program state machines

- Paralleism:
  > In machines with multiple processors, threads provide an efficient way to achieve true parallelism
  > As each thread receives its own virtualized processor and is independently schedulable entity, multiple threads
    may run on multiple processors at the same time, improving a system's throughput

- Blocking I/O:
  > Without threads, blocking I/O halts the whole process
  > This can be detrimental to both throughput and latency
  > In a multithreaded process, individual threads may block, waiting on I/O, while other threads make forward progress.
    Asynchronous and non-blocking I/O are an alternative solutions to threadfs for this issue.

- Memory Savings:
  > Threads provide an efficient way to share memory yet utilize multiple units of execution
  > In this manner they are alternative to multipel processes.

Drawbacks:
- Increased complexity in the form of needing to manage concurrency through mechanisms such as mutexes and condition variables.
- With Processors with multiple cores and systems with multiple processors, threading will onluy be useful in system programming.

