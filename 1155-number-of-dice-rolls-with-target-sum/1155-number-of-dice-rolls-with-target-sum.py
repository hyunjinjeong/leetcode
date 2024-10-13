class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        @cache
        def dfs(count, t): # 아 항상 n번을 던져야 함
            if count == n:
                return 1 if t == 0 else 0

            res = 0
            for num in range(1, k + 1):
                res += dfs(count + 1, t - num)
            return res
        
        return dfs(0, target) % (10**9 + 7)