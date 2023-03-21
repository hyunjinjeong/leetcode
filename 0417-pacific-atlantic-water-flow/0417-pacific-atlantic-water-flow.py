class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # dfs에 visited 보면 될 듯.
        # 아.. 끝에서부터 시작해서 도달할 수 있는지를 확인하면 되는구나
        pacific_visited = set()
        atlantic_visited = set()

        M, N = len(heights), len(heights[0])
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def dfs(x, y, visited):
            if (x, y) in visited:
                return
            visited.add((x, y))
            
            for dx, dy in directions:
                next_x, next_y = x + dx, y + dy
                if 0 <= next_x < M and 0 <= next_y < N:
                    # 조건 체크
                    if heights[next_x][next_y] >= heights[x][y]:
                        dfs(next_x, next_y, visited)
        
        for r in range(M):
            dfs(r, 0, pacific_visited)
            dfs(r, N-1, atlantic_visited)
        
        for c in range(N):
            dfs(0, c, pacific_visited)
            dfs(M-1, c, atlantic_visited)
        
        ans = []
        for r in range(M):
            for c in range(N):
                if (r, c) in pacific_visited and (r, c) in atlantic_visited:
                    ans.append([r, c])
        return ans