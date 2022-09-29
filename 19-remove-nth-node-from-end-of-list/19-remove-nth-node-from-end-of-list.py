# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 길이를 구한 다음에 뺴면 되지 않으려나?
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        curr_length = 0
        prev, curr = None, head
        while curr:
            curr_length += 1
            if curr_length == length - n + 1:
                if curr_length == 1:
                    head = head.next
                else:
                    prev.next = curr.next
                    
                break
                
            prev = curr
            curr = curr.next
        
        return head