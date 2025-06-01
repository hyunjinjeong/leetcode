# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums_set = set(nums)
        dummy = ListNode(next=head)

        node = dummy
        while node.next:
            if node.next.val in nums_set:
                node.next = node.next.next
            else:
                node = node.next
        
        return dummy.next
