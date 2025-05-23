class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = prices[:]
        
        stack = []
        for i, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                res[stack.pop()] -= price
            stack.append(i)

        return res