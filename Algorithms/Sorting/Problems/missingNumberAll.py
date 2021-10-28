"""
range is from 1 to n

4 3 2 7 8 2 3 1
8 3 2 7 4 2 3 1
8 3 2 7 4 2 3 1
8 7 2 3 4 2 3 1
8 1 2 3 4 2 3 7
8 1 2 3 4 2 3 7

"""
a = [4,3,2,7,8,2,3,1]

def missingAll(a):
    n = max(a)
    N = len(a)

    for i in range(N):
        val = a[i]
        index = val

        if i == index or index > N-1 or a[i] == a[index]:
            i += 1
        else:
            a[i], a[index] = a[index], a[i]

    print(a)
    sol = []
    for i in range(1, N):
        if i != a[i]:
            sol.append(i)
    return sol

print(a)
print(missingAll(a))
