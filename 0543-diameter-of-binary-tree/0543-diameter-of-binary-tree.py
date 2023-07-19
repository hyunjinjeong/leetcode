# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # 재귀로 하면 쉬운데..
        def dfs(node, height):
            if not node:
                return height
            
            left, right = dfs(node.left, height), dfs(node.right, height)
            diameter = (left - height) + (right - height)
            self.ans = max(diameter, self.ans)
            
            return max(left, right) + 1
        
        self.ans = 0
        dfs(root, 0)
        return self.ans