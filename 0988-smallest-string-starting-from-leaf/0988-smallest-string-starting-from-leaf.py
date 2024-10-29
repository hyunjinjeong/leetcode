# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        # backtracking 해서 하나씩 보면 되려나?

        def dfs(node, string):
            # array를 써도 어차피 reverse해야 해서 그냥 string 쓰면 되겠다.
            string = chr(ord('a') + node.val) + string

            if node.left and node.right:
                return min(dfs(node.left, string), dfs(node.right, string))
            elif node.left:
                return dfs(node.left, string)
            elif node.right:
                return dfs(node.right, string)
            
            return string

        return dfs(root, "")