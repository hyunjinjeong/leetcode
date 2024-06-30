class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # # 너무 dp 문젠데
        # M, N = len(grid), len(grid[0])

        # @cache
        # def dfs(i, j):
        #     right = dfs(i + 1, j) if i + 1 < M else float("inf")
        #     down = dfs(i, j + 1) if j + 1 < N else float("inf")
            
        #     sub_min = min(right, down) if min(right, down) != float("inf") else 0
        #     return sub_min + grid[i][j]

        # return dfs(0, 0)

        # bottom up으로 풀어보자
        M, N = len(grid), len(grid[0])
        dp = [[float("inf")] * (N+1) for _ in range(M+1)]

        # dp[i][j] = min(dp[i+1][j], dp[i][j+1]) + grid[i][j]
        # 33 
        for i in range(M-1, -1, -1):
            for j in range(N-1, -1, -1):
                if i + 1 < M or j + 1 < N:
                    dp[i][j] = min(dp[i+1][j], dp[i][j+1]) + grid[i][j]
                else:
                    dp[i][j] = grid[i][j]
        
        return dp[0][0]