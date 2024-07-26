# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # 이건 그 색깔입히기 같은데
        # 각각 합 중에 max 리턴하면 될 듯
        RED, WHITE = 1, 0
        red_money, white_money = 0, 0

        stack = [(root, RED)]
        while stack:
            node, color = stack.pop()
            if color == RED:
                red_money += node.val
            else:
                white_money += node.val
            
            if node.left:
                stack.append((node.left, RED if color == WHITE else WHITE))
            if node.right:
                stack.append((node.right, RED if color == WHITE else WHITE))

        return max(red_money, white_money)