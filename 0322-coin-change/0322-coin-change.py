class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0 # base

        for curr_amount in range(1, amount + 1):
            for coin in coins:
                prev_amount = curr_amount - coin
                if prev_amount < 0:
                    continue
                dp[curr_amount] = min(dp[prev_amount] + 1, dp[curr_amount])

        return dp[amount] if dp[amount] != amount + 1 else -1