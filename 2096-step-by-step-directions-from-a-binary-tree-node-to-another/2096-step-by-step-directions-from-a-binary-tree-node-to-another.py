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
        
        def generate_path(node, target, path):
            if not node:
                return False
            if node.val == target:
                return True
            
            path.append("L")
            if generate_path(node.left, target, path):
                return True
            path.pop()

            path.append("R")
            if generate_path(node.right, target, path):
                return True
            path.pop()

        lca = find_lowest_common_ancestor(root)
        
        start_path, dest_path = [], []
        generate_path(lca, startValue, start_path)
        generate_path(lca, destValue, dest_path)

        res = ["U"] * len(start_path) + dest_path
        return "".join(res)
