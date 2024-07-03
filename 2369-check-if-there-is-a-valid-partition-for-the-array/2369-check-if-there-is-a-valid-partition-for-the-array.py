class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        dp = [False] * N + [True]

        for i in range(N-1, -1, -1):
            if i >= 1:
                if nums[i] == nums[i-1]:
                    dp[i-1] |= dp[i+1]
            if i >= 2:
                if nums[i] == nums[i-1] + 1 and nums[i-1] == nums[i-2] + 1 or nums[i] == nums[i-1] and nums[i-1] == nums[i-2]:
                    dp[i-2] |= dp[i+1]
        
        return dp[0]