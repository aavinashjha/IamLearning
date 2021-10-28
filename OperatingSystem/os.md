Operating System:
- Special layer of software that provides application software
  access to software resources
  > Convenient abstraction of complex hardware devices
  > Protected access to shared resources
  > Security and authentication
  > Communication amongst logical entities

OS is a referee, illusionist and glue
- Referee: Manage sharing of resources, protection, isolation [Resource allocation, Isolation, Communication] 
- Illusionist: Provide clean easy to use abstractions of physical resources
               > Infinite memory, dedicated machine
               > Higher level objects: files, users, messages
               > Masking limitations, virtualization
- Glue: Common services
        > Storage, Window System, Networking
        > Sharing, Authorization
        > Look and feel

------------
Applications
------------ Virtual Machine Interface
     OS
------------ Physical Machine Interface
  Hardware
------------

"Virtual Machine" Boundary

--------------------------
	Software
--------------------------
OS Hardware virtualization
--------------------------
	Hardware
--------------------------

- Two types of virtual machine
 > Process VM: supports the execution of a single program, this functionality typically provided by user
 > System VM: Supports the execution of entire OS and its application

- File browsing should be same for actual hard disk or USB drive: That abstraction is provided by OS
- Moore's Law: 2X transistors/chip every 1.5 years

Four fundamental OS concepts:
- Thread (Thread of control)
  > Single Unique Execution Context
  > Program Counter, Registers, Execution Flags, Stack
  > A thread is executing on a processor when it is resident in the process registers
  > PC register holds the address of executing instruction in the thread
  > Certain registers hold the context of thread
    - Stack Pointer holds the address of top of the stack
      [Other conventions frame pointer, heap pointer, data]
    - May be defined by the instruction set architecture or by compiler conventions
  > Registers hold the root state of the thread, rest is in memory
  > Threads encapsulate concurrency: "Active" component

- Address Space with translation
   Code
   Static Data
   Heap
   Stack

  > Programs execute in an address space that is distinct from the memory space
    of physical machine
  > Address space = set of accessible addresses + state associated with them
  > 32 bit processor, there are 2^32 addresses (0 to 2^32-1)
  > What happens when you read or write to an address?
    - Perhaps nothing
    - Perhaps acts like regular memory
    - Perhaps ignores writes
    - Perhaps causes I/O operation (Memory mapped I/O)
    - Perhaps causes exception (fault)
  > If there are multiprocessors equal to number of threads, we could run each thread
    on each procesor, they will do it parallely, because thread is nothing but its state
    is in processor's register like PC.
  > To give illusion on a single processor system, we could create virtual CPUs, which are
    nothing but time shared, that means for sometime thread 1 address is set in  PC of processor, after
    some time other thread's address is set in PC
  > Each virtual CPU needs a structure to hold:
    PC, SP, Registers(Integer, Floating Point, others?)
  > How we switch from one virtual CPU to next?
    - Save PC, SP and registers in currenet state block
    - Load PC, SP and registers from new state block
  > What triggers switch?
    - Timer, Voluntary Yield, I/O, other things 
  > Address spaces encapsulate protection: Passive part  

- Process
 > An instance of an executing program is a process consisting of an address space
   and one or more threads of control
 > The Basic problem of concurrency involves resources:
   - Hardware: single CPU, single DRAM, single I/O devices
   - Multiprogramming API: processes think they have exclusive access to shared resources
 > OS has to coordinate all activity:
   Multiple processes, I/O interrupts
 > Basic Idea: Use Virtual Machine abstraction
   - Simple machine abstraction for processes
   - Multiplex these abstract machines
 > Properties of simple multiprogramming technique:
   - All virtual CPUs share same non-CPU resources
     > I/O devices the same
     > Memory the same
   - Consequence of sharing:
     > Each thread can access, the data for every other thread (good for sharing bad for protection)  
     > Can threads overwrite OS functions?
   - (Unprotected Model) Used in embedded applications - Windows 95-ME
 > Process: Execution environment with restricted rights
   - Address space with 1 or more threads
   - Owns memory(Address Space)
   - Owns file descriptor, file system context
   - Encapsulate one or more threads sharing process resources
 > Why Processes?
   - Protected from each other
   - OS protected from them
   - Navigate fundamental tradeoff between protection and efficiency
   - Processes provide memory protection
   - Threads more efficient than processes
   - Application instances consists of one or more processes

- Dual mode operation/Protection
 > Only the system has the ability to access certain resources
 > The OS and the hardware are protected from user programs
 > User programs are isolated from one another by controlling the
   translation from program virtual addresses to machine physical addresses
 > Operating System must protect itself from user programs
   - Reliability: compromising the operating system generally causes it to crash
   - Security: limit the scope of what processes can do
   - Privacy: limit each process to the data it is permitted to access
   - Fairness: each should be limited to its appropriate share
 > Primary Mechanism:
   - Limit the translation from program address space to physical memory space
   - Can only touch what is mapped
 > Additionally: privileged instructions, syscalls processing, subsystem (file access rights)
 > Hardware provides atleast two modes:
   - Kernel Mode/Supervisor/Protected
   - User Mode: Normal programs executed
 > What is needded in hardware to support dual mode?
   - a bit of state (user/system mode bit)
   - Certain operations/actions only supported in kernel mode
   - In user mode they fail or trap
   - User -> Kernel transition sets system mode and saves the user PC
   - Operating system code carefully puts aside user state then performs
     the necessary operations
   - Kernel -> User transition clears system mode and restores appropriate
     user PC [Return from interrupt]
 > Simple Protection: Base(>=) and Bound(<) Protection
   - Requires relocating loader
 > RTU: Return to User
 > 3 types of mode transfer: syscall, interrupt, Trap or Exception
 
OS Bottom Line: Run Programs
- Load instruction and data segments of executable file into memory
- Create stack and heap
- "Transfer control to it"
- Provide services to it
- While protecting OS and it

Heap and stack grows in opposite directly, with a hole in between,
to provide opportunity for growth


PC (Program Counter) points to an instruction which has to be run next
This is instruction cycle
- Instruction fetch
- Decode
- Execute (Registers and ALU)
- Write results to registers/memory
- PC = Next PC
- Repeat

