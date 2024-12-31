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
        for target in range(n):
            q = collections.deque()
            q.append((0, BLUE, 0))
            q.append((0, RED, 0)) # 이렇게 두 개 넣어야 하나..?
            red_visited = set()
            blue_visited = set()

            while q:
                node, color, length = q.popleft()

                if node == target and res[target] == -1:
                    res[node] = length
                    continue
                
                if color == BLUE:
                    blue_visited.add(node)
                    for adj in red_graph[node]:
                        if adj not in red_visited:
                            q.append((adj, RED, length + 1))
                else:
                    red_visited.add(node)
                    for adj in blue_graph[node]:
                        if adj not in blue_visited:
                            q.append((adj, BLUE, length + 1))
        
        return res