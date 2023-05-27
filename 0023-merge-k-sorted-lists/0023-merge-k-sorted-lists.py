# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # heap을 사용하는데 k개만큼만 넣으면서 하는 방법도 있다!
        # 이 경우 전체 갯수를 n개라고 하면 시간은 O(nlogk), 공간은 O(k).
        heap = []
        for i, node in enumerate(lists):
            # index를 넣는건 heapq 모듈이 tuple 순서대로 비교하기 떄문에..
            # 값이 같은 경우 tie breaker임.
            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        dummy_head = ListNode()
        node = dummy_head
        while heap:
            # 가장 작은 원소를 꺼내서 연결하고...
            _val, index, temp_node = heapq.heappop(heap)
            
            node.next = temp_node
            node = node.next
            # 그 다음꺼 heap에다가 넣기
            if node.next:
                heapq.heappush(heap, (node.next.val, index, node.next))
        
        return dummy_head.next