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
