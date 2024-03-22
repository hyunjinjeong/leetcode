# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(node, curr_sum):
            if not node:
                return False
            
            if curr_sum + node.val == targetSum and node.left is None and node.right is None:
                return True
            
            return dfs(node.left, curr_sum + node.val) or dfs(node.right, curr_sum + node.val)
        
        return dfs(root, 0)