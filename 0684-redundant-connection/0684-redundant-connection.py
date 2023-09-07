class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # topological sort는 안 되는 것 같고...
        # edge를 하나씩 연결하면서 기존 graph에서 u, v를 연결할 수 있으면 해당 edge가 중복
        graph = collections.defaultdict(set)

        for u, v in edges:
            if u in graph and v in graph and self.can_reach(u, v, set(), graph):
                return u, v

            graph[u].add(v)
            graph[v].add(u)
    
    def can_reach(self, source, target, visited, graph):
        if source in visited:
            return False

        visited.add(source)
        if source == target:
            return True
        
        result = False
        for next_source in graph[source]:
            result = self.can_reach(next_source, target, visited, graph) or result
        
        return result