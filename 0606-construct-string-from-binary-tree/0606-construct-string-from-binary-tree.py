# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def dfs(node, tree_str):
            if not node:
                return tree_str
            
            tree_str += str(node.val)
            if node.left and node.right:
                tree_str += f"({dfs(node.left, '')})"
                tree_str += f"({dfs(node.right, '')})"
            elif node.left:
                tree_str += f"({dfs(node.left, '')})"
            elif node.right:
                tree_str += "()"
                tree_str += f"({dfs(node.right, '')})"
            
            return tree_str
        
        return dfs(root, "")