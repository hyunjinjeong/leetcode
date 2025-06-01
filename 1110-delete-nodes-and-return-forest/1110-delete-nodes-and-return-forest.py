# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        # 그래프를 먼저 만들고 그 다음에 union find 돌리면 되지 않을까
        # 근데 root를 리턴해야 한다는 제약이 있음. directed edge로 연결해서 in_degree가 0인 노드들부터 시작하면 될 듯?
        # 음 그냥 루프 돌면서 할 수도 있구나
        forest = []

        to_delete_set = set(to_delete)
        if root.val not in to_delete_set:
            forest.append(root)
        
        q = collections.deque([root])
        while q:
            node = q.popleft()

            if node.left:
                q.append(node.left)
                if node.left.val in to_delete_set:
                    node.left = None
            if node.right:
                q.append(node.right)
                if node.right.val in to_delete_set:
                    node.right = None
            
            if node.val in to_delete_set:
                if node.left:
                    forest.append(node.left)
                if node.right:
                    forest.append(node.right)

        return forest
