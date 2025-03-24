class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # 흠.. 일단 -1은 어떻게 찾지?
        # edge가 모두 연결되어 있어야 함. Connected components? 단순히 DFS로 모든 노드 방문 가능한지 확인해도 되고
        # 여기까진 ok. 문제는 어떤 노드를 제거해도 되는지 어떻게 알지
        # 최종 형상은 Alice(1+3)랑 Bob(2+3)에 대해서 각각은 모든 노드에 연결된 선이 1개씩만 있는 모습일 듯?
        # UF 쓰면 된다! 당연히 3번 먼저 써야 할 거고
        alice, bob = UnionFind(n), UnionFind(n)

        t1, t2, t3 = [], [], []
        for node, (t, u, v) in enumerate(edges):
            if t == 1:
                target = t1
            if t == 2:
                target = t2
            elif t == 3:
                target = t3
            target.append((u - 1, v - 1, node))

        for u, v, node in t3:
            if alice.should_connect(u, v):
                alice.union(u, v, node)
            if bob.should_connect(u, v):
                bob.union(u, v, node)
        
        for u, v, node in t1:
            if alice.should_connect(u, v):
                alice.union(u, v, node)

        for u, v, node in t2:
            if bob.should_connect(u, v):
                bob.union(u, v, node)
        
        if not (alice.all_connected() and bob.all_connected()):
            return -1

        return len(edges) - len(alice.nodes | bob.nodes)


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        self.nodes = set()
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, u, v, node):
        pu, pv = self.find(u), self.find(v)
        if self.size[pu] > self.size[pv]:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
        else:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]
        
        self.nodes.add(node)
    
    def should_connect(self, u, v):
        return self.find(u) != self.find(v)
    
    def all_connected(self):
        return any(s == len(self.size) for s in self.size)