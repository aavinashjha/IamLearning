Key UNIX I/O design concepts
- Uniformity
  > file operations, device I/O and interprocess communication through open, read/write, close
  > allows simple composition of programs - find | grep | wc
- Open before use
  > Provides opprtunity for access control and arbitration
  > Sets up the underlying machinery i.e. data structures
- Byte Oriented
  > Even if the blocks are transferred, addressing is in bytes
- Kernel Buffered Reads
  > 3-8ms seek time
  > Processor time is in nano seconds
  > very large as compared to process time
  > Streaming and block devices look the same
  > read blocks process, yielding processor to other task
  > Million instructions time to read from disk
- Kernel Buffered Writes
  > Completion of outgoing transfer decoupled from the application,
    allowing it to continue
- Explicit close

- When write returns data is on its way to disk, and can be read, but it may not be actually be permanent

Internal OS File Descriptor
- Where it resides
- Its status
- How to access it
