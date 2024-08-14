class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])

        def dfs(i, j):
            if i == 0 or i == M - 1:
                return False
            if j == 0 or j == N - 1:
                return False

            grid[i][j] = 1 # visited
            is_closed_island = True
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                next_i, next_j = i + di, j + dj
                if 0 <= next_i < M and 0 <= next_j < N and grid[next_i][next_j] == 0:
                    is_closed_island &= dfs(next_i, next_j)

            return is_closed_island                    
        
        res = 0
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                if grid[i][j] == 0:
                    if dfs(i, j):
                        res += 1
        
        return res