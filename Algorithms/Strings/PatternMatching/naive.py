"""
Heuristics:
    T: Text
    P: Pattern
    We want to search occurrence(s) of pattern in text

    
    The first approach which comes to mind is sliding window mechanism
    ----------------------------------------------------------
    |                         TEXT                           |
    |                                                        |
    ----------------------------------------------------------
    <------------------------N------------------------------->
    -----------------
    |   PATTERN     |
    |               |
    -----------------
    <------M-------->
    Start with a character in T and match with char in P.
    Start with a character in T and match with char in P.
    if match occurs - increment char pointers for both T and P
    if mismatch occurs - reset char pointer for P and start with next char in T

    Worst Case: T: aaa..b (all a's with b as last char)
                P: aaa..b (very less a's but similar)
                What will happen in this case is we compare 1..m-1 chars where there is match and mth char is mismatch
                so we start again from 2..m chars where and m+1 th is a mismatch
                Therfore for every char in T we do m comparions with P
                (n-m+1) * m comparisons = O(nm)
"""
def match(T, P):
    N, M = len(T), len(P)
    for i in range(N-M+1):
        j = 0
        while T[i+j] == P[j]:
            if j == M-1:
                return i
            j += 1

    return -1

print(match("aaaaaaaab", "aab"))
print(match("aaaaxaaab", "axab"))
    
