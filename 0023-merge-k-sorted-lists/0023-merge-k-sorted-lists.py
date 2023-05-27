# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 포인터가 k개가 있는데
        # 그러면 k개 중 최솟값을 찾아서 계속 돌려야 함.
        # brute force로 하면 매번 k번 도니까.. O(kn)일 건데
        # 생각해보니까 어차피 이거 다 돌아야 하는구나.. 그럼 시간은 저게 최소인듯?
        # 다 heap에 넣어서 빼는 건 어떨까..
        heap = []
        for node in lists:
            n = node
            while n:
                heapq.heappush(heap, n.val)
                n = n.next
        
        dummy_head = ListNode()
        node = dummy_head
        while heap:
            node.next = ListNode(heapq.heappop(heap))
            node = node.next
        
        return dummy_head.next