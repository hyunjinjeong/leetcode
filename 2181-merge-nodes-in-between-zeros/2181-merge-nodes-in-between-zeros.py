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
            merged_sum = 0
            while node and node.val != 0:
                merged_sum += node.val
                node = node.next
            
            merged_node.val = merged_sum

            node = node.next
            merged_node.next = node
            
            merged_node = merged_node.next
            
        return head
