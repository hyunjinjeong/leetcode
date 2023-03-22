# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow, fast = head, head
        
        for _ in range(n-1):
            fast = fast.next
        
        prev = slow
        while fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next
        
        prev.next = slow.next
        
        # 특수 케이스
        if slow is head:
            return slow.next
        
        return head