Python
------
- nonlocal: Python3, used in nested function to use outside variable

https://medium.com/100-days-of-algorithms/day-41-union-find-d0027148376d

Amortized Analysis:
- A bad one today but next one will beocme good becuase of this
- Like QuickFind may be take O(logN) with path compression but next one will become better
- Dynamic array is also amortized O(1), which when exhausted takes O(N) but only once in a while
- Different from QuickSort random where worst case is O(n^2), average is O(NlgN) but one run doesn't 
  improve next one as it is random
- Binary Counter
  Flipping bit is units of work
  For k bits and n numbers it looks like O(nk)
  Incrementing evne number requires only 1 unit of work
  When incrementing odd number, we are going from LSB to see if its 1 we flip it and in end we see 0 we flip that
  Valid for even as well
  Going from A to B and coming back from B to A Rs 10 each
  Or Going from A to B, buying round ticket Rs 20 and B to A is free
  Suppose we considered changing a bit from 0 to 1(going up) and changing bit from 1 to 0(going down)
  Now suppose that when we go up, we buy a round trip ticket, we pay 2 when going from 0 to 1
  and flipping from 1 to 0 is free (Each increment of number than takes 2 operations) 
  2n = O(n)
  Always one bit will be charged for flipping from 0 to 1(going) other will come for free in this or coming iterations
  
  Potential function:
  Phi maps each data structure Di to a real number Phi(Di) which is the potential associated with data structure
  
  Let Phi(Di) = bi the number of 1s in i
  0000 -> 0001
   _
  ci = ci + phi(di) - phi(di-1) = 1+1-0 = 2
  no 1 initially so no free rides
 
  0011 -> 0100
  2 free rides available as 2 1s
  _
  ci = ci + phi(di) - phi(di-1) = 3+1-2 = 2

  where ci is actual cost
  phi(di-1) : free rides available

  phi difference takes care of how many free rides we have and how many we loose
  Lost some potential and gained some

Invariant:
- A fact about a data structure that is always true

- Not every class is ADTs. Some classes just store data (no invariants)

How to prove an algorithm is wrong?
- Counter examples > Should not be large/long, they should be short and crisp
  Knapsack: First fit counter example {1, 2} Tragte is 2 will fail in first fit
  These ways are called heuristics: first fit, smallest to largest best fit, largest to smallest

RAM Model of Computation
------------------------
- Algorithms can be studied in a machine/language independent way
- This is because we use RAM model of computation for all our analysis
- Each simple operation (+, -, =, if, call) takes 1 step
- Loops and subroutine calls are not simple operations
  They depend on the size of data and the contents of a subroutine

- How many instructions executed by machine? 
- Random Access Machine
- Each memory access takes exactly 1 step

Worst Case Complexity
---------------------
The worst case complexity of an algorithm is the function defined by maximum number of steps
taken on any instance of size n

Best Case Complexity
--------------------
The best case complexity of an algorithm is the function defined by the minimum number of steps
taken on any instanjce of size n

Average Case Complexity
----------------------
The average case complexity of the algorithm is the function defined by an average number of steps
taken on any instance of size n

Each of these functions defines a numerical function: time vs size
Worst case easy to obtan by analysis and pessimistic view

 
Asymptotic Notation
-------------------
Best, worst and average case are difficult to deal with precisely
because the details are very complicated

It is easier to talk about upper and lower bounds of the function

g(n) = O(f(n)) means c*f(n) is an upper bound on g(n)
      g(n) is actual fn and it is O upper bound by f(n)
atmost as fast as: O
Lower bound
Tight bound

g(n) E O(f(n)) where O(f(n)) is a set of functions
We do not care about small values hence a constant n0 beyond whihc they are satisfied
n0- threshold >= 0
c - multiplicative constant > 0

Running time grow as input size grows: Function Growth
10 billion instruction/s
256 input size
- 2^N does 10^77 operations (10^59 years)
- N^2 does 65536 operations
- N does 256 operations
- LgN does 8 operations
- N^k is polynomial
- 2^N is exponential

If the amount of work at subsequent levels of the recursion tree form a decreasing geometric progression, the
amount of work is asymptotically the same as amount of work done at root level
f(N) = 3*f(N/2) + Theta(N^3)..GP with 3/8 ratio

f(N) = 5*f(N/3) + Theta(N)
Level 1: N
Level 2: 5*N/3
Level 3: 5 (5*n/3^2)

Work is increasing level by level
Max work will be done at lowest level
Size of problem at lowest level is 1
Lets say we have k levels
n/3^k = 1, k = log N base 3
Nuber of nodes increasing by a factor of 5
So total work = 5^level = 5^logN = N^log5 with base 3

If work remains same across levels = work done on each level * number of levels

