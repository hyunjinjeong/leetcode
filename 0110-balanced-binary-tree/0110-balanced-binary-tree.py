# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.is_balanced = True
        
        def height(node, depth=0):
            if not node:
                return depth
            
            left_depth, right_depth = height(node.left, depth+1), height(node.right, depth+1)
            if abs(left_depth - right_depth) > 1:
                self.is_balanced = False
            
            return max(left_depth, right_depth)
        
        height(root)
        
        return self.is_balanced