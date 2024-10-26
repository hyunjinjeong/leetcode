class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        # 아무 cell에서 시작해서 모든 방향으로 갈 수 있고, 각 cell은 한 번만 방문 가능, 0인 cell은 방문 불가.
        # 모든 cell에서 DFS 돌려보고 max값을 구하면 될 것 같은데?

        def dfs(r, c):
            value = grid[r][c]
            grid[r][c] = 0 # visited
            
            sub_max = 0
            for next_r, next_c in [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]:
                if 0 <= next_r < M and 0 <= next_c < N and grid[next_r][next_c] > 0:
                    sub_max = max(sub_max, dfs(next_r, next_c))
            
            grid[r][c] = value
            return value + sub_max
        
        M, N = len(grid), len(grid[0])

        res = 0
        for r in range(M):
            for c in range(N):
                if grid[r][c] > 0:
                    res = max(res, dfs(r, c))

        return res