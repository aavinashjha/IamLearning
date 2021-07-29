"""
Height: Number of edges from leaf to node
Depth: Number of edges from root to node
DFS: Each subtree is visited completely before moving to next subtree
     - Left Subtree, Node Itself, Right Subtree: 3! = 6 ways, but we consider left child first, thatswhy 3
     - Stack
BFS: Level Order
     - Queue
"""
from collections import deque
class Queue:
    def __init__(self):
        self.q = deque()

    def enqueue(self, x):
        self.q.append(x)

    def dequeue(self):
        return self.q.popleft()

    def isEmpty(self):
        return len(self.q) == 0

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return "Node <{}>".format(self.data)

class BST:
    def __init__(self):
        self.root = None

    def search(self, data):
        def find(root):
            if not root: return
            if data == root.data: return root
            elif data < root.data: return find(root.left)
            else: return find(root.right)
        return find(self.root)

    def insert(self, data):
        def ins(root):
            if not root: return Node(data)
            if data < root.data: root.left = ins(root.left)
            else: root.right = ins(root.right)
            return root

        self.root = ins(self.root)

    def preorder(self):
        traverse = list()
        def preodr(root):
            if not root: return
            traverse.append(root.data)
            preodr(root.left)
            preodr(root.right)
        preodr(self.root)
        return traverse

    def inorder(self):
        traverse = list()
        def inodr(root):
            if not root: return
            inodr(root.left)
            traverse.append(root.data)
            inodr(root.right)
        inodr(self.root)
        return traverse

    def postorder(self):
        traverse = list()
        def postodr(root):
            if not root: return
            postodr(root.left)
            postodr(root.right)
            traverse.append(root.data)
        postodr(self.root)
        return traverse

    def level(self):
        traverse = list()
        if not self.root: return
        q = Queue()
        q.enqueue(self.root)

        while not q.isEmpty():
            node = q.dequeue()
            traverse.append(node.data)
            if node.left: q.enqueue(node.left)
            if node.right: q.enqueue(node.right)

        return traverse

bst = BST()
"""
bst.insert(4)
bst.insert(2)
bst.insert(5)
bst.insert(1)
"""
bst.insert('F')
bst.insert('D')
bst.insert('J')
bst.insert('B')
bst.insert('E')
bst.insert('G')
bst.insert('K')
bst.insert('A')
bst.insert('C')
bst.insert('I')
bst.insert('H')

print("Preorder: {}".format(bst.preorder()))
print("Inorder: {}".format(bst.inorder()))
print("Postorder: {}".format(bst.postorder()))
print("Level: {}".format(bst.level()))
print("Search: X - {}".format(bst.search('X')))
print("Search: G - {}".format(bst.search('G')))
"""
print("Search: 6 - {}".format(bst.search(6)))
print("Search: 5 - {}".format(bst.search(5)))
"""
