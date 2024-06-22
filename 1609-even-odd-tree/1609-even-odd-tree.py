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
        even_last_num, odd_last_num = 0, float("inf")
        while q:
            node, level = q.popleft()

            # odd && strictly increasing
            if level % 2 == 0:
                odd_last_num = float("inf")
                if node.val % 2 == 0:
                    return False
                if node.val <= even_last_num:
                    return False
                even_last_num = node.val
            else: # even && strictly decreasing
                even_last_num = 0 
                if node.val % 2 == 1:
                    return False
                if node.val >= odd_last_num:
                    return False
                odd_last_num = node.val
            
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))

        return True