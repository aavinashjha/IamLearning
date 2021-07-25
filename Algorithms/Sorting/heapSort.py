"""
Not inplace
"""
import heapq

def sort(a):
    h = a[:]
    heapq.heapify(h)

    index = 0
    while h:
        a[index] = heapq.heappop(h)
        index += 1

a = [1, 3, 4, 2, 0]
print('Input', a)
sort(a)
print(a)
