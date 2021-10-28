"""
Drawbacks of naive approach:
    - Worst time complexity: O(nm) for repetitive characters
    - Backup: In many applications we want to backup in text stream
      > Treat input as stream of data
      > Abstract model: standard input
      Brute force algorithm needs backup for very mismatch
      M characters need to be backed up for compaison to occur but can be issue if M is large
"""
def naive(s, p):
    # MN char compare
    # Slow if text and pattern are repetitive

    print(s, p)
    N, M = len(s), len(p)

    for i in range(N-M+1):
        for j in range(M):
            if s[i+j] != p[j]: break
            if j == M-1: return i
    return -1

def kmp(s, p):

    def failure(pat):
        M = len(pat)
        f, p = [0], 0
        
        # ending at r i.e. suffix
        for s in range(1, M):
            if pat[s] == pat[p]:
                p += 1
                # suffix is incremented in main loop
            else:
                p = 0
            f.append(p)
        return f

    M, N = len(p), len(s)

    j = 0
    ff = failure(p)
    for i in range(N):
        if s[i] == p[j]:
            j += 1
            if j == M: return i-M+1
        else:
            j = ff[j-1]

    return -1

s = "adacadabrac"
p = "abra"
print(naive(s, p))
print(kmp(s, p))

