# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        cache = {}
        
        def make_full_binary(k):
            if k % 2 == 0:
                return []
            if k == 1:
                return [TreeNode(0)]
            if k in cache:
                return cache[k]
            
            res = []

            left, right = 1, k - 2
            while left < k:
                left_children, right_children = make_full_binary(left), make_full_binary(right)
                for left_child in left_children:
                    for right_child in right_children:
                        res.append(TreeNode(0, left_child, right_child))

                left += 2
                right -= 2
            
            cache[k] = res
            return res
        
        return make_full_binary(n)