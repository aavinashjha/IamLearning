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
    def top(self):
        return self.s[-1]
    
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Idea:
        - left, root, right
        - Root would be visited after every left element
        - Root could be pushed in
        - If no left then pop root
        
        
        2 3
        
          1
        2   3  
        """
        s = Stack()
        node = root
        t = []
        while node or not s.empty():
            while node:
                s.push(node)
                node = node.left
                
            node = s.pop()
            t.append(node.val)
            node = node.right
                
        return t
        
