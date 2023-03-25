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
            
            new_sum = current_sum + node.val
            new_path = path + [node.val]
            
            if new_sum == targetSum and node.left is None and node.right is None:
                ans.append(new_path)
                return
            
            dfs(node.left, new_sum, new_path)
            dfs(node.right, new_sum, new_path)
            
        ans = []
        dfs(root, 0, [])
        return ans