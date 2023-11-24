class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # 옆의 cell이 water거나 없으면 1 더하면 되려나
        # dfs 돌 필요도 없이 그냥 하나씩 체크하면 될 듯?
        M, N = len(grid), len(grid[0])
        ans = 0
        
        for r in range(M):
            for c in range(N):
                if grid[r][c] == 1:
                    # left
                    if c == 0 or grid[r][c-1] == 0:
                        ans += 1
                    # right
                    if c == N - 1 or grid[r][c+1] == 0:
                        ans += 1
                    # up
                    if r == 0 or grid[r-1][c] == 0:
                        ans += 1
                    # down
                    if r == M - 1 or grid[r+1][c] == 0:
                        ans += 1
        
        return ans