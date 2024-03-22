# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        tree_str = []
        
        def dfs(node):
            if not node:
                return
            
            tree_str.append(str(node.val))
            
            if not node.left and not node.right:
                return
            
            tree_str.append("(")
            dfs(node.left)
            tree_str.append(")")
            
            if node.right:
                tree_str.append("(")
                dfs(node.right)
                tree_str.append(")")
        
        dfs(root)
        return "".join(tree_str)