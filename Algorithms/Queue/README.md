First Come First Serve (FIFO)
Abstract Data Type with the following operations:
- Enqueue(Key): Adds the key to the collection
- Key Dequeue(): Removes and returns the least recently-added key
- Boolean empty() - have any elements?

With arrays:
- maintain two indexes
  > read (head) -> where dequeue operation will happen
  > write (tail) -> where enqueue operation will happen
  > empty read == write
  > buffer of one elemnt between read and write index
    [f, _, c, d ,e]
    read : 2
    write: 1
    enqueue(g) -> ERROR
  > Queue will have a maximum size
- For both array and linked list, operations will be O(1)

Circular Buffer/Circular Queue/Cyclic Buffer/Ring Buffer:
- Is a data structure that uses a single, fixed size buffer as if it were connected end-to-end. 
