- Dictionary(Abstract Data Type)
- Maintain a set of items, each item has key
  > Insert(item) - overwrite any existing key
  > Delete(item)
  > Search(key): Return item with given key or report doesn't exist
- Different from Binary Search Tree Search as it could give nearest element as well predecessor or successor (bit not here)

- AVL does it in O(lgN)
- Motivation
  > Document Distance
  > Database (Some use search trees some use hashing)
  > Compilers and interpreters (Variable Name to Address)
  > Network router
  > Network server (Which application to direct packet received on NIC)
  > substring search
  > string commonalities
  > file/dir synchronization (files changed or not)
  > cryptography

Simple Approach:
- Direct access table
- Store items in array indexed by key
- But keys have to be non-negative

> Badness:
- Key may not be non-negative integers
  > Solution: Prehash [Map keys to non-negative integers]
              In theory, keys are finite and discrete(string of bits)
              Python: hash(obj), generates a prehash but hash('\0B') = hash('\00C') = 64
	      Ideally, if hash(x) == hash(y), then x = y
	      __hash__: physical location of object in memory
 	      That should not change over time, thatswhy non-mutable could not be hashed
	      As if they change, we cannot get back it from the hash table 
- Gigantic Memory hog
 > Solution: Reduce universe U of all keys (integers) down to reasonable size m for table
             Idea: m = O(N) #keys in dictionary
	     Pigeonhole principle
- Chaining: Grow collided items as linked list
            Hash functions nicely distribute item and most of these lists will have constant length
	    H : U -> {0, 1, 2,...m-1}

Simple Uniform Hashing:
- Each key is equally likely to be hashed to any slot of the table
- Independent to where other keys are hashing

Analysis: Hashing with Chaining
- Expected length of chain for n keys m slots = n/m (1/m + 1/m +..n times in case they are independent)
- This is called alpha or load factor of the table
- O(1) if m = O(n)
- Running time O(1+length of chain)
- 1 is calculating hash constant time
- length of chain is alpha
- O(1+alpha)

Hash Functions:
- Division method: h(k) = k mod m, good when m is prime and not near power of 2
- Multiplication method: h(k) = [(a.k)mod2^w] >> (w-r)
  w bit machine [word size]               
  a.k could be 2 words long
  mod 2^w: Talke the right word
  get left r bits of right w bits

  After multiplication of a.k both w bits wide
  |-------------------------||-------------------------|
  <----------w--------------><----------w-------------->
                             <--r-->
  m = 2 ^ r

  hashing: cut stuff, collide, merge, get pieces, its causing randomization
  r bits chosen are random, mixed up well, due to addition of various shifted version of k

Universal Hashing:
- h(k) = [(ak+b) mod p]mod m
- a and b are random numbers between {0, 1, 2,.. p-1}
- For worst case keys k1 != k2
  Pr{h(k1) == h(k2)} = 1/m

How to choose m?
- Want m = O(n) => alpha = O(1)
- Start small m = 8
  Grow/Shrink as necessary
- Grow table (m->m'): Make a table of size m' (n > m)
  where m' could be smaller than m
- Build new hash h'
- rehash: for each item in old table insert in new table
- O(n+m+m') ~ O(n)

- If m' = m+1 O(1+2+3+..) = O(n^2) [triangular number]

Table doubling m' = 2m
- n insertions
- O(1+2+4+8+...+n) = O(n)

- Operation takes O(n) amortized if k operations takes <= k.T(n) time
- T(n) avg, where average over all operations

Deletion:
- if m = n/2, the shrink to m/2
      Insert
  2^k ----> 2^k + 1
     <-----
      Delete
  O(n) per operation
- if m = n/4 then shrink to m/2
  amortized time becomes O(1)
- Any constant will work till deletion constant is smaller than the insertion constant

- Open Addressing:
  > No chaining
  > one item per slot
  > m (#slots) >= n (#items)

Probing:
- Hash function specifies order of slots to probe for a key (insert/search/delete)
- h: U x {0, 1, ..., m-1} -> {1, 2, .., m-1}
    universe   trial count     
- For arbitrary key k,
  h(k, 1), h(k, 2), ....h(k. m-1) is a permutation of numberss 1, 2.., m-1

Insert(k): Search for empty slot, till that time probe and finally insert
Search(k): As long as slots are occupied by keys != k keep probing until you
           encounter k or empty slot
Delete(k): Replace not with None but with different flag but deleteMe
> Insert treats deleteMe same as None
> Search continues and not halts 

Probing strategies:
- Linear Probing:
  > h(k, i) = (h'(k)+i) mod m
    h'(k) is ordinary hash funtion
    h: takes extra argument for trial count
  Problem: Cluserting: consecutive groups of occupied slots which keep longer
  0.01 < alpha (load factor) = n/m < 0.99
  Size of cluster is O(lgN) which causes insert/search/delete to become O(lgN) and not O(1)
- Double hashing:
  > h(k, i) = (h1(k) - i*h2(k)) mod m
    if h2(k) is relatively prime to m -> permutation

Uniform Hashing: Each key is equally likely to have any one of m! permutations as its probe sequence
- maintain alpha stays around 0.5 otherwise make table again
p = m-n/m = 1-alpha (probability of empty slot)
expected number of trials is 1/p, therfore 1/1-alpha

Python lists use segments of RAM and RAM acts like python list
- RAM is a vast array
- Addressed by sequential integers
- Its first address is 0
- Easy to implement a list atop memory

Dictionary is really a list
Keys are hashed to produce index - 32 bits of 1 or 0
Single differnce gets scattered
To build an index python uses bottom n bits of hash

Idx Hash Key Value
When we print dictionary it comes in same order as its stored in hash table

If at first don't exist try again
- uses backup algorithm

Because collisions move keys away from their natural hash values, key order is quite sensitive to dictionary history 
- their different history put their history in differnt order
-Open Addressing used by python with backup paths

Dicts refuse to get full
- To keep collisions rare, dicst resize when only 2/3 full
- When < 50k entries, size * 4
- When > 50k entries, size * 2
- Starts with 8 size  (Only 3 bottom bits are used)

Don't rely on order
Don't insert while iterating
Can't have multiple keys

Dictionaries trade space for time
