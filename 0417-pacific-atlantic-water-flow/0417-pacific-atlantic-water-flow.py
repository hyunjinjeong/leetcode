class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ans = []
        for x in range(len(heights)):
            for y in range(len(heights[0])):
                if self.is_pacific_valid(x, y, heights) and self.is_atlantic_valid(x, y, heights):
                    ans.append([x, y])
        return ans
    
    def is_pacific_valid(self, x, y, heights):
        if x == 0 or y == 0:
            return True

        ans = False

        current_val = heights[x][y]
        heights[x][y] = "#"
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_x, next_y = x + dx, y + dy
            if 0 <= next_x < len(heights) and 0 <= next_y < len(heights[0]) and heights[next_x][next_y] != "#" and heights[next_x][next_y] <= current_val:
                ans = self.is_pacific_valid(next_x, next_y, heights) or ans
                if ans:
                    break
        heights[x][y] = current_val
        
        return ans
    
    def is_atlantic_valid(self, x, y, heights):
        if x == len(heights) - 1 or y == len(heights[0]) - 1:
            return True

        ans = False

        current_val = heights[x][y]
        heights[x][y] = "#"
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_x, next_y = x + dx, y + dy
            if 0 <= next_x < len(heights) and 0 <= next_y < len(heights[0]) and heights[next_x][next_y] != "#" and heights[next_x][next_y] <= current_val:
                ans = self.is_atlantic_valid(next_x, next_y, heights) or ans
                if ans:
                    break
        heights[x][y] = current_val
        
        return ans