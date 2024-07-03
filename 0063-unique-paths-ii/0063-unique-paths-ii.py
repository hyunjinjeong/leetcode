class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        M, N = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * N for _ in range(M)]

        row_has_obstacle, col_has_obstacle = False, False
        for i in range(M):
            if obstacleGrid[i][0] == 1:
                row_has_obstacle = True
            dp[i][0] = 0 if row_has_obstacle else 1
        for j in range(N):
            if obstacleGrid[0][j] == 1:
                col_has_obstacle = True
            dp[0][j] = 0 if col_has_obstacle else 1

        for i in range(1, M):
            for j in range(1, N):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[M-1][N-1]