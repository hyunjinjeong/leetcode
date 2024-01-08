# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        # bfs로 돌면서 중간에 빈 노드가 있으면 complete이 아님
        q = collections.deque([root])
        has_null = False

        while q:
            node = q.popleft()
            if node is None:
                has_null = True
            else:
                if has_null:
                    return False
                q.append(node.left)
                q.append(node.right)
        
        return True