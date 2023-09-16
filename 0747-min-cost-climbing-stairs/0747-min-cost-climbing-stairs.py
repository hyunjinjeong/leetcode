class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp...
        # 근데 0에서 시작할 수도 있고 1에서 시작할 수도 있음
        # dp[i] = cost[i] + min(dp[i+1], dp[i+2])
        # 뒤에서부터 거꾸로 돌면 됨
        N = len(cost)

        dp = [0] * N
        dp[N-1] = cost[N-1]
        dp[N-2] = cost[N-2]

        for i in range(N-3, -1, -1):
            dp[i] = cost[i] + min(dp[i+1], dp[i+2])
        
        return min(dp[0], dp[1])