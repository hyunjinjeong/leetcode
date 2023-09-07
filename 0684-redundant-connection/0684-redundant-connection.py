class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    #     # topological sort는 안 되는 것 같고...
    #     # edge를 하나씩 연결하면서 기존 graph에서 u, v를 연결할 수 있으면 해당 edge가 중복
    #     graph = collections.defaultdict(set)

    #     for u, v in edges:
    #         if self.can_reach(u, v, set(), graph):
    #             return u, v

    #         graph[u].add(v)
    #         graph[v].add(u)
    
    # def can_reach(self, source, target, visited, graph):
    #     if source in visited:
    #         return False

    #     visited.add(source)
    #     if source == target:
    #         return True
        
    #     result = False
    #     for next_source in graph[source]:
    #         result = self.can_reach(next_source, target, visited, graph) or result
        
    #     return result

        # 2. Union-Find도 된다. 위의 솔루션이 생각해보면 disjoint set을 합치는 과정임
        # 이미 같은 set에 있으면 중복인 edge.
        union_find = UnionFind(len(edges))
        for u, v in edges:
            if not union_find.union(u, v):
                return [u, v]

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.size = [1] * (n + 1)
        
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x]) # Path compression
        return self.parent[x]
    
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False  # Return False if u and v are already union
        
        # Union by rank
        larger, smaller = (pu, pv) if self.size[pu] > self.size[pv] else (pv, pu)
        self.size[larger] += self.size[smaller]
        self.parent[smaller] = larger
        
        return True