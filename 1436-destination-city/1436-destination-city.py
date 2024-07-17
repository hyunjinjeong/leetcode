class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # topological sort? 도 되겠고
        # 그냥 DFS 돌려서 도착지도 될듯?
        # 아니면 그냥 outgoing path가 0인거 찾으면 되잖아..?

        graph = {}
        for u, v in paths:
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            
            graph[u].append(v)
            
        for city in graph:
            if len(graph[city]) == 0:
                return city