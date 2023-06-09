class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
        right = float("-inf")
        for i, lst in enumerate(nums):
            num = lst[0]
            heapq.heappush(heap, (num, i, 0))
            right = max(right, num)
        
        ans = [float("-inf"), float("inf")]
        while heap:
            left, i, j = heapq.heappop(heap)
            if right - left < ans[1] - ans[0]: # 길이가 같으면 기존꺼 유지
                ans = [left, right]
            
            if j + 1 == len(nums[i]): # 리스트 하나라도 끝나면 더 이상 의미 없음
                break
            
            # pop된 리스트에서 넣기
            num = nums[i][j+1]
            right = max(right, num)
            heapq.heappush(heap, (num, i, j+1))
        
        return ans