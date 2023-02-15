class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # BFS로..?
        
        rotting = collections.deque()
        fresh_count = 0
        # 일단 초기화
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                tomato = grid[r][c]
                if tomato == 2:
                    rotting.append((r, c))
                elif tomato == 1:
                    fresh_count += 1
        
        minutes = 0
        # rotting: 2인데 방문 안 한 토마토들, fresh_count는 남아 있는 fresh 갯수.
        # 그래서 둘 다 체크 필요.
        while rotting and fresh_count:
            minutes += 1
            for _ in range(len(rotting)):
                x, y = rotting.popleft()
                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    next_x, next_y = x + dx, y + dy
                    if 0 <= next_x < len(grid) and 0 <= next_y < len(grid[0]) and grid[next_x][next_y] == 1:
                        fresh_count -= 1
                        grid[next_x][next_y] = 2
                        rotting.append((next_x, next_y))
        
        return minutes if fresh_count == 0 else -1