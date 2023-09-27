class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp 문제... buy와 sell을 따로 관리하는 것이 핵심
        N = len(prices)
        # buy[i], sell[i]는 각각 i번째 날에 수행한 action. 그 때의 max profit
        buy, sell = [0] * N, [0] * N
        buy[0] = -1 * prices[0]

        for i in range(1, N):
            # 오른쪽은 각각 cooldown인 경우를 의미.
            buy[i] = max(sell[i-2] - prices[i], buy[i-1])
            sell[i] = max(buy[i-1] + prices[i], sell[i-1])
        
        return max(buy[N-1], sell[N-1])