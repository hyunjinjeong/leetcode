# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # dfs? binary search? how?
        # root는 무조건 lca임.
        # 그 밑으로는 한 쪽에서만 lca가 존재할 수 있으니까 아닌 쪽은 버리는 거고
        # 그 쪽으로 dfs로 타고 가다가 왼쪽 오른쪽 둘다 lca가 아닌 친구가 나오면 그게 lca.
        def dfs(node, p, q):
            if not node:
                return node
            if node is p or node is q:
                return node
            
            left = dfs(node.left, p, q)
            right = dfs(node.right, p, q)
            
            if left and right:
                return node
            return left or right
        
        return dfs(root, p, q)