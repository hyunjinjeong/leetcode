# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def is_same(n1, n2):
            if not n1 and not n2:
                return True
            if n1 and not n2:
                return False
            if not n1 and n2:
                return False
            if n1.val != n2.val:
                return False
            
            return is_same(n1.left, n2.left) and is_same(n1.right, n2.right)
        
#         s = [root]
#         while s:
#             n = s.pop()
#             if is_same(n, subRoot):
#                 return True
            
#             if n.left:
#                 s.append(n.left)
#             if n.right:
#                 s.append(n.right)
        
#         return False
        
        self.is_sub_tree = False
        def dfs(node):
            if not node or self.is_sub_tree:
                return
            
            if is_same(node, subRoot):
                self.is_sub_tree = True
                return
            
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        return self.is_sub_tree