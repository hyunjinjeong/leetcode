"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # 일단 bfs로 구현
        if not root:
            return root
        
        q = collections.deque([root])
        while q:
            prev = None
            for _ in range(len(q)):
                node = q.popleft()

                node.next = prev
                prev = node
                
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
        
        return root