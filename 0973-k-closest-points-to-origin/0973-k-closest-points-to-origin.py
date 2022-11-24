class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # 걍 heap 써서 k개 찾으면 되는거 아닌가..?
        import heapq
        
        def get_distance(x, y):
            return x ** 2 + y ** 2
        
        heap = []
        for x, y in points:
            heapq.heappush(heap, (get_distance(x, y), (x, y)))
        
        answer = []
        for _ in range(k):
            answer.append(heapq.heappop(heap)[1])
        
        return answer