"""
Rolling Hash ADT
- r.append(c) - add character to end of X
- r.popleft() / r.skip(c) - delete first character of X (assuming it is c)
- r() - hash value of X = h(X)
These have to be done in constant time

Karp-Rabin algorithm:
- for c in P: rp.append(c)
- for c in T[:len(P)]: rt.append(c)
- for i in range(len(P), len(T)):
    rt.skip(T[i-len(P)])
    rt.append(T[i])
    if rp == rt:...

Hash values are equal, doesn't mean string themselves are equal
because there are collisions and distinct strings also map to same
column

check whether P == T[i-len(P)+1: i+1] 
- compare them character by character
if equal:
    found match # O(P)
else:
    happens with probability <= 1/|P|

O(|P|+|T|+ #match.|P|)

- Hashing will not be 100% deterministically correct
- Rolling hash/Recursive hashing/Rolling 

We can use random prime > |P|
and division method should also work
h(k) = k mod m where m is random prime >= |P|

Treat X as a multi digit number in base a - alphabet size
"""
class RollingHash:
    m = 100001
    p = 29 
    def __init__(self, s):
        self.s = [c for c in s]
        self.start = 0
        self.N = len(s)
        self.h = None
        self.ppow = dict()

    def integer(self, x):
        return ord(x)-ord('a') +1

    def ppower(self, N):
        self.ppow[0] = 1
        for i in range(1, N+1):
            self.ppow[i] = RollingHash.p * self.ppow[i-1]

    def pow(self, i):
        return self.ppow[i]

    def rehash(self, s):
        N, h = len(s), 0
        for i in range(N):
            h += (self.pow(i) * self.integer(s[self.N-i-1]))
            h %= RollingHash.m
        return h

    def hash(self):
        if not self.h:
            self.ppower(self.N)
            self.h = self.rehash(self.s)
        return self.h

    def append(self, c):
        print('Appending {} - {}'.format(c, self.h))
        self.s.append(c)
        self.h = RollingHash.p * self.h + self.integer(c)
        self.h %= RollingHash.m
        print('{} Appended {} - {}'.format(self.s[self.start:], c, self.h))

    def skip(self, c):
        print('Skipping {} - {}'.format(c, self.h))
        if c == self.s[self.start]:
            self.h -= self.pow(self.N) * self.integer(self.s[self.start])
            self.h %= RollingHash.m
            self.start += 1
        else:
            print("Wrong skip")
        print('{} Skipped {} - {}'.format(self.s[self.start:], c, self.h))

class RabinKarp:
    def __init__(self, T, P):
        print("Text: {}, Pattern: {}".format(T, P))
        self.M, self.N = len(P), len(T)
        self.T, self.P = T, P
        self.rp = RollingHash(self.P)
        print('Pattern Hash: {}'.format(self.rp.hash()))
        self.rt = RollingHash(self.T[0: self.M])


    def equal(self, s1, s2):
        print("Equal: {} and {}".format(s1, s2))
        M, N = len(s1), len(s2)
        if M != N: return False

        for i in range(M):
            if s1[i] != s2[i]:
                return False
        return True

    def find(self):
        for s in range(1, self.N-self.M+1):
            if self.rt.hash() == self.rp.hash():
                print('Hash matched at index: {}'.format(s-1))
                # It could be collision check it for exact match
                if self.equal(self.T[s-1: s+self.M-1], self.P):
                    return s-1 
            self.rt.append(T[s+self.M-1])
            self.rt.skip(T[s-1])
        if self.rt.hash() == self.rp.hash():
            print('Hash matched at index: {}'.format(s-1))
            # It could be collision check it for exact match
            if self.equal(self.T[s-1: s+self.M-1], self.P):
                return s-1 

        return -1

P = "bcd"
T = "aacbcde"

rk = RabinKarp(T, P)
print(rk.find())
    

P = "bcde"
T = "abcdef"

rk = RabinKarp(T, P)
print(rk.find())
    
P = "bca"
T = "abcde"

rk = RabinKarp(T, P)
print(rk.find())
    
