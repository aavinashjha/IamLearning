"""
Select the minimum and place it at the last place of unsorted array
I: unsorted input
S: Sorted array
Inplace
Removing from unsorted array and placing in sorted array
Using same array initial half to store sorted array, hence inplace
"""

def sort(a):
    N = len(a)

    def findMin(a, lo, hi): # both inclusive
        minimum, minIndex = float('inf'), -1
        for j in range(lo, hi+1):
            if a[j] < minimum:
                minimum = a[j]
                minIndex = j
        return minIndex, minimum

    for i in range(N): # Till i we have array already sorted
        minIndex, minimum = findMin(a, i, N-1)
        a[i], a[minIndex] = a[minIndex], a[i]

a = [1, 4, 2, 0, 5, 3]
print('Input', a)
sort(a)
print(a)


