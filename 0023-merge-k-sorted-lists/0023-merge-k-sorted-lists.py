# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # heap에다가 넣고 하나씩 뽑으면 되지 않을까..?
        dummy_head = ListNode()

        heap = []
        for index, node in enumerate(lists):
            if node:
                # index는 tie breaker... 
                heapq.heappush(heap, (node.val, index, node))
                index += 1

        curr = dummy_head
        while heap:
            val, index, node = heapq.heappop(heap)
            if node.next:
                heapq.heappush(heap, (node.next.val, index, node.next))

            curr.next = node
            curr = curr.next

        return dummy_head.next