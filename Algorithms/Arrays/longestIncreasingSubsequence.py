from bisect import bisect_left
"""
LongestIncreasingSubsequence:
    2 1 5 7
    1 1 2 3

Constraints:
- Consider Strictly increasing
- LongestIncreasingSubsequence: That subsequence will be sorted

Idea:
    - The first thing which comes in mind is to find out all subsequences which takes O(2^N)
    and for evaluating every sequence for finding maximum subsequence O(N)
      T: O(N*2^N), S: O(N)
    - Two pointers - ahead one compare with all previous ones and select maximum ending at a particular position
      L(i): Longest subsequence ensing at ith index
      L(i) = max(1+L[j]) where j 0 <= j < i
      T: O(N^2), S: O(N)
    - One minor optimization is to consider max in loops only so that extra O(N) is avoided
    - When longest increasing subsequence is formed : It would have all elements sorted
      We want to make room for elements as much as possible
      Thatswhy we select minimum possible element for a position
      If new element encountered is larger than the last element of tmp array, we insert and increase longest increasing subsequence by 1
      If the new element is shorter we will try to replace it with the number in tmp array such that lower_bound(num) is the current element
      Important thing to notice here is the size of tmp array always increases
      As we are writing in lower_bound place, its not guaranteed to have actual longest increasing subsequence
      But its length will be correct
      The tmp array is always sorted thatswhy we can insert it in lgn time
      Scanning the actual array will take O(n) time
      T: O(NlogN), S: O(N)
"""
def LongestIncreasingSubsequence(a):
    print('Sequence', a)
    N = len(a) # 4
    sol = [1] * N # [1 1 1 1]
    length = 0
    for i in range(N): # 0..3
        for j in range(0, i): # 0..i-1
            if a[i] <= a[j]: # O(1)
                continue
            if sol[j] + 1 > sol[i]:
                sol[i] = sol[j]+1
                if sol[i] > length:
                    length = sol[i]

    print('cache', sol)
    return length

def longest_increasing_subsequence(sequence):
    N = len(sequence)
    cache, parent = [1] * N, [-1] * N

    for i in range(N):
        for j in range(i):
            if sequence[i] > sequence[j]:
                if 1 + cache[j] > cache[i]:
                    cache[i] = 1 + cache[j]
                    parent[i] = j

    i, sol, length = N-1, [], max(cache)
    while len(sol) != length:
        sol.append(sequence[i])
        i = parent[i]

    sol.reverse()
    return sol

def LongestIncreasingSubsequenceBinarySearch(a):
    N, t = len(a), [a[0]]

    def replace(num):
        index = bisect_left(t, num) # Lower bound of number in array
        if index != len(t) and num == t[index]:
            # Do nothing
            return

        t[index] = num # Point of insertion

    for i in range(1, N):
        if a[i] > t[-1]: # Greater than last element insert
            t.append(a[i])
        else:
            replace(a[i])

    return len(t) 

"""
0 1  2 3 4 5 6 7  8 9 10
3 4 -1 5 8 2 3 12 7 9 10

-1 4 
0  1
"""
a = [3, 4, -1, 5, 8, 2, 3 ,12, 7, 9 ,10]
print('LongestIncreasingSubsequence: ', LongestIncreasingSubsequence(a))
print('LongestIncreasingSubsequenceBS: ', LongestIncreasingSubsequenceBinarySearch(a))
