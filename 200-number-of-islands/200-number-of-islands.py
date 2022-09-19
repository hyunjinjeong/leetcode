class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 그냥 DFS로 하나씩 다 찾으면 되지 않으려나?
        # 1이 나올 때마다 DFS 돌리고 갯수 +1씩 해주면 될 것 같음
        visited = set()
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        m, n  = len(grid), len(grid[0])
        
        def dfs(x, y):
            if (x, y) in visited:
                return
            
            visited.add((x, y))
            for dx, dy in directions:
                next_x, next_y = x+dx, y+dy
                if 0 <= next_x < m and 0 <= next_y < n and grid[next_x][next_y] == "1":
                    dfs(next_x, next_y)
        
        ans = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y] == "1" and (x, y) not in visited:
                    ans += 1
                    dfs(x, y)
        
        return ans