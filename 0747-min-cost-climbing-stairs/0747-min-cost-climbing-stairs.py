class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp...
        # 근데 0에서 시작할 수도 있고 1에서 시작할 수도 있음
        N = len(cost)
        dp = [0] * N
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, N):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        
        return min(dp[N-1], dp[N-2])