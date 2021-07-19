"""
Wiggle/ZigZag Subsequence:
    Constraints:
    - Strictly wiggle (equal values not allowed)
    Idea1:
    - Select the first element
    - We need to add the peaks
    - Assume we are going on road (1D)
    - And whenever we change direction add the previous point
    Example:
    1 7 4 9 2 5
     + - + - +
    Using first 2 points find direction
    N <= 2 : return N
    Direction: + (7-1)
    4-7 = -3 (-ve)
    add previous point
    sol = [1, 7, 4, 9, 2]

    Idea2:
    1 4 3 5 2
inc 1 2 3 4 5
dec 1 2 3 4 5

    When we are at a particular index in inc we are seeing array ending in increasing subsequence at i considering that element
    When we are at a particular index in dec we are seeing array ending in decreasing subsequence at i considering that element

    S(i) = Maximum wiggle subsequence length ending at i including that element

    2 3 4 6 1 0 4 5 9 6 8 3 7 4
inc 1 2 2 2 1 1  
dec 1 1 1 1 2 3
"""
def wiggleSubsequenceLength(a):
    N = len(a)
    if N <= 2: return N
    d = a[1] > a[0] # True: Increasing, False: Decreasing
    sol = [a[0]]
    for i in range(2, N):
        if i+1 >= N:
            continue
        nd = a[i+1] > a[i]
        if nd != d:
            d = nd
            sol.append(a[i])
    sol.append(a[-1])
    return len(sol)

def wiggleSubsequenceDP(a):
    N = len(a)
    inc = [1] * N
    dec = [1] * N
    for i in range(N):
        for j in range(0, i):
            if a[i] > a[j]: inc[i] = max(inc[i], 1+dec[j])
            if a[i] < a[j]: dec[i] = max(dec[i], 1+inc[j])

    return max(max(inc), max(dec))
a = [2, 3, 4, 6, 1, 0, 4, 5, 9, 6, 8, 3, 7, 4]
print(wiggleSubsequenceLength(a))
print(wiggleSubsequenceDP(a))
