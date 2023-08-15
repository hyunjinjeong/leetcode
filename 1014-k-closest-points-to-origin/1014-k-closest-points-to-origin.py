class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # heap 써서 k번 뽑으면?
        heap = []
        for point in points:
            distance = point[0]**2 + point[1]**2 # root는 안 씌워도 될 듯?
            heapq.heappush(heap, (distance, point))
        
        ans = []
        while len(ans) < k:
            _, point = heapq.heappop(heap)
            ans.append(point)
        
        return ans