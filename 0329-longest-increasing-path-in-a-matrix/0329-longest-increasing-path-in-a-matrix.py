class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def dfs(x, y):
            if dp[x][y]: # visited
                return dp[x][y]
            
            moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            max_sub_length = 0
            for dx, dy in moves:
                next_x, next_y = x + dx, y + dy
                # 조건들을 모두 충족하는 경우에만.
                if (0 <= next_x < M) and (0 <= next_y < N) and (matrix[next_x][next_y] > matrix[x][y]):
                    max_sub_length = max(max_sub_length, dfs(next_x, next_y))
                
            dp[x][y] = max_sub_length + 1
            return dp[x][y]
        
        # edge cases
        if not (matrix and matrix[0]):
            return 0
        
        M, N = len(matrix), len(matrix[0])
        
        dp = [[0 for _ in range(N)] for _ in range(M)]
        
        ans = 0
        for r in range(M):
            for c in range(N):
                curr_length = dfs(r, c)
                ans = max(ans, curr_length)
        
        return ans
                
        
        