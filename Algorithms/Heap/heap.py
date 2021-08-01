class Heap:
    def __init__(self, A):
        self.A = A
        self.N = len(A)

    def parent(self, i):
        return (i-1)//2

    def left(self, i):
        return 2*i + 1

    def right(self, i):
        return 2*i + 2

    def maxHeapify(self, i):
        """
        Down heap bubbling
        T(n) <= T(2n/3) + O(1)
        at(n/b)
        a = 1, b = 3/2
        n^logb(a) = n^log1 = 1
        O(lgN)
        """
        l, r = self.left(i), self.right(i)
        largest = i
        if l < self.N and self.A[l] > self.A[largest]: largest = l
        if r < self.N and self.A[r] > self.A[largest]: largest = r
        if largest != i:
            self.A[r], self.A[i] = self.A[i], self.A[r]
            self.maxHeapify(largest)


    def buildMaxHeap(self):
        """
        Complete Binary Tree: Leaves are N/2
        Partial complete binary tree: leaves < N/2 but internal nodes are N/2

        We are going bottom up as that will enable us to asympotically perform
        maxHeapify in O(lgN) and not O(N)
        """
        for i in range(self.N//2-1, -1, -1):
            self.maxHeapify(i)

    def maximum(self):
        return self.A[0]

    def sort(self):
        self.buildMaxHeap()
        for i in range(self.N):
            self.A[0], self.A[self.N-1-i] = self.A[self.N-1-i], self.A[0]
            self.N -= 1
            self.maxHeapify(0)

    def increaseKey(self, i, key):
        """
        Increase the value pf i's key to the new key, which is assumed to be
        atleast as larage as i's current key value
        In maximum we only increase and not decrease
        Because of increase in a node, its parent might need to be validated
        as children will be still less as this key is bigger than the previous key
        """
        self.A[i] = key

        def bubbleUp(i):
            if i == 0: return # root is still maximum
            pi = self.parent(i)
            if self.A[i] > self.A[pi]:
                self.A[i], self.A[pi] = self.A[pi], self.A[i]
                bubbleUp(pi)

        bubbleUp(i)

    def insert(self, key):
        """
        - Add as last element
        - Bubble up (Up heap bubbling)
        - O(lgN)
        """
        self.A.append(float('-inf'))
        self.N += 1
        self.increaseKey(self.N-1, key)

    def delete(self):
        """
        - Down heap bubbling
        """
        self.A[0], self.A[self.N-1] = self.A[self.N-1], self.A[0]
        deleted = self.A[self.N-1]
        del self.A[self.N-1]
        self.N -= 1
        self.maxHeapify(0)
        return deleted

    def __str__(self):
        return " ".join([str(i) for i in self.A])


A= [3, 1, 4] 
h = Heap(A)
print('Before building max heap: {}'.format(h))
h.buildMaxHeap()
print('After building max heap: {}'.format(h))

hs = Heap(A)
hs.sort()
print('Sorted: {}'.format(hs))

h = Heap(A)
h.buildMaxHeap()
print('Max heap before insertion: {}'.format(h))
h.insert(5)
print('Max heap after insertion: {}'.format(h))

h = Heap(A)
h.buildMaxHeap()
print('Max heap before deletion: {}'.format(h))
deleted = h.delete()
print("Deleted: {}".format(deleted))
print('Max heap after deletion: {}'.format(h))
