class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # 이렇게 깔끔한 버전이 있넹..
        if n == 1:
            return [0]
        
        graph = [set() for _ in range(n)]
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        leaves = [node for node in range(n) if len(graph[node]) == 1]

        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for node in leaves:
                nei = graph[node].pop()
                graph[nei].remove(node)
                if len(graph[nei]) == 1:
                    new_leaves.append(nei)
            
            leaves = new_leaves
        
        return leaves