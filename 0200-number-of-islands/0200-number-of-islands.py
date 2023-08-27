class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if self.is_island(row, col, grid):
                    ans += 1
        return ans
    
    def is_island(self, row, col, grid):
        val = grid[row][col]
        if val != "1":
            return False
        
        grid[row][col] = "#" # visited
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_row, next_col = row + dx, col + dy
            if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]) and grid[next_row][next_col] == "1":
                self.is_island(next_row, next_col, grid)

        return True