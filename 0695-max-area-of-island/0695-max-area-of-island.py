class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                ans = max(self.get_island_area(x, y, 0, grid), ans)
        return ans
        
    def get_island_area(self, x, y, curr_area, grid):
        val = grid[x][y]
        if val != 1:
            return 0
        
        grid[x][y] = 0 # visited
        sub_area = 0
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_x, next_y = x + dx, y + dy
            if 0 <= next_x < len(grid) and 0 <= next_y < len(grid[0]) and grid[next_x][next_y] == 1:
                sub_area += self.get_island_area(next_x, next_y, curr_area, grid)
        
        return 1 + sub_area