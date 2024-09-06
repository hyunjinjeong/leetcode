# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        def dfs(node):
            if not node:
                return ""
            tree_str = "(" + dfs(node.left) + ")" + str(node.val) + "(" + dfs(node.right) + ")"
            self.hash[tree_str] += 1
            if self.hash[tree_str] == 2:
                self.res.append(node)
            return tree_str
        
        self.res = []
        self.hash = collections.defaultdict(int)
        dfs(root)
        return self.res
