# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #         # 1. 재귀
#         def invert(node):
#             if not node:
#                 return
            
#             node.left, node.right = invert(node.right), invert(node.left)
#             return node
        
#         return invert(root)

        # 2. 스택 사용
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack.append(node.left)
                stack.append(node.right)
        return root