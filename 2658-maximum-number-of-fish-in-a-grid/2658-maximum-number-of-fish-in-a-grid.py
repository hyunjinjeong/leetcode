class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        # 간단하게 DFS 돌면 될 듯
        R, C = len(grid), len(grid[0])

        def dfs(r, c):
            count = grid[r][c]
            grid[r][c] = -1 # mark visited
            
            for adj_r, adj_c in [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]:
                if 0 <= adj_r < R and 0 <= adj_c < C and grid[adj_r][adj_c] > 0:
                    count += dfs(adj_r, adj_c)
            
            return count
        
        visited = set()
        
        res = 0
        for r in range(R):
            for c in range(C):
                cell = grid[r][c]
                if cell > 0:
                    res = max(dfs(r, c), res)
        
        return res
