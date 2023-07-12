# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 3단계로 나눠야 할 듯?
        # 1. mid 찾기
        # 2. 오른쪽 리스트는 reverse
        # 3. 왼쪽/오른쪽 리스트 합치기
        # 코너 케이스
        if not (head and head.next):
            return head
        
        # 1. find mid
        prev, slow, fast = None, head, head
        while fast and fast.next:
            prev = slow
            fast = fast.next.next
            slow = slow.next
        
        # slow == prev.next가 mid.
        # 연결 끊기
        mid = prev.next
        prev.next = None
        
        # 2. 오른쪽 list reverse
        prev, curr = None, mid
        while curr:
            tmp = curr.next
            curr.next = prev
            
            prev = curr
            curr = tmp
        
        # 이 시점에서 prev가 이제 오른쪽 list의 head가 됨
        # 3. 왼쪽/오른쪽 리스트 합치기
        l1, l2 = head, prev
        while l1 and l2:
            tmp_l1_next = l1.next
            tmp_l2_next = l2.next
            l1.next = l2
            # l2가 1개 더 많은 경우가 있기 때문에, 코너 케이스.
            l2.next = tmp_l1_next if tmp_l1_next else tmp_l2_next

            l1 = tmp_l1_next
            l2 = tmp_l2_next