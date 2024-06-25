# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        slow, fast = dummy, head

        i = 1
        while i < left:
            fast = fast.next
            slow = slow.next
            i += 1
        
        new_tail = fast
        prev_start = slow

        # 뒤집는건 뒤집는 건데... 처음이랑 마지막 노드 처리가 애매한데?
        # start.next = end.next
        # prev_start.next = end
        # 요렇게 되겠다.

        prev, node = new_tail, new_tail.next
        while i < right:
            print(prev.val, node.val)

            nxt = node.next
            node.next = prev
            
            prev = node
            node = nxt

            i += 1
        
        prev_start.next = prev
        new_tail.next = node

        return dummy.next