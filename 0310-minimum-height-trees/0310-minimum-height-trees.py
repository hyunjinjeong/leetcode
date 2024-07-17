class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # height라는게 결국 node 기준으로 DFS를 돌려서 가장 긴 경로를 나타내는거 아닌가?
        # 근데 모든 노드에 다 돌리는건 안될거 같은데..
        # topological sort?
        # in_degree가 1인 친구들만 슉슉 지우면 될 거 같은데
        # 그러다가 남은 노드가 1개나 2개면 멈추기.
        if n <= 2:
            return [i for i in range(n)]

        graph = [[] for _ in range(n)]
        in_degree = [0] * n
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

            in_degree[u] += 1
            in_degree[v] += 1

        q = collections.deque()
        for node in range(n):
            if in_degree[node] == 1:
                q.append(node)

        visited = set()
        while q and len(visited) < n - 2:
            for _ in range(len(q)):
                node = q.popleft()
                visited.add(node)

                in_degree[node] -= 1

                for nei in graph[node]:
                    in_degree[nei] -= 1
                    if nei not in visited:
                        if in_degree[nei] == 1:
                            q.append(nei)

        ans = []
        for node in range(n):
            if node not in visited:
                ans.append(node)
        
        return ans