# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # 이거 그냥 dfs해서 찾으면 안 되나?
        
        def dfs(node, current_sum, path):
            if not node:
                return
            
            path.append(node.val)
            new_sum = current_sum + node.val
            
            if not node.left and not node.right:
                if new_sum == targetSum:
                    ans.append(path[:])
            else:
                dfs(node.left, new_sum, path)
                dfs(node.right, new_sum, path)
            
            # backtracking
            path.pop()
            
        ans = []
        dfs(root, 0, [])
        return ans