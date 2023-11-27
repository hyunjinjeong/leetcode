class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        M, N = len(rooms), len(rooms[0])
        INF = 2147483647
        
        # gate에서부터 시작하는게 더 쉬울듯?
        # dfs보단 bfs가 편할 것 같고
        
        q = collections.deque()
        for i in range(M):
            for j in range(N):
                if rooms[i][j] == 0:
                    q.append((i, j))
        
        distance = 0
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                rooms[i][j] = min(distance, rooms[i][j])
                for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < M and 0 <= nj < N and rooms[ni][nj] > distance:
                        q.append((ni, nj))
            
            distance += 1