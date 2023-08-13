class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # max heap을 쓰면 될 듯?
        # 2번 꺼내서 계산하고 다시 넣고... 이렇게 해서 1개가 될 때까지 반복
        max_heap = []
        for stone in stones:
            heapq.heappush(max_heap, -1 * stone)
        
        while len(max_heap) > 1:
            heavier = -1 * heapq.heappop(max_heap)
            lighter = -1 * heapq.heappop(max_heap)
            
            remaining = heavier - lighter
            if remaining:
                heapq.heappush(max_heap, -1 * remaining)
        
        return -1 * max_heap[0] if max_heap else 0