class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp. dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        N = len(nums)
        # 엣지 케이스
        if N == 1:
            return nums[0]
        if N == 2:
            return max(nums[0], nums[1])

        dp = [0] * N
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, N):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        
        return dp[N-1]
            

        