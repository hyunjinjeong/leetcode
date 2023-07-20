# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.ans = False
        self.dfs(root, subRoot)
        return self.ans
    
    def dfs(self, root, subRoot):
        if not root:
            return
        
        if self.is_same(root, subRoot):
            self.ans = True
            return
        
        self.dfs(root.left, subRoot)
        self.dfs(root.right, subRoot)
        
    def is_same(self, n1, n2):
        if not n1 and not n2:
            return True
        if n1 and not n2:
            return False
        if not n1 and n2:
            return False
        
        if n1.val != n2.val:
            return False
        return self.is_same(n1.left, n2.left) and self.is_same(n1.right, n2.right)