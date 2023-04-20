# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # 부모 노드를 다 만들어주면 target 노드로부터 bfs 가능. (부모, 자식)
        parents = {}
        def make_parents(node): # dfs
            if not node:
                return
            
            if node.left:
                parents[node.left.val] = node
            if node.right:
                parents[node.right.val] = node
            
            make_parents(node.left)
            make_parents(node.right)
        
        # bfs
        make_parents(root)
        ans = []
        q = collections.deque([(target, 0)])
        visited = set()
        while q:
            node, distance = q.popleft()
            if node.val in visited:
                continue
            
            visited.add(node.val)
            if distance == k:
                ans.append(node.val)
                continue
            
            # root 노드의 경우 없음.
            if node.val in parents:
                q.append((parents[node.val], distance+1))
            if node.left:
                q.append((node.left, distance+1))
            if node.right:
                q.append((node.right, distance+1))
        
        return ans