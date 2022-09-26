# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         # 이건 iterative 버전이고..
#         prev, curr = None, head
        
#         while curr:
#             temp_next = curr.next
#             curr.next = prev
            
#             prev = curr
#             curr = temp_next
        
#         return prev
        
        # 재귀로 짜보면?
        def reverse(curr, prev=None):
            if not curr:
                return prev
            
            temp_next = curr.next
            curr.next = prev
            return reverse(temp_next, curr)
        
        return reverse(head)
