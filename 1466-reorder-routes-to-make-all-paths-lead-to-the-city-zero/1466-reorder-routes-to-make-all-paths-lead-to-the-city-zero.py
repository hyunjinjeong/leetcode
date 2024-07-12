class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # 방향이 없는 그래프처럼 생각하면 됨..!
        graph = {i: [] for i in range(n)}

        for u, v in connections:
            graph[u].append((v, True))
            graph[v].append((u, False))
        
        ans = 0

        q = collections.deque([0])
        visited = set()
        while q:
            node = q.popleft()
            visited.add(node)
            for neighbor, is_reversed in graph[node]:
                if neighbor not in visited:
                    if is_reversed:
                        ans += 1
                    q.append(neighbor)
        
        return ans
