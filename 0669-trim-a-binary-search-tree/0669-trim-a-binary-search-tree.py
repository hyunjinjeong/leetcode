# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        # 특정 범위를 만족하는 노드만 남긴다..
        # search 하면서 내려가다가
        # 자기자신이 범위를 만족하지 않는다. 그러면
        # value < low인 경우에는
        # 자기 자신 포함해서 left는 다 필요 없음. right는 필요할 수도 아닐 수도.
        # value > high인 경우에는
        # 자기 자신 포함해서 right는 다 필요 없음. left는 필요할 수도 아닐 수도.
        def dfs(node):
            if not node:
                return None
            
            if low <= node.val <= high:
                # 이 때는 node는 남고, 양쪽 다 돌아야 하고
                node.left = dfs(node.left)
                node.right = dfs(node.right)
                return node
            elif node.val < low:
                # 여긴 node 포함 왼쪽은 다 버리고, 오른쪽에 대해서 마저 돌아야 하고
                node.left = None
                return dfs(node.right)
            elif node.val > high:
                # 여긴 오른쪽 다 버리고 왼쪽에 마저 돌고.
                return dfs(node.left)

        return dfs(root)