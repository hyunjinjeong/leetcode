class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 너무 dp 문젠데
        M, N = len(grid), len(grid[0])

        @cache
        def dfs(i, j):
            right = dfs(i + 1, j) if i + 1 < M else float("inf")
            down = dfs(i, j + 1) if j + 1 < N else float("inf")
            
            sub_min = min(right, down) if min(right, down) != float("inf") else 0
            return sub_min + grid[i][j]

        return dfs(0, 0)