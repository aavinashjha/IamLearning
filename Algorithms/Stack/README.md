Stack are also called LIFO Queues
Stack is an abstract data type with the following operations:
- Push(Key): adds key to collection
- Key Top(): returns most recently added key
- Key Pop(): removes and returns most recently-added key
- Boolean Empty(): are there any elements?

Applications:
- Balanced Brackets:
  Input: A string str consisting of '(', ')', '[' or ']' characters
  Output: Return whether or not the string's parenthesis and square brackets are balanced

Both Linked List and Array representation have O(1) Time Complexity for all operations

NGE:
j depends on i: Stack
LIFO
- We want next greater element
- There could be multiple larger elements but we want nearest one
- To keep it on top of stack traverse from right side(end of list)

MinInStack:
- keep other stack with top also inserted with min with new insertion in actual stack
- Or directly a tuple with second field as minimum element


