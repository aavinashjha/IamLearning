"""
Set mismatch
All numbers from 1 to n
[1,2,2,4]

"""
def mismatch(a):
    n = len(a)
    i = 0
    while i < n:
        val = a[i]
        index = val-1

        if i == index:
            i += 1
        elif a[i] == a[index]:
            return [i+1, a[i]]
        else:
            a[i], a[index] = a[index], a[i]
a=[1,2,2,4]
print(a)
print(mismatch(a))
