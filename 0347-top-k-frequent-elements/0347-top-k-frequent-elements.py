class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # 3 2 4 1 5면 
        # 3 2 -> 3 4 -> 1 4 -> 4 5

        # Build a counter and use k-sized min-heap
        counter = collections.Counter(nums)
        min_heap = []

        for num, count in counter.items():
            if len(min_heap) < k:
                heapq.heappush(min_heap, (count, num))
            else:
                heapq.heappushpop(min_heap, (count, num))

        res = []
        for _ in range(k):
            _, num = heapq.heappop(min_heap)
            res.append(num)
        
        return res

