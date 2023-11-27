class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # union-find?
        parents = [i for i in range(n)]
        
        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]
        
        def union(u, v):
            root_u, root_v = find(u), find(v)
            if root_u != root_v:
                parents[root_v] = root_u
        
        for u, v in edges:
            union(u, v)
        
        return len(set([find(x) for x in parents]))