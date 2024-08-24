class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # 노드에 들어오는 엣지가 n-1개고 나가는 엣지가 0개면 될 듯
        in_degrees, out_degrees = [0] * (n + 1), [0] * (n + 1)
        for u, v in trust:
            out_degrees[u] += 1
            in_degrees[v] += 1
        
        for i in range(1, n + 1):
            if in_degrees[i] == n - 1 and out_degrees[i] == 0:
                return i
        return -1