"""
nums: have n+1 integers
value is 1..n
one repeated number in nums
1 3 4 2 2
1 4 3 2 2
1 2 3 4 2
"""
a=[1,3,4,2,2]
def duplicate(a):
    N = len(a)
    i = 0
    while i < N:
        val = a[i]
        index = val-1

        if i == index: 
            i += 1
        elif a[i] == a[index]:
            return a[i]
        else:
            a[i], a[index] = a[index], a[i]

    #for i in range(N):
    #    if i != a[i]-1:
    #        return a[i]

print(a)
print(duplicate(a))
