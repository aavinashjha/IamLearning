"""
Boyer Moore:
    This algorithm scans the characters of pattern from right to left
    Two approaches: bad character and good suffix

    Bad Character: The character of the text which doesn't match with the current character of pattern is called bad character.

    Upon mismatch we shift the pattern until
    - The mismatch becomes a match: If mismatch occurs see bad match table for shifting the pattern
    - Pattern P move past the mismatch character: If the mismatch occur and the mismacth character not available in mismatch table

    Heuristics: Boyer Moore makes use of two heuristics to skip unnecessary comparisons between T and P
    - First is that we begin comparisons from the last character in the pattern instead of first character nad move backwards
    - Second if P character p mismatches with T character t, if t doesn't appear anywhere in the P then shift the pattern completely
      past t. Otherwise, shift the pattern to align t with the last occurrence of t in pattern

    0 1 2 3 4 5 6 7
    T E A M M A S T
   
    T 7 1
    E 6
    A 5 2
    M 4 5
    S 1

    0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
    W E L C O M E T O T E  A  M  M  A  S  T
   
    T E A M M A S T
                ^
                |
             Mismatch: i = 6, j = 6, i += 6
              T E A M M A  S  T
    
    T E A M S
    7 6 2 3 1 

     
       M
    <------>
    TEAMMAST
     ^
     |
    last
    M - last: will align E with E in text

    i
T = a a a a a a
P = b a a
    j
Align last a with T, but that will take other chars at negative index (hence minimum)
Boyer Moore is very fast on large alphabet (as compared to length of pattern)
Last Function: O(M + |Alphabets|)
Search: O(NM + |Alphabets|)
KMP recommended for binary strings
"""

class BadMatchTable:
    def __init__(self, P):
        self.M = len(P)
        self.P = P
        self.construct()

    def last(self, k):
        if k not in self.badMatch:
            return -1
        return self.badMatch[k]

    def construct(self):
        self.badMatch = dict()
        for i in range(self.M-1): # Last letter if not already defined is length else leave as it is
            self.badMatch[self.P[i]] = self.M-i-1
        if self.P[-1] not in self.badMatch:
            self.badMatch[self.P[-1]] = self.M

def BoyerMoore(T, P):
    N, M = len(T), len(P)
    tbl = BadMatchTable(P)

    i, j = M-1, M-1

    while i < N:
        if T[i] == P[j]:
            if j == 0:
                return i
            else:
                j -= 1
                i -= 1
        else:
            # Mismatch: if T[i] not present in table, increment i by M
            #           if present in table align it with T[i]
            i = i + M - min(j, 1+tbl.last(T[i]))
            j = M-1

    return -1


T = "WELCOMETOTEAMMAST"
P = "TEAMMAST"
print(BoyerMoore(T, P))
