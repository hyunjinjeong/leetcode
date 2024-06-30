class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        # 걍 큰거 2개 작은거 2개 뽑는거 아님?
        # 가장 간단하게 sorting...
        # min heap max heap 써도 될거고. <- 이걸로 해보자
        min_heap, max_heap = [], []

        for i in range(2):
            heapq.heappush(min_heap, nums[i])
            heapq.heappush(max_heap, -nums[i])
        
        for i in range(2, len(nums)):
            heapq.heappushpop(min_heap, nums[i])
            heapq.heappushpop(max_heap, -nums[i])
        
        # min_heap에는 큰거 2개, max_heap에는 작은거 2개.
        return min_heap[0] * min_heap[1] - max_heap[0] * max_heap[1]