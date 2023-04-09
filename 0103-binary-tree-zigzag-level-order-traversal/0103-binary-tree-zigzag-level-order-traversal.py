# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root
        
        ans = []
        
        LEFT, RIGHT = 1, -1
        # root부터해서 left -> right -> left...
        direction = LEFT
        
        q = collections.deque([root])
        while q:
            curr_level = collections.deque()
            for _ in range(len(q)):
                node = q.popleft()
                
                if direction == LEFT:
                    curr_level.append(node.val)
                else:
                    curr_level.appendleft(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            ans.append(curr_level)
            direction *= -1
        
        return ans