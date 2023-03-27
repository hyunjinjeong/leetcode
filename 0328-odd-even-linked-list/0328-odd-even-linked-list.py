# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        # odd -> odd, even -> even 이런 식으로 쭉 연결하다가
        # 마지막에 odd.next = even_head만 해주면 되는구낭
        
        odd, even = head, head.next
        even_head = even
        
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            
            odd, even = odd.next, even.next
        
        odd.next = even_head
        
        return head
        