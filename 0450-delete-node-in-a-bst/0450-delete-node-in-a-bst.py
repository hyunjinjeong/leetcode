# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # right의 leftmost로 바꿔주면 되려나?
        def delete(node):
            if not node:
                return node

            if node.val > key:
                node.left = delete(node.left)
            elif node.val < key:
                node.right = delete(node.right)
            else:
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left
                
                successor = find_leftmost_of_right_child(node)
                node.val, successor.val = successor.val, node.val
                node.right = delete(node.right)
            
            return node

        def find_leftmost_of_right_child(node):
            curr = node.right
            while curr and curr.left:
                curr = curr.left
            return curr

        return delete(root)