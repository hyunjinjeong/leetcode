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
        # 3단계로 나눠서 풀기. 1. mid 구하기, 2. 오른쪽 반 reverse, 3. merge
        # 1. mid 구하기. slow가 mid가 됨
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # 2. 오른쪽 반 뒤집기. 짝수일 때 생각해보면 slow.next부터 뒤집어야 함.
        # 홀수일 때도 slow가 중간이니까 상관 없고..
        prev, curr = None, slow.next
        while curr:
            tmp_next = curr.next
            
            curr.next = prev
            prev = curr
            
            curr = tmp_next
        # 사이클 방지. 다 뒤집었으면 slow.next는 끝이 됨.
        slow.next = None
        
        # 3. 두 LL 병합하기
        head1, head2 = head, prev
        while head1 and head2:
            next1, next2 = head1.next, head2.next
            
            head1.next = head2
            head1 = next1
            
            head2.next = head1
            head2 = next2
        
#         # 아니면 스택을 이용할 수도 있음. 다 array에 집어넣고 ...
#         s = []
#         curr = head
#         while curr:
#             s.append(curr)
#             curr = curr.next
        
#         curr = head
#         mid = len(s) // 2
#         for _ in range(mid):
#             tmp = curr.next
            
#             curr.next = s.pop()
#             curr = curr.next
#             curr.next = tmp
            
#             curr = curr.next
        
#         # 사이클 방지
#         if curr != None:
#             curr.next = None