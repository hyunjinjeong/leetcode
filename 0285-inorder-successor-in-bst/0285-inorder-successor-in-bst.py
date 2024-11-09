# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        
        # def leftmost(node):
        #     if node.left:
        #         return leftmost(node.left)
        #     return node

        # def find_parent(node):
        #     if not node:
        #         return
            
        #     if node.left is p or node.right is p:
        #         return node
            
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            
            if self.prev is p:
                self.res = node
                return
            self.prev = node

            inorder(node.right)

        self.prev = None
        self.res = None

        inorder(root)
        return self.res