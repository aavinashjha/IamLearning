Priority Queue
--------------
- Implements a set S of elements, each of the elements associated with a key
- > Insert(S, x)         : Insert element x into S
- > Max(S)               : Returns element of S with largest key
- > ExtractMax(S)        : Returns element of S with largest key and also removes it from S
- > IncreaseKey(S, x, k) : Increase the x's key to k

Complete Binary Tree
--------------------
A binary tree with height h is complete binary tree if the levels 0, 1, 2.., h-1 have maximum
number of nodes possible(that is level i has 2^i nodes for 0 <= i <= h-1) and in level h-1
all the internal nodes are to left of external nodes

Maximum number of elements in a subtree = 2n/3

Heap
----
- Implementation of priority queue
- Visualized as nearly complete binary tree but linear in storage
- Similar to Level order traversal
- Max Heap Property: Node's key is >= child's key
- Min Heap Property: Node's key is <= child's key
- Top of heap is called root node
- Highest/Lowest priority element is stored in root
- Heap is not a sorted data structure, it can be regarded as being partially ordered
- Almost complete
- When complete it has smallest possible height
- Heap as a tree
	1    2    3    4   5
      | 16 | 14 | 10 | 8 | 7 |

		16
	       /  \
	      14  10
	     / \
	    8   7	
- > Root of the tree has highest element
- > parent(i) = i/2
- > left(i) = 2i
- > right(i) = 2i + 1

- | 2 | 4 | 1 | : Neither max/min heap, its just a heap
- Elements A[n/2 +1, ....n] are all leaves
- Heap Operations
- > maxHeapify  : Correct a single violation of the heap property in a subtree's root
    maxHeapify(A, i) : Assume that the trees rooted at left(i) and right(i) are max heaps
		       We are going level by level and its complete binary tree, hence O(lgN)
- > buildMaxHeap: Produces a max heap from an unordered array
		  Works in bottom up A[n/2..1] that means we have precondition always satisfied
		  left(i) and right(i) are always satisfied
		  We are starting from non leaf nodes
		  as we are near to leaves we have less comparisons but nodes are large
		  but as we move up nodes decrease and operation increase
		  maxHeapify takes O(1) time for nodes that are level above the leaves
		  and in general O(l) times for nodes that aare l levels above the leaves.
		  n/2 leaves
		  Level 1   : n/4 nodes (Parent of leaf)
		  Level 2   : n/8 nodes
		  Level lgN : 1 node (root)

		  Total amount of work in the for loop
			(n/4) (1 Comparison) + (n/8) * (2C) + (n/16) * (3C) + 1 * (lgN C)
			Set n/4 = 2^k, n = 4*2^k, lg n = k
			1/2^0 + 2/2^1 + ... + (k+1)/2^k: Converging series is a constant
			Sum(i+1/2^i) i = 0..k
		  O(n)

