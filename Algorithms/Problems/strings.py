"""
Constraints:
    - string s and constant k
    - 
Goal:
    - return all substrings of length k such that there are k-1 distinct characters in each substring

Idea:
    - n^2 substrings
    - contiguous
    - only one duplicate in each substring k length
    S = "awaglk", k = 4

    awag, wagl, aglk

    - Keep pointer for each substring
    - No need to make a new substring
    - make a set for each substring
"""

def substr(s, k):
    N = len(s)
    sol = []
    for i in range(N-k+1):
        if len(set(s[i: i+k])) != k-1: continue
        sol.append(s[i: i+k])
    return sol

s = "awaglk"
k = 4
print(substr(s, k))


