class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        
        left = 0
        for right in range(1, len(prices)):
            profit = prices[right] - prices[left]
            
            if prices[left] < prices[right]:
                max_profit = max(profit, max_profit)
            else:
                left = right
        
        return max_profit