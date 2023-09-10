class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Minimum Spanning Tree 알고리즘...
        
        # # 1. Prim 알고리즘. Priority Queue 이용.
        # graph = collections.defaultdict(list)

        # for i in range(len(points)):
        #     for j in range(i+1, len(points)):
        #         distance = self.distance(points[i], points[j])
        #         graph[i].append((j, distance))
        #         graph[j].append((i, distance))
        
        # ans = 0
        # visited = set()
        # heap = [(0, 0)]
        # while heap:
        #     distance, index = heapq.heappop(heap)
        #     if index in visited:
        #         continue
            
        #     visited.add(index)
        #     ans += distance

        #     for n_index, n_distance in graph[index]:
        #         if n_index not in visited:
        #             heapq.heappush(heap, (n_distance, n_index))
        
        # return ans

        # 2. Kruskal 알고리즘. Union-Find 사용
        edges = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                distance = self.distance(points[i], points[j])
                edges.append([distance, i, j])

        ans = 0        
        uf = UnionFind(len(points))

        edges.sort() # 거리 순으로 정렬 필요
        for distance, u, v in edges:
            if uf.find(u) == uf.find(v):
                continue

            uf.union(u, v)
            ans += distance

        return ans

    def distance(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
    
    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u]) # path compression
        return self.parent[u]
    
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if self.size[pu] > self.size[pv]: # Union by rank
            self.size[pu] += self.size[pv]
            self.parent[pv] = self.parent[pu]
        else:
            self.size[pv] += self.size[pu]
            self.parent[pu] = self.parent[pv]