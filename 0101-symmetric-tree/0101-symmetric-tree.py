# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#         return self.is_mirror(root.left, root.right)
        
#     def is_mirror(self, left, right):
#         # 둘 다 None이면 leaf이므로 True
#         if left is None and right is None:
#             return True
#         # 한 쪽만 None이면 당연히 False
#         if left is None or right is None:
#             return False
        
#         # left, right 다 있는 경우.
#         # 두 값이 다르면 당연히 False
#         if left.val != right.val:
#             return False
        
#         # left.right == right.left 와 left.left == right.right 도 재귀적으로 비교
#         return self.is_mirror(left.right, right.left) and self.is_mirror(left.left, right.right)

        # 2. iterative로 짜보면
        stack = [(root.left, root.right)]
        while stack:
            left, right = stack.pop()
            
            if not left and not right:
                continue
            if not left or not right:
                return False
            
            if left.val != right.val:
                return False
            
            stack.append((left.right, right.left))
            stack.append((left.left, right.right))
        
        return True