class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # dp인줄 알았는데 아니었다
        # 전체 sum을 구한 다음에 subarray 중 sum - x인게 있는지 찾으면 됨
        target_sum = sum(nums) - x
        
        res = -1
        left, curr = 0, 0
        for right in range(len(nums)):
            curr += nums[right]
            while left <= right and curr > target_sum:
                curr -= nums[left]
                left += 1
            if curr == target_sum:
                res = max(res, right - left + 1)
        
        return len(nums) - res if res != -1 else -1