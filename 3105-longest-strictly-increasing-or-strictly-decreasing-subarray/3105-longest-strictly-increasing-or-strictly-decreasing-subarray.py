class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        res = 0
        streak = 1
        
        prev = nums[0]
        for num in nums:
            if num > prev:
                streak += 1
            else:
                streak = 1
            res = max(streak, res)
            prev = num
        
        prev = nums[0]
        for num in nums:
            if num < prev:
                streak += 1
            else:
                streak = 1
            res = max(streak, res)
            prev = num
        
        return res