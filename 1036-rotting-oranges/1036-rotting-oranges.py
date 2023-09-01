class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 이건 BFS 같은데?
        # 2인 cell들을 처음에 골라서 넣어두고 N번 돌고..
        # 근데도 1인 cell이 있으면 -1인거
        M, N = len(grid), len(grid[0])
        
        q = collections.deque()
        fresh_orange_count = 0
        
        for r in range(M):
            for c in range(N):
                orange = grid[r][c]
                if orange == 2:
                    q.append((r, c))
                elif orange == 1:
                    fresh_orange_count += 1
        
        minute = 0
        while q and fresh_orange_count > 0: # fresh도 체크...
            minute += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    next_r, next_c = r + dr, c + dc
                    if 0 <= next_r < M and 0 <= next_c < N and grid[next_r][next_c] == 1:
                        grid[next_r][next_c] = 2
                        fresh_orange_count -= 1
                        q.append((next_r, next_c))
        
        return minute if fresh_orange_count == 0 else -1