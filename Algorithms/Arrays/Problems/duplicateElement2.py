"""
- Keep track of incoming pointers to a position
- Every number in array points to its correct position
- Number with multiple incoming pointers is duplicate

- The last position is n+1 position and will have no incoming pointers
  as that number is not possible n+1
- That position acts as head node
        

- 1 2 2 3
  1 2 3 4

  4th position will point to 3rd position, because 3's correct value is at 3rd position
  3rd position will point to 2nd position
  2nd and 1st positions will have self loops
  2nd position will have two incoming pointers, hence it would be duplicate (as 2 numbers want to sit there)

- First node of cycle will be duplicate as it would have multiple incoming links, one from cycle and another from
  original list

- Length of cycle is obtained by starting and waiting till its same

- Get inside cycle by starting at head and moving n steps
  1 2 3 4 4
  <-<-<-<--
  1 is also a self loop
  Cycle at max could be last node we hit as we traverse the lis trom head

"""
def traverse(a, n):
    # After n steps we would be in the cycle

    pos = n+1 # No incoming links
    while n:
        pos = a[pos-1]
        n -= 1
    
    start = pos
    next = a[start-1]
    count = 1
    while next != pos:
        next = a[next-1]
        count += 1
    print("Loop length: ", count)

    # Start from head again
    first = n+1
    second = n+1

    while count:
        second = a[second-1]
        count -= 1

    # Difference between first and second is of length of cycle
    # Move both together till they are at same position

    while first != second:
        first = a[first-1]
        second = a[second-1]
    return first


a=[4,3,1,1,4]
#a=[3,4,2,3,1,5]
# Len is n+1 than it could have n elements thatswhy len-1
print(a)
print(traverse(a, len(a)-1))
