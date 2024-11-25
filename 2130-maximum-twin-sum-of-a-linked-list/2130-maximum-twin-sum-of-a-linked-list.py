# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Reverse the right-half
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev, curr = None, slow
        while curr:
            tmp_next = curr.next
            curr.next = prev

            prev = curr
            curr = tmp_next

        # now prev is the new head
        res = 0
        node1, node2 = head, prev

        while node1 and node2:
            res = max(res, node1.val + node2.val)
            node1 = node1.next
            node2 = node2.next
        
        return res