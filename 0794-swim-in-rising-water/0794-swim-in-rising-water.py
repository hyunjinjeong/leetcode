class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # Union Find 쓰면 되지 않으려나?
        # 시간에 따라서 슉슉 합치고
        # (0, 0), (n-1, n-1)이 같은 부모가 되면 해당 시간 리턴하는 식으로...
        # heap 쓰면 매번 돌지 않고 뽑아낼 수 있음...
        def get_pos(r, c):
            return r * N + c

        def merge(r, c):
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                next_r, next_c = r + dr, c + dc
                if 0 <= next_r < N and 0 <= next_c < N and grid[next_r][next_c] <= grid[r][c]:
                    pos = get_pos(r, c)
                    next_pos = get_pos(next_r, next_c)
                    if uf.union(pos, next_pos):
                        merge(next_r, next_c)

        N = len(grid)

        # heap 만들기
        heap = []
        for r in range(N):
            for c in range(N):
                heap.append((grid[r][c], r, c))
        heapq.heapify(heap)

        uf = UnionFind(N * N)
        while heap:
            time, r, c = heapq.heappop(heap)
            merge(r, c)
            if uf.find(get_pos(0, 0)) == uf.find(get_pos(N-1, N-1)):
                return time

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
    
    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        
        if self.size[pu] > self.size[pv]:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
        else:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]
        
        return True