"""
Its like inserting the card at correct place
I: Unsorted input
S: Sorted array
Invariant: Maintain S sorted
Compare elements to previous elements starting from right side of S and not left
As S has sorted list, if element is greater than S's rightest element, we need just one comparison
Otherwise we just move left

-------------------
|         |       |
-------------------
     <--  j i-->

Like we are placing cards i correct order
0 1 3 4    2
We start comparing 2 with 4, if its less we continue
If we reach to a point where current j is less than value at i
We insert our card at j+1 place

Time Complexity:
    In worst case we need to move j from i-1 to 0, in that case complexity would be O(n^2)
    But if thats not the case then Insertion Sort could run in O(n) time
    So if inversions are less than it becomes linear algorithm
"""

def sort(a):
    N = len(a)

    for i in range(N): # The first unsorted element
        for j in range(i-1, -1, -1): # The last sorted element
            if a[i] > a[j]:
                a[i], a[j+1] = a[j+1], a[i]
                break

a = [1, 4, 0, 2, 5, 3]
print('Input', a)
sort(a)
print(a)

