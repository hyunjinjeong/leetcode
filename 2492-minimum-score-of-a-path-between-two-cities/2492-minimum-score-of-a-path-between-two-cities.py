class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # 1이랑 n 사이의 경로 중, 최소 cost를 구하면 됨. 끊어진 경로는 포함하면 안되고.
        # 즉 그래프에서 서로 연결된 요소의 집합을 구해야 함.
        # 그런데 1-n 사이에 최소 하나의 경로라도 있다는건 1에서 출발해서 들리는 모든 경로가 집합에 포함된다.
        # 그럼 걍 최솟값을 구하면 될 듯?

        graph = {i: [] for i in range(1, n + 1)}
        for start, end, cost in roads:
            graph[start].append((end, cost))
            graph[end].append((start, cost))
        
        res = float("inf")
        q = collections.deque([1])
        visited = set()
        
        while q:
            city = q.popleft()
            visited.add(city)
            for nei, cost in graph[city]:
                if nei not in visited:
                    res = min(cost, res)
                    q.append(nei)
        
        return res