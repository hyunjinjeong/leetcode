class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Minimum Spanning Tree 알고리즘..? 근데 어케 쓰지
        # 그래프를 생성해서 돌리면 된다.
        graph = collections.defaultdict(set)

        for i in range(len(points)):
            for j in range(i+1, len(points)):
                distance = self.distance(points[i], points[j])
                graph[i].add((j, distance))
                graph[j].add((i, distance))
        
        # 1. Prim 알고리즘
        ans = 0
        visited = set()
        heap = [(0, 0)]
        while heap:
            distance, index = heapq.heappop(heap)
            if index in visited:
                continue
            
            visited.add(index)
            ans += distance

            for n_index, n_distance in graph[index]:
                if n_index not in visited:
                    heapq.heappush(heap, (n_distance, n_index))
        
        return ans
        
        # 2. Kruskal 알고리즘

    
    def distance(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])