# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # k만큼 rotate하면
        # 끝에서 k만큼 뚝 떼서 head에다가 붙이면 되는데..
        # 문제는 k가 길이보다 클 때.
        # 길이를 구해서 remainder로 가야하나?
        if not head:
            return head
        
        # 길이 구하기
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        
        # remainder
        k = k % length
        if k == 0:
            return head
        
        # 뒤에서 k만큼 구하는건 slow fast pointer로
        slow, fast = head, head
        for _ in range(k):
            fast = fast.next
        
        # fast.next까지만 봐야 slow가 원하는 노드 이전 지점에서 끊김
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        new_head = slow.next
        slow.next = None
        # 지금 fast가 tail이므로 기존 head에 연결해줌
        fast.next = head
        
        return new_head