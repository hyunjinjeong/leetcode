# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def is_same(arr1, arr2):
            if len(arr1) != len(arr2):
                return False
            
            for item1, item2 in zip(arr1, arr2):
                if item1 != item2:
                    return False
            
            return True
        
        def get_leaves(node):
            if not node:
                return []
            
            if not node.left and not node.right:
                return get_leaves(node.left) + [node.val] + get_leaves(node.right)
            else:
                return get_leaves(node.left) + get_leaves(node.right)
        
        leaves1, leaves2 = get_leaves(root1), get_leaves(root2)
        return is_same(leaves1, leaves2)