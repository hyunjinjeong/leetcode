class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # 걍 heap 써서 k개 찾으면 되는거 아닌가..?
        import heapq
        
        heap = []
        for x, y in points:
            distance = x ** 2 + y ** 2
            # min-heap을 max-heap으로 만들어서 큰 거는 빼기
            heapq.heappush(heap, (-distance, (x, y)))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [tup[1] for tup in heap]