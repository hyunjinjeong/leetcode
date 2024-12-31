class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        RED, BLUE = 0, 1

        red_graph = collections.defaultdict(list)
        for a, b in redEdges:
            red_graph[a].append(b)
        
        blue_graph = collections.defaultdict(list)
        for u, v in blueEdges:
            blue_graph[u].append(v)

        res = [-1] * n
        
        # 노드 0부터 각각 blue 시작, red 시작 각각 돌리면 될 듯?
        q = collections.deque()
        q.append((0, BLUE, 0))
        q.append((0, RED, 0)) # 이렇게 두 개 넣어야 하나..?
        visited = set()

        while q:
            node, color, length = q.popleft()
            visited.add((node, color))

            if res[node] == -1:
                res[node] = length
            
            if color == BLUE:
                for adj in red_graph[node]:
                    if (adj, RED) not in visited:
                        q.append((adj, RED, length + 1))
            else:
                for adj in blue_graph[node]:
                    if (adj, BLUE) not in visited:
                        q.append((adj, BLUE, length + 1))
        
        return res