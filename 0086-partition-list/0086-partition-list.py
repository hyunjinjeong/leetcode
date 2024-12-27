# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # list 하나 따로 만들어서 이어 붙이면 되려나?
        small_head = ListNode()
        great_head = ListNode()
        
        small_node = small_head
        great_node = great_head

        node = head
        while node:
            if node.val >= x:
                great_node.next = ListNode(node.val)
                great_node = great_node.next
            else:
                small_node.next = ListNode(node.val)
                small_node = small_node.next
            
            node = node.next
        
        small_node.next = great_head.next
        return small_head.next