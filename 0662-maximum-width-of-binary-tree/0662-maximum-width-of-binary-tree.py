# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # BFS 돌려서 레벨마다 최댓값 - 최솟값 구하고, max를 추적하고 있으면 되지 않을까
        # lefTChild는 *2, rightChild는 *2+1. width는 max(right) - max(left) + 1
        q = collections.deque([(root, 1)])
        ans = 0
    
        while q:
            leftmost, rightmost = q[0][1], q[-1][1]
            ans = max(rightmost - leftmost + 1, ans)

            for _ in range(len(q)):
                node, index = q.popleft()
                leftmost = min(index, leftmost)
                rightmost = max(index, rightmost)

                if node.left:
                    q.append((node.left, index * 2))
                if node.right:
                    q.append((node.right, index * 2 + 1))

        return ans
