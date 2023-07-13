# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # target이 head인 경우를 처리하기 위해..
        dummy_head = ListNode()
        dummy_head.next = head

        # slow fast 포인터 이용하면 될 듯.. n번 앞으로 먼저 가서...
        slow, fast = head, head
        prev = dummy_head
        for _ in range(n):
            fast = fast.next
        
        # 이제 마지막까지 돌면 slow가 target임.
        while fast:
            prev = slow
            fast = fast.next
            slow = slow.next
        
        # target (slow) 제거
        prev.next = slow.next
        return dummy_head.next
