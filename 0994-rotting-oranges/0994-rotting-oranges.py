class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # BFS로..?
        
        rotten = collections.deque()
        fresh_count = 0
        # 일단 초기화
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                tomato = grid[r][c]
                if tomato == 2:
                    rotten.append((r, c))
                elif tomato == 1:
                    fresh_count += 1
        
        minutes = 0
        while rotten and fresh_count:
            minutes += 1
            
            for _ in range(len(rotten)):
                x, y = rotten.popleft()
                
                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    next_x, next_y = x + dx, y + dy
                    # out of range
                    if not (0 <= next_x < len(grid)) or not (0 <= next_y < len(grid[0])):
                        continue
                    
                    next_tomato = grid[next_x][next_y]
                    # skip empty or rotten
                    if next_tomato in (0, 2):
                        continue
                    
                    fresh_count -= 1
                    grid[next_x][next_y] = 2
                    rotten.append((next_x, next_y))
        
        return minutes if fresh_count == 0 else -1