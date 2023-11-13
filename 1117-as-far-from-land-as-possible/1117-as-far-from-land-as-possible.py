class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        # cache = {}

        # 적당히 dfs 돌리면 될 거 같은디
        # 이 방식으론 안 됨... 4방향 탐색할 때 무한 재귀... bfs로 가보자.
        # def dfs(i, j):
        #     print(i, j)

        #     if not (0 <= i < M and 0 <= j < N):
        #         return 0
        #     if grid[i][j] == 1:
        #         return 0
        #     if (i, j) in cache:
        #         return cache[(i, j)]
            
        #     # 상하좌우
        #     left = dfs(i - 1, j)
        #     right = dfs(i + 1, j)
        #     up = dfs(i, j - 1)
        #     down = dfs(i, j + 1)

        #     cache[(i, j)] = max(left, right, up, down) + 1
        #     return res
        q = collections.deque()
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    q.append((i, j))
        
        steps = -1
        while q:
            steps += 1

            # 아 여기를 한 번에 하나씩 하면 안 되고, 1에서 동시에 돌려야 함
            for _ in range(len(q)):
                i, j = q.popleft()

                for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    next_i, next_j = i + di, j + dj
                    if 0 <= next_i < M and 0 <= next_j < N and grid[next_i][next_j] == 0:
                        q.append((next_i, next_j))
                        grid[next_i][next_j] = 1 # visited
        
        return steps if steps > 0 else -1 # 다 1인 경우