# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            
            if self.prev is p and not self.res:
                self.res = node
                return
            self.prev = node

            inorder(node.right)

        self.prev = None
        self.res = None

        inorder(root)
        return self.res