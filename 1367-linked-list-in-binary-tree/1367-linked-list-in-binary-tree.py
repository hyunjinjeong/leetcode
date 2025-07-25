# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        # 모든 노드에서 실행해봐야 함..
        def is_valid(list_node, tree_node):
            if list_node is None:
                return True
            if tree_node is None:
                return False
            
            if list_node.val != tree_node.val:
                return False
            return is_valid(list_node.next, tree_node.left) or is_valid(list_node.next, tree_node.right)

        def dfs(tree_node):
            if tree_node is None:
                return False
            
            if is_valid(head, tree_node):
                return True
            return is_valid(head, tree_node.left) or is_valid(head, tree_node.right)
        
        return dfs(root)
