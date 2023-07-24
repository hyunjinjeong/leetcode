# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # inorder로 돌아서 k번째를 찾으면 됨
        # 이것도 iterative로..
        
        stack = []
        curr = root
        index = 0
        
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            index += 1
            curr = stack.pop()
            if index == k:
                return curr.val
            
            curr = curr.right
                