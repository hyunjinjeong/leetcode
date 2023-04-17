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
        # 중간을 찾아서
        # 오른쪽 뒤집고
        # 그담에 하나씩 순서대로 연결하면 되지 않을까?
        
        # 1. 중간 찾기
        prev, slow, fast = None, head, head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        # circular 방지
        if prev:
            prev.next = None
        
        # 2. 오른쪽 뒤집기
        prev, curr = None, slow
        while curr:
            temp_next = curr.next
            curr.next = prev

            prev = curr
            curr = temp_next

        # 3. 하나씩 순서대로 연결하기
        left, right = head, prev
        tail = None
        while left and right:
            tmp_left_next, tmp_right_next = left.next, right.next
            tail = right
            left.next = right
            right.next = tmp_left_next
            
            left, right = tmp_left_next, tmp_right_next
        
        # 홀수개일 경우 right가 1개 더 많음
        if right:
            tail.next = right