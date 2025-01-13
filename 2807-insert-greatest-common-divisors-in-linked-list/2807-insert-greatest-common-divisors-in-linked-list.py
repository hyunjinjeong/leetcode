# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        prev, curr = None, head
        while curr:
            if prev and curr:
                new_node = ListNode(gcd(prev.val, curr.val))
                new_node.next = curr
                prev.next = new_node
            
            prev, curr = curr, curr.next
        
        return head
            

