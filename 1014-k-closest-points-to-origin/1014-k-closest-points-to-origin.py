class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # size가 k인 max-heap 쓰면 될 듯?
        heap = []
        for point in points:
            distance = point[0]**2 + point[1]**2
            heapq.heappush(heap, (-distance, point)) 

            if len(heap) > k:
                heapq.heappop(heap)
        
        return [tup[1] for tup in heap]