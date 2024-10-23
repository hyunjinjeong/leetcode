class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # 음... 그냥 DFS나 BFS로 돌면 되려나? 아니면 다익스트라 같은 알고리즘이 필요할까?
        # 그래프를 가장한 다른 문제일 수도 있나?
        # 일단 경로의 확률은 path의 prob를 다 곱해서 나오는 값.
        # 그러면 모든 경로를 다 돌고 max를 고르면 되는 건데...
        graph = {i: [] for i in range(n)}
        for i in range(len(edges)):
            u, v = edges[i]
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))
        
        max_prob = [0.0] * n
        max_prob[start_node] = 1.0

        q = collections.deque([start_node])
        while q:
            node = q.popleft()
            for nei, prob in graph[node]:
                if max_prob[node] * prob <= max_prob[nei]:
                    continue
                max_prob[nei] = max_prob[node] * prob
                q.append(nei)

        return max_prob[end_node]