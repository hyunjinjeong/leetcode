# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(l, r):
            if not l and not r:
                return None
            if l and not r:
                return l
            if not l and r:
                return r
            
            node = TreeNode(l.val + r.val)
            node.left = dfs(l.left, r.left)
            node.right = dfs(l.right, r.right)
            return node
    
        return dfs(root1, root2)