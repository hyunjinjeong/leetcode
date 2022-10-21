# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, curr_depth):
            if not node:
                return curr_depth
            
            return max(dfs(node.left, curr_depth), dfs(node.right, curr_depth)) + 1
        
        return dfs(root, 0)
            