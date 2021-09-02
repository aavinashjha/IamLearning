Array:
- Contiguous area of memory consisting of equal size elements indexed by contiguous integers
- Numbered list of variables
- 0 based indexing/1 based indexing
- Constant Time access
  > array_addr + elem_size * (i-first_index): thats is where equal size thing comes into picture and gives us constant time access
- Multi Dimensional Array
  > array_addr + elem_size * ((3-1)*6 + (4-1)) [address of (3, 4)]
  > (1, 1) (1, 2) (1, 3), (2, 1) (2, 2): Row major as columns are changing more frequently
  > (1, 1) (2, 1) (3, 1): Column major as rows are changing more frequently
- Time:
                 Add    Remove
  Beginning      O(N)    O(N)
  End            O(1)    O(1)
  Middle         O(N)    O(N)
- Dynamic Arrays:
  >> The problem with static arrays is they are static: int a[100]
     Determine size at compile time
  >> Semi Solution: dynamically allocated arrays
                    int *my_array = new int[size];
     Problem: Might not know the max size when allocating an array
  >> All problems in computer science can be solved by another level of indirection
  >> Solution: Store a pointer to a dynamically allocated array, and replace it with
               a newly allocated array as needed
               Dynamic arrays (also known as resizeable array)
  >> Abstract data type with the following operations (at a minimum)
     - Get(i) -> returns element at location i
     - Set(i, val) -> Sets element i to val
     And these operations have to be O(1)
     - PushBack(val): Add val to the end
     - Remove(i): Removes element at location i
     - Size() - number of elements
  >> Store:
     - arr: dynamically allocated array
     - capacity: size of the dynamically allocated array
     - size: the number of elements currentlly in the array

- Jagged arrays: Array of arrays
  >> int[] []ml = new int[4][]; // 4 rows
     ml[0] = new int[6];
