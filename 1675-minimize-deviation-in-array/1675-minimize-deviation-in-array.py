class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        minimum = float("inf")
        evens = []
        for num in nums:
            even = num * 2 if num % 2 == 1 else num
            minimum = min(even, minimum)
            evens.append(-even)
        
        heapq.heapify(evens)

        res = float("inf")
        while evens:
            curr = -heapq.heappop(evens)
            res = min(curr - minimum, res)
            
            if curr % 2 == 1: # 현재가 홀수면 최댓값이 더 이상 작아질 수 없음.
                break
            minimum = min(minimum, curr // 2)
            heapq.heappush(evens, -(curr // 2))

        return res