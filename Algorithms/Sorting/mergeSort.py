"""
- Divide array into half
- Merge in sorted order
- Single element is always sorted: Base Case

Time Complexity:
    - MergeSort uses at most NlgN compares and 6NlgN array accesses to sort any array of size N
    - C(N) <= C(ceil(N/2)) + C(ceil(N/2)) + N for N>1 with C(1) = 0
    - A(N) <= A(ceil(N/2)) + A(ceil(N/2)) + 6N for N>1 with A(1) = 0
Improvements:
    - Use a cutoff value below that use insertion sort (avoid recursive calls)
    - While merging do nothing if The biggest item in first half is less than or equal to smallest item in second half
Already sorted array:
    - Comapirisons made are: 1/2 nlogn and optimized version a[mid] <= a[mid+1] makes n-1 comparisons

"""

def merge(a, aux, lo, mid, hi):
    # a[lo..mid]: Already sorted
    # a[mid+1..high]: Already sorted
    # Maintains original copy, a is updated

    for k in range(lo, hi+1):
        aux[k] = a[k]

    #if aux[mid] <= aux[mid+1]: return

    i, j = lo, mid+1

    for k in range(lo, hi+1):
        if i > mid: # All elements of left half are exhausted
            a[k] = aux[j]
            j += 1
        elif j > hi:
            a[k] = aux[i]
            i += 1
        elif aux[i] <= aux[j]:
            a[k] = aux[i]
            i += 1
        else: # aux[j] < aux[i]
            a[k] = aux[j]
            j += 1

def sort(array, aux, lo, hi):
    if hi <= lo: return

    mid = lo + (hi-lo)//2

    sort(array, aux, lo, mid)
    sort(array, aux, mid+1, hi)

    # The biggest item in first half is less than or equal to smallest item in second half
    merge(array, aux, lo, mid, hi)

def mergeSort(array):
    aux = [-1] * len(array)
    sort(array, aux, 0, len(array)-1)

def bottomUpMergeSort(array):
    N = len(array)
    aux = [-1] * N
    size = 1
    while size < N:
        for lo in range(0, N-size+1, size):
            mid, hi = lo+size, min(lo+2*size, N-1)
            merge(array, aux, lo, mid, hi)
        size += size

array = [3, 4, 1, 2, 5]
mergeSort(array)
print(array)

array = [3, 4, 1, 2, 5]
bottomUpMergeSort(array)
print(array)
