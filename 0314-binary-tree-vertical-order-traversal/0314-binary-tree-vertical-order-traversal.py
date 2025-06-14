# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 전체 index 개수는 처음에 구해야 하나?
        # 아니지 index는 상대적인 순서만 중요하니까 나중에 넣으면 될 듯
        # BFS 돌리면서 하나씩 넣으면 되지 않을까?
        order_map = collections.defaultdict(list)
        
        q = collections.deque()
        q.append((root, 0))

        while q:
            node, index = q.popleft()
            if not node:
                continue
            
            order_map[index].append(node.val)

            q.append((node.left, index - 1))
            q.append((node.right, index + 1))
        
        return [order_map[key] for key in sorted(order_map.keys())]
