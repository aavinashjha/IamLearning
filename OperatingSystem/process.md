Process Control Block
- Kernel represents each process as a process control block (PCB)
- Status (running, ready, blocked)
- Register State (When not ready)
- Process ID (PID), User, Executable, Priority
- Execution Time
- Memory Space, Translation
Kernel Scheduler maintains a data structure containing the PCBs
Scheduling algorithm selects next one to run

Scheduler:
 if (readyProcesses(PCBs)):
	nextPCB = selectProcess(PCBs)
	run (nextPCB)
 else:
	runIdleProcess() # Puts processor in low power state - not wasting power
Scheduling: Mechanism for deciding which processes/threads receive the CPU
Lots of different scheduling policies provide:
- Fairness
- Realtime guarantee
- Latency Optimization

Implementing Safe Kernel Mode Transfers
- Separate Kernel Stack
- Controlled transfer from kernel (eg. syscall table)
- shouldn't be possible for buggy or malicious user program to cause the kernel to corrupt itself
- Kernel needs space to work, couldn't place everything on user stack
- Two-stack model:
  > OS thread has interrupt stack (located in kernel memory) plus user stack (located in user memory)
  > Syscall handler copies user args to kernel space before invoking specific function (eg. open)
  > Interrupts
- Every process has user and kernel stack

Kernel System Call Handler
- Vector through well defined syscall entry-points
  > Table mapping system call number to handler
- Locate arguments
  > In registers or user stack
- Copy arguments
  > from user memory to kernel memory
  > protect kernel from malicious code evading checks
- Validate arguments
  > protect kernel from errors in user code
- Copy results back
  > into user memory 

Hardware Support: Interrupt Control
- Interrupt processing not to be visible to user process:
  > Occurs between instructions, restarted transparently
- Interrupt handler invoked with interrupts disabled
  > Re-enabled upon interrupt completion
  > Non-blocking  (run to completion no waits)
  > Pack up in a queue and pass off to an OS thread for hard work
    - Wake up a nexisting OS thread
- OS Kernel may enable/disable interrupts
  > On x86: CLI(disable interrupts), STI (enable)
  > Atomic section when select next process/thread to run
  > Atomic return from interrupt or syscall
- HW may have multiple levels of interrupt
  > Mask off certain interrupts
  > non maskable interrupts (nmi) - kernel seg fault

Fork: Clones process
- Fork creates copy of process
- > 0: Parent [Return value is pid of new child]
- = 0: Child
- < 0: Error
Both processes run in parallel
fork internally calls clone
After fork is completed, both processes start after next instruction of fork
Lot of processes are children of shell

UNIX fork:
- system call to create a copy of current process, and start it running (no arguments)
- application developers rarely use syscalls, fork for example is in standard libraries
UNIX exec:
- system call to change the program being run by the current process
UNIX wait:
- system call to wait for its children (process) to finish
UNIX signal:
- system call to send a notification to another process
- often people write their own signal handlers so that they can do some more intelligent things than only dying

Process has a current working directory
- Thatswhy we can use relative path as well along with absolute path
- pipe connects STDOUT to STDIN

Process VM
----------
- Programming simplicity
  > Each process thinks it has all memory/CPU time
  > Each process thinks it owns all the devices
  > Different devices appear to have same high level interface
  > Device interfaces more powerful than raw hardware
    - Bitmapped Display : Windowing system
    - Ethernet card: reliable ordered networking (TCP/IP)
- Fault Isolation
  > Processes unable to directly impact other processes
  > Bugs cannot crash whole machine
- Protection and Portability
  > Java interface safe and stable across many platforms

- Process: Operating System Abstraction to represent what is needed to run a single program
  > Often called a "HeavyWeight Process"
  > No concurrency in a "HeavyWeight Process"
- Two Parts:
  > Sequential Program Execution Stream:
    - Code executed as sequential stream of execution (i.e. thread)
    - Includes state of CPU registers
  > Protected Resources:
    - Main memory state (contents of Address Space)
    - I/O state (i.e. file descriptors)

How do we multiplex process?
- The current state of process held in a Process Control Block(PCB)
  > This is snapshot of the execution and protection environment
  > Only 1 PCB active at a time

Context Switch: CPU Switch from process to process
> Saving/Restoring State
> Unload old thread
> Load and execute new thread
> Frequency of performing context switches: 10-100ms
> Context switch time in linux: 3-4 microseconds
> Thread switching faster than process switching: 100 ns
> But switching across cores about 2x more expensive than within core-switching
> Context switch time increases sharply with the size of the working set and can increase 100x or more
> The working set is the subset of memory used by the process in a time window

Lifecycle of process:
- new: The process is being created
- ready: The process is waiting to run
- running: Instructions are being executed
- waiting: Process waiting for some event to occur
- terminated: when we do exit call. The process has finished execution.

Modern Process with threads:
- Thread: a sequential execution stream within process (sometimes called a lighweight process)
          process still contains a single address space
          no protection between threads
- Multithreading:
  > A single program made up of number of different concurrent activities

Why have multiple threads per appdress space?
- switching to different address space is expensive
- sharing between threads is just memory sharing
- only registers and stack are own, code and files are shared

Thread State:
- State shared by all threads in process/addr space
  > Content of memory (global variables, heap)
  > I/O state (file descriptors, network connections etc.)

- State "private" to each thread
  > Kept in TCB: Thread Control Block
  > CPU registers: including PC program counters

- Execution Stack:
  > Keeps track of where to continue from after return

- 2 threads:
  Stack1 growing down

  Stack2 growing down

  Heap Going up
  Global Data
  Code

Running Thread:
- How do I run a thread?
  > Load its state (registers, PC, stack pointer) into CPU
  > Load environment (virtual memory space etc.)
  > Jump to the PC

- How do dispatcher get control back?
  > Internal events: thread return control voluntarily
  > External events: thread gets preempted

Internal events:
- Blocking on I/O: The act of requesting I/O implicitly yields the CPU
- Waiting on a "signal" from other thread
  > Thread asks to wait and thus yields the CPU
- Thread executing a yield()
  > Thread volunteers to give up the CPU

What happens when thread block to I/O ?
- CopyFile
- read (Trap to OS)
- kernel_thread
- run_new_thread
- switch 
