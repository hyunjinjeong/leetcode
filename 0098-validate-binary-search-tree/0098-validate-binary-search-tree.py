# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # BST면 inorder로 돌아서 항상 val[i] < val[i+1] 이면 된다.
        # 더 최적화해서 O(1) 공간 쓰도록. 물론 재귀 스택을 포함하면 O(N)임
        def check_bst(node, left, right):
            if not node:
                return True

            if not left < node.val < right:
                return False

            return check_bst(node.left, left, node.val) and check_bst(node.right, node.val, right)
        
        return check_bst(root, float("-inf"), float("inf"))
	
    