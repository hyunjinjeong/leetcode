class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        # island가 하나만 있을 때가 connected. 그러면 2개로만 쪼개면 disconnected임
        # 처음부터 disconnected일 수도 있다. 1의 개수를 세서 모두 연결되어 있는지 확인하면 됨
        # connected grid를 disconnect 시키려면? 일단 max가 2인데? 모서리에 2개 떼어내면 됨.
        M, N = len(grid), len(grid[0])

        def dfs(i, j, visited):
            if not (0 <= i < M):
                return
            if not (0 <= j < N):
                return
            if grid[i][j] == 0:
                return
            if (i, j) in visited:
                return

            visited.add((i, j))
            for adj_i, adj_j in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                dfs(adj_i, adj_j, visited)
        
        def get_island_count():
            island_count = 0
            visited = set()
            for i in range(M):
                for j in range(N):
                    if grid[i][j] == 1 and (i, j) not in visited:
                        dfs(i, j, visited)
                        island_count += 1
            return island_count

        if get_island_count() != 1:
            return 0

        for i in range(M):
            for j in range(N):
                if grid[i][j] == 0:
                    continue
                
                grid[i][j] = 0
                if get_island_count() != 1:
                    return 1
                grid[i][j] = 1
        
        return 2