# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # inorder로 돌았을 때 항상 이전 값 < 현재 값이어야 함.
        # iterative로 해볼까...
        
        stack = []
        curr = root
        prev_val = float("-inf")
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                if prev_val >= curr.val:
                    return False
                prev_val = curr.val
                curr = curr.right
        
        return True
            
            