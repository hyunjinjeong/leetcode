# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder면 node -> left -> right
        # inorder면 left -> node -> right
        
        # 아.. inorder는 root 찾으면 divide and conquer가 가능하다. root는 preorder에서 계속 뽑고
        # 우선 다른 최적화 같은거 안하고 기본 개념만.
#         if not inorder:
#             return
        
#         root_val = preorder.pop(0)
#         root = TreeNode(root_val)
#         root_index = inorder.index(root_val)
        
#         root.left = self.buildTree(preorder, inorder[:root_index])
#         root.right = self.buildTree(preorder, inorder[root_index+1:])
        
#         return root
        
        # 여기서 pop(0)이 매번 O(n)이고 index 찾는 것도 매번 O(n)이라서 각각 deque, hashmap 써서 O(1)로 최적화할 수 있음.        
        preorder_queue = collections.deque(preorder)
        inorder_dt = { val: i for i, val in enumerate(inorder) }
            
        def dfs(left, right):
            if left > right: # element가 없는 경우
                return
            
            val = preorder_queue.popleft()
            root = TreeNode(val)
            root_index = inorder_dt[val]
            
            root.left = dfs(left, root_index-1)
            root.right = dfs(root_index+1, right)
            return root
            
        return dfs(0, len(preorder)-1)
        