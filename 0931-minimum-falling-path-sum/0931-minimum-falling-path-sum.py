class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # dp..?
        N = len(matrix)
        dp = [0] * N

        # 0번째 row 초기화...
        for c in range(N):
            dp[c] = matrix[0][c]

        for r in range(1, N):
            temp_dp = [0] * N
            for c in range(N):
                left_upper = upper = right_upper = float("inf")
                if c > 0:
                    left_upper = dp[c - 1]
                upper = dp[c]
                if c < N - 1:
                    right_upper = dp[c + 1]
                temp_dp[c] = min(left_upper, upper, right_upper) + matrix[r][c]
            
            dp = temp_dp

        return min(dp)