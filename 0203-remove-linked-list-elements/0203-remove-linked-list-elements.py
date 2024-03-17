# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()

        node = head
        dummy_node = dummy
        while node:
            if node.val != val:
                dummy_node.next = ListNode(node.val)
                dummy_node = dummy_node.next
            node = node.next
        
        return dummy.next