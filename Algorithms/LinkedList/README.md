<<interface>>
    List
-------------
add()
size()
-------------
Implementations
--> ArrayList: Implements using an array [Python list is ArrayList, vectors are also arraylist]
--> LinkedList

Lists:
- Store list of ints as an array
- Disadvantages: Insert item at beginning or middle [Time proportional to length of array]
                 Arrays have fixed length

- Therefore we use linked lists
- A recursive data type: using its own reference (next)
Advantages:
- Inserting item in middle takes constant time if we have pointer to previous node
- Lists can keep growing until we have memory
Disadvantages:
- Finding nth item O(N) - constant time on array list

- In general, arrays are faster to read and lists are faster to write
- Implementing merge sort with arrays was 10-20 times slower than linked lists though both were O(NlogN)
  as merge sort requires making another array and copying (writing) to it for which lists are preferred
- LinkedList traversal is actually acessing different memory (as it is allocated at different places)
  hence faces more cache misses - unfortunately it is considered good for non-random access
- Arrays aare close in memory, hence cache miss is less - though it is for random access, but in arrays
  accessing is bound to be less random

- We can implement a SList class instead of exposing nodes
  > keep the fields private
  > SList Node is not directly returned, so it could not be messed up

PushFront(Key) 		Add to front		O(1)
Key TopFront() 		Return front item	O(1)
PopFront()     		Remove front item	O(1)
PushBack(Key)  		Add to back		O(N) [No tail] --> O(1) [With tail]
Key TopBack()  		Return back item	O(N) [No tail] --> O(1) [With tail]
PopBack()      		Remove back item	O(N) [No tail and with tail]
Bool Find(Key) 		Is key in List?		O(N)
Erase(Key)    		Remove key from list	O(N)
Bool empty()		Empty List?		O(1)
AddBefore(Node, Key)    Add key before node	O(N)
AddAfter(Node, Key)	Add key after node	O(1)

- We don't have link to previous node hence PopBack and AddBefore becomes O(N)
