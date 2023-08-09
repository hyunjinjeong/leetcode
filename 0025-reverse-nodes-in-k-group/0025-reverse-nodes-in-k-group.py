# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        total_count = 0
        node = head
        while node:
            total_count += 1
            node = node.next
        
        dummy = ListNode()
        dummy.next = head
        
        prev, curr = dummy, dummy.next
        while total_count >= k:
            new_head, new_tail, new_next_tail = self.reverse(curr, k)
            
            new_tail.next = new_next_tail # count < k 인 경우 대비...
            prev.next = new_head # 이전 node의 next는 변경된 head를 가리켜야 함
            
            prev = new_tail
            curr = new_next_tail # == prev.next
            
            total_count -= k
            
        return dummy.next
    
    # 요건 단순 reverse
    def reverse(self, node, k):
        prev, curr = None, node
        for _ in range(k):
            temp_next = curr.next
            curr.next = prev
            
            prev = curr
            curr = temp_next
        
        head, tail, next_tail = prev, node, curr
        return head, tail, next_tail