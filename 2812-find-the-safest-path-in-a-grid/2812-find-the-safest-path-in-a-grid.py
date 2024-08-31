class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        N = len(grid)

        # 음.. 1인 cell들로부터 BFS 돌리면 각각의 distance는 구할 수 있는데
        # 그걸로 max 값을 어떻게 낼 수 있으려나
        # greedy는 안 되는 구나...가 아니고 제대로 구현하면 되네
        # 사실상의 다익스트라였음.
        q = collections.deque()
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    q.append((r, c, 0))
        
        factor = [[0] * N for _ in range(N)]
        
        visited = set()
        while q:
            r, c, distance = q.popleft()
            if (r, c) in visited:
                continue
            visited.add((r, c))

            factor[r][c] = distance
            for next_r, next_c in [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]:
                if 0 <= next_r < N and 0 <= next_c < N and (next_r, next_c) not in visited:
                    next_distance = distance + 1 if grid[next_r][next_c] == 0 else 0
                    q.append((next_r, next_c, next_distance))
        
        res = 0
        heap = [(-factor[0][0], 0, 0)]
        visited = set()

        while heap:
            distance, r, c = heapq.heappop(heap)
            if (r, c) in visited:
                continue
            visited.add((r, c))

            if r == N - 1 and c == N - 1:
                res = -distance
                break
            
            for next_r, next_c in [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]:
                if 0 <= next_r < N and 0 <= next_c < N and (next_r, next_c) not in visited:
                    heapq.heappush(heap, (-min(-distance, factor[next_r][next_c]), next_r, next_c))
            
        return res
