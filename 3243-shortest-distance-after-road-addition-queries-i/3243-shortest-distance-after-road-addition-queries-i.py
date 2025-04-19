class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # brute force는 매번 shortest path를 직접 구하는 방법
        # 일단 그렇게 해봅시다
        graph = {i: [] for i in range(n)}
        for i in range(n - 1):
            graph[i].append(i + 1)
        
        def get_shortest_path_to_end():
            visited = set([0])
            q = collections.deque([(0, 0)])
            while q:
                city, dist = q.popleft()
                if city == n - 1:
                    return dist
                
                for adj in graph[city]:
                    if adj not in visited:
                        q.append((adj, dist + 1))
                        visited.add(adj)
        
        res = []
        for query in queries:
            graph[query[0]].append(query[1])
            res.append(get_shortest_path_to_end())        
        return res
