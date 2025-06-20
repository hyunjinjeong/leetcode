# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 흠 3부터는 어떻게 하지
        # pair가 되는 노드를 같이 넘겨주자

        # def dfs(node1, node2, level):
        #     if not node1:
        #         return
            
        #     if level % 2 == 1:
        #         node1.val, node2.val = node2.val, node1.val

        #     dfs(node1.left, node2.right, level + 1)
        #     dfs(node1.right, node2.left, level + 1)

        # dfs(root.left, root.right, 1)
        # return root

        q = collections.deque()
        q.append((root.left, root.right, 1))

        while q:
            node1, node2, level = q.popleft()
            if not node1:
                continue
            if level % 2 == 1:
                node1.val, node2.val = node2.val, node1.val

            q.append((node1.left, node2.right, level + 1))
            q.append((node1.right, node2.left, level + 1))
        
        return root
