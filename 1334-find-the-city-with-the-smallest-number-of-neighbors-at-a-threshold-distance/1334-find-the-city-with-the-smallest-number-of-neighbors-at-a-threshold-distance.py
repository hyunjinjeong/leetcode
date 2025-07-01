class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # brute force는 각 city에서 BFS를 돌려서 reachableCities 수를 구하면 될 것 같은데
        # 아 BFS로 돌다 보면 더 뒤에 있는데 distance가 짧은 애들이 스킵될 수 있음
        # 그럼 dijkstra로...
        def get_counts(start):
            heap = [(0, start)]
            dist = [float("inf") for _ in range(n)]
            dist[start] = 0

            visited = set()
            while heap:
                curr_dist, city = heapq.heappop(heap)
                
                if city in visited:
                    continue
                visited.add(city)
                
                for adj, adj_dist in graph[city]:
                    next_dist = curr_dist + adj_dist
                    if next_dist <= distanceThreshold and next_dist <= dist[adj]:
                        heapq.heappush(heap, (next_dist, adj))
                        dist[adj] = next_dist
            
            return len(visited) - 1 # 자기 자신 제외

        
        graph = {i: [] for i in range(n)}
        for start, end, distance in edges:
            graph[start].append((end, distance))
            graph[end].append((start, distance))
        
        lowest_city = 0
        lowest_count = float("inf")
        for city in range(n):
            count = get_counts(city)
            if count <= lowest_count:
                lowest_city = city
                lowest_count = count
        
        return lowest_city
