class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[n]은 nums[n]으로 끝나는 LIS 길이
        dp = [1] * len(nums)
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
        
        return max(dp)