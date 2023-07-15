# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry, number = 0, 0
        dummy_head = ListNode()

        n1, n2 = l1, l2
        new_node = dummy_head
        while n1 and n2:
            _sum = n1.val + n2.val + carry
            carry, number = _sum // 10, _sum % 10

            new_node.next = ListNode(number)
            new_node = new_node.next

            n1, n2 = n1.next, n2.next
        
        while n1 or n2:
            _sum = (n1.val if n1 else n2.val) + carry
            carry, number = _sum // 10, _sum % 10

            new_node.next = ListNode(number)
            new_node = new_node.next

            if n1:
                n1 = n1.next
            if n2:
                n2 = n2.next

        if carry:
            new_node.next = ListNode(carry)

        return dummy_head.next