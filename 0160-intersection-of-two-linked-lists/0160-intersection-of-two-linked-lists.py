# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # 1. 두 LL의 길이를 파악
        # 2. 길이가 긴 LL의 시작점을 길이 차이만큼 전진
        # 3. 각각 하나씩 전진하면서 같은게 있는지 체크

        # 1번
        len_a, len_b = 0, 0
        node = headA
        while node:
            len_a += 1
            node = node.next
        
        node = headB
        while node:
            len_b += 1
            node = node.next
        
        # 2번
        node_a, node_b = headA, headB

        if len_a < len_b:
            diff = len_b - len_a
            while diff:
                node_b = node_b.next
                diff -= 1
        else:
            diff = len_a - len_b
            while diff:
                node_a = node_a.next
                diff -= 1
        
        # 3번
        while node_a:
            if node_a is node_b:
                return node_a
            
            node_a = node_a.next
            node_b = node_b.next
        
        return None