# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # dfs로 될 듯?
        self.ans = float("-inf")
        self.dfs(root)
        return self.ans
            
    def dfs(self, node):
        if not node:
            return 0
        
        # -인 경우 해당 경로를 버리는게 좋으므로 0으로.
        left_max = max(self.dfs(node.left), 0)
        right_max = max(self.dfs(node.right), 0)

        self.ans = max(left_max + right_max + node.val, self.ans)
        # 위로 올려보낼 때는 더 큰 path를 선택해야 함
        return max(left_max, right_max) + node.val
