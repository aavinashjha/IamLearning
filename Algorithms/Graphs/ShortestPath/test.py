import heapq
a=[(4, 'a'), (5, 'b'), (2, 'c'), (6, 'd')]
print(a)
heapq.heapify(a)
while a:
    print(heapq.heappop(a))

