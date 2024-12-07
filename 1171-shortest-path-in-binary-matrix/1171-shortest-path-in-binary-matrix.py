class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # graph일 듯. dp는 sub problem 정의하기가 어렵다.
        # 8방향에 대해서 다 탐색하면서.. 간단하게 BFS?
        # 음 dijkstra 쓰면 되려나
        N = len(grid)
        if grid[0][0] == 1 or grid[N - 1][N - 1] == 1:
            return -1

        heap = [(1, 0, 0)]
        visited = set([(0, 0)])
        while heap:
            length, r, c = heapq.heappop(heap)
            if (r, c) == (N - 1, N - 1):
                return length

            for adj_r, adj_c in [(r, c + 1), (r, c - 1), (r - 1, c), (r + 1, c)
                , (r + 1, c + 1), (r + 1, c - 1), (r - 1, c + 1), (r - 1, c - 1)]:
                if 0 <= adj_r < N and 0 <= adj_c < N and grid[adj_r][adj_c] == 0 and (adj_r, adj_c) not in visited:
                    heapq.heappush(heap, (length + 1, adj_r, adj_c))
                    visited.add((adj_r, adj_c))
            
        return -1