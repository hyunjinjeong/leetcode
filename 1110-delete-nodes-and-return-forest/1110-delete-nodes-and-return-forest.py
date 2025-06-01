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
        graph = collections.defaultdict(list)
        in_degree = {}
        
        value_to_node = {}
        to_delete_set = set(to_delete)
        
        q = collections.deque([(root, None)])
        while q:
            node, parent = q.popleft()

            if node.val not in value_to_node:
                value_to_node[node.val] = node
            if node.val not in to_delete_set and node.val not in in_degree:
                in_degree[node.val] = 0

            if node.val not in to_delete_set and parent is not None and parent.val not in to_delete_set:
                graph[parent.val].append(node.val)
                in_degree[node.val] += 1
            
            if node.left:
                q.append((node.left, node))
                if node.left.val in to_delete_set:
                    node.left = None
            if node.right:
                q.append((node.right, node))
                if node.right.val in to_delete_set:
                    node.right = None

        return [value_to_node[k] for k, v in in_degree.items() if v == 0]
