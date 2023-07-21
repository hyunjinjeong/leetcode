# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # BST니까.. 경우들을 고려해보면
        # 1. node < p, node < q면 오른쪽으로 가야 함
        # 2. node > p, node > q면 왼쪽으로 가야 함
        # 3. 나머지 경우엔 다 자기 자신이 LCA
        
        node = root
        while True:
            if node.val < p.val and node.val < q.val:
                node = node.right
            elif node.val > p.val and node.val > q.val:
                node = node.left
            else:
                return node