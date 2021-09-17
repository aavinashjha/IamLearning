"""
In place partition:
- In place
- maintain two indexes
- left of i less
- right of i more than pivot
- j unprocessed
- initially j is at 1
- i is at 0
- as a[j] is more than pivot, increment j
- if a[j] is less increment i and j
[3, 2, 1, 4, 5]
       i     j

"""
def partition(a):
    N = len(a)
    if N <= 1: return # Already sorted
    # Division, Mover

    d, pivot = 0, a[0]  

    for m in range(1, N):
        if a[m] < pivot:
            d += 1
            a[d], a[m] = a[m], a[d]
        print(a)

    a[d], a[0] = a[0], a[d]
"""
a=[3,2,1,4,5]
partition(a)
print(a)

a=[4,2,1,3,5]
partition(a)
print(a)
"""
a = [3, 8, 2, 5, 1, 4, 7, 6]
partition(a)
print(a)

