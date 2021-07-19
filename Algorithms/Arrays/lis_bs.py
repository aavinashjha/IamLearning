"""
Longest Increasing subsequence
- Iterate through all the elements
- Whenever we get a smaller number it could not be part of longest increasing subsequence
- Hence overwrite the earlier smaller one
- Whenever we get a larger number, store it in next array index and create a link
- link could be created by another array having reference to this one

This is 1D representation of Patience sort in which we make piles of card
and create a link between top of the previous pile and next element
  index: 0  1   2  3  4  5  6  7   8  9  10
  elem:  3, 4, -1, 5, 8, 2, 3 ,12, 7, 9 ,10

2 6 3 4
{0: -1, 1: 0, 3: 1, 4: 3, 5: 2, 6: 2, }

Maximum number of piles could be equal to numbers
increasing order of N

 0   1  2   3  4   5   6   7  8
[16, 3, 5, 19, 10, 14, 12, 0, 15]

We can implement it with Piles but that would take extra space, so lets store the index

"""
from bisect import bisect_left

def lis(sequence):
    N = len(sequence)

    if N == 0: return []

    p = [0] # Piles: Base case, single card
    v = [sequence[0]]
    l = [-1] * N

    for i in range(1, N):
        index = bisect_left(v, sequence[i])
        if index != len(p):
            p[index] = i
            l[i] = -1 if index == 0 else p[index-1]
            v[index] = sequence[i]
        else:
            l[i] = p[-1]
            v.append(sequence[i])
            p.append(i)

    sol = []
    if len(l) == 0:
        return sequence[0]
   
    i = p[-1]
    while i != -1:
        sol.append(sequence[i])
        i = l[i]

    sol.reverse()
    return sol

a = [3, 4, -1, 5, 8, 2, 3 ,12, 7, 9 ,10]
print(lis(a))
