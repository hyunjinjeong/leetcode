# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # level order traversal로 다 돌면 O(N). 공간 복잡도는 O(1).
        if not root:
            return []
        
        res = []
        
        q = collections.deque([root])
        while q:
            curr_max = float("-inf")
            for _ in range(len(q)):
                node = q.popleft()
                curr_max = max(curr_max, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(curr_max)
        
        return res