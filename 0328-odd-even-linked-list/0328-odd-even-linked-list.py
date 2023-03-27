# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 길이가 홀수면 그냥 뒤로 밀어넣으면 되고
        # 길이가 짝수면 tail 앞으로 밀어넣어야 함.
        if not head:
            return head
        
        # tail, 길이 구하기
        prev_tail, tail, length = None, head, 1
        while tail.next:
            prev_tail = tail
            tail = tail.next
            length += 1
        
        if length % 2 == 1:
            count = length // 2
            pivot = tail
        else:
            count = length // 2 - 1
            pivot = prev_tail
        
        odd, even = head, head.next
        while count:
            odd.next = even.next

            pivot.next, even.next = even, pivot.next
            pivot = even

            odd = odd.next
            even = odd.next
            
            count -= 1
        
        return head