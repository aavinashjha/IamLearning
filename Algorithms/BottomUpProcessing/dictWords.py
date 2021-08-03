"""
Dictionary words = [abc, abca, de]
s = abcade
Goal: Need to find if s could be split into words of dictionary
Constraints: All the letters should be considered
             We should not select greedy first word as that might lead to no solution
             For example: If abc is considered, then ade is not present in words
                          but if abca is considered then de is present
             Assume that duplicates could be used
Idea:
    1) We can start searching for a word, if word is found start looking for other word
       - Not work for all cases
    2) Split at every portion and check recursively if that will work O(2^n)
    3) Consider each anagram and check recursively if it satisfies
    P(0, N-1) = Possibility that entire string is formed by joining words of dict

    P(i, j) = P(i, k) and P(k+1, j) where i < k < j
    P(0, 5) = P(0, 0) and P(1, 5) = a and bcade
              P(0, 1) and P(2, 5) = ab and cade
              P(0, 2) and P(3, 5) = abc and ade
              P(0, 3) and P(4, 5) = abca and de
              P(0, 4) and P(5, 5) = abcad and e

    P(i, j): Possibility of forming string from i to j index (both included) with the words in dictionary
             This could have multiple words in itself
    P(0, N-1) = This is what needs to be found
    Consider an index k if P(i, k) and P(k+1, j) is possible then P(i, j) is possible
    We want to start from smaller lengths and then continue to larger lengths

    P(0, 5) = P(0, 3) and P(4, 5)
    that is we should solve every subproblem

    Solve problems for all possible indexes for all lengths

    Length 1: P(0, 0), P(1, 1) ...P(5, 5) [start: 0..len-1]
    Length 2: P(0, 1), P(1, 2) ...P(4, 5) [start: 0..len-2]
    Length 6: P(0, 5)                      [start: 0..len-6]

    P(0, 1) = P(0, 0) + P(1, 1)
    P(0, 2) = P(0, 0) + P(1, 1) + P(2, 2)
              P(0, 1) + P(2, 2)
              P(0, 2)
    For every subproblem we are dependent on more subproblems
    If subproblem is not earlier solved: solve it

    P(0, 5) = P(0,4) + P(4, 4)
      0 1 2 3 4 5
      a b c a d e
    a F F T T F 
    b   F F F F F  
    c     F F F F
    a       F F F
    d         F T
    e           F

    Current character is present in dict: than what is in previous j-1
    Current charcater not present in dict: check (i, j)
"""
def possible(words, s):
    words1, N, P = set(words), len(s), dict()
    print(s, words)
    length = 1 # Subproblem Length

    def check(i, j):
        p = False
        for k in range(i, j+1): # Where to split
            first = P[(i, k)] if (i, k) in P else (not s[i: k+1] or s[i: k+1] in words)
            second = P[(k+1, j)] if (k+1, j) in P else (not s[k+1: j+1] or s[k+1: j+1] in words)
            # We have solved smaller problems thatsehy this would already be present
            p =  first and second
            if p: break # No need to check other ways as we are aware this is possible
        P[(i, j)] = p

    while length <= N:
        for i in range(N-length+1):
            j = i+length-1
            if (i, j) not in P: check(i, j)

        length += 1

    return P[(0, N-1)]
words = ["abc", "abca", "de"]
words = ["abc", "de"]
words = ["abc", "de", "a"]
s = "abcade"
print(possible(words, s))
