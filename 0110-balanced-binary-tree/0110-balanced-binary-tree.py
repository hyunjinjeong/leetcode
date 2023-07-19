# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def height(node):
            if not node:
                return -1
            
            left, right = height(node.left), height(node.right)
            if abs(right - left) >= 2:
                self.ans = False
            
            return max(left, right) + 1
        
        self.ans = True
        height(root)
        return self.ans