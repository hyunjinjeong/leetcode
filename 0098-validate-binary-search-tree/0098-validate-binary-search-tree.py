# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # right의 최솟값이 node보다 커야 하고, left의 최댓값이 node보다 작아야 함
        def get_max(node):
            if not node:
                return float('-inf')
            return max(node.val, get_max(node.left), get_max(node.right))
            
            
        def get_min(node):
            if not node:
                return float('inf')
            return min(node.val, get_min(node.left), get_min(node.right))
        
        def dfs(node):
            if not node:
                return True
            
            if node.val <= get_max(node.left):
                return False
            if node.val >= get_min(node.right):
                return False
            
            return dfs(node.left) and dfs(node.right)
            
        return dfs(root)