"""
Numbers ranging from 1..n
n+1 places
Atleast one duplicate
[1, 3, 4, 2, 4]
Idea:
    - O(n^2)  - one by one comparison
    - O(nlogn) - inplace we don't want to modify input
    - Pigeonhole principle
    - One hole would be there, which have 2 pigeons
    - distinct integers + 1 = integers
    - Base case single element could not be duplicate
"""
def duplicate(array):
    N = len(array)

    l, r = 1, N-1
    def scan(low, high): #N
        count = 0
        for e in array:
            if e >= low and e <= high:
                count += 1
        return high-low+1 < count # duplicates

    while l < r: # Dividing the problem in half eveytime logN
        m = l+((r-l)//2)
        if scan(l, m):
            r = m
        else:
            l = m+1
    return l
array=[1,3,4,2,4]
#array=[1,3,4,2,7,4, 5, 6]
array=[1,3,4,2,7,5, 5, 6]
print(duplicate(array))
"""
1 3 4 2 7 4 5 6

1 2 3 4 5 6 7

"""

            
        

