# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        # level order traversal..? kind of BFS
        q = collections.deque([(root, 0)])
        last_level = -1
        while q:
            node, level = q.popleft()

            if level > last_level:
                even_last_num, odd_last_num = 0, float("inf")
                last_level = level

            # odd && strictly increasing
            if level % 2 == 0:
                if node.val % 2 == 0 or node.val <= even_last_num:
                    return False
                even_last_num = node.val
            else: # even && strictly decreasing
                if node.val % 2 == 1 or node.val >= odd_last_num:
                    return False
                odd_last_num = node.val
            
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))

        return True