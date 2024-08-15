class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # 두 섬을 하나로 잇기 위한 최소 flip 수
        # 섬 두 개를 찾는거야 쉬운데
        # 요걸 하나로 만들려면? 뭘 해야 하지
        # 특정 좌표가 섬 1인지 섬 2인지를 저장해두고
        # 섬 1에서 시작해서.. 섬 2를 만날 때까지 여행을 떠나면 되지 않을까
        # -> 그러면 두 개를 찾을 필요 없이 섬을 하나만 찾고 나머지 하나를 찾으면 될 듯?
        N = len(grid)

        island_1 = set()
        q = collections.deque()

        def dfs(i, j, visited):
            if i < 0 or i >= N or j < 0 or j >= N:
                return
            if (i, j) in visited:
                return
            if grid[i][j] == 0:
                visited.add((i, j))
                q.append((i, j)) # 경계선은 모두 담자
                return
            
            visited.add((i, j))
            island_1.add((i, j))
            
            dfs(i + 1, j, visited)
            dfs(i - 1, j, visited)
            dfs(i, j + 1, visited)
            dfs(i, j - 1, visited)

        def find_island():
            # 1. 섬 1을 찾고...
            for i in range(N):
                for j in range(N):
                    if grid[i][j] == 1:
                        dfs(i, j, set())
                        return

        find_island()

        # 2. 섬 2로 여행을 떠나자
        cnt = 0
        visited = set()
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                if grid[i][j] == 1:
                    if (i, j) not in island_1:
                        return cnt
                else:
                    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        next_i, next_j = i + di, j + dj
                        if 0 <= next_i < N and 0 <= next_j < N and (next_i, next_j) not in visited:
                            q.append((next_i, next_j))
                            visited.add((next_i, next_j))
            
            cnt += 1