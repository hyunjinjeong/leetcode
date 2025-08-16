# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # BST 정의는? left.val < curr.val < right.val
        # O(N)은 쉬움. BST에서는 inorder가 정렬되어 있으니까 쭉 돌고 난 다음에 정렬이 안된거 찾으면 됨
        # 근데 in place로 바꿔야 함. 어떻게 swap해주지?
        # value가 unique 한가? no. 그러면 배열에다가 node를 저장하면 될 듯?

        def get_inorder_array(node):
            if node is None:
                return []
            
            return get_inorder_array(node.left) + [node] + get_inorder_array(node.right)
        
        inorder_array = get_inorder_array(root)

        x, y = None, None
        for i in range(len(inorder_array) - 1):
            if inorder_array[i + 1].val < inorder_array[i].val:
                y = inorder_array[i + 1]
                if x is None:
                    x = inorder_array[i]
                else:
                    break
        
        x.val, y.val = y.val, x.val
