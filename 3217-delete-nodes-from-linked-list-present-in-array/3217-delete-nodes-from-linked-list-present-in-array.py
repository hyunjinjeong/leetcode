# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums_set = set(nums)
        dummy = ListNode(next=head)

        prev, node = dummy, head
        while node:
            while node and node.val in nums_set:
                node = node.next
            
            prev.next = node
            if node:
                prev, node = node, node.next
        
        return dummy.next
