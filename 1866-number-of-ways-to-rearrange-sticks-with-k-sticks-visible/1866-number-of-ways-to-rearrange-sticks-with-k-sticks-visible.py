class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        # dp[n][k]에서 k번째가 가장 긴 스틱일 때와 아닐 때로 나눠서 생각하면 됨
        # 가장 긴 스틱이면 dp[n-1][k-1], 아니면 (n - 1) * dp[n-1][k]. 즉
        # dp[n][k] = dp[n-1][k-1] + (n - 1) * dp[n-1][k].
        # 어떻게 생각하는 거지;;
        MOD = 10 ** 9 + 7

        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(1, k + 1):
            dp[i][i] = 1

        for i in range(2, n + 1):
            for j in range(1, k + 1):
                dp[i][j] = (dp[i - 1][j - 1] + ((i - 1) * dp[i - 1][j]) % MOD) % MOD

        return dp[n][k]