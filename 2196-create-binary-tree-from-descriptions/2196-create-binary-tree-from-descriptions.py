# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {} # val -> (TreeNode, is_root)

        for parent, child, is_left in descriptions:
            if parent not in nodes:
                nodes[parent] = (TreeNode(parent), True)
            if child not in nodes:
                nodes[child] = (TreeNode(child), False)

            parent_node, _ = nodes[parent]
            child_node, is_child_node_root = nodes[child]

            if is_left:
                parent_node.left = child_node
            else:
                parent_node.right = child_node
            
            if is_child_node_root:
                nodes[child] = (child_node, False)
        
        for node, is_root in nodes.values():
            if is_root:
                return node
