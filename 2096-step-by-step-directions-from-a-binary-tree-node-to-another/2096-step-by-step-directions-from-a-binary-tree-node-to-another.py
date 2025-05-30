# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # shortest path면.. 최소 공통 조상? 까지 가면 될 듯
        # DFS로 start dest를 모두 찾으면 리턴, 아니면 올라오는 식으로 하면 될 듯. 
        # start에서 부모까지는 U, 부모에서 dest까지는 L or R

        def find_lowest_common_ancestor(node):
            if not node:
                return None
            if node.val in [startValue, destValue]:
                return node
            
            find_left = find_lowest_common_ancestor(node.left)
            find_right = find_lowest_common_ancestor(node.right)

            if find_left and find_right:
                return node
            else:
                return find_left or find_right
        
        def generate_path(lca, target, is_start):
            q = collections.deque([(lca, "")])
            
            while q:
                node, curr_path = q.popleft()
                if node.val == startValue:
                    return curr_path
                
                if node.left:
                    q.append((node.left, curr_path + ("U" if is_start else "L")))
                if node.right:
                    q.append((node.right, curr_path + ("U" if is_start else "R")))
            
            return ""

        lca = find_lowest_common_ancestor(root)            
        return generate_path(lca, startValue, True) + generate_path(lca, destValue, False)
