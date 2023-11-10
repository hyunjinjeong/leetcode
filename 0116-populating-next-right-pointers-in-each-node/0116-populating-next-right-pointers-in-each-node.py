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
        # constant space로 어케 하지..?
        # pointer를 몇 개 더 쓰면 된다. next를 이용해서 레벨마다 도는 것..
        if not root:
            return root
        
        node = root
        while node.left:
            curr = node
            while curr:
                curr.left.next = curr.right
                
                if curr.next:
                    curr.right.next = curr.next.left
                
                curr = curr.next
            
            node = node.left
        
        return root