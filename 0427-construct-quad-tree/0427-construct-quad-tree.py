"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        # 걍 4분면으로 잘라서 재귀 돌리면 될 거 같은데?
        # 그냥 top_left랑 N만 주면 될 것 같음.
        def build_quad_tree(r, c, N):
            curr_sum = 0
            for i in range(r, r + N):
                for j in range(c, c + N):
                    curr_sum += grid[i][j]
            
            if curr_sum == 0:
                return Node(val=False, isLeaf=True)
            if curr_sum == N ** 2:
                return Node(val=True, isLeaf=True)
            
            node = Node(val=True, isLeaf=False)
            node.topLeft = build_quad_tree(r, c, N // 2)
            node.topRight = build_quad_tree(r, c + N // 2, N // 2)
            node.bottomLeft = build_quad_tree(r + N // 2, c, N // 2)
            node.bottomRight = build_quad_tree(r + N // 2, c + N // 2, N // 2)
            return node

        return build_quad_tree(0, 0, len(grid))