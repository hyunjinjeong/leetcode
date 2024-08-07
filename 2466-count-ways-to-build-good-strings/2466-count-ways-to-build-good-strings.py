class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        # 이거는 너무 dp 같은데
        # dp[i] = dp[i-zero] + dp[i-one] 요런 느낌?
        # dp[0]은 1일거고..
        dp = [0] * (high + 1)
        dp[0] = 1

        MOD = 10**9 + 7

        for i in range(high + 1):
            if i >= one:
                dp[i] += dp[i - one]
            if i >= zero:
                dp[i] += dp[i - zero]
            dp[i] %= MOD
        
        ans = 0
        for i in range(low, high + 1):
            ans = (dp[i] + ans) % MOD

        return ans