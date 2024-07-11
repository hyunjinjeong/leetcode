class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # 각각의 stone이 +일지 -일지...
        # 0-1 knapsack 문제였음
        stone_sum = sum(stones)
        half_sum = stone_sum // 2
        dp = [0 for i in range(half_sum + 1)]

        for stone in stones:
            for w in range(half_sum, stone - 1, -1):
                dp[w] = max(dp[w - stone] + stone, dp[w])
        
        return stone_sum - 2 * dp[half_sum]