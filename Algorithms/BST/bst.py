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

    def isValid(self):
        """
        node.left.data <= node.data
        node.right.data >= node.data
        This property should be satisfied by all nodes
        def IsBST(node):
            IsSubTreeLesser(node.left, node.data) &&
            IsSubTreeGreater(node.right, node.data) &&
            IsBST(node.left) && 
            IsBST(node.right) 

        O(N^2): As for every node we check all its left and right subtree
        Optimized approach: Use range
        Define valid range for each node recursively
        Entire subtree should be in that range
        This is an O(N) solution

        Other solution is to do Inorder traversal

        """

        def isBST(node, s, e): # Both inclusive
            if not node: return True # Empty tree is valid BST

            return node.data >= s and \
                    node.data <= e and \
                    isBST(node.left, s, node.data) and \
                    isBST(node.right, node.data, e)


        return isBST(self.root, float('-inf'), float('inf'))

    def isValidv2(self):
        """
        Do inorder traversal and whenever the previous element is not less than or equal
        to current element we could say its not binary seearch tree.
        """
        prev = None
        def inodr(node):
            if not node: return True

            if not inodr(node.left): return False

            nonlocal prev
            if prev and prev > node.data: return False
            prev = node.data

            if not inodr(node.right): return False
            return True

        return inodr(self.root)

    def inorderSuccessor(self, key):
        """
        When we have reached a node for which inorder successor have to be found,
        We have already traced all ancestors
        We need to find nearest ancestor for which node falls in left subtree to ancestor
        That could be also called deppest ancestor from root for which node is on left side
        That is how it would be next inorder traversal element

        Node with right subtree: Minimum in right subtree
        Node without right subtree:
          - Right child of parent: -1
          - Left child of parent: parent
        """
        def minimum(node):
            if not node: return
            if not node.left: return node

            return minimum(node.left)

        def succ_right(node):
            if not node: return
            if not node.right: return
            return minimum(node.right)

        def isucc(node):
            if not node: return

            if key == node.data:
                succ = succ_right(node)
            elif key < node.data:
                succ = isucc(node.left)
                if not succ: succ = node
            else:
                succ = isucc(node.right)

            return succ 

        succ = isucc(self.root)
        return succ.data if succ else -1

    def delete(self, key):
        """
        Leaf Node i.e. no left and right child: just set parent left or right to NULL

              B                                     B
             / \           Leaf Node               / \
            A   C           =======>              A   C
                 \
                  D

        Node with only one child: Just set parent's parent point to node's child
              B                                     B
             / \           Single Child            / \
            A   C           =======>              A   D
                 \
                  D

        Both children: Replace node with its immediate successor
                       Successor can have at most 1 children falling to previous case

              B                            C          C
             / \           Both Child     / \        / \
            A   C           =======>     A   C      A   D
                 \                            \ 
                  D                            D

        """
        def minimum(node):
            if not node: return
            while node.left:
                node = node.left
            return node

        def successor(node):
            if not node: return
            if not node.right: return
            return minimum(node.right)
            
        def delt(node, key):
            if not node: return node

            if node.data == key:
                if not node.left and not node.right: # Leaf node
                    node = None
                elif not node.left: # Only right child
                    node = node.right
                elif not node.right: # Only left child
                    node = node.left
                else: #both
                    """
                    Copy successor key to node
                    and recursively run delete on right node with successor key
                    to remove the duplicate
                    """
                    succ = successor(node)
                    node.data = succ.data
                    node.right = delt(node.right, succ.data)
            elif key < node.data:
                node.left = delt(node.left, key)
            else:
                node.right = delt(node.right, key)
            return node

        self.root = delt(self.root, key)


bst = BST()
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

bst = BST()
bst.insert(4)
bst.insert(2)
bst.insert(5)
bst.insert(1)

print("Valid BST: {}".format(bst.isValid()))
print("Valid BST V2: {}".format(bst.isValidv2()))

bst = BST()
bst.root = Node(4)
bst.root.left = Node(3)
bst.root.right = Node(6)
bst.root.left.right = Node(5)

"""
    4
   / \
  3   6
   \
    5
"""
print("Valid BST: {}".format(bst.isValid()))
print("Valid BST V2: {}".format(bst.isValidv2()))

bst = BST()
bst.insert('B')
bst.insert('A')
bst.insert('C')
bst.insert('D')
print("Inorder Before Deletion: {}".format(bst.inorder()))
#bst.delete('D') # Leaf
# bst.delete('C') # Single child
bst.delete('B') # Both child
print("Inorder Before After Deletion: {}".format(bst.inorder()))


bst = BST()
bst.insert('B')
bst.insert('A')
bst.insert('C')
bst.insert('D')
print("Inorder Successor: A: {}".format(bst.inorderSuccessor('A')))
print("Inorder Successor: B: {}".format(bst.inorderSuccessor('B')))
print("Inorder Successor: C: {}".format(bst.inorderSuccessor('C')))
print("Inorder Successor: D: {}".format(bst.inorderSuccessor('D')))


bst = BST()
bst.insert(15)
bst.insert(10)
bst.insert(8)
bst.insert(12)
bst.insert(6)
bst.insert(11)
bst.insert(20)
bst.insert(17)
bst.insert(16)
bst.insert(25)
bst.insert(28)
print("Inorder Successor: 12: {}".format(bst.inorderSuccessor(12)))
