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
        
        def dfs(node, parent):
            time = 0
            
            for adj in graph[node]:
                if adj != parent:
                    time += dfs(adj, node)
            
            if time > 0 or hasApple[node]:
                return time + 2
            
            return 0
        
        return max(dfs(0, -1) - 2, 0)