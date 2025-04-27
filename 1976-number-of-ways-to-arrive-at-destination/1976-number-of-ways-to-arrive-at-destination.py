class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # shortest path count를 저장하는게 핵심이었음
        MOD = 10 ** 9 + 7

        graph = [[] for _ in range(n)]
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))
        
        shortest_times = [float("inf")] * n
        shortest_times[0] = 0

        path_counts = [0] * n
        path_counts[0] = 1
        
        heap = [(0, 0)]
        while heap:
            curr_time, curr_node = heapq.heappop(heap)
            for adj_node, adj_time in graph[curr_node]:
                if curr_time + adj_time < shortest_times[adj_node]:
                    shortest_times[adj_node] = curr_time + adj_time
                    path_counts[adj_node] = path_counts[curr_node]
                    heapq.heappush(heap, (shortest_times[adj_node], adj_node))
                elif curr_time + adj_time == shortest_times[adj_node]:
                    path_counts[adj_node] = (path_counts[adj_node] + path_counts[curr_node]) % MOD

        return path_counts[n - 1]
