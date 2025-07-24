# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # in place로 바꿔야 하나보다
        # 2번 돌면 쉬운데 1번으로 되나
        # 0에다가 합을 저장하고 마지막 0은 버리면 될 듯?
        merged_node = head
        node = head.next

        while node:
            while node and node.val != 0:
                merged_node.val += node.val
                node = node.next
            
            merged_node.next = node if node.next is not None else None
            merged_node = node
            node = node.next
            
        return head
