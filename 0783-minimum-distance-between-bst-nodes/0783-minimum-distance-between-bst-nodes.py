# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        min_diff = float("inf")
        values = []
        
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            values.append(node.val)
            dfs(node.right)
        
        dfs(root)
        for i in range(1, len(values)):
            min_diff = min(values[i] - values[i-1], min_diff)
        
        return min_diff