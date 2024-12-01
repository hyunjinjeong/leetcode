# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 엣지 케이스 처리
        if not (head and head.next):
            return head
        
        new_head = head.next
        
        prev, curr = None, head
        while curr and curr.next:
            tmp_next = curr.next
            
            # swap
            curr.next = tmp_next.next
            tmp_next.next = curr
            if prev:
                prev.next = tmp_next
            
            # next
            prev = curr
            curr = curr.next
    
        return new_head