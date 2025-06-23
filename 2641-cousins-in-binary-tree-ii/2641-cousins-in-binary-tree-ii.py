# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # level sum을 구해서 sibling sum을 빼면 되는구만
        level_sums = []

        q = collections.deque([(root, 0)])
        while q:
            node, level = q.popleft()
            if level == len(level_sums):
                level_sums.append(0)
            
            level_sums[level] += node.val
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))
        
        def dfs(node, level, sibling_sum):
            if not node:
                return None
            
            node.val = level_sums[level] - sibling_sum
            if node.left and node.right:
                children_sum = node.left.val + node.right.val
                node.left = dfs(node.left, level + 1, children_sum)
                node.right = dfs(node.right, level + 1, children_sum)
            elif node.left:
                node.left = dfs(node.left, level + 1, node.left.val)
            elif node.right:
                node.right = dfs(node.right, level + 1, node.right.val)

            return node
        
        return dfs(root, 0, root.val)
