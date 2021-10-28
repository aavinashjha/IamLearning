class Stack:
    def __init__(self):
        self.s = list()
    
    def push(self, e):
        self.s.append(e)
    
    def pop(self):
        return self.s.pop()
    
    def empty(self):
        return len(self.s) == 0
    
    def top(self):
        return self.s[-1]
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
  1
2   3  
  
"""
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        while curr and no stack empty:
        - keep pushing left
        - if node has no right, discover it
        - popped element is right child of top of stack - then pop top of stack as well
        - else visit right side of tree
        
        
        """
        s = Stack()
        curr = root
        t = []
        while curr or not s.empty():
            while curr:
                s.push(curr)
                curr = curr.left
        
            if s.top().right is not None:
                curr = s.top().right
            else:
                popped = s.pop()
                t.append(popped.val)
                while not s.empty() and s.top().right == popped:
                    popped = s.pop()
                    t.append(popped.val)
        
        return t
    
        s = Stack()
        if root: s.push(root)
        t = Stack()
        while not s.empty():
            node = s.pop()
            t.push(node.val)
            
            if node.left:
                s.push(node.left)
            
            if node.right:
                s.push(node.right)
        
        sol = []
        while not t.empty():
            sol.append(t.pop())
        return sol
