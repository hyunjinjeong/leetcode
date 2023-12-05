class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # union find 쓰면 되지 않으려나
        # union에서 이미 합쳐져 있으면, 즉 parent가 같으면 false. 
        # 또 마지막에 parent가 하나가 아니면 false.
        parent = [i for i in range(n)]
        
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(u, v):
            pu, pv = find(u), find(v)
            if pu == pv:
                return False
            
            parent[pu] = pv
            return True
        
        for u, v in edges:
            if not union(u, v):
                return False
        
        return len(set([find(x) for x in parent])) == 1