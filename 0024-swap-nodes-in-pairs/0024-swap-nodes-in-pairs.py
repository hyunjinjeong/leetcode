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
        
        prev, curr, nxt = None, head, head.next
        while curr and nxt:
            # swap
            curr.next = nxt.next
            nxt.next = curr
            if prev:
                prev.next = nxt
            
            if not (curr.next and curr.next.next):
                break
            
            prev = curr
            curr = curr.next
            nxt = curr.next
    
        return new_head