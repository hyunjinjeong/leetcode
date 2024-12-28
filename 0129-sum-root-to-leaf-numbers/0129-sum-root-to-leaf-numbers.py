# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        stack = [(root, 0)]
        while stack:
            node, prev_sum = stack.pop()
            curr_sum = prev_sum * 10 + node.val
            
            if not (node.left or node.right):
                res += curr_sum
                continue

            if node.left:
                stack.append((node.left, curr_sum))
            if node.right:
                stack.append((node.right, curr_sum))

        return res