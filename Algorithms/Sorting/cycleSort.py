"""
When numbers given in range 1..n use cyclic sort
index = value -1 in sorted array
Each unique elements is swapped once so O(N)
Only n-1 swaps as nth will be at correct place
n-1+n = 2n-1

When all needs to be found do a second pass on sorted array
"""
def cyclicSort(a):
    N, i = len(a), 0
    while i < N:
        # Value should be at index value-1 i.e. value 1 should be at index 0
        val = a[i]
        index = val-1
        if index == i:
            i += 1
        else:
            a[i], a[index] = a[index], a[i]

a=[3,4,1,2,5]
print(a)
cyclicSort(a)
print(a)
