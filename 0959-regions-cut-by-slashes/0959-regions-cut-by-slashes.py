class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        # region이 나뉘는걸 어떻게 알 수 있지?
        # 0, 1로 바꾸면 섬 개수 구하는 문제랑 같아진다고 함. 근데 이런 직관을 어떻게 얻는 걸까..;
        N = len(grid)

        graph = [[0] * (3 * N) for _ in range(3 * N)]
        for i in range(N):
            row = i * 3
            for j in range(N):
                col = j * 3
                if grid[i][j] == "/":
                    graph[row][col + 2] = 1
                    graph[row + 1][col + 1] = 1
                    graph[row + 2][col] = 1
                elif grid[i][j] == "\\":
                    graph[row][col] = 1
                    graph[row + 1][col + 1] = 1
                    graph[row + 2][col + 2] = 1
        
        def dfs(r, c):
            graph[r][c] = -1
            for adj_r, adj_c in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if 0 <= adj_r < len(graph) and 0 <= adj_c < len(graph) and graph[adj_r][adj_c] == 0:
                    dfs(adj_r, adj_c)
            
        regions = 0
        for r in range(len(graph)):
            for c in range(len(graph)):
                if graph[r][c] == 0:
                    dfs(r, c)
                    regions += 1

        return regions
