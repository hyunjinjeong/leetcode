class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        # 위상 정렬한 다음에... 아 그래프가 아니고 하나의 path에 대해서구나
        # 각 path에 대해서 컬러별 최댓값을 저장해주면 된다.
        N = len(colors)

        in_degree = {i: 0 for i in range(N)}
        graph = {i: [] for i in range(N)}
        
        for start, end in edges:
            graph[start].append(end)
            in_degree[end] += 1
        
        q = collections.deque()
        for node in in_degree:
            if in_degree[node] == 0:
                q.append(node)
        
        res = -1
        color_counter = [collections.defaultdict(int) for _ in range(N)]
        visited = 0

        while q:
            node = q.popleft()

            color = colors[node]
            color_counter[node][color] += 1
            res = max(color_counter[node][color], res)
            
            visited += 1

            for nei in graph[node]:
                for c in "abcdefghijklmnopqrstuvwxyz":
                    color_counter[nei][c] = max(color_counter[nei][c], color_counter[node][c])

                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    q.append(nei)
        
        return res if visited == N else -1