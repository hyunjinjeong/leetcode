class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        # dp[i][j]는 (i, j)가 bottom-right인 값
        M, N = len(matrix), len(matrix[0])

        res = 0

        dp = [[0] * (N + 1) for _ in range(M + 1)]
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 0:
                    continue
                
                up = dp[i - 1][j] if i > 0 else 0
                left = dp[i][j - 1] if j > 0 else 0
                up_left = dp[i - 1][j - 1] if i > 0 and j > 0 else 0
                
                dp[i][j] = min(up, left, up_left) + 1
                res += dp[i][j]
        
        return res
