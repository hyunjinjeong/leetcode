# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        # postorder로 돌기?
        
        def dfs(node):
            if not (node.left or node.right):
                return node.val == target
            
            if node.left:
                delete_left = dfs(node.left)
                if delete_left:
                    node.left = None
            if node.right:
                delete_right = dfs(node.right)
                if delete_right:
                    node.right = None
            
            if not (node.left or node.right):
                return node.val == target
            else:
                return False
        
        dfs(root)
        # root는 따로 처리
        if not (root.left or root.right) and root.val == target:
            return None
        return root