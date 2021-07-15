def stringMult(a, b):
    N, M = len(a), len(b)

    sol = [0] * (N + M)
    a = a[::-1]
    b = b[::-1]
    for i in range(N):
        for j in range(M):
            sol[i+j] += (int(a[i]) * int(b[j]))# Single digit multiplication is allowed
            sol[i+j+1] += (sol[i+j] // 10)
            sol[i+j] %= 10

    sol.reverse()
    beg = 0 
    while True:
        if sol[beg] != 0: break
        beg += 1

    res = map(str, sol[beg:])
    return "".join(res)


print(stringMult("12", "11"))
#print(stringMult("123", "456"))
print(stringMult("456", "123"))



