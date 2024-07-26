# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # 아 문제를 잘못 이해함
        # 색깔 입히기 문제는 아니고... dfs 돌면서 dp처럼 계산해야 할 듯?
        # max(left), max(right)가 있을 거고... 
        # 그럼 max(node)는? 바로 직전 자식을 포함하냐 마냐가 중요함.
        # max(자식 포함 + 0, 자식 비포함 + current_node.val) 이런 식일거 같은데..
        # 자식이 아니고 부모라고 생각하면 되겠다!
        
        @cache
        def dfs(node, parent_node_used):
            if not node:
                return 0

            if parent_node_used:
                return dfs(node.left, False) + dfs(node.right, False)
            else:
                return max(node.val + dfs(node.left, True) + dfs(node.right, True), dfs(node.left, False) + dfs(node.right, False))
            
        return dfs(root, False)