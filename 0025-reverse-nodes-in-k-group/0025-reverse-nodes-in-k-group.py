# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # k만큼 가서 reverse?
        # k 되기 전에 end가 나오면 안 하고..
        count = 0
        node = head
        while node and count < k:
            node = node.next
            count += 1
        
        if count < k:
            return head
        
        new_head, new_tail, next_new_tail = self.reverse(head, k)
        new_tail.next = self.reverseKGroup(next_new_tail, k)
        return new_head
    
    # 요건 단순 reverse
    def reverse(self, node, k):
        prev, curr = None, node
        count = 0
        while curr and count < k:
            count += 1
            temp_next = curr.next
            curr.next = prev
            
            prev = curr
            curr = temp_next
        
        head, tail, next_tail = prev, node, curr
        return head, tail, next_tail