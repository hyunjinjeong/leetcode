class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # 답은 맞았는데 코드를 좀 정리하자...
        N = len(grid)

        # 1. 섬 찾기
        def find_first_island_coordinates():
            for i in range(N):
                for j in range(N):
                    if grid[i][j] == 1:
                        return (i, j)
        
        first_x, first_y = find_first_island_coordinates()

        # 2. 섬 하나 찾기
        q = collections.deque()
        def dfs(i, j, visited):
            if (i, j) in visited:
                return
            
            visited.add((i, j))
            if grid[i][j] == 0:
                q.append((i, j)) # 경계는 queue에 넣기
                return

            grid[i][j] = 2 # visited 처리
            for next_i, next_j in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= next_i < N and 0 <= next_j < N:
                    dfs(next_i, next_j, visited)
        
        dfs(first_x, first_y, set())
        
        # 3. minimum count 구하기
        cnt = 0
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                if grid[i][j] == 1:
                    return cnt
                elif grid[i][j] == 0:
                    grid[i][j] = 2 # visited 처리
                    for next_i, next_j in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                        if 0 <= next_i < N and 0 <= next_j < N:
                            q.append((next_i, next_j))
            cnt += 1