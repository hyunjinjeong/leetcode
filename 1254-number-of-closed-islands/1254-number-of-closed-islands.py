class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or i > M - 1 or j < 0 or j > N - 1:
                return 0
            if grid[i][j] == 1:
                return 1

            grid[i][j] = 1 # visited

            left = dfs(i, j - 1)
            right = dfs(i, j + 1)
            up = dfs(i - 1, j)
            down = dfs(i + 1, j)

            return 1 if left and right and up and down else 0
        
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    res += dfs(i, j)
        
        return res