class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        res = 0
        increasing, decreasing = 1, 1
        
        prev = nums[0]
        for num in nums:
            if num > prev:
                increasing += 1
                decreasing = 1
            elif num < prev:
                increasing = 1
                decreasing += 1
            else:
                increasing = 1
                decreasing = 1
            res = max(res, increasing, decreasing)
            prev = num
        
        return res