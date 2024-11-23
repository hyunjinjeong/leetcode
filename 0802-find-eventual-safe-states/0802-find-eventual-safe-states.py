class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        N = len(graph)

        self.safe_nodes = set()
        for node in range(N):
            if not graph[node]:
                self.safe_nodes.add(node)
        
        # dfs 돌리기?
        # 모든 nei에 대해서
        # nei가 safe node면 true
        # 아니면 false
        # 해서 all()을 만족하면 걔도 safe_nodes에 추가
        # 이런 식으로...

        def dfs(node, visited):
            if node in self.safe_nodes:
                return True
            
            visited.add(node)

            is_safe = True
            for nei in graph[node]:
                if nei in visited:
                    is_safe = is_safe and nei in self.safe_nodes
                else:
                    is_safe = is_safe and dfs(nei, visited)
                                    
            if is_safe:
                self.safe_nodes.add(node)
            return is_safe

        for node in range(N):
            dfs(node, set())
        
        return sorted(list(self.safe_nodes))