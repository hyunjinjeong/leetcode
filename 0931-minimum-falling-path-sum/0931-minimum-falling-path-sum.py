class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        N = len(matrix)
        dp = [0] * N

        # 0번째 row 초기화...
        for c in range(N):
            dp[c] = matrix[0][c]

        for r in range(1, N):
            temp_dp = [0] * N
            for c in range(N):
                upper = dp[c]
                left_upper = dp[c - 1] if c > 0 else float("inf")
                right_upper = dp[c + 1] if c < N - 1 else float("inf")
                
                temp_dp[c] = min(left_upper, upper, right_upper) + matrix[r][c]
            
            dp = temp_dp

        return min(dp)