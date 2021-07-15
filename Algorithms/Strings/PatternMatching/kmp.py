"""
Knuth Morris Prat
Heuristics:
    - Whenever there is a mismatch between T and P, we reset our pointer in text
    string to next character from where we started last time. For instance:
    i   0 1 2 3 4 5 6 7 8 9 10 11 12  13 14
    T = b a c b a b a b a a b  c  b   a  b
    P =         a b a b a c a
                          ^
                          |
                       mismatch

    - At index 9 of T there is a mismatch 
    In next iteration we have option to start comparing from index 5 i.e. prevIndex + 1
    But that is an extra work because we know the comparisons were succesfull till i-1
    and is violated only on index i.
    - If all characters are unique in pattern, then we know that if earlier comparisons were
    successfull, comparing this time with shifted comparisons will fail and now we can start
    comparing from index where mismatch occurred.
    
    - But what if current failure index is after some prefix in pattern, we need to consider that as well
    For example: if there are multiple a's in pattern and a at index 4 in text matched with pattern's first a
    , if pattern is shifted it will match with index at 6 or 8 or 9.
    This algorithm avoids restarting comparisons/rollback to prevStart+1 and sees if we could skip some comparisions.

    a b a b a c a
    0 0 1 2 3 0 1
        k   q          match
          k   q        mismatch


    Prefix function
    pi(i) = Length of proper prefix which is also suffix
    pi(i+1) <= pi(i) + 1
    Atmost increase by 1

    Two finger approach:
    - k at left side, takes care of prefix 
    - q at right side, takes care of suffix
    - if equal increment both pointers
    - if unequal rollback

    Observations about k:
        - At start its 0, increments in else statement, at most increase m-1, no. of times loop executes
        - q increments every iteration, but k not surely increments every iteration hence q > k
        - pi[q] = k < q, hence while loop decreases k
        - k > 0, never becomes negative
        - Total decrease in k from the while loop is bounded from above by total increase in k over all
          iterations of for loop, m-1
    
    Two finger approach:
    - p at left side, takes care of prefix 
    - s at right side, takes care of suffix
    - if equal increment both pointers
    - if unequal rollback

    Observations about p:
        - At start its 0, increments in else statement, at most increase M-1, no. of times loop executes
        - s increments every iteration, but p not surely increments every iteration hence s > p
        - pi[s] = p < s, hence while loop decreases p
        - p > 0, never becomes negative
        - Total decrease in p from the while loop is bounded from above by total increase in p over all
          iterations of for loop, M-1

    Prefix funxtion is also called failure function
    The value stored in the failure function means the current character is the ith character in a prefix of the pattern.

    a b a b x
    0 0 1 2 0
          |
          This value means that b is the 2nd character in prefix of pattern

    When there is a mismatch, we check the failure function to find the new index in the pattern where we will continue
    checking against the mismatched character in the text
"""
def failure(P):
    M = len(P)

    f, p = [0], 0 # For 0th element There is no prefix

    for s in range(1, M):
        if P[p] == P[s]:
            p += 1
        else:
            p = 0
        f.append(p)
    return f

def kmp(T, P):
    N, M = len(T), len(P)
    i, j, f = 0, 0, failure(P)

    print(f)
    while i < N:
        if T[i] == P[j]:
            i += 1
            j += 1
            if j == M: # Complete match
                return i-M
        elif j > 0: # Mismatch but we have advanced in the pattern
            # We know that this charcater is mismatch, but previous characters were a match
            # Hence we don't want to compare them again
            # Failure function stores the number of characters which are prefix
            # Lets say b has 2 value which means 2 characters are prefix and have matched
            # as previous to hitting this case all characters were matching
            # 0 and 1 index are matched and we want to start from 2
            # Hence char count is actually next index which we want to start matching
            j = f[j-1]
        else: # Mismatch but j is 0 we haven't advanced in P
            i += 1

    return -1

print(kmp("aaaaaaaab", "aab"))
print(kmp("aaaaxaaab", "axab"))
