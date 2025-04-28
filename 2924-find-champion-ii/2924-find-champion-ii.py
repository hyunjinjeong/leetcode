class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        # 걍 topological sort인데 처음에 in_degree가 0인 노드 개수만 세도 될 듯
        in_degrees = [0] * n
        for u, v in edges:
            in_degrees[v] += 1
        
        candidates = []
        for node in range(n):
            if in_degrees[node] == 0:
                candidates.append(node)
        
        return candidates[0] if len(candidates) == 1 else -1
