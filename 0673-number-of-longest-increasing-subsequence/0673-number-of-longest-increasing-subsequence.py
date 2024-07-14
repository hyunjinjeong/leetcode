class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # LIS는 dp인데...
        # count를 따로 관리하기?
        N = len(nums)
        dp = [1] * N
        count = [1] * N

        for i in range(N):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    elif dp[j] + 1 == dp[i]:
                        count[i] += count[j]
        
        ans = 0
        lis_length = max(dp)
        for i in range(N):
            if dp[i] == lis_length:
                ans += count[i]

        return ans