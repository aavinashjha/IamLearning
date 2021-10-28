(1) AND in a range
- If any bit flips for a given position in range [M to N] the entire column AND value is 0
- If any bit flips, all the columns on right of bit are also flipped

- O(Q.(M-N)): Brute Force
- Whenever we include a bit, we are flipping it because earlier it was implicitly 0
 00
 01
 10
 11
100 --> flip
- Whenever we include a new larger bit, we reset lower bits to restart counting
- Leftmost consecutive common elements in M and N are alwayts fixed in given range

How to find left most common bits?
- check M == N and right shift
