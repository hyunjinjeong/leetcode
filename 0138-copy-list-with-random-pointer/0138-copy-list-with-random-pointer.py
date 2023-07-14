"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy_head = Node(-1)
        # old node -> new node 매핑.. 중복 생성 방지
        cache = {}

        old = head
        curr = dummy_head
        while old:
            if old in cache:
                new_node = cache[old]
            else:
                new_node = Node(old.val)
                cache[old] = new_node

            # random 설정
            if old.random:
                if old.random in cache:
                    new_node.random = cache[old.random]
                else:
                    new_node.random = Node(old.random.val)
                    cache[old.random] = new_node.random
            # next 설정
            curr.next = new_node
        
            old = old.next
            curr = new_node
        
        return dummy_head.next