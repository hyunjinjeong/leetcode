# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # node.val보다 큰 값을 다 더해야 함
        # 즉.. 본인의 right subtree 및 부모가 자신보다 클 경우 부모 + 부모의 right subtree를 다 더해야 함
        # 그것보다.. 가장 오른쪽부터 거꾸로 돌 수 있으면 그동안의 sum을 더해가면서 할 수 있음
        curr_sum = 0
        
        node = root
        stack = []
        while stack or node:
            while node:
                stack.append(node)
                node = node.right
            
            node = stack.pop()
            node.val += curr_sum
            curr_sum = node.val

            node = node.left
        
        return root