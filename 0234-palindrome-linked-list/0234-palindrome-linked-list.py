# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 1. mid를 찾는다. slow, fast 포인터 이용
        # 2. mid에서부터 뒤집는다
        # 3. 둘이 돌면서 같은지 비교
        
        # 1. Find the mid
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 2. Reverse the right half
        prev, node = None, slow
        while node:
            tmp_next = node.next
            node.next = prev
            
            prev = node
            node = tmp_next
        
        # 3. Compare each node
        while head and prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        
        return True
        
            