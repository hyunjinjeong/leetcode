class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(row, col):
            if grid[row][col] == "0":
                return
            
            grid[row][col] = "0"
            
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dx, dy in directions:
                next_row, next_col = row + dx, col + dy
                if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]):
                    dfs(next_row, next_col)
            
        result = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                num = grid[row][col]
                if num == "1":
                    result += 1
                    dfs(row, col)
        
        return result