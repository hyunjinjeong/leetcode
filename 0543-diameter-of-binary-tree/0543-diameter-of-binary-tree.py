# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.answer = 0
        
        def depth(node):
            if not node:
                return -1
            
            left_depth, right_depth = depth(node.left), depth(node.right)
            self.answer = max(self.answer, left_depth + right_depth + 2) # node->left, node->right 때문에 2
            return max(left_depth, right_depth) + 1
        
        depth(root)
            
        return self.answer