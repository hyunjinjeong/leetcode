class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        # 간단하게 DFS 돌면 될 듯
        R, C = len(grid), len(grid[0])

        def dfs(r, c):
            if not (0 <= r < R and 0 <= c < C):
                return 0
            if grid[r][c] == 0:
                return 0
            if (r, c) in visited:
                return 0

            count = grid[r][c]
            visited.add((r, c))
            
            for adj_r, adj_c in [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]:
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
