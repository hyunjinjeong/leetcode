# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 1 -> 2 -> 3 // 4 -> 5
        # 일단 길이를 구하고.. N이라고 하면
        # N - k만큼 앞으로 간 다음에
        # 그 노드의 next는 None으로 하고
        if not head:
            return head

        prev, node = None, head
        length = 0
        while node:
            length += 1
            prev = node
            node = node.next
        tail = prev
        
        k %= length
        if k == 0:
            return head
        
        new_tail, new_head = None, head
        count = 0
        while count < length - k:
            count += 1
            new_tail = new_head
            new_head = new_head.next
        
        new_tail.next = tail.next
        tail.next = head

        return new_head