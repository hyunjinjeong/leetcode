# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # 0-indexed인데 1부터 시작이니까 dummy는 필요 없겠다.
        # a-1번째 노드의 next를 list2.head로, list2.tail의 next를 b+1번째 노드로 하면 될 듯

        node = list1
        count = 0

        while count < a - 1:
            node = node.next
            count += 1
        a_prev = node

        while count < b + 1:
            node = node.next
            count += 1
        b_next = node

        node = list2
        while node and node.next:
            node = node.next
        
        a_prev.next = list2
        node.next = b_next

        return list1