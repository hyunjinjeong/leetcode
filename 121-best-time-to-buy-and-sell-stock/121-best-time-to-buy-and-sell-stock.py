class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        
        left, right = 0, 1
        
        while right < len(prices):
            num_left, num_right = prices[left], prices[right]
            profit = num_right - num_left
            
            if num_left < num_right:
                max_profit = max(profit, max_profit)
            else:
                left = right
            
            right += 1
        
        return max_profit
        