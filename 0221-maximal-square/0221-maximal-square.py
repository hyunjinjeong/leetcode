class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # dp(i,j)는 maximum square의 변의 길이
        # dp(i,j) = min(dp(i-1,j), dp(i, j-1), dp(i-1, j-1))+1
        R, C = len(matrix), len(matrix[0])
        dp = [[0] * (C+1) for _ in range(R+1)]
        
        max_side_length = 0
        for r in range(R):
            for c in range(C):
                if matrix[r][c] == "1":
                    dp[r+1][c+1] = min(dp[r][c+1], dp[r+1][c], dp[r][c]) + 1
                    max_side_length = max(max_side_length, dp[r+1][c+1])
        
        return max_side_length * max_side_length