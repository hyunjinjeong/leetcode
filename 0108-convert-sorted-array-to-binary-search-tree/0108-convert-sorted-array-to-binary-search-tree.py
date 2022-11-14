# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def convert(left, right):
            if left > right:
                return None
            
            mid = (left + right) // 2
            return TreeNode(val=nums[mid], left=convert(left, mid-1), right=convert(mid+1, right))
        
        return convert(0, len(nums)-1)