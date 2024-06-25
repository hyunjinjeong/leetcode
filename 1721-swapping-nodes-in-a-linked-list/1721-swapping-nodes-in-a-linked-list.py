# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        slow, fast = head, head
        i = 0
        while k > 1:
            fast = fast.next
            k -= 1
        
        # 여기서 fast가 앞에서 n번째
        nth_from_head = fast

        while fast.next:
            fast = fast.next
            slow = slow.next

        # slow가 뒤에서 n번째
        nth_from_tail = slow

        nth_from_head.val, nth_from_tail.val = nth_from_tail.val, nth_from_head.val
        return head