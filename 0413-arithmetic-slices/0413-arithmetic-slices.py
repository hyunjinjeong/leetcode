class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        N = len(nums)
        res = 0

        dp = [0] * N
        for i in range(2, N):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                dp[i] += dp[i - 1] + 1
                res += dp[i]
        
        return res