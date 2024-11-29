# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        @cache
        def build(start, end):
            res = []
            for root in range(start, end + 1):
                left_subtrees = build(start, root - 1) or [None]
                right_subtrees = build(root + 1, end) or [None]
                
                for left in left_subtrees:
                    for right in right_subtrees:
                        res.append(TreeNode(root, left, right))
            return res
        
        return build(1, n)