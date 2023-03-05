# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
#         # 레벨 별로 가장 오른쪽에 있는 노드를 보여주면 된다!
#         # 그러면 어떻게.. pre-order에서 node -> right -> left 순으로 찾는 거임.
#         def traverse(node, level):
#             if not node:
#                 return
            
#             # 레벨 별로 가장 오른쪽에 있는 노드가 처음으로 여기 들어오게 된다
#             if level == len(ans):
#                 ans.append(node.val)
            
#             traverse(node.right, level+1)
#             traverse(node.left, level+1)
            
#         ans = []
#         traverse(root, 0)
        
#         return ans

        # 요건 BFS 버전. 좀 더 직관적인 듯?
        ans = []
        q = collections.deque()
        if root:
            q.append(root)

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if i == 0:
                    ans.append(node.val) # 레벨별로 맨 왼쪽에 있는 친구가 맨 오른쪽 노드
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)

        return ans