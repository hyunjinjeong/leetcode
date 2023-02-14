class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(row, col):
            if row < 0 or row >= len(grid):
                return
            if col < 0 or col >= len(grid[0]):
                return
            if grid[row][col] == "0":
                return
            
            grid[row][col] = "0"
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)
        
        result = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                num = grid[row][col]
                if num == "0":
                    continue
                result += 1
                dfs(row, col)
        
        return result