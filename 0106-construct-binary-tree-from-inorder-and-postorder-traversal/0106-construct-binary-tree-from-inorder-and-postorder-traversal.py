# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # inorder -> left -> node -> right
        # postorder -> left -> right -> node
        # 처음에 postorder[-1]으로 root를 구할 수 있음
        # inorder는 어떻게 활용하지
        # inorder에서 root의 왼쪽에 있는 친구들은 left subtree, 오른쪽에 있으면 right subtree임
        inorder_dt = { value: i for i, value in enumerate(inorder) }

        def dfs(left, right):
            if left > right:
                return

            val = postorder.pop()
            node = TreeNode(val)

            inorder_index = inorder_dt[val]
            
            node.right = dfs(inorder_index + 1, right)
            node.left = dfs(left, inorder_index - 1)
            return node
            
        return dfs(0, len(inorder) - 1)