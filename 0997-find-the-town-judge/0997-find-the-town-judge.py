class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # 노드에 들어오는 엣지가 n-1개고 나가는 엣지가 0개면 될 듯
        in_edges, out_edges = [0] * n, [0] * n
        for u, v in trust: # 1부터 시작이라...
            out_edges[u - 1] += 1
            in_edges[v - 1] += 1
        
        for i in range(n):
            if in_edges[i] == n - 1 and out_edges[i] == 0:
                return i + 1
        return -1