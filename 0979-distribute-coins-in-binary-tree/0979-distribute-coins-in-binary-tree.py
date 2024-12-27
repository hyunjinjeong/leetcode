# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        # leaf에서부터 시작해서 모든 노드의 값을 1로 만들면 되는구나
        # 그럼 4 0 0 0 같은 경우
        # 4 0 -2 1
        # 4 -5 1 1
        # 1 1 1 1 (-6)
        def post_order(node):
            if not node:
                return 0
            
            left = post_order(node.left)
            right = post_order(node.right)
            self.res += abs(left) + abs(right)
            return left + right + node.val - 1
        
        self.res = 0
        post_order(root)
        return self.res