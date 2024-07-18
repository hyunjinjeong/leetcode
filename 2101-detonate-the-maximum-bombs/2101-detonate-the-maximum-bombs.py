class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # 폭탄 범위 내에 있는지 확인하려면
        # (y2 - y1) ** 2 + (x2 - x1) ** 2 <= r ** 2
        N = len(bombs)
        graph = {i: set() for i in range(N)}

        # 최대 100개니까 그냥 2번 돌리면 될 듯?
        for u in range(N):
            x1, y1, r1 = bombs[u]
            for v in range(u+1, N):
                x2, y2, r2 = bombs[v]

                if (x2 - x1) ** 2 + (y2 - y1) ** 2 <= r1 ** 2:
                    graph[u].add(v)
                if (x2 - x1) ** 2 + (y2 - y1) ** 2 <= r2 ** 2:
                    graph[v].add(u)
        
        def dfs(node, visited):
            visited.add(node)
            
            res = 0
            for nei in graph[node]:
                if nei not in visited:
                    res += dfs(nei, visited)
            
            return 1 + res

        ans = 1
        for node in range(N):
            ans = max(dfs(node, set()), ans)
            
        return ans