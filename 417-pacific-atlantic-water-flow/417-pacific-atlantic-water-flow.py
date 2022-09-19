class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # 거꾸로 edge에서 도달 가능한 점들을 찾으면 된다.
        # pacific이랑 atlantic이랑 각각 찾아서 교집합 구하기
        p_visited, a_visited = set(), set()
        rows, cols = len(heights), len(heights[0])
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        
        def traverse(x, y, visited):
            if (x, y) in visited:
                return
            
            visited.add((x, y))
            for dx, dy in directions:
                next_x, next_y = x+dx, y+dy
                if 0 <= next_x < rows and 0 <= next_y < cols:
                    # edge에서 도달 가능하려면 높이가 같거나 커야 함
                    if heights[next_x][next_y] >= heights[x][y]:
                        traverse(next_x, next_y, visited)
        
        for row in range(rows):
            traverse(row, 0, p_visited) # Left edge
            traverse(row, cols-1, a_visited) # Right edge
        
        for col in range(cols):
            traverse(0, col, p_visited) # Top edge
            traverse(rows-1, col, a_visited) # Bottom edge
        
        return list(p_visited & a_visited)
    
#         # 위는 DFS인데... BFS도 알아두기
#         rows, cols = len(heights), len(heights[0])
#         directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        
#         def bfs(starts):
#             q = deque(starts)
#             visited = set(starts)
#             while q:
#                 x, y = q.popleft()
#                 for dx, dy in directions:
#                     next_x, next_y = x+dx, y+dy
#                     if 0 <= next_x < rows and 0 <= next_y < cols:
#                         # edge에서 도달 가능하려면 높이가 같거나 커야 함 + 방문 안한거
#                         if (next_x, next_y) not in visited and heights[next_x][next_y] >= heights[x][y]:
#                             q.append((next_x, next_y))
#                             visited.add((next_x, next_y))
#             return visited
        
#         pacific = [(0, i) for i in range(cols)] + [(i, 0) for i in range(rows)]
#         atlantic = [(rows-1, i) for i in range(cols)] + [(i, cols-1) for i in range(rows)]
        
#         return bfs(pacific) & bfs(atlantic)