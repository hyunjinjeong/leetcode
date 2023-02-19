# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # dfs? binary search? how?
        # root는 무조건 true이고...
        # 그 밑으로는 한 쪽에서만 후손들이 존재할 수 있으니까 그 쪽으로 타고 들어가다가
        # 양 쪽이 모두 후손이면 그게 LCA!
        def dfs(node, p, q):
            if not node:
                return None
            if node is p or node is q:
                return node
            
            left = dfs(node.left, p, q)
            right = dfs(node.right, p, q)
            
            # 양쪽에서 모두 노드를 리턴하는 경우. 즉 p q를 둘 다 찾았단 얘기이고 얘가 lca임
            if left and right:
                return node
            # 한 쪽에서만 찾은 경우. 그러면 그 쪽으로 내려가야 lca가 나옴.
            return left or right
        
        return dfs(root, p, q)