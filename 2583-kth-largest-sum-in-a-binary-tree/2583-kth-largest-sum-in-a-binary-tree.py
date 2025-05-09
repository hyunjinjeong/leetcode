# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        # level sum은 쉽고.. 정렬해도 되고 크기 k짜리 min heap의 0번째 원소.
        level_sums = []

        q = collections.deque([(root, 0)])
        while q:
            node, level = q.popleft()
            if len(level_sums) == level:
                level_sums.append(0)
            
            level_sums[level] += node.val
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))
        
        if len(level_sums) < k:
            return -1

        level_sums.sort(reverse=True)
        return level_sums[k - 1]
