class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # dp..? 
        # dp[i:j]는 dp[i+1][j], dp[i][j-1], dp[i+1][j-1] 로부터 구할 수 있는데
        # s[i] == s[j]면 dp[i+1][j-1] + 2가 되나?
        # 아니면 max(dp[i][j-1], dp[i+1][j])

        # d, b d, b b d
        # a b c d e f b h b j b 이런 식이면
        # bbbb 4개짜리가 있는데
        # 세 가지 경우를 다 봐야 할 듯?
        N = len(s)
        dp = [[0] * (N) for _ in range(N)]
        
        for i in range(N - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, N):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        
        return dp[0][N - 1]