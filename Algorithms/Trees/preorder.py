# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Stack:
    def __init__(self):
        self.s = []
    def push(self, e):
        self.s.append(e)
    def pop(self):
        return self.s.pop()
    def empty(self):
        return len(self.s) == 0
    
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Preorder:
        root left right
        - append in sol root
        - 
        1
       2  3 
        
        """
        s = Stack()
        node = root
        t = []
        while node or not s.empty():
            while node:
                t.append(node.val)
                s.push(node)
                node = node.left
            
            node = s.pop()
            node = node.right
        return t
                
            
            
        
