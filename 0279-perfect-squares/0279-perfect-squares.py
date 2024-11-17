class Solution:
    def numSquares(self, n: int) -> int:
        # # perfect square라면.. sqrt(n)까지겠네
        # @cache
        # def dfs(num_left):
        #     if num_left == 0:
        #         return 0
            
        #     res = float("inf")
        #     for num in range(1, int(sqrt(num_left)) + 1):
        #         res = min(res, dfs(num_left - num ** 2) + 1)
            
        #     return res
        
        # return dfs(n)

        dp = [float("inf")] * (n + 1)
        dp[0] = 0

        for num in range(1, n + 1):
            for root in range(1, int(sqrt(num)) + 1):
                if num - root ** 2 < 0:
                    continue
                dp[num] = min(dp[num], dp[num - root ** 2] + 1)
        
        return dp[n]