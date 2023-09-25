class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp...
        # dp[i][j]는 text1[0:i], text2[0:j]의 LCS
        M, N = len(text1), len(text2)
        dp = [[0] * (N+1) for _ in range(M+1)]

        for i in range(1, M + 1):
            c1 = text1[i-1]
            for j in range(1, N + 1):
                c2 = text2[j-1]

                if c1 == c2:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        
        return dp[M][N]