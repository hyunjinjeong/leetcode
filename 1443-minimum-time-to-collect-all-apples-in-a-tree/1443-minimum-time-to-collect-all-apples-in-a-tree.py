class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # 출발점은 정할 필요 없다. 0에서 출발 후 0에서 되돌아오는 시간.
        # 근데 특정 노드에서 더 갈지, 되돌아올지를 알아야 함. 그 뒤로 hasApple이 모두 false이면 되돌아오면 되는데
        # 어떻게 알지? 그건 모름.
        # 그러면 다 돌아보고 계산해야 한다.
        # DFS?

        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        def dfs(node):
            if node in visited:
                return 0

            visited.add(node)
            time = 0
            for adj in graph[node]:
                time += dfs(adj)
            
            if time > 0:
                return time + 2
            
            return 2 if hasApple[node] else 0
        
        return max(dfs(0) - 2, 0)