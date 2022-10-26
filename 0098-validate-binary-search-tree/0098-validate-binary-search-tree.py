# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # BST면 inorder로 돌아서 항상 val[i] < val[i+1] 이면 된다.
        vals = []
        def in_order(node):
            if not node:
                return
            
            in_order(node.left)
            vals.append(node.val)
            in_order(node.right)
        
        in_order(root)
        for i in range(len(vals)-1):
            if vals[i] >= vals[i+1]:
                return False
        
        return True