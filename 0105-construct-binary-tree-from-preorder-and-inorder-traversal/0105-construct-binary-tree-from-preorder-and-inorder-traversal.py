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
        # 이 두개가 주어졌을 때 원래 순서라..
        
        # 아.. inorder는 root 찾으면 divide and conquer가 가능하다. root는 preorder에서 계속 뽑고
        # 우선 다른 최적화 같은거 안하고 기본 개념만.
        if not inorder:
            return
        
        root_val = preorder.pop(0)
        root = TreeNode(root_val)
        root_index = inorder.index(root_val)
        
        root.left = self.buildTree(preorder, inorder[:root_index])
        root.right = self.buildTree(preorder, inorder[root_index+1:])
        
        return root
        
#         pre = deque(preorder)
                
#         dt = {}
#         for val, i in enumerate(inorder):
#             dt[val] = i
            
#         def dfs(left, right):
#             if not pre:
#                 return
            
#             val = pre.popleft()
#             root = TreeNode(val)
#             root_index = dt[val]
            
            
        
#         root = preorder[0]
        