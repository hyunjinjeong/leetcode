# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # 뭔가 자식 tree를 어떻게 재활용할 수 있을 것 같은디
        # 일단 brute force 버전
        def dfs(node):
            if not node:
                return
            
            validate(node, 0)
            dfs(node.left)
            dfs(node.right)
            
        def validate(node, curr_sum):
            if not node:
                return
            
            if curr_sum + node.val == targetSum:
                self.ans += 1
            
            validate(node.left, curr_sum + node.val)
            validate(node.right, curr_sum + node.val)
            
        self.ans = 0
        dfs(root)
        return self.ans