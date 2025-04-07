class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(heap)

        count = 0
        while count < k:
            num, i = heapq.heappop(heap)
            heapq.heappush(heap, (num * multiplier, i))
            count += 1
        
        res = [0] * len(nums)
        for num, i in heap:
            res[i] = num
        return res