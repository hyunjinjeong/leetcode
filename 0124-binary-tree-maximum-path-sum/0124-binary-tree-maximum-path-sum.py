# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = float("-inf")
        
        def dfs(node):
            if not node:
                return 0
            
            # -인 경우 대비해서 0
            left_max = max(dfs(node.left), 0)
            right_max = max(dfs(node.right), 0)
            
            curr_max = node.val + left_max + right_max
            self.ans = max(self.ans, curr_max)
            
            # 현재 노드를 포함해서 올려야 함.
            return node.val + max(left_max, right_max)
        
        dfs(root)
        return self.ans