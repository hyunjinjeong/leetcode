class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        M, N = len(matrix), len(matrix[0])

        ans = 0
        cache = {}
        for r in range(M):
            for c in range(N):
                ans = max(self.dfs(r, c, cache, matrix), ans)
        
        return ans
    
    def dfs(self, r, c, cache, matrix):
        M, N = len(matrix), len(matrix[0])

        if (r, c) in cache:
            return cache[(r, c)]
        
        length = 1
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_r, next_c = r + dr, c + dc
            if 0 <= next_r < M and 0 <= next_c < N and matrix[next_r][next_c] > matrix[r][c]:
                length = max(self.dfs(next_r, next_c, cache, matrix) + 1, length)
        
        cache[(r, c)] = length
        return cache[(r, c)]