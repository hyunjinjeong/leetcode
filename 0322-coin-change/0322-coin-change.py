class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        
        # dp[i]가 i까지의 최솟값이라고 하면, 밑에서부터 구해져 있으니까
        # 코인을 돌면서 최솟값을 찾아서 +1을 더하면 됨.
        for i in range(1, amount+1):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], dp[i-coin]+1)
        
        return dp[amount] if dp[amount] <= amount else -1