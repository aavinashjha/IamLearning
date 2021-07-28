import math
def primes(n):
    p = [True] * (n+1) # Initially all are primes
    for m in range(2, int(math.ceil(math.sqrt(n)))):
        if not p[i]: continue
        for i in range(m, n+1, m):
            p[i] = False

    p[0] = False
    p[1] = False
    print(p)
    return [i for i in range(n) if p[i]]

print(primes(16))
print(primes(20))
