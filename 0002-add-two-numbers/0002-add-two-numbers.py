# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        node = dummy
        
        n1, n2 = l1, l2
        carry = 0
        while n1 or n2 or carry:
            n1_val = n1.val if n1 else 0
            n2_val = n2.val if n2 else 0
            _sum = n1_val + n2_val + carry
            remainder, carry = _sum % 10, _sum // 10
            
            node.next = ListNode(val=remainder)
            node = node.next
            if n1:
                n1 = n1.next
            if n2:
                n2 = n2.next
        
        return dummy.next