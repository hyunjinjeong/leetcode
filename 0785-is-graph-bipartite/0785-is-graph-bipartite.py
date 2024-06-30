class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # union find 느낌이긴 한데...
        # 아니면 bfs?
        # graph coloring 이라고 한다. 뭐여 이게...
        # 인접한 노드들은 서로 다른 색을 갖도록 하는것?
        
        # colors = [0] * len(graph)
        
        # def dfs(node, color):
        #     if colors[node] != 0:
        #         return colors[node] == color # 이미 다른 색으로 칠해진 경우
            
        #     colors[node] = color
        #     for neighbor in graph[node]:
        #         if not dfs(neighbor, -color):
        #             return False
            
        #     return True
        
        # for i in range(len(graph)):
        #     if colors[i] == 0:
        #         if not dfs(i, 1):
        #             return False
        
        # return True

        colors = [0] * len(graph)

        for i in range(len(graph)):
            if colors[i] != 0:
                continue
            
            colors[i] = 1
            q = collections.deque([i])
            while q:
                node = q.popleft()
                for neighbor in graph[node]:
                    if colors[neighbor] == colors[node]:
                        return False
                    
                    if colors[neighbor] == 0:
                        colors[neighbor] = -colors[node]
                        q.append(neighbor)
            
        return True
                        

            

        