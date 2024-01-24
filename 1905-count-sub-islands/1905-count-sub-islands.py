class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        # 둘이 크기가 동일하니까 grid2에서 dfs를 돌면서
        # grid1에도 동시에 돌아서 grid2가 1일때 grid1도 1인지 확인하면 될 듯?
        # 둘 중 하나가 0이면 빠져나오면 되고..
        M, N = len(grid1), len(grid1[0])
        visited = set()

        def dfs(i, j, is_valid):
            visited.add((i, j))
        
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                next_i, next_j = i + di, j + dj
                if 0 <= next_i < M and 0 <= next_j < N and grid2[next_i][next_j] == 1 and (next_i, next_j) not in visited:
                    is_valid = dfs(next_i, next_j, grid1[next_i][next_j] == 1) and is_valid
            
            return 1 if is_valid else 0
        
        ans = 0
        for i in range(M):
            for j in range(N):
                if grid2[i][j] == 1 and (i, j) not in visited:
                    ans += dfs(i, j, grid1[i][j] == 1)
        
        print(visited)

        return ans