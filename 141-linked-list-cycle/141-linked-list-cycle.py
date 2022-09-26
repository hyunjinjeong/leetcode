# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        
        # slow runner, fast runner 이용
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow is fast:
                return True
        
        return False