# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # level order로 돌고
        # max width 구하는 방법만 찾으면 될 듯?
        # root로부터 왼쪽은 2n, 오른쪽은 2n+1 이걸 돌면서 부여할 수 있으려나?
        # 길이는 right-left-1 이 될거고..
        max_length = 0
        
        q = collections.deque()
        q.append((root, 1))
        
        while q:
            left, right = 0, 0
            # level 단위로 전체 순회
            level_length = len(q)
            for i in range(level_length):
                node, num = q.popleft()
                
                if i == 0:
                    left = num
                if i == level_length-1:
                    right = num
                
                if node.left:
                    q.append((node.left, num*2))
                if node.right:
                    q.append((node.right, num*2+1))
            
            max_length = max(max_length, right-left+1)
        
        return max_length