# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, prev_sum):
            if not node:
                return
            
            curr_sum = prev_sum * 10 + node.val
            if node.left and node.right:
                dfs(node.left, curr_sum)
                dfs(node.right, curr_sum)
            elif node.left:
                dfs(node.left, curr_sum)
            elif node.right:
                dfs(node.right, curr_sum)
            else:
                self.res += curr_sum

        self.res = 0
        dfs(root, 0)
        return self.res