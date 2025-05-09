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

        q = collections.deque([root])
        while q:
            level_sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                level_sum += node.val
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            heapq.heappush(level_sums, level_sum)
            if len(level_sums) > k:
                heapq.heappop(level_sums)
        
        if len(level_sums) < k:
            return -1

        return level_sums[0]