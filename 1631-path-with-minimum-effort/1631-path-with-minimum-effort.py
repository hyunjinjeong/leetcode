class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROW, COL = len(heights), len(heights[0])

        def can_reach(threshold):
            visited = set()
            q = collections.deque([(0, 0, 0)])

            while q:
                r, c, diff = q.popleft()
                if r == ROW - 1 and c == COL - 1:
                    return True
                
                visited.add((r, c))
                for adj_r, adj_c in [(r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c)]:
                    if not (0 <= adj_r < ROW and 0 <= adj_c < COL):
                        continue
                    if (adj_r, adj_c) in visited:
                        continue
                    
                    diff = abs(heights[adj_r][adj_c] - heights[r][c])
                    if diff > threshold:
                        continue

                    q.append((adj_r, adj_c, abs(heights[adj_r][adj_c] - heights[r][c])))
            
            return False
        
        left, right = 0, 10 ** 6
        while left < right:
            mid = left + (right - left) // 2

            if can_reach(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
