# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 요건 iterative solution. 이래야 공간이 O(1).
        total_count = 0
        node = head
        while node:
            total_count += 1
            node = node.next
        
        dummy = ListNode()
        dummy.next = head
        
        prev, curr = dummy, dummy.next
        while total_count >= k:
            new_head, new_tail, next_new_tail = self.reverse(curr, k)
            
            new_tail.next = next_new_tail # count < k 인 경우 대비...
            prev.next = new_head # 이전 node의 next는 변경된 head를 가리켜야 함
            
            prev = new_tail
            curr = next_new_tail # or prev.next
            
            total_count -= k
            
        return dummy.next
    
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
        
        
#         # k만큼 가서 reverse?
#         # k 되기 전에 end가 나오면 안 하고..
#         count = 0
#         node = head
#         while node and count < k:
#             node = node.next
#             count += 1
        
#         if count < k:
#             return head
        
#         # 아 head가 tail이 되니까.. new_tail은 굳이 없어도 됨.
#         new_head, next_new_tail = self.reverse(head, k)
#         head.next = self.reverseKGroup(next_new_tail, k)
#         return new_head
    
#     # 요건 단순 reverse
#     def reverse(self, node, k):
#         prev, curr = None, node
#         count = 0
#         while curr and count < k:
#             count += 1
#             temp_next = curr.next
#             curr.next = prev
            
#             prev = curr
#             curr = temp_next
        
#         head, next_tail = prev, curr
#         return head, next_tail