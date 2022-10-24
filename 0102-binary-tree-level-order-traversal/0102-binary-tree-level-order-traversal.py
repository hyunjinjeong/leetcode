# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        answer = []
        def dfs(n, level):
            if not n:
                return
            
            if len(answer) < level+1:
                answer.append([])
            answer[level].append(n.val)
            
            dfs(n.left, level+1)
            dfs(n.right, level+1)
        
        dfs(root, 0)
        return answer