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
        # 아니면 스택을 이용할 수도 있음. 다 array에 집어넣고 ...
        s = []
        curr = head
        while curr:
            s.append(curr)
            curr = curr.next
        
        curr = head
        mid = len(s) // 2
        for _ in range(mid):
            tmp = curr.next
            
            curr.next = s.pop()
            curr = curr.next
            curr.next = tmp
            
            curr = curr.next
        
        if curr != None:
            curr.next = None
        
        return head