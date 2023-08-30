class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        M, N = len(heights), len(heights[0])
        p_visited, a_visited = set(), set()

        for row in range(M):
            self.dfs(row, 0, p_visited, heights)
            self.dfs(row, N - 1, a_visited, heights)
        
        for col in range(N):
            self.dfs(0, col, p_visited, heights)
            self.dfs(M - 1, col, a_visited, heights)
        
        return [[dup[0], dup[1]] for dup in p_visited & a_visited]
    
    # 조건을 반대로 해서 edge에서 각 점에 도달 가능하면 됨. p, a 모두 도달한 점들이 답.
    def dfs(self, x, y, visited, heights):
        if (x, y) in visited:
            return
        
        visited.add((x, y))
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_x, next_y = x + dx, y + dy
            if 0 <= next_x < len(heights) and 0 <= next_y < len(heights[0]) and (next_x, next_y) not in visited and heights[next_x][next_y] >= heights[x][y]:
                self.dfs(next_x, next_y, visited, heights)