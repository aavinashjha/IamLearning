Device specific code in the kernel that interacts directly with the device hardware
- Supports a standard, internal interface
- Same kernel I/O system can interact easily with different device drivers
- Special device specific configuration supported with the ioctl system call

Device drivers typically divided into two pieces
- Top Half: accessed in call path from system calls
  > Implements a set of standard, cross device calls like open, close, read, write, ioctl, strategy
  > This is the kernel's interface to device driver
  > Top half will start I/O to device, may put thread to sleep until finished
- Bottom Half: run as interrupt routine
  > Gets input or transfers next block of output
  > may wake sleeping threads if I/O now complete

Life Cycle of an I/O Request
----------------------------
User Program
Kernel I/O Subsystem
Device Driver Top Half
Device Driver Bottom Half
Device Hardware 

Can we view files as communication channels?
                        Comm Channel
- write(wfd, wbuf, len) -----------> read(rfd, rbuf, len)
- Producer and consumer of a file may be distinct process
- May be seperated in time (or not)
- However what if data written once and consumed once?

Connected across the world looks like file I/O?
- Connected queues over the internet
- But what's the analag of open?
- What is the namespace? - IP addresses
- How are they connected in time?
