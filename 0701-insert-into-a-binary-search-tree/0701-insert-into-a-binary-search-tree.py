# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        node = root
        prev = None
        
        while node:
            prev = node
            if node.val <= val:
                node = node.right
            else:
                node = node.left

        if prev.val >= val:
            prev.left = TreeNode(val)
        else:
            prev.right = TreeNode(val)

        return root