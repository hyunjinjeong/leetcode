class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])

        q = collections.deque()
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    q.append((i, j))
        
        steps = -1 # 무조건 1번은 도니까
        while q:
            steps += 1

            # 여기를 한 번에 하나씩 하면 안 되고, 동시에 돌려야 함
            for _ in range(len(q)):
                i, j = q.popleft()

                for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    next_i, next_j = i + di, j + dj
                    if 0 <= next_i < M and 0 <= next_j < N and grid[next_i][next_j] == 0:
                        q.append((next_i, next_j))
                        grid[next_i][next_j] = 1 # visited
        
        return steps if steps > 0 else -1 # 다 1인 경우