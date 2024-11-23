class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        N = len(graph)

        reversed_graph = {i: [] for i in range(N)}
        in_degree = {i: 0 for i in range(N)}

        for node in range(N):
            for nei in graph[node]:
                reversed_graph[nei].append(node)
                in_degree[node] += 1
        
        q = collections.deque()
        for node in range(N):
            if in_degree[node] == 0:
                q.append(node)
        
        res = []
        while q:
            node = q.popleft()
            res.append(node)

            for nei in reversed_graph[node]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    q.append(nei)
        
        return sorted(res)