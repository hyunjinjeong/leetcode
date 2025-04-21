class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # connected component는 DSU 쓰면 되고
        # complete는..? 컴포넌트를 구성하는 edge의 수가 nC2 이면 됨.
        uf = UnionFind(n)
        for u, v in edges:
            uf.union(u, v)
        return uf.get_complete_components_count()


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        self.edge_count = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, u, v):
        p_u, p_v = self.find(u), self.find(v)
        if p_u == p_v: # 이미 합쳐져 있으면 edge만 증가시키자.
            self.edge_count[p_u] += 1
            return
        
        if self.size[p_u] < self.size[p_v]:
            p_u, p_v = p_v, p_u
        
        self.parent[p_v] = p_u
        self.size[p_u] += self.size[p_v]
        self.edge_count[p_u] += self.edge_count[p_v] + 1
    
    def get_complete_components_count(self):
        count = 0
        for i in range(len(self.parent)):
            if self.parent[i] == i and self.edge_count[i] == (self.size[i] * (self.size[i] - 1) // 2):
                print(i, "is coplete")
                count += 1
        return count
