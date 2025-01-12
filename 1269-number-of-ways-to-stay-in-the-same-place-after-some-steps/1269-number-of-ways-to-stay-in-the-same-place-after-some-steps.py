class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        # # dp?
        MOD = 10 ** 9 + 7

        # @cache
        # def dfs(i, step):
        #     if step == steps:
        #         return 1 if i == 0 else 0 # stay
            
        #     stay = dfs(i, step + 1)
        #     left = dfs(i - 1, step + 1) if i > 0 else 0
        #     right = dfs(i + 1, step + 1) if i < arrLen - 1 else 0
            
        #     return (((stay + left) % MOD) + right) % MOD

        # return dfs(0, 0)

        # bottom up으로 해봅시당
        # 바로 이전 step만 사용하니까 1D array로 가능할 듯?
        arr_len = min(arrLen, steps)
        dp = [0] * arr_len
        dp[0] = 1 # base

        for _ in range(steps):
            next_dp = [0] * arr_len
            for i in range(arr_len):
                stay = dp[i]
                left = dp[i - 1] if i > 0 else 0
                right = dp[i + 1] if i < arr_len - 1 else 0
                next_dp[i] = (((stay + left) % MOD) + right) % MOD
            dp = next_dp
        
        return dp[0]