class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp.

        dp = [0] * (amount + 1)
        dp[0] = 1 # 베이스 케이스

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]

        return dp[amount]

        # 1: 1 => 1
        # 2: 1+1, 2 => 2
        # 3: 1+1+1, 2+1 => 2
        # 4: 1+1+1+1, 2+2, 2+1+1 => 3
        # 5: 1+1+1+1+1, 2+2+1, 2+1+1+1, 5 => 4