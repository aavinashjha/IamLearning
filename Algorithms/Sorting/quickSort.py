"""
1) Shuffle the array
2) Choose the pivot element as the first element
3) Partition - Will bring pivot to correct place
4) Invariant: Elements on left of i are less than pivot, elemnents on the right of pivot are greater than pivot
     -1       N-1
      i       j
5) Elements sandwiched between i and j are yet to be sorted
6) After one partition pivot element is at correct place
7) Recursively partition

Consider first element as pivot, thatswhy start processing elements from lo+1
"""
def partition(a, lo, hi):

    pivot = a[lo]
    i, j = lo+1, hi

    while True:

        while i <= j and a[i] <= pivot:
            i += 1

        while i <= j and a[j] >= pivot:
            j -= 1

        if i > j: break
        a[i], a[j] = a[j], a[i]

    a[lo], a[j] = a[j], a[lo]

    return j

def sort(a, lo, hi):
    if lo > hi: return
    p = partition(a, lo, hi)
    sort(a, lo, p-1)
    sort(a, p+1, hi)

def quickSort(a):
    N = len(a)
    sort(a, 0, N-1)

a = [2, 5, 1, 4, 3, 6, 0]
print('Input', a)
quickSort(a)
print(a)

