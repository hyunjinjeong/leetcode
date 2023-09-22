class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        # dp
        dp = [1] * N

        for i in range(N):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])
            
        return max(dp)