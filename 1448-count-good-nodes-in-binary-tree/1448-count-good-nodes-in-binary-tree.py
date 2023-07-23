# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # dfs 돌면서 curr_max를 저장하고.. 노드 값이랑 비교하면 될 듯?
        self.ans = 0
        self.dfs(root, root.val)
        return self.ans
    
    def dfs(self, node, curr_max):
        if not node:
            return
        
        if node.val >= curr_max:
            self.ans += 1
        
        max_val = max(node.val, curr_max)
        self.dfs(node.left, max_val)
        self.dfs(node.right, max_val)
        