# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        high, low = (p, q) if p.val > q.val else (q, p)
        # 경우를 나눠서 돌면 됨.
        # node.val < low.val 이면 오른쪽으로 가야 하고
        # node.val > high.val 이면 왼쪽으로 가면 되고
        # 아니면 node가 LCA.
        
        def dfs(node):
            if node.val < low.val:
                return dfs(node.right)
            if node.val > high.val:
                return dfs(node.left)
            return node
        
        return dfs(root)