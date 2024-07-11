class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # 각각의 stone이 +일지 -일지...
        # 0-1 knapsack 문제였음
        total = sum(stones)
        max_weight = total // 2
        dp = [0] * (max_weight + 1)

        for stone in stones:
            for w in range(max_weight, stone - 1, -1):
                dp[w] = max(dp[w - stone] + stone, dp[w])
        
        return total - 2 * dp[max_weight]