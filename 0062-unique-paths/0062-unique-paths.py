class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp[i][j]를 grid[i][j]에서의 unique path 갯수라고 하면..
        # 기본적으로 dp[i][j] = dp[i-1][j] + dp[i][j-1] 가 될건데
        # 코너 케이스는 i나 j가 0인 경우? 다 1로 처리해주기.
        
        dp = [[0] * n for _ in range(m)]
        
        # 코너 케이스
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[-1][-1]