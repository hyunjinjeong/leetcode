# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 어떻게 활용해야 할까...
        # preorder는 node -> left -> right
        # inorder는 left -> node -> right
        # leaf가 아닌 node는 left나 right 중 하나는 있음... 근데 그게 뭔지 알려면?
        # node의 위치를 inorder에서 찾아서... 왼쪽에 원소가 있는지 봐야 함.
        # 이 과정을 divide-and-conquer로.
        # preorder를 level-order로 착각해서 헤맴 ㅠ
        preorder_queue = collections.deque(preorder)
        inorder_dt = { val: i for i, val in enumerate(inorder) }
            
        def dfs(left, right):
            if left > right: # element가 없는 경우
                return
            
            val = preorder_queue.popleft()
            node = TreeNode(val)
            node_index = inorder_dt[val]
            
            node.left = dfs(left, node_index - 1)
            node.right = dfs(node_index + 1 , right)
            return node
            
        return dfs(0, len(preorder)-1)
        
        
        