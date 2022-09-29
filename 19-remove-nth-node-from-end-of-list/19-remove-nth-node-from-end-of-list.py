# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         # 길이를 구한 다음에 뺴면 되지 않으려나?
#         length = 0
#         curr = head
#         while curr:
#             length += 1
#             curr = curr.next
        
#         curr_length = 0
#         prev, curr = None, head
#         while curr:
#             curr_length += 1
#             if curr_length == length - n + 1:
#                 if curr_length == 1:
#                     head = head.next
#                 else:
#                     prev.next = curr.next
                    
#                 break
                
#             prev = curr
#             curr = curr.next
        
#         return head
        # 1-pass로 하려면 slow, fast 포인터 사용. fast를 n개만큼 미리 떙겨놓으면 된다.
        slow, fast = head, head
        for _ in range(n):
            fast = fast.next
        # 여기 fast가 없다면 n이 리스트 길이와 같다는 뜻. 뒤에서부터니 head가 된다.
        if not fast:
            return head.next
        
        # slow가 타겟의 prev까지 가게 됨
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return head