class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10 ** 9 + 7

        # @cache
        # def dfs(i, curr_members, curr_profit):
        #     if i == len(group):
        #         return 1 if curr_profit >= minProfit else 0

        #     # not pick
        #     res = dfs(i + 1, curr_members, curr_profit)
        #     if curr_members + group[i] <= n: # pick
        #         res += dfs(i + 1, curr_members + group[i], min(curr_profit + profit[i], minProfit))
            
        #     return res % MOD
        
        # return dfs(0, 0, 0)

        # bottom-up
        G = len(group)

        dp = [[[0] * (minProfit + 1) for _ in range(n + 1)] for _ in range(G + 1)]
        for curr_members in range(n + 1):
            dp[G][curr_members][minProfit] = 1 # i == len(group)일 때
        
        for i in range(G - 1, -1, -1):
            for curr_members in range(n + 1):
                for curr_profit in range(minProfit + 1):
                    key = (i, curr_members, curr_profit)
                    # not pick
                    dp[i][curr_members][curr_profit] = dp[i + 1][curr_members][curr_profit]
                    if curr_members + group[i] <= n: # pick
                        dp[i][curr_members][curr_profit] += dp[i + 1][curr_members + group[i]][min(curr_profit + profit[i], minProfit)]
                    dp[i][curr_members][curr_profit] %= MOD
        
        return dp[0][0][0]