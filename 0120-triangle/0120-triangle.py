class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [0] * (len(triangle) + 1)

        for row in reversed(triangle):
            new_dp = [0] * (len(row) + 1)
            for i in range(len(row)):
                new_dp[i] = row[i] + min(dp[i], dp[i + 1])
            dp = new_dp
        
        return dp[0]