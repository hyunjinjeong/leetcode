class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        
        def dfs(i, j):
            if not 0 <= i < M or not 0 <= j < N:
                return
            if grid[i][j] == 0:
                return
            
            grid[i][j] = 0
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                next_i, next_j = i + di, j + dj
                dfs(next_i, next_j)
            
        for i in range(M):
            dfs(i, 0)
            dfs(i, N - 1)
        
        for j in range(N):
            dfs(0, j)
            dfs(M - 1, j)
        
        ans = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    ans += 1
        return ans