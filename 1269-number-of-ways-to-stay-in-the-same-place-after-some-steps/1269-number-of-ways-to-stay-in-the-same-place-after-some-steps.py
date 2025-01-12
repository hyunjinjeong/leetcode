class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        # dp?
        MOD = 10 ** 9 + 7

        @cache
        def dfs(i, step):
            if step == steps:
                return 1 if i == 0 else 0 # stay
            
            stay = dfs(i, step + 1)
            
            left, right = 0, 0
            if i > 0:
                left = dfs(i - 1, step + 1)
            if i < arrLen - 1:
                right = dfs(i + 1, step + 1)
            
            return (((stay + left) % MOD) + right) % MOD

        return dfs(0, 0)