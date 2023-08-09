# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # linked list 뒤집는 거야 별거 아닌데...
        # 이걸 k번씩 어떻게 하지?
        # 마지막에 k개가 있는지 없는지를 알아야 함.
        # 길이를 구하면 된다.
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1
        
        curr_head = head
        is_first = True

        prev, curr = None, head
        last_node = None
        while length >= k:
            tmp_last_node = curr

            for _ in range(k):
                tmp_next = curr.next
                curr.next = prev

                prev = curr
                curr = tmp_next
            
            if is_first:
                curr_head = prev
                is_first = False
            
            if last_node:
                last_node.next = prev
            
            last_node = tmp_last_node
            prev = None
            length -= k
        
        if length:
            last_node.next = curr

        return curr_head